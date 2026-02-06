"""
Cyber Coding Game - Lucene Search Simulator

Simulates Lucene-style log queries against in-memory JSON data.

This module does NOT connect to any external services.
All data is local and pre-defined for educational purposes.
"""

import re
from typing import List, Dict, Any, Optional
from ..models import SearchResult, LogEntry


class LuceneSearchSimulator:
    """
    Simulate Lucene-style queries against fake log data.
    
    Supports:
    - field:value (exact match)
    - field:*partial* (wildcard)
    - field:[min TO max] (range)
    - AND, OR operators
    """
    
    def __init__(self):
        """Initialize with fake log data."""
        self.logs = self._create_fake_logs()
    
    def _create_fake_logs(self) -> List[Dict[str, Any]]:
        """Create realistic-looking fake log data."""
        return [
            # Normal activity
            {"timestamp": "2024-01-15 09:00:15", "level": "INFO", "user": "sarah", "action": "login", "status": "success", "ip": "192.168.1.51", "hour": 9},
            {"timestamp": "2024-01-15 09:15:00", "level": "INFO", "user": "sarah", "action": "file_access", "status": "success", "ip": "192.168.1.51", "hour": 9},
            {"timestamp": "2024-01-15 09:30:00", "level": "INFO", "user": "mike", "action": "login", "status": "success", "ip": "192.168.1.52", "hour": 9},
            
            # Failed logins (brute force pattern)
            {"timestamp": "2024-01-15 10:45:01", "level": "WARN", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99", "hour": 10},
            {"timestamp": "2024-01-15 10:45:05", "level": "WARN", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99", "hour": 10},
            {"timestamp": "2024-01-15 10:45:10", "level": "WARN", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99", "hour": 10},
            {"timestamp": "2024-01-15 10:45:15", "level": "WARN", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99", "hour": 10},
            {"timestamp": "2024-01-15 10:45:20", "level": "WARN", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99", "hour": 10},
            {"timestamp": "2024-01-15 10:45:25", "level": "WARN", "user": "john", "action": "login", "status": "success", "ip": "10.0.50.99", "hour": 10},  # Finally got in!
            
            # Normal activity continues
            {"timestamp": "2024-01-15 11:00:00", "level": "INFO", "user": "sarah", "action": "logout", "status": "success", "ip": "192.168.1.51", "hour": 11},
            {"timestamp": "2024-01-15 14:00:00", "level": "INFO", "user": "admin", "action": "config_change", "status": "success", "ip": "192.168.1.100", "hour": 14},
            
            # After-hours admin access (suspicious!)
            {"timestamp": "2024-01-15 23:15:00", "level": "INFO", "user": "admin", "action": "login", "status": "success", "ip": "10.0.50.99", "hour": 23, "path": "/admin/panel"},
            {"timestamp": "2024-01-15 23:20:00", "level": "INFO", "user": "admin", "action": "file_access", "status": "success", "ip": "10.0.50.99", "hour": 23, "path": "/admin/users"},
            {"timestamp": "2024-01-16 02:30:00", "level": "WARN", "user": "unknown", "action": "scan", "status": "blocked", "ip": "10.0.50.99", "hour": 2, "path": "/admin/config"},
            {"timestamp": "2024-01-16 03:17:00", "level": "ERROR", "user": "svc_backup", "action": "database_access", "status": "success", "ip": "10.0.50.99", "hour": 3, "path": "/admin/db"},
            
            # More normal traffic
            {"timestamp": "2024-01-16 09:00:00", "level": "INFO", "user": "mike", "action": "login", "status": "success", "ip": "192.168.1.52", "hour": 9},
            {"timestamp": "2024-01-16 09:30:00", "level": "INFO", "user": "sarah", "action": "login", "status": "success", "ip": "192.168.1.51", "hour": 9},
        ]
    
    def search(self, query: str, mission_id: Optional[str] = None, max_results: int = 100) -> SearchResult:
        """
        Execute a Lucene-style search query.
        
        Supports:
        - field:value
        - field:*wildcard*
        - field:[min TO max]
        - AND, OR
        """
        query = query.strip()
        
        if not query:
            return SearchResult(
                query=query,
                total_matches=0,
                results=[],
                feedback="Enter a search query. Example: status:failed"
            )
        
        try:
            matching_logs = self._execute_query(query)
        except Exception as e:
            return SearchResult(
                query=query,
                total_matches=0,
                results=[],
                feedback=f"Query error: {str(e)}. Check your syntax!"
            )
        
        # Limit results
        matching_logs = matching_logs[:max_results]
        
        # Convert to LogEntry objects
        results = [
            LogEntry(
                timestamp=log.get("timestamp", ""),
                level=log.get("level", "INFO"),
                user=log.get("user"),
                action=log.get("action", ""),
                status=log.get("status", ""),
                ip=log.get("ip"),
                details=log.get("path")
            )
            for log in matching_logs
        ]
        
        # Determine if query is correct for mission
        is_correct = self._check_mission_query(query, mission_id, len(results))
        
        feedback = self._generate_feedback(query, len(results), mission_id, is_correct)
        
        return SearchResult(
            query=query,
            total_matches=len(results),
            results=results,
            is_correct=is_correct,
            feedback=feedback
        )
    
    def _execute_query(self, query: str) -> List[Dict]:
        """Parse and execute a Lucene-style query."""
        # Handle AND/OR operators
        if " AND " in query.upper():
            parts = re.split(r'\s+AND\s+', query, flags=re.IGNORECASE)
            result = self.logs.copy()
            for part in parts:
                part_matches = self._execute_single_query(part.strip())
                result = [log for log in result if log in part_matches]
            return result
        
        if " OR " in query.upper():
            parts = re.split(r'\s+OR\s+', query, flags=re.IGNORECASE)
            result = []
            for part in parts:
                part_matches = self._execute_single_query(part.strip())
                for match in part_matches:
                    if match not in result:
                        result.append(match)
            return result
        
        return self._execute_single_query(query)
    
    def _execute_single_query(self, query: str) -> List[Dict]:
        """Execute a single query term."""
        # Range query: field:[min TO max]
        range_match = re.match(r'(\w+):\[(\d+)\s+TO\s+(\d+)\]', query)
        if range_match:
            field = range_match.group(1)
            min_val = int(range_match.group(2))
            max_val = int(range_match.group(3))
            return [
                log for log in self.logs
                if field in log and isinstance(log[field], int) 
                and min_val <= log[field] <= max_val
            ]
        
        # Field:value query
        field_match = re.match(r'(\w+):(.+)', query)
        if field_match:
            field = field_match.group(1)
            value = field_match.group(2).strip('"\'')
            
            # Wildcard matching
            if '*' in value:
                pattern = value.replace('*', '.*')
                return [
                    log for log in self.logs
                    if field in log and re.search(pattern, str(log[field]), re.IGNORECASE)
                ]
            
            # Exact matching
            return [
                log for log in self.logs
                if field in log and str(log[field]).lower() == value.lower()
            ]
        
        # Fallback: search all fields
        return [
            log for log in self.logs
            if any(query.lower() in str(v).lower() for v in log.values())
        ]
    
    def _check_mission_query(self, query: str, mission_id: Optional[str], result_count: int) -> bool:
        """Check if query satisfies mission objectives."""
        if not mission_id:
            return result_count > 0
        
        if mission_id == "mission03":
            # Looking for failed logins
            return "status:failed" in query.lower() or ("failed" in query.lower() and result_count > 0)
        
        if mission_id == "mission06":
            # Looking for after-hours admin access
            checks = [
                "admin" in query.lower(),
                any(x in query.lower() for x in ["hour", "23", "02", "03", "night"])
            ]
            return all(checks) and result_count > 0
        
        return result_count > 0
    
    def _generate_feedback(self, query: str, result_count: int, mission_id: Optional[str], is_correct: bool) -> str:
        """Generate helpful feedback based on results."""
        if result_count == 0:
            return "No results found. Try adjusting your query. Available fields: user, status, action, ip, level, hour"
        
        if is_correct:
            if mission_id == "mission03":
                return f"🎯 Found {result_count} failed events! Notice the IP 10.0.50.99 appears multiple times — that's a pattern worth investigating!"
            elif mission_id == "mission06":
                return f"🌙 Found {result_count} after-hours admin accesses! This is suspicious behavior that a real analyst would escalate."
            return f"✅ Found {result_count} matching entries."
        
        return f"Found {result_count} results. Review them to see if they match what you're looking for."

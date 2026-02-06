"""
Brute Force Detector - Educational Example
===========================================
An advanced Python script that detects brute force attacks
by analyzing login patterns.

This demonstrates:
- Time-based analysis
- IP address tracking
- Alert generation
"""

from datetime import datetime, timedelta


# Sample log data
logs = [
    {"timestamp": "2024-01-15 10:45:01", "user": "john", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:05", "user": "john", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:10", "user": "john", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:15", "user": "john", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:20", "user": "john", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:25", "user": "john", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 11:00:00", "user": "sarah", "status": "success", "ip": "192.168.1.51"},
]


def parse_timestamp(ts_string):
    """Convert timestamp string to datetime object."""
    return datetime.strptime(ts_string, "%Y-%m-%d %H:%M:%S")


def detect_rapid_failures(entries, window_seconds=60, threshold=3):
    """
    Detect rapid-fire login failures (multiple failures in short time).
    
    Args:
        entries: List of log entries
        window_seconds: Time window to check (default 60 seconds)
        threshold: Number of failures that triggers alert
        
    Returns:
        List of detected attack patterns
    """
    # Get only failed logins, sorted by time
    failures = [e for e in entries if e["status"] == "failed"]
    failures.sort(key=lambda x: x["timestamp"])
    
    attacks = []
    
    # Group by IP address
    ip_failures = {}
    for entry in failures:
        ip = entry["ip"]
        if ip not in ip_failures:
            ip_failures[ip] = []
        ip_failures[ip].append(entry)
    
    # Check each IP for rapid failures
    for ip, ip_entries in ip_failures.items():
        for i, entry in enumerate(ip_entries):
            # Count failures within window
            count = 0
            start_time = parse_timestamp(entry["timestamp"])
            
            for j in range(i, len(ip_entries)):
                check_time = parse_timestamp(ip_entries[j]["timestamp"])
                if (check_time - start_time).seconds <= window_seconds:
                    count += 1
            
            if count >= threshold:
                attacks.append({
                    "ip": ip,
                    "count": count,
                    "start_time": entry["timestamp"],
                    "target_user": entry["user"]
                })
                break  # One alert per IP
    
    return attacks


def main():
    """Run the brute force detector."""
    print("=" * 50)
    print("🔐 BRUTE FORCE DETECTOR")
    print("=" * 50)
    print()
    
    attacks = detect_rapid_failures(logs)
    
    if attacks:
        print("🚨 BRUTE FORCE ATTACKS DETECTED:")
        print()
        for attack in attacks:
            print(f"   Source IP: {attack['ip']}")
            print(f"   Target User: {attack['target_user']}")
            print(f"   Attempts: {attack['count']}")
            print(f"   First Seen: {attack['start_time']}")
            print()
    else:
        print("✅ No brute force attacks detected.")
    
    print("=" * 50)


if __name__ == "__main__":
    main()

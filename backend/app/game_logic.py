"""
Cyber Coding Game - Game Logic

Handles mission management, progress tracking, and validation.
"""

from typing import Dict, List, Optional
from .models import Mission, PlayerProgress


class GameLogic:
    """
    Core game logic for missions and progress.
    
    In a production app, this would use a database.
    For this educational demo, we use in-memory storage.
    """
    
    def __init__(self):
        self._missions = self._create_missions()
        self._progress = PlayerProgress(
            current_tier=1,
            current_tier_name="New Trainee",
            completed_missions=[],
            total_missions=len(self._missions),
            badges=[],
            total_xp=0
        )
    
    def _create_missions(self) -> Dict[str, Mission]:
        """Create all game missions."""
        missions = {}
        
        # ==========================================
        # Tier 1: New Trainee
        # ==========================================
        
        missions["mission01"] = Mission(
            id="mission01",
            tier=1,
            tier_name="New Trainee",
            title="Your First Line of Code",
            description="Learn to print messages in Python",
            story="""Welcome to CyberShield Corp, recruit! I'm Alex, your mentor.
            
            Every cyber defender needs to know a little coding. Don't worry — 
            we'll start with something super simple. Let's make the computer 
            say "Hello, World!" """,
            coding_concept="Variables and print()",
            security_concept="Why automation helps defenders",
            language="python",
            starter_code='# Type your code below:\nprint("Hello, World!")',
            expected_output="Hello, World!",
            hints=[
                "Use the print() function to display text",
                "Put your message inside quotes",
                "Make sure to use parentheses: print(\"message\")"
            ],
            is_locked=False,
            xp_reward=10,
            badge="Terminal Trainee"
        )
        
        missions["mission02"] = Mission(
            id="mission02",
            tier=1,
            tier_name="New Trainee",
            title="Meet the Terminal",
            description="Learn basic Bash commands to navigate systems",
            story="""Alex shows you a black screen with blinking cursor.
            
            "This is a terminal — it's how we talk to computers directly.
            It might look scary, but it's actually just typing commands.
            Let's start with 'ls' to see what files are here." """,
            coding_concept="Basic Bash commands (ls, cat, pwd)",
            security_concept="Understanding system navigation",
            language="bash",
            starter_code="# Type 'ls' to list files in the current directory",
            expected_output=None,
            hints=[
                "Type 'ls' (lowercase L and S) and press Enter",
                "Commands are case-sensitive in Linux",
                "Try 'cat filename.txt' to read a file"
            ],
            is_locked=False,
            xp_reward=10,
            badge="Command Liner"
        )
        
        missions["mission03"] = Mission(
            id="mission03",
            tier=1,
            tier_name="New Trainee",
            title="What Are Logs?",
            description="Learn to search through system logs",
            story="""Alex points to a screen full of scrolling text.
            
            "These are logs — automatic records of everything that happens
            on our systems. Finding the important stuff in all this noise
            is a superpower. Let me show you how to search!" """,
            coding_concept="Simple Lucene-style queries",
            security_concept="Introduction to log analysis",
            language="lucene",
            starter_code="# Search for failed logins:\nstatus:failed",
            expected_output=None,
            hints=[
                "Use field:value format, like status:failed",
                "Fields include: status, user, action, ip",
                "Try searching for a specific user"
            ],
            is_locked=False,
            xp_reward=15,
            badge="Log Reader"
        )
        
        # ==========================================
        # Tier 2: Analyst
        # ==========================================
        
        missions["mission04"] = Mission(
            id="mission04",
            tier=2,
            tier_name="Analyst",
            title="Build a Log Scanner",
            description="Write Python to detect suspicious login patterns",
            story="""Your team lead approaches with a task.
            
            "We need a script that counts failed logins per user. If someone
            fails more than 5 times, that could be an attacker guessing
            passwords. Can you build it?" """,
            coding_concept="Python loops and conditionals",
            security_concept="Brute force detection",
            language="python",
            starter_code='''logs = [
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "john", "status": "failed"},
    {"user": "sarah", "status": "success"},
]

# Count failed logins per user
# Print alert if any user has more than 5 failures
''',
            expected_output="ALERT",
            hints=[
                "Use a dictionary to count failures per user",
                "Loop through each log entry",
                "Check if status equals 'failed'"
            ],
            is_locked=False,
            xp_reward=25,
            badge="Pattern Finder"
        )
        
        missions["mission05"] = Mission(
            id="mission05",
            tier=2,
            tier_name="Analyst",
            title="Bash Pipeline Power",
            description="Chain commands to analyze log files",
            story="""A massive log file just came in — thousands of lines.
            
            "We need to find which IP addresses appear most often. That
            might help us identify an attacker. Use command pipelines
            to filter and count!" """,
            coding_concept="grep, sort, uniq pipelines",
            security_concept="IP address frequency analysis",
            language="bash",
            starter_code="# Extract IPs, sort them, count occurrences\n# Hint: grep | sort | uniq -c",
            expected_output=None,
            hints=[
                "grep can find patterns in files",
                "sort arranges lines alphabetically",
                "uniq -c counts repeated lines (requires sorted input)"
            ],
            is_locked=False,
            xp_reward=25,
            badge="Pipeline Pro"
        )
        
        missions["mission06"] = Mission(
            id="mission06",
            tier=2,
            tier_name="Analyst",
            title="Advanced Log Hunting",
            description="Use complex queries to find suspicious patterns",
            story="""Your lead has a theory about after-hours access.
            
            "I think someone is accessing admin pages at night when no
            one is watching. Can you search for admin access between
            11 PM and 5 AM?" """,
            coding_concept="Complex Lucene queries (AND, OR, ranges)",
            security_concept="Temporal analysis",
            language="lucene",
            starter_code="# Find admin access during night hours\n# path:*admin* AND hour:[23 TO 5]",
            expected_output=None,
            hints=[
                "Use AND to combine conditions",
                "Use OR to match alternatives",
                "Ranges use [min TO max] format"
            ],
            is_locked=False,
            xp_reward=30,
            badge="Search Expert"
        )
        
        # ==========================================
        # Tier 3: Threat Hunter
        # ==========================================
        
        missions["mission07"] = Mission(
            id="mission07",
            tier=3,
            tier_name="Threat Hunter",
            title="The Midnight Breach",
            description="Investigate a simulated security incident",
            story="""🚨 ALERT: Unusual activity detected at 3:17 AM.
            
            Someone accessed the database server during off-hours. We need
            answers: Who was it? How did they get in? What did they access?
            
            Use everything you've learned to investigate. """,
            coding_concept="Multi-tool investigation",
            security_concept="Incident response basics",
            language="python",
            starter_code="# Start your investigation\n# Check auth logs, access logs, and system events",
            expected_output=None,
            hints=[
                "Start by finding all events around 3:17 AM",
                "Look for unusual authentication patterns",
                "Check what files or databases were accessed"
            ],
            is_locked=False,
            xp_reward=50,
            badge="Night Detective"
        )
        
        missions["mission08"] = Mission(
            id="mission08",
            tier=3,
            tier_name="Threat Hunter",
            title="Fix the Vulnerable Code",
            description="Find and fix a security vulnerability",
            story="""The security scanner flagged our user registration code.
            
            "There's a SQL injection vulnerability in here somewhere.
            Can you find it and fix it before attackers do?" """,
            coding_concept="Code review and input validation",
            security_concept="SQL injection prevention",
            language="python",
            starter_code='''def create_user(username, email):
    # VULNERABLE CODE - Fix me!
    query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
    database.execute(query)
    return "User created!"
''',
            expected_output=None,
            hints=[
                "Never put user input directly into SQL queries",
                "Use parameterized queries instead",
                "The ? placeholder separates code from data"
            ],
            is_locked=False,
            xp_reward=50,
            badge="Code Fixer"
        )
        
        missions["mission09"] = Mission(
            id="mission09",
            tier=3,
            tier_name="Threat Hunter",
            title="Build a Brute Force Detector",
            description="Create an advanced detection algorithm",
            story="""We need smarter detection. Simple counting isn't enough.
            
            "Build a detector that can catch both fast attacks (many
            failures in seconds) and slow attacks (spread across hours).
            Can you think like an attacker to catch them?" """,
            coding_concept="Algorithm design with time windows",
            security_concept="Advanced attack pattern recognition",
            language="python",
            starter_code="# Detect both:\n# - Fast attacks: >5 failures in 1 minute\n# - Slow attacks: >10 failures in 10 minutes",
            expected_output=None,
            hints=[
                "Track timestamps, not just counts",
                "Use sliding time windows",
                "Consider multiple attack patterns"
            ],
            is_locked=False,
            xp_reward=60,
            badge="Attack Detector"
        )
        
        missions["mission10"] = Mission(
            id="mission10",
            tier=3,
            tier_name="Threat Hunter",
            title="Final Challenge",
            description="Complete incident investigation",
            story="""This is it — your final test, Threat Hunter.
            
            Last weekend's anomalous activity triggered multiple alerts.
            We need a FULL investigation: timeline, attack vector,
            affected systems, and recommendations.
            
            Show us everything you've learned. """,
            coding_concept="Full investigation workflow",
            security_concept="Complete incident response",
            language="python",
            starter_code="# Investigate, analyze, report\n# Use Python, Bash, and log searches",
            expected_output=None,
            hints=[
                "Build a timeline first",
                "Identify the initial entry point",
                "Document everything for your report"
            ],
            is_locked=False,
            xp_reward=100,
            badge="Threat Hunter Elite"
        )
        
        return missions
    
    def get_all_missions(self) -> List[Mission]:
        """Get all missions as a list."""
        return list(self._missions.values())
    
    def get_mission(self, mission_id: str) -> Optional[Mission]:
        """Get a specific mission by ID."""
        return self._missions.get(mission_id)
    
    def get_progress(self) -> PlayerProgress:
        """Get current player progress."""
        return self._progress
    
    def complete_mission(self, mission_id: str) -> Dict:
        """Mark a mission as complete and award rewards."""
        mission = self.get_mission(mission_id)
        if not mission:
            return {"error": "Mission not found"}
        
        result = {}
        
        # Don't double-complete
        if mission_id not in self._progress.completed_missions:
            self._progress.completed_missions.append(mission_id)
            self._progress.total_xp += mission.xp_reward
            result["xp"] = mission.xp_reward
            
            # Award badge
            if mission.badge and mission.badge not in self._progress.badges:
                self._progress.badges.append(mission.badge)
                result["badge"] = mission.badge
            
            # Check for tier upgrades
            tier1_missions = ["mission01", "mission02", "mission03"]
            tier2_missions = ["mission04", "mission05", "mission06"]
            
            if all(m in self._progress.completed_missions for m in tier1_missions):
                if self._progress.current_tier < 2:
                    self._progress.current_tier = 2
                    self._progress.current_tier_name = "Analyst"
                    result["tier_unlocked"] = 2
            
            if all(m in self._progress.completed_missions for m in tier2_missions):
                if self._progress.current_tier < 3:
                    self._progress.current_tier = 3
                    self._progress.current_tier_name = "Threat Hunter"
                    result["tier_unlocked"] = 3
        
        return result
    
    def reset_progress(self):
        """Reset all progress (for debugging)."""
        self._progress = PlayerProgress(
            current_tier=1,
            current_tier_name="New Trainee",
            completed_missions=[],
            total_missions=len(self._missions),
            badges=[],
            total_xp=0
        )

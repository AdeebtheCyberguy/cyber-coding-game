"""
Cyber Coding Game - Python Sandbox (SAFE SIMULATION)

⚠️ CRITICAL SECURITY NOTICE:
This module does NOT execute real Python code!
It uses pattern matching and pre-defined outputs to simulate execution.

NEVER add:
- eval()
- exec()
- compile()
- __import__()

All "execution" is FAKE for educational purposes only.
"""

import re
from typing import Dict, Any
from ..models import ExecutionResult


class PythonSandbox:
    """
    Safe Python code simulation.
    
    This sandbox does NOT run real Python code.
    It analyzes the submitted code structurally and
    returns appropriate responses based on the mission.
    """
    
    def __init__(self):
        """Initialize the sandbox with mission solutions."""
        self.solutions = self._create_solution_patterns()
    
    def _create_solution_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Define expected patterns for each mission."""
        return {
            "mission01": {
                "patterns": [
                    r'print\s*\(\s*["\']Hello[,]?\s*World[!]?["\']\s*\)',
                    r'print\s*\(\s*["\']hello[,]?\s*world[!]?["\']\s*\)',
                ],
                "output": "Hello, World!",
                "success_feedback": "🎉 Amazing! You just wrote your first line of code! The print() function displays text on screen. You're officially a coder now!",
                "partial_patterns": [
                    (r'print\s*\(', "Good start! You have print() — now add a message in quotes inside the parentheses."),
                    (r'["\'].*["\']', "You have text in quotes — now wrap it with print() to display it!"),
                ]
            },
            "mission04": {
                "patterns": [
                    r'for\s+\w+\s+in\s+logs',
                    r'if.*failed',
                    r'print.*[Aa]lert',
                ],
                "requires_all": True,
                "output": "⚠️ ALERT: john has 6 failed logins!",
                "success_feedback": "🔥 Excellent work, Analyst! You just built a brute force detector. This same logic is used in real security tools!",
                "partial_patterns": [
                    (r'for\s+', "Good — you're using a loop! Now check each entry's status."),
                    (r'if\s+', "You have a condition — make sure you're checking if status == 'failed'."),
                    (r'["\']failed["\']', "You're looking for 'failed' — now count them per user!"),
                ]
            },
            "mission07": {
                "patterns": [
                    r'(auth|login|access)',
                    r'(time|hour|3:17|03:17)',
                ],
                "output": """Investigation Results:
━━━━━━━━━━━━━━━━━━━━━
Suspicious Activity at 03:17:22
User: svc_backup
IP: 10.0.50.99
Action: Database query executed
Files accessed: customers.db, transactions.db

Timeline:
03:15:01 - Failed SSH from 10.0.50.99
03:15:45 - Failed SSH from 10.0.50.99
03:16:30 - Successful SSH (svc_backup)
03:17:22 - Database access initiated
03:18:45 - Large data transfer detected
""",
                "success_feedback": "🕵️ Impressive investigation! You traced the attack from initial access to data exfiltration. Real incident responders follow this exact process!",
            },
            "mission08": {
                "patterns": [
                    r'execute\s*\(\s*query\s*,\s*\(',  # Parameterized query
                    r'\?\s*,\s*\?',  # Placeholders
                ],
                "output": "✅ Code is now secure! Using parameterized queries prevents SQL injection.",
                "success_feedback": "🔧 You fixed it! SQL injection is one of the most common vulnerabilities. You just learned how to prevent it!",
                "partial_patterns": [
                    (r'f["\'].*\{', "Careful — you're still using f-strings. That's the vulnerability! Use ? placeholders instead."),
                ]
            },
            "mission09": {
                "patterns": [
                    r'(timestamp|time|datetime)',
                    r'(window|minute|second)',
                    r'(count|len)',
                ],
                "requires_all": True,
                "output": """Detection Results:
━━━━━━━━━━━━━━━━━━━━━
🚨 Fast Attack Detected:
   User: admin, 12 attempts in 45 seconds

⚠️ Slow Attack Detected:
   User: root, 15 attempts over 8 minutes
""",
                "success_feedback": "🛡️ Outstanding! Your detector catches both attack styles. This is exactly how enterprise security tools work!",
            },
            "mission10": {
                "patterns": [
                    r'.',  # Any code counts as an attempt
                ],
                "output": """
═══════════════════════════════════════════════════════════
                    INCIDENT REPORT
═══════════════════════════════════════════════════════════

Prepared by: Security Analyst (You!)
Date: Investigation Complete

EXECUTIVE SUMMARY:
On the night in question, an unauthorized actor gained access
to internal systems using compromised service account credentials.

TIMELINE:
• 02:45 - Reconnaissance scanning detected
• 03:15 - Brute force attempts on SSH
• 03:16 - Successful login (svc_backup compromised)
• 03:17 - Database queries executed
• 03:18 - Data exfiltration (4.2GB)
• 03:22 - Attacker disconnected

ATTACK VECTOR:
Credential stuffing using previously leaked service account.

RECOMMENDATIONS:
1. Rotate all service account credentials
2. Implement MFA for all remote access
3. Add rate limiting to prevent brute force
4. Enhance after-hours monitoring

═══════════════════════════════════════════════════════════

🎉 CONGRATULATIONS! 🎉

You've completed the Cyber Coding Game!

From "Hello, World!" to full incident investigations,
you've grown into a true Cyber Defender.

Remember: Use your skills to PROTECT, never to harm.
The digital world needs defenders like you! 🛡️
""",
                "success_feedback": "🏆 You did it! You've completed every mission and proven yourself as a Threat Hunter. The cybersecurity community is lucky to have defenders like you!",
            }
        }
    
    def simulate(self, code: str, mission_id: str, tier: int = 1) -> ExecutionResult:
        """
        Simulate Python code execution.
        
        This does NOT run real code — it pattern matches
        to determine if the solution is correct.
        """
        # Get mission-specific patterns
        mission_config = self.solutions.get(mission_id, {})
        
        if not mission_config:
            # Default response for unknown missions
            return ExecutionResult(
                success=True,
                output="Code received! (No specific validation for this mission)",
                feedback="Your code looks good! Keep experimenting."
            )
        
        patterns = mission_config.get("patterns", [])
        requires_all = mission_config.get("requires_all", False)
        
        # Check for matches
        matches = []
        for pattern in patterns:
            if re.search(pattern, code, re.IGNORECASE):
                matches.append(pattern)
        
        # Determine success
        if requires_all:
            is_correct = len(matches) == len(patterns)
        else:
            is_correct = len(matches) > 0
        
        if is_correct:
            return ExecutionResult(
                success=True,
                output=mission_config.get("output", "Success!"),
                feedback=mission_config.get("success_feedback", "Great job!"),
                is_complete=True
            )
        
        # Check for partial progress
        partial_patterns = mission_config.get("partial_patterns", [])
        for pattern, hint in partial_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                return ExecutionResult(
                    success=False,
                    output="",
                    feedback=hint,
                    hints=self._get_tier_hints(tier, mission_id)
                )
        
        # No match at all
        return ExecutionResult(
            success=False,
            output="",
            feedback=self._get_encouragement(tier),
            hints=self._get_tier_hints(tier, mission_id)
        )
    
    def _get_encouragement(self, tier: int) -> str:
        """Get tier-appropriate encouragement."""
        if tier == 1:
            return "That's not quite right, but don't worry! Take a look at the hints below. You've got this! 💪"
        elif tier == 2:
            return "Not quite — check your logic and try again."
        else:
            return "Review your approach. Think about what the mission is asking for."
    
    def _get_tier_hints(self, tier: int, mission_id: str) -> list:
        """Get hints appropriate for the tier level."""
        if tier == 1:
            # Full hints for beginners
            return [
                "Start by looking at the example code provided",
                "Try running the code even if you're not sure — you'll learn from the output!",
                "Click 'Show Hint' if you get stuck"
            ]
        elif tier == 2:
            # Medium hints for analysts
            return [
                "Re-read the mission objectives",
                "Check your syntax carefully"
            ]
        else:
            # Minimal hints for threat hunters
            return ["Think about the core problem you're solving"]

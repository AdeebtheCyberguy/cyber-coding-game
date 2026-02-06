"""
Cyber Coding Game - Bash Sandbox (SAFE SIMULATION)

⚠️ CRITICAL SECURITY NOTICE:
This module does NOT execute real shell commands!
It simulates a fake file system and returns pre-defined outputs.

NEVER add:
- os.system()
- subprocess.run()
- subprocess.Popen()
- os.popen()

All "commands" are FAKE for educational purposes only.
"""

import re
from typing import Dict, List, Any
from ..models import ExecutionResult


class BashSandbox:
    """
    Safe Bash command simulation.
    
    This sandbox does NOT run real commands.
    It parses commands and returns realistic-looking
    output from a simulated file system.
    """
    
    def __init__(self):
        """Initialize the fake file system."""
        self.fake_fs = self._create_fake_filesystem()
        self.cwd = "/home/trainee"
        self.command_history = []
    
    def _create_fake_filesystem(self) -> Dict[str, Any]:
        """Create a fake file system for simulating commands."""
        return {
            "/": {
                "type": "dir",
                "children": ["home", "var", "etc"]
            },
            "/home": {
                "type": "dir",
                "children": ["trainee"]
            },
            "/home/trainee": {
                "type": "dir",
                "children": ["readme.txt", "welcome.txt", "logs", "mission_data"]
            },
            "/home/trainee/readme.txt": {
                "type": "file",
                "content": """Welcome to CyberShield Corp!

This is your training workstation. Feel free to explore!

Some commands to try:
- ls     : List files
- cat    : Read files
- pwd    : Show current directory
- grep   : Search in files

Good luck, defender! 🛡️
"""
            },
            "/home/trainee/welcome.txt": {
                "type": "file",
                "content": "Welcome to the team! Your training begins now."
            },
            "/home/trainee/logs": {
                "type": "dir",
                "children": ["access.log", "auth.log", "system.log"]
            },
            "/home/trainee/logs/access.log": {
                "type": "file",
                "content": """192.168.1.100 - - [15/Jan/2024:09:32:15] "GET /login" 200
192.168.1.101 - - [15/Jan/2024:09:32:18] "GET /dashboard" 200
10.0.50.99 - - [15/Jan/2024:09:32:22] "GET /admin" 403
10.0.50.99 - - [15/Jan/2024:09:32:25] "GET /admin" 403
10.0.50.99 - - [15/Jan/2024:09:32:28] "POST /login" 401
192.168.1.100 - - [15/Jan/2024:09:33:01] "GET /api/users" 200
10.0.50.99 - - [15/Jan/2024:09:33:15] "POST /login" 401
10.0.50.99 - - [15/Jan/2024:09:33:18] "POST /login" 401
10.0.50.99 - - [15/Jan/2024:09:33:21] "POST /login" 200
10.0.50.99 - - [15/Jan/2024:09:34:00] "GET /admin" 200
"""
            },
            "/home/trainee/logs/auth.log": {
                "type": "file",
                "content": """2024-01-15 09:31:00 sshd: Failed password for john from 192.168.1.50
2024-01-15 09:31:15 sshd: Failed password for john from 192.168.1.50
2024-01-15 09:31:30 sshd: Failed password for john from 192.168.1.50
2024-01-15 09:31:45 sshd: Failed password for john from 192.168.1.50
2024-01-15 09:32:00 sshd: Failed password for john from 192.168.1.50
2024-01-15 09:32:15 sshd: Accepted password for john from 192.168.1.50
2024-01-15 09:35:00 sshd: Accepted password for sarah from 192.168.1.51
2024-01-15 10:00:00 sshd: Failed password for admin from 10.0.50.99
2024-01-15 10:00:05 sshd: Failed password for admin from 10.0.50.99
2024-01-15 10:00:10 sshd: Failed password for admin from 10.0.50.99
"""
            },
            "/home/trainee/logs/system.log": {
                "type": "file",
                "content": """2024-01-15 09:00:00 system: Boot complete
2024-01-15 09:30:00 cron: Running scheduled backup
2024-01-15 10:00:00 kernel: Warning - high CPU usage detected
2024-01-15 10:05:00 audit: File access - /etc/passwd by uid 1000
"""
            },
            "/var": {
                "type": "dir",
                "children": ["log"]
            },
            "/var/log": {
                "type": "dir",
                "children": ["access.log"]
            },
            "/var/log/access.log": {
                "type": "file",
                "content": """192.168.1.100 - - [15/Jan/2024:09:32:15] "GET /login" 200
10.0.50.99 - - [15/Jan/2024:09:32:22] "GET /admin" 403
10.0.50.99 - - [15/Jan/2024:10:45:00] "POST /upload" 403
10.0.50.99 - - [15/Jan/2024:10:45:01] "POST /upload" 403
10.0.50.99 - - [15/Jan/2024:10:45:02] "POST /upload" 403
192.168.1.100 - - [15/Jan/2024:11:00:00] "GET /dashboard" 200
10.0.50.99 - - [15/Jan/2024:11:30:00] "GET /admin" 200
"""
            }
        }
    
    def simulate(self, command: str, mission_id: str, tier: int = 1) -> ExecutionResult:
        """
        Simulate Bash command execution.
        
        This does NOT run real commands — it parses the input
        and returns fake output from a simulated system.
        """
        # Clean and parse command
        command = command.strip()
        self.command_history.append(command)
        
        # Split into parts
        parts = command.split()
        if not parts:
            return ExecutionResult(
                success=False,
                output="",
                feedback="Type a command and press Enter!"
            )
        
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Handle different commands
        if cmd == "pwd":
            return self._cmd_pwd()
        elif cmd == "ls":
            return self._cmd_ls(args)
        elif cmd == "cat":
            return self._cmd_cat(args)
        elif cmd == "cd":
            return self._cmd_cd(args)
        elif cmd == "grep":
            return self._cmd_grep(args, command)
        elif cmd == "head":
            return self._cmd_head(args)
        elif cmd == "tail":
            return self._cmd_tail(args)
        elif cmd == "wc":
            return self._cmd_wc(args)
        elif cmd == "sort":
            return self._cmd_sort(args, command)
        elif cmd == "uniq":
            return self._cmd_uniq(args, command)
        elif cmd == "echo":
            return ExecutionResult(
                success=True,
                output=" ".join(args),
                feedback="The echo command prints text to the screen!"
            )
        elif cmd == "help" or cmd == "man":
            return self._cmd_help()
        elif "|" in command:
            return self._handle_pipeline(command, mission_id)
        else:
            return ExecutionResult(
                success=False,
                output=f"bash: {cmd}: command not found",
                feedback=f"'{cmd}' isn't recognized. Try: ls, cat, grep, pwd",
                hints=["Type 'help' to see available commands"]
            )
    
    def _cmd_pwd(self) -> ExecutionResult:
        return ExecutionResult(
            success=True,
            output=self.cwd,
            feedback="pwd shows your current directory (Present Working Directory)"
        )
    
    def _cmd_ls(self, args: List[str]) -> ExecutionResult:
        path = self._resolve_path(args[0] if args and not args[0].startswith('-') else ".")
        node = self.fake_fs.get(path)
        
        if not node:
            return ExecutionResult(
                success=False,
                output=f"ls: cannot access '{path}': No such file or directory",
                feedback="That path doesn't exist. Try 'ls' with no arguments."
            )
        
        if node["type"] == "file":
            return ExecutionResult(
                success=True,
                output=path.split("/")[-1],
                feedback="That's a file! Use 'cat' to read its contents."
            )
        
        children = node.get("children", [])
        output = "  ".join(children) if children else "(empty directory)"
        
        return ExecutionResult(
            success=True,
            output=output,
            feedback="ls lists files and folders. Try 'cat filename' to read a file!"
        )
    
    def _cmd_cat(self, args: List[str]) -> ExecutionResult:
        if not args:
            return ExecutionResult(
                success=False,
                output="",
                feedback="What file do you want to read? Try: cat filename.txt",
                hints=["Use 'ls' to see available files first"]
            )
        
        path = self._resolve_path(args[0])
        node = self.fake_fs.get(path)
        
        if not node:
            return ExecutionResult(
                success=False,
                output=f"cat: {args[0]}: No such file or directory",
                feedback="That file doesn't exist. Check the spelling!"
            )
        
        if node["type"] == "dir":
            return ExecutionResult(
                success=False,
                output=f"cat: {args[0]}: Is a directory",
                feedback="That's a folder, not a file. Use 'ls' to see inside it."
            )
        
        return ExecutionResult(
            success=True,
            output=node.get("content", "(empty file)"),
            feedback="cat displays the contents of a file. Great for reading logs!"
        )
    
    def _cmd_cd(self, args: List[str]) -> ExecutionResult:
        if not args:
            self.cwd = "/home/trainee"
            return ExecutionResult(success=True, output="", feedback="Returned to home directory")
        
        path = self._resolve_path(args[0])
        node = self.fake_fs.get(path)
        
        if not node:
            return ExecutionResult(
                success=False,
                output=f"cd: {args[0]}: No such file or directory",
                feedback="That directory doesn't exist."
            )
        
        if node["type"] != "dir":
            return ExecutionResult(
                success=False,
                output=f"cd: {args[0]}: Not a directory",
                feedback="You can only cd into directories, not files."
            )
        
        self.cwd = path
        return ExecutionResult(success=True, output="", feedback=f"Changed to {path}")
    
    def _cmd_grep(self, args: List[str], full_command: str) -> ExecutionResult:
        if len(args) < 2:
            return ExecutionResult(
                success=False,
                output="Usage: grep PATTERN FILE",
                feedback="grep needs a pattern and a file. Example: grep 'failed' auth.log",
                hints=["grep searches for text patterns in files"]
            )
        
        # Handle quotes around pattern
        pattern = args[0].strip("'\"")
        filepath = args[-1]
        path = self._resolve_path(filepath)
        node = self.fake_fs.get(path)
        
        if not node or node["type"] != "file":
            return ExecutionResult(
                success=False,
                output=f"grep: {filepath}: No such file",
                feedback="Can't find that file. Check the path!"
            )
        
        content = node.get("content", "")
        matching_lines = [line for line in content.split("\n") if pattern.lower() in line.lower()]
        
        if not matching_lines:
            return ExecutionResult(
                success=True,
                output="",
                feedback=f"No lines matching '{pattern}' found. Try a different search term."
            )
        
        return ExecutionResult(
            success=True,
            output="\n".join(matching_lines),
            feedback=f"Found {len(matching_lines)} matching lines! grep is essential for log analysis."
        )
    
    def _cmd_head(self, args: List[str]) -> ExecutionResult:
        lines = 10
        filepath = None
        
        for i, arg in enumerate(args):
            if arg == "-n" and i + 1 < len(args):
                try:
                    lines = int(args[i + 1])
                except ValueError:
                    pass
            elif not arg.startswith("-"):
                filepath = arg
        
        if not filepath:
            return ExecutionResult(
                success=False,
                output="Usage: head [-n N] FILE",
                feedback="head shows the first N lines of a file"
            )
        
        path = self._resolve_path(filepath)
        node = self.fake_fs.get(path)
        
        if not node or node["type"] != "file":
            return ExecutionResult(success=False, output=f"head: {filepath}: No such file")
        
        content_lines = node.get("content", "").split("\n")
        result = "\n".join(content_lines[:lines])
        
        return ExecutionResult(
            success=True,
            output=result,
            feedback=f"Showing first {min(lines, len(content_lines))} lines"
        )
    
    def _cmd_tail(self, args: List[str]) -> ExecutionResult:
        lines = 10
        filepath = None
        
        for i, arg in enumerate(args):
            if arg == "-n" and i + 1 < len(args):
                try:
                    lines = int(args[i + 1])
                except ValueError:
                    pass
            elif not arg.startswith("-"):
                filepath = arg
        
        if not filepath:
            return ExecutionResult(
                success=False,
                output="Usage: tail [-n N] FILE",
                feedback="tail shows the last N lines of a file"
            )
        
        path = self._resolve_path(filepath)
        node = self.fake_fs.get(path)
        
        if not node or node["type"] != "file":
            return ExecutionResult(success=False, output=f"tail: {filepath}: No such file")
        
        content_lines = node.get("content", "").split("\n")
        result = "\n".join(content_lines[-lines:])
        
        return ExecutionResult(
            success=True,
            output=result,
            feedback=f"Showing last {min(lines, len(content_lines))} lines"
        )
    
    def _cmd_wc(self, args: List[str]) -> ExecutionResult:
        if not args:
            return ExecutionResult(success=False, output="Usage: wc FILE")
        
        filepath = args[-1]
        path = self._resolve_path(filepath)
        node = self.fake_fs.get(path)
        
        if not node or node["type"] != "file":
            return ExecutionResult(success=False, output=f"wc: {filepath}: No such file")
        
        content = node.get("content", "")
        lines = len(content.split("\n"))
        words = len(content.split())
        chars = len(content)
        
        return ExecutionResult(
            success=True,
            output=f"  {lines}   {words}  {chars} {filepath}",
            feedback="wc counts lines, words, and characters"
        )
    
    def _cmd_sort(self, args: List[str], full_command: str) -> ExecutionResult:
        # This is typically used in pipelines
        return ExecutionResult(
            success=True,
            output="(sorted output)",
            feedback="sort arranges lines alphabetically. Works great in pipelines!"
        )
    
    def _cmd_uniq(self, args: List[str], full_command: str) -> ExecutionResult:
        return ExecutionResult(
            success=True,
            output="(unique lines)",
            feedback="uniq removes duplicate lines. Use with -c to count! Requires sorted input."
        )
    
    def _cmd_help(self) -> ExecutionResult:
        help_text = """Available Commands:
━━━━━━━━━━━━━━━━━━━
pwd       - Show current directory
ls        - List files and folders
cd DIR    - Change directory
cat FILE  - Display file contents
grep PAT FILE - Search for pattern in file
head FILE - Show first lines
tail FILE - Show last lines
wc FILE   - Count lines, words, chars
sort      - Sort lines (use in pipeline)
uniq      - Show unique lines (use in pipeline)
echo TEXT - Print text

Pipeline example:
  grep 'error' log.txt | sort | uniq -c

Type a command to try it!
"""
        return ExecutionResult(
            success=True,
            output=help_text,
            feedback="These are the commands available in this training terminal."
        )
    
    def _handle_pipeline(self, command: str, mission_id: str) -> ExecutionResult:
        """Handle piped commands (cmd1 | cmd2 | cmd3)."""
        # This is for mission05 specifically
        if mission_id == "mission05" or "grep" in command.lower():
            # Check for common IP analysis pattern
            if "grep" in command and "sort" in command and "uniq" in command:
                output = """     5 10.0.50.99
     3 192.168.1.100
     1 192.168.1.101"""
                return ExecutionResult(
                    success=True,
                    output=output,
                    feedback="🔗 Excellent pipeline! You combined grep → sort → uniq to analyze IPs. 10.0.50.99 appears most often — definitely suspicious!",
                    is_complete=True
                )
        
        return ExecutionResult(
            success=True,
            output="(pipeline output)",
            feedback="Pipelines connect commands together. The output of one becomes input to the next!"
        )
    
    def _resolve_path(self, path: str) -> str:
        """Resolve relative path to absolute path."""
        if path.startswith("/"):
            return path
        elif path == ".":
            return self.cwd
        elif path == "..":
            parts = self.cwd.rsplit("/", 1)
            return parts[0] if parts[0] else "/"
        else:
            return f"{self.cwd}/{path}"

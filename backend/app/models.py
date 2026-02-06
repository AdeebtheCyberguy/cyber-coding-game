"""
Cyber Coding Game - Data Models

Pydantic models for request/response validation.
These ensure all data is properly validated before processing.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class TierLevel(int, Enum):
    """Player progression tiers."""
    NEW_TRAINEE = 1
    ANALYST = 2
    THREAT_HUNTER = 3


class Mission(BaseModel):
    """A single mission/lesson in the game."""
    id: str = Field(..., description="Unique mission identifier")
    tier: int = Field(..., ge=1, le=3, description="Difficulty tier (1-3)")
    tier_name: str = Field(..., description="Human-readable tier name")
    title: str = Field(..., max_length=100, description="Mission title")
    description: str = Field(..., description="Brief mission description")
    story: str = Field(..., description="Narrative setup for the mission")
    coding_concept: str = Field(..., description="Programming skill taught")
    security_concept: str = Field(..., description="Security awareness taught")
    language: str = Field(..., description="Primary language: python, bash, lucene")
    starter_code: Optional[str] = Field(None, description="Starter code for the mission")
    expected_output: Optional[str] = Field(None, description="Expected output pattern")
    hints: List[str] = Field(default_factory=list, description="Available hints")
    is_locked: bool = Field(False, description="Whether mission requires previous completion")
    xp_reward: int = Field(10, description="XP awarded on completion")
    badge: Optional[str] = Field(None, description="Badge awarded on completion")


class MissionList(BaseModel):
    """List of missions with metadata."""
    missions: List[Mission]
    total: int


class CodeSubmission(BaseModel):
    """Code submitted by player for evaluation."""
    code: str = Field(
        ..., 
        max_length=10000,
        description="The code to evaluate"
    )
    mission_id: str = Field(..., description="Mission this submission is for")
    language: Optional[str] = Field(None, description="Code language (auto-detected if not provided)")


class ExecutionResult(BaseModel):
    """Result of code/command simulation."""
    success: bool = Field(..., description="Whether the solution is correct")
    output: str = Field(..., description="Simulated output")
    error: Optional[str] = Field(None, description="Error message if any")
    hints: List[str] = Field(default_factory=list, description="Hints for improvement")
    feedback: str = Field("", description="Tier-appropriate feedback message")
    is_complete: bool = Field(False, description="Whether mission is now complete")


class SearchQuery(BaseModel):
    """Lucene-style log search query."""
    query: str = Field(
        ..., 
        max_length=1000,
        description="Lucene-style search query"
    )
    mission_id: Optional[str] = Field(None, description="Mission context for the search")
    max_results: Optional[int] = Field(100, ge=1, le=100, description="Maximum results to return")


class LogEntry(BaseModel):
    """A single log entry."""
    timestamp: str
    level: str
    user: Optional[str] = None
    action: str
    status: str
    ip: Optional[str] = None
    details: Optional[str] = None


class SearchResult(BaseModel):
    """Result of a log search."""
    query: str
    total_matches: int
    results: List[LogEntry]
    is_correct: bool = Field(False, description="Whether query matches expected for mission")
    feedback: str = Field("", description="Feedback on the query")


class PlayerProgress(BaseModel):
    """Player's current progress in the game."""
    current_tier: int = Field(1, ge=1, le=3)
    current_tier_name: str = Field("New Trainee")
    completed_missions: List[str] = Field(default_factory=list)
    total_missions: int = Field(10)
    badges: List[str] = Field(default_factory=list)
    total_xp: int = Field(0)
    
    @property
    def completion_percentage(self) -> float:
        if self.total_missions == 0:
            return 0
        return (len(self.completed_missions) / self.total_missions) * 100


class CompletionRequest(BaseModel):
    """Request to mark a mission as complete."""
    mission_id: str = Field(..., description="Mission to mark complete")
    final_code: Optional[str] = Field(None, description="Player's final solution")

import { useState, useEffect } from 'react'
import { Routes, Route, Link, useLocation } from 'react-router-dom'
import HomePage from './pages/HomePage'
import MissionListPage from './pages/MissionListPage'
import MissionDetailPage from './pages/MissionDetailPage'

/**
 * Main Application Component
 * 
 * Handles routing and global state for the game.
 */
function App() {
    const [progress, setProgress] = useState({
        currentTier: 1,
        currentTierName: 'New Trainee',
        completedMissions: [],
        badges: [],
        totalXp: 0
    })

    const [user, setUser] = useState({
        name: 'Cyber Trainee',
        isLoggedIn: true
    })

    const location = useLocation()

    // Fetch progress from backend
    useEffect(() => {
        fetchProgress()
    }, [])

    const fetchProgress = async () => {
        try {
            const response = await fetch('/api/progress')
            if (response.ok) {
                const data = await response.json()
                setProgress({
                    currentTier: data.current_tier,
                    currentTierName: data.current_tier_name,
                    completedMissions: data.completed_missions || [],
                    badges: data.badges || [],
                    totalXp: data.total_xp || 0
                })
            }
        } catch (error) {
            console.log('Backend not available, using demo mode')
        }
    }

    const handleMissionComplete = (missionId, badge, xp) => {
        setProgress(prev => ({
            ...prev,
            completedMissions: [...prev.completedMissions, missionId],
            badges: badge ? [...prev.badges, badge] : prev.badges,
            totalXp: prev.totalXp + (xp || 0)
        }))
    }

    return (
        <div className="app">
            {/* Navigation */}
            <nav className="navbar">
                <Link to="/" className="nav-brand">
                    <span className="brand-icon">🛡️</span>
                    <span className="brand-text">Cyber Coding Game</span>
                </Link>

                <div className="nav-links">
                    <Link
                        to="/"
                        className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
                    >
                        <span className="nav-icon">🏠</span>
                        Home
                    </Link>
                    <Link
                        to="/missions"
                        className={`nav-link ${location.pathname.includes('/missions') ? 'active' : ''}`}
                    >
                        <span className="nav-icon">🎯</span>
                        Missions
                    </Link>
                    <Link
                        to="/progress"
                        className={`nav-link ${location.pathname === '/progress' ? 'active' : ''}`}
                    >
                        <span className="nav-icon">📊</span>
                        Progress
                    </Link>
                </div>

                <div className="nav-user">
                    <div className="user-avatar">{user.name.charAt(0)}</div>
                    <span className="user-name">{user.name}</span>
                    <span className="user-tier tier-badge" data-tier={progress.currentTier}>
                        {progress.currentTierName}
                    </span>
                </div>
            </nav>

            {/* Main Content */}
            <main className="main-content">
                <Routes>
                    <Route path="/" element={<HomePage progress={progress} />} />
                    <Route path="/missions" element={<MissionListPage progress={progress} />} />
                    <Route
                        path="/missions/:missionId"
                        element={
                            <MissionDetailPage
                                progress={progress}
                                onComplete={handleMissionComplete}
                            />
                        }
                    />
                    <Route path="/progress" element={<ProgressPage progress={progress} />} />
                </Routes>
            </main>

            {/* Footer */}
            <footer className="footer">
                <p>Made with 💚 for future cyber defenders</p>
                <p className="footer-note">
                    🔒 This is a safe, educational environment. All code execution is simulated.
                </p>
            </footer>
        </div>
    )
}

/**
 * Progress Page - Shows player achievements
 */
function ProgressPage({ progress }) {
    return (
        <div className="page progress-page">
            <div className="page-header">
                <h1>Your Progress</h1>
                <p>Track your journey from trainee to threat hunter!</p>
            </div>

            <div className="progress-stats">
                <div className="stat-card">
                    <div className="stat-icon">🎖️</div>
                    <div className="stat-value">{progress.currentTierName}</div>
                    <div className="stat-label">Current Rank</div>
                </div>
                <div className="stat-card">
                    <div className="stat-icon">✅</div>
                    <div className="stat-value">{progress.completedMissions.length}</div>
                    <div className="stat-label">Missions Complete</div>
                </div>
                <div className="stat-card">
                    <div className="stat-icon">⭐</div>
                    <div className="stat-value">{progress.totalXp}</div>
                    <div className="stat-label">Total XP</div>
                </div>
                <div className="stat-card">
                    <div className="stat-icon">🏅</div>
                    <div className="stat-value">{progress.badges.length}</div>
                    <div className="stat-label">Badges Earned</div>
                </div>
            </div>

            {progress.badges.length > 0 && (
                <div className="badges-section">
                    <h2>Your Badges</h2>
                    <div className="badges-grid">
                        {progress.badges.map((badge, index) => (
                            <div key={index} className="badge-item">
                                <div className="badge-icon">🏅</div>
                                <div className="badge-name">{badge}</div>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            <div className="tier-progression">
                <h2>Tier Progression</h2>
                <div className="tier-track">
                    <div className={`tier-node ${progress.currentTier >= 1 ? 'completed' : ''}`}>
                        <div className="tier-number">1</div>
                        <div className="tier-name">New Trainee</div>
                    </div>
                    <div className={`tier-connector ${progress.currentTier >= 2 ? 'completed' : ''}`}></div>
                    <div className={`tier-node ${progress.currentTier >= 2 ? 'completed' : ''}`}>
                        <div className="tier-number">2</div>
                        <div className="tier-name">Analyst</div>
                    </div>
                    <div className={`tier-connector ${progress.currentTier >= 3 ? 'completed' : ''}`}></div>
                    <div className={`tier-node ${progress.currentTier >= 3 ? 'completed' : ''}`}>
                        <div className="tier-number">3</div>
                        <div className="tier-name">Threat Hunter</div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default App

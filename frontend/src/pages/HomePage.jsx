import { Link } from 'react-router-dom'

/**
 * HomePage Component
 * 
 * The landing page that welcomes players and explains what the game is about.
 * Designed to be encouraging and accessible for complete beginners.
 */
function HomePage({ progress }) {
    const nextMission = progress.completedMissions.length + 1
    const hasStarted = progress.completedMissions.length > 0

    return (
        <div className="page home-page">
            {/* Hero Section */}
            <section className="hero">
                <div className="hero-badge">
                    ✨ Learn Cyber Security Through Coding
                </div>

                <h1 className="hero-title">
                    Become a <span className="accent">Cyber Defender</span>
                </h1>

                <p className="hero-subtitle">
                    Master Python, Bash, and security concepts through hands-on missions.
                    Start as a trainee, evolve into a threat hunter.
                </p>

                <div className="hero-buttons">
                    <Link to={`/missions/mission0${Math.min(nextMission, 10)}`} className="btn btn-primary">
                        ▶ {hasStarted ? 'Continue Training' : 'Start Training'}
                    </Link>
                    <Link to="/missions" className="btn btn-secondary">
                        View All Missions →
                    </Link>
                </div>
            </section>

            {/* Features Section */}
            <section className="features">
                <div className="features-header">
                    <h2>Why Cyber Coding Game?</h2>
                    <p>A safe, fun way to learn real security skills</p>
                </div>

                <div className="features-grid">
                    <div className="feature-card">
                        <div className="feature-icon cyan">💻</div>
                        <h3>Learn Real Skills</h3>
                        <p>
                            Python, JavaScript, Bash commands, and log searching —
                            all skills used by real security professionals.
                        </p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon green">🔒</div>
                        <h3>Safe Environment</h3>
                        <p>
                            Practice in a completely simulated world. No real systems
                            are ever at risk. Experiment freely!
                        </p>
                    </div>

                    <div className="feature-card">
                        <div className="feature-icon amber">⚡</div>
                        <h3>Progressive Learning</h3>
                        <p>
                            Start as a New Trainee with guided help, grow into a
                            Threat Hunter tackling complex challenges.
                        </p>
                    </div>
                </div>
            </section>

            {/* Journey Section */}
            <section className="journey-section">
                <div className="features-header">
                    <h2>Your Journey: Noob → Pro</h2>
                    <p>We meet you where you are and grow with you</p>
                </div>

                <div className="features-grid">
                    <div className="feature-card">
                        <div className="mission-tier tier-1" style={{ width: 'fit-content', marginBottom: '1rem' }}>
                            🟢 Tier 1
                        </div>
                        <h3>New Trainee</h3>
                        <p>
                            Never coded before? Perfect. We start with the basics —
                            clicking buttons, filling blanks, and celebrating every small win.
                            No scary jargon, just friendly guidance.
                        </p>
                    </div>

                    <div className="feature-card">
                        <div className="mission-tier tier-2" style={{ width: 'fit-content', marginBottom: '1rem' }}>
                            🟡 Tier 2
                        </div>
                        <h3>Analyst</h3>
                        <p>
                            Now you're writing real scripts! Count failed logins with Python,
                            search logs with Bash pipelines, and spot suspicious patterns.
                            You're building actual skills.
                        </p>
                    </div>

                    <div className="feature-card">
                        <div className="mission-tier tier-3" style={{ width: 'fit-content', marginBottom: '1rem' }}>
                            🔴 Tier 3
                        </div>
                        <h3>Threat Hunter</h3>
                        <p>
                            Investigate simulated incidents. Fix security vulnerabilities.
                            Think like a defender. You've come so far — now show what you've learned!
                        </p>
                    </div>
                </div>
            </section>

            {/* Current Progress */}
            {hasStarted && (
                <section className="progress-preview">
                    <div className="features-header">
                        <h2>Your Progress</h2>
                        <p>Keep going — you're doing great!</p>
                    </div>

                    <div className="progress-stats" style={{ maxWidth: '600px', margin: '0 auto' }}>
                        <div className="stat-card">
                            <div className="stat-icon">🎖️</div>
                            <div className="stat-value">{progress.currentTierName}</div>
                            <div className="stat-label">Current Rank</div>
                        </div>
                        <div className="stat-card">
                            <div className="stat-icon">✅</div>
                            <div className="stat-value">{progress.completedMissions.length}/10</div>
                            <div className="stat-label">Missions Complete</div>
                        </div>
                        <div className="stat-card">
                            <div className="stat-icon">⭐</div>
                            <div className="stat-value">{progress.totalXp} XP</div>
                            <div className="stat-label">Experience Points</div>
                        </div>
                    </div>
                </section>
            )}

            {/* CTA Section */}
            <section className="cta-section" style={{ textAlign: 'center', padding: '3rem 0' }}>
                <h2 style={{ marginBottom: '1rem' }}>Ready to Begin?</h2>
                <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
                    No experience needed. Just curiosity and a willingness to learn.
                </p>
                <Link to="/missions" className="btn btn-primary btn-lg">
                    🛡️ Start Your Training
                </Link>
            </section>
        </div>
    )
}

export default HomePage

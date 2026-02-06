import { Link } from 'react-router-dom'

function MissionCard({ mission, isCompleted }) {
    const langEmoji = { python: '🐍', bash: '💻', lucene: '🔍', javascript: '📜' }

    return (
        <Link to={`/missions/${mission.id}`} className={`mission-card ${isCompleted ? 'completed' : ''}`}>
            <div className="mission-header">
                <span className={`mission-tier tier-${mission.tier}`}>
                    {mission.tier === 1 ? '🟢' : mission.tier === 2 ? '🟡' : '🔴'} {mission.tier_name}
                </span>
                <span className="mission-status">{isCompleted ? '✅' : '▶'}</span>
            </div>
            <h3>{mission.title}</h3>
            <p>{mission.description}</p>
            <div className="mission-meta">
                <span className="mission-tag">{langEmoji[mission.language]} {mission.language}</span>
                <span className="mission-tag">⭐ {mission.xp_reward} XP</span>
            </div>
        </Link>
    )
}

export default MissionCard

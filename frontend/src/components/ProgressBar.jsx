function ProgressBar({ current, total, label }) {
    const percentage = total > 0 ? (current / total) * 100 : 0

    return (
        <div className="progress-container">
            {label && <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                <span style={{ fontSize: '0.875rem', color: 'var(--text-secondary)' }}>{label}</span>
                <span style={{ fontSize: '0.875rem', color: 'var(--accent-primary)' }}>{current}/{total}</span>
            </div>}
            <div className="progress-bar">
                <div className="progress-bar-fill" style={{ width: `${percentage}%` }} />
            </div>
        </div>
    )
}

export default ProgressBar

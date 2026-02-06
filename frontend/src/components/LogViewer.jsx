function LogViewer({ value, onChange }) {
    const sampleLogs = [
        { timestamp: '2024-01-15 09:32:15', level: 'INFO', message: 'user:john action:login status:success ip:192.168.1.50' },
        { timestamp: '2024-01-15 10:45:01', level: 'WARN', message: 'user:john action:login status:failed ip:10.0.50.99' },
        { timestamp: '2024-01-15 10:45:05', level: 'WARN', message: 'user:john action:login status:failed ip:10.0.50.99' },
        { timestamp: '2024-01-15 10:45:10', level: 'WARN', message: 'user:john action:login status:failed ip:10.0.50.99' },
        { timestamp: '2024-01-15 11:00:00', level: 'INFO', message: 'user:sarah action:login status:success ip:192.168.1.51' },
        { timestamp: '2024-01-15 23:15:00', level: 'WARN', message: 'user:admin action:login status:success ip:10.0.50.99 path:/admin' },
    ]

    return (
        <div className="log-viewer">
            <div className="log-viewer-header">
                <span>📋 Log Entries</span>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{sampleLogs.length} entries</span>
            </div>
            <div className="log-viewer-body">
                {sampleLogs.map((log, i) => (
                    <div key={i} className="log-entry">
                        <span className="log-timestamp">{log.timestamp}</span>
                        <span className={`log-level ${log.level}`}>{log.level}</span>
                        <span className="log-message">{log.message}</span>
                    </div>
                ))}
            </div>
            <div style={{ padding: '1rem', borderTop: '1px solid var(--glass-border)' }}>
                <input
                    type="text"
                    value={value}
                    onChange={(e) => onChange(e.target.value)}
                    placeholder="Enter search query... (e.g., status:failed)"
                    style={{ width: '100%', padding: '0.75rem', background: 'var(--bg-tertiary)', border: '1px solid var(--glass-border)', borderRadius: '8px', color: 'var(--text-primary)', fontFamily: 'var(--font-mono)' }}
                />
            </div>
        </div>
    )
}

export default LogViewer

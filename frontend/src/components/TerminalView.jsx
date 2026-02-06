function TerminalView({ value, onChange }) {
    return (
        <div className="terminal">
            <div className="terminal-header">
                <div className="terminal-title">🖥️ trainee@cybershield:~</div>
            </div>
            <div className="terminal-body">
                <div className="terminal-line">
                    <span className="terminal-output">Welcome to the CyberShield training terminal.</span>
                </div>
                <div className="terminal-line">
                    <span className="terminal-output">Type commands below and press Run.</span>
                </div>
            </div>
            <div className="terminal-input">
                <span className="terminal-prompt">$</span>
                <input
                    type="text"
                    value={value}
                    onChange={(e) => onChange(e.target.value)}
                    placeholder="Type your command here..."
                    maxLength={5000}
                />
            </div>
        </div>
    )
}

export default TerminalView

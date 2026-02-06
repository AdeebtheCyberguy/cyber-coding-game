function CodeEditor({ value, onChange, language = 'python' }) {
    const langLabels = { python: '🐍 Python', javascript: '📜 JavaScript', bash: '💻 Bash' }

    return (
        <div className="code-editor">
            <div className="code-editor-header">
                <div className="code-editor-dots">
                    <span className="code-editor-dot red"></span>
                    <span className="code-editor-dot yellow"></span>
                    <span className="code-editor-dot green"></span>
                </div>
                <div className="code-editor-title">{langLabels[language] || language}</div>
            </div>
            <textarea
                value={value}
                onChange={(e) => onChange(e.target.value)}
                placeholder={`# Write your ${language} code here...\n`}
                spellCheck="false"
                maxLength={10000}
            />
        </div>
    )
}

export default CodeEditor

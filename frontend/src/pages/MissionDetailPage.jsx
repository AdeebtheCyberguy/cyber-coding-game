import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import CodeEditor from '../components/CodeEditor'
import TerminalView from '../components/TerminalView'
import LogViewer from '../components/LogViewer'
import getApiUrl from '../utils/api'

function MissionDetailPage({ progress, onComplete }) {
    const { missionId } = useParams()
    const [mission, setMission] = useState(null)
    const [code, setCode] = useState('')
    const [result, setResult] = useState(null)
    const [showHints, setShowHints] = useState(false)
    const [loading, setLoading] = useState(true)
    const [submitting, setSubmitting] = useState(false)

    useEffect(() => { fetchMission() }, [missionId])

    const fetchMission = async () => {
        try {
            const response = await fetch(getApiUrl(`/api/missions/${missionId}`))
            if (response.ok) {
                const data = await response.json()
                setMission(data)
                setCode(data.starter_code || '')
            }
        } catch (error) {
            setMission(getDemoMission(missionId))
        } finally {
            setLoading(false)
        }
    }

    const getDemoMission = (id) => ({
        id, tier: 1, tier_name: 'New Trainee', title: 'Your First Line of Code',
        description: 'Learn to print messages in Python',
        story: 'Welcome to CyberShield Corp! Your mentor Alex says: "Let\'s start simple. Make the computer say Hello, World!"',
        coding_concept: 'Variables and print()', security_concept: 'Automation helps defenders',
        language: 'python', starter_code: '# Type your code below:\nprint("Hello, World!")',
        hints: ['Use print() to display text', 'Put message in quotes', 'Check spelling carefully'],
        xp_reward: 10, badge: 'Terminal Trainee'
    })

    const handleSubmit = async () => {
        setSubmitting(true)
        try {
            const endpoint = mission.language === 'bash' ? '/api/run/bash' : mission.language === 'lucene' ? '/api/search/logs' : '/api/run/python'
            const body = mission.language === 'lucene' ? { query: code, mission_id: missionId } : { code, mission_id: missionId }
            const response = await fetch(getApiUrl(endpoint), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
            if (response.ok) {
                const data = await response.json()
                setResult(data)
                if (data.success || data.is_complete) onComplete(missionId, mission.badge, mission.xp_reward)
            }
        } catch (error) {
            setResult({ success: code.includes('print') && code.includes('Hello'), output: 'Hello, World!', feedback: code.includes('Hello') ? '🎉 You did it!' : 'Try again!' })
            if (code.includes('Hello')) onComplete(missionId, mission?.badge, mission?.xp_reward)
        } finally {
            setSubmitting(false)
        }
    }

    if (loading) return <div className="page" style={{ textAlign: 'center', padding: '4rem' }}>Loading...</div>
    if (!mission) return <div className="page"><h1>Mission not found</h1><Link to="/missions">← Back</Link></div>

    const isCompleted = progress.completedMissions.includes(missionId)

    return (
        <div className="page mission-detail-page">
            <div className="page-header">
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', justifyContent: 'center', marginBottom: '0.5rem' }}>
                    <span className={`mission-tier tier-${mission.tier}`}>{mission.tier_name}</span>
                    {isCompleted && <span style={{ color: 'var(--success)' }}>✅ Completed</span>}
                </div>
                <h1>{mission.title}</h1>
                <p>{mission.description}</p>
            </div>

            <div className="mission-detail">
                <div className="mission-content">
                    <div className="story-panel"><h3>📖 Mission Briefing</h3><p className="story-text">{mission.story}</p></div>

                    <div className="learning-goals" style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
                        <div className="mission-tag">💻 {mission.coding_concept}</div>
                        <div className="mission-tag">🔒 {mission.security_concept}</div>
                        <div className="mission-tag">⭐ {mission.xp_reward} XP</div>
                    </div>

                    {mission.language === 'python' && <CodeEditor value={code} onChange={setCode} language="python" />}
                    {mission.language === 'bash' && <TerminalView value={code} onChange={setCode} />}
                    {mission.language === 'lucene' && <LogViewer value={code} onChange={setCode} />}

                    <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
                        <button className="btn btn-primary" onClick={handleSubmit} disabled={submitting}>{submitting ? 'Running...' : '▶ Run Code'}</button>
                        <button className="btn btn-secondary" onClick={() => setShowHints(!showHints)}>{showHints ? 'Hide Hints' : '💡 Show Hints'}</button>
                    </div>

                    {result && (
                        <div className={`feedback-panel ${result.success ? 'success' : 'error'}`}>
                            {result.output && <pre style={{ fontFamily: 'var(--font-mono)', marginBottom: '0.5rem' }}>{result.output}</pre>}
                            <p>{result.feedback}</p>
                            {result.success && mission.badge && <p style={{ marginTop: '0.5rem' }}>🏅 Badge earned: {mission.badge}</p>}
                        </div>
                    )}
                </div>

                <div className="mission-sidebar">
                    {showHints && mission.hints && (
                        <div className="hint-panel"><h3>💡 Hints</h3><ul className="hint-list">{mission.hints.map((h, i) => <li key={i}>{h}</li>)}</ul></div>
                    )}
                    <div style={{ padding: '1rem' }}><Link to="/missions" className="btn btn-outline" style={{ width: '100%', justifyContent: 'center' }}>← All Missions</Link></div>
                </div>
            </div>
        </div>
    )
}

export default MissionDetailPage

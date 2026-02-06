import { useState, useEffect } from 'react'
import MissionCard from '../components/MissionCard'

function MissionListPage({ progress }) {
    const [missions, setMissions] = useState([])
    const [loading, setLoading] = useState(true)
    const [filter, setFilter] = useState('all')

    useEffect(() => { fetchMissions() }, [])

    const fetchMissions = async () => {
        try {
            const response = await fetch('/api/missions')
            if (response.ok) {
                const data = await response.json()
                setMissions(data.missions)
            }
        } catch (error) {
            setMissions(getDemoMissions())
        } finally {
            setLoading(false)
        }
    }

    const getDemoMissions = () => [
        { id: 'mission01', tier: 1, tier_name: 'New Trainee', title: 'Your First Line of Code', description: 'Learn to print messages in Python', language: 'python', xp_reward: 10 },
        { id: 'mission02', tier: 1, tier_name: 'New Trainee', title: 'Meet the Terminal', description: 'Learn basic Bash commands', language: 'bash', xp_reward: 10 },
        { id: 'mission03', tier: 1, tier_name: 'New Trainee', title: 'What Are Logs?', description: 'Search through system logs', language: 'lucene', xp_reward: 15 },
        { id: 'mission04', tier: 2, tier_name: 'Analyst', title: 'Build a Log Scanner', description: 'Detect suspicious login patterns', language: 'python', xp_reward: 25 },
        { id: 'mission05', tier: 2, tier_name: 'Analyst', title: 'Bash Pipeline Power', description: 'Chain commands to analyze logs', language: 'bash', xp_reward: 25 },
        { id: 'mission06', tier: 2, tier_name: 'Analyst', title: 'Advanced Log Hunting', description: 'Complex queries for patterns', language: 'lucene', xp_reward: 30 },
        { id: 'mission07', tier: 3, tier_name: 'Threat Hunter', title: 'The Midnight Breach', description: 'Investigate a security incident', language: 'python', xp_reward: 50 },
        { id: 'mission08', tier: 3, tier_name: 'Threat Hunter', title: 'Fix the Vulnerable Code', description: 'Find and fix vulnerabilities', language: 'python', xp_reward: 50 },
        { id: 'mission09', tier: 3, tier_name: 'Threat Hunter', title: 'Build a Brute Force Detector', description: 'Create detection algorithm', language: 'python', xp_reward: 60 },
        { id: 'mission10', tier: 3, tier_name: 'Threat Hunter', title: 'Final Challenge', description: 'Complete investigation', language: 'python', xp_reward: 100 }
    ]

    const filteredMissions = missions.filter(m => filter === 'all' || m.tier === parseInt(filter))
    const tierStats = { 1: missions.filter(m => m.tier === 1).length, 2: missions.filter(m => m.tier === 2).length, 3: missions.filter(m => m.tier === 3).length }

    if (loading) return <div className="page" style={{ textAlign: 'center', padding: '4rem' }}><div className="loading">Loading...</div></div>

    return (
        <div className="page mission-list-page">
            <div className="page-header"><h1>Missions</h1><p>Choose your challenge!</p></div>
            <div className="filter-tabs">
                <button className={`filter-tab ${filter === 'all' ? 'active' : ''}`} onClick={() => setFilter('all')}>All ({missions.length})</button>
                <button className={`filter-tab ${filter === '1' ? 'active' : ''}`} onClick={() => setFilter('1')}>🟢 Trainee ({tierStats[1]})</button>
                <button className={`filter-tab ${filter === '2' ? 'active' : ''}`} onClick={() => setFilter('2')}>🟡 Analyst ({tierStats[2]})</button>
                <button className={`filter-tab ${filter === '3' ? 'active' : ''}`} onClick={() => setFilter('3')}>🔴 Hunter ({tierStats[3]})</button>
            </div>
            <div className="progress-bar" style={{ marginBottom: '2rem' }}><div className="progress-bar-fill" style={{ width: `${(progress.completedMissions.length / missions.length) * 100}%` }} /></div>
            <div className="missions-grid">{filteredMissions.map(m => <MissionCard key={m.id} mission={m} isCompleted={progress.completedMissions.includes(m.id)} />)}</div>
        </div>
    )
}

export default MissionListPage

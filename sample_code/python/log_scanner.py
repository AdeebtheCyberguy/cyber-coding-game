"""
Log Scanner - Educational Example
==================================
A basic Python script that analyzes log entries for suspicious patterns.

This demonstrates:
- Reading and processing log data
- Using dictionaries to count occurrences
- Conditional logic for threat detection
"""

# Sample log data (in real life, this would come from a file or API)
logs = [
    {"timestamp": "2024-01-15 10:45:01", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:05", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:10", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:15", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:20", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 10:45:25", "user": "john", "action": "login", "status": "failed", "ip": "10.0.50.99"},
    {"timestamp": "2024-01-15 11:00:00", "user": "sarah", "action": "login", "status": "success", "ip": "192.168.1.51"},
    {"timestamp": "2024-01-15 11:15:00", "user": "john", "action": "login", "status": "success", "ip": "192.168.1.50"},
]


def count_failed_logins(log_entries):
    """
    Count failed login attempts per user.
    
    Args:
        log_entries: List of log dictionaries
        
    Returns:
        Dictionary mapping usernames to failure counts
    """
    failed_counts = {}
    
    for entry in log_entries:
        # Only count failed login attempts
        if entry["action"] == "login" and entry["status"] == "failed":
            user = entry["user"]
            # Increment count (or initialize to 1)
            if user in failed_counts:
                failed_counts[user] += 1
            else:
                failed_counts[user] = 1
    
    return failed_counts


def detect_brute_force(failed_counts, threshold=5):
    """
    Identify potential brute force attacks.
    
    Args:
        failed_counts: Dictionary of user -> failure count
        threshold: Number of failures that triggers an alert
        
    Returns:
        List of suspicious users
    """
    suspicious = []
    
    for user, count in failed_counts.items():
        if count > threshold:
            suspicious.append({
                "user": user,
                "failed_attempts": count,
                "reason": "Exceeded failure threshold"
            })
    
    return suspicious


def main():
    """Main function to run the log scanner."""
    print("=" * 50)
    print("🔍 LOG SCANNER - Educational Tool")
    print("=" * 50)
    print()
    
    # Count failed logins
    failures = count_failed_logins(logs)
    print("📊 Failed Login Counts:")
    for user, count in failures.items():
        print(f"   {user}: {count} failures")
    print()
    
    # Detect possible attacks
    suspicious = detect_brute_force(failures)
    
    if suspicious:
        print("⚠️  ALERTS:")
        for alert in suspicious:
            print(f"   🚨 {alert['user']}: {alert['failed_attempts']} failed attempts")
            print(f"      Reason: {alert['reason']}")
    else:
        print("✅ No suspicious activity detected.")
    
    print()
    print("=" * 50)


if __name__ == "__main__":
    main()

#!/bin/bash
# ===========================================
# Log Analysis Script - Educational Example
# ===========================================
# Demonstrates Bash pipelines for log analysis
#
# IMPORTANT: This uses simulated log data.
# Real log analysis would use actual log files.
# ===========================================

echo "=============================================="
echo "📋 LOG ANALYSIS TOOLS"
echo "=============================================="
echo ""

# Create sample log data
cat << 'EOF' > /tmp/sample_access.log
2024-01-15 10:45:01 WARN user:john action:login status:failed ip:10.0.50.99
2024-01-15 10:45:05 WARN user:john action:login status:failed ip:10.0.50.99
2024-01-15 10:45:10 WARN user:john action:login status:failed ip:10.0.50.99
2024-01-15 10:45:15 WARN user:john action:login status:failed ip:10.0.50.99
2024-01-15 10:45:20 WARN user:john action:login status:failed ip:10.0.50.99
2024-01-15 10:45:25 WARN user:john action:login status:failed ip:10.0.50.99
2024-01-15 11:00:00 INFO user:sarah action:login status:success ip:192.168.1.51
2024-01-15 11:15:00 INFO user:john action:login status:success ip:192.168.1.50
2024-01-15 12:00:00 INFO user:admin action:access status:success ip:192.168.1.100
2024-01-15 23:15:00 WARN user:admin action:access status:success ip:10.0.50.99 path:/admin
EOF

LOG_FILE="/tmp/sample_access.log"

echo "📊 Sample Log Data:"
echo "-------------------------------------------"
cat $LOG_FILE
echo ""
echo "-------------------------------------------"
echo ""

# Analysis 1: Count by status
echo "1️⃣ COUNT BY STATUS:"
echo "   Command: grep -oE 'status:[a-z]+' $LOG_FILE | sort | uniq -c"
echo ""
grep -oE 'status:[a-z]+' $LOG_FILE | sort | uniq -c
echo ""

# Analysis 2: Find failed logins
echo "2️⃣ FAILED LOGIN ATTEMPTS:"
echo "   Command: grep 'status:failed' $LOG_FILE"
echo ""
grep 'status:failed' $LOG_FILE
echo ""

# Analysis 3: Top IPs
echo "3️⃣ TOP IP ADDRESSES:"
echo "   Command: grep -oE 'ip:[0-9.]+' | sort | uniq -c | sort -rn"
echo ""
grep -oE 'ip:[0-9.]+' $LOG_FILE | sort | uniq -c | sort -rn
echo ""

# Analysis 4: Off-hours activity
echo "4️⃣ OFF-HOURS ACTIVITY (after 11 PM):"
echo "   Command: grep '^2024-01-15 2[3]' $LOG_FILE"
echo ""
grep '^2024-01-15 2[3]' $LOG_FILE
echo ""

# Cleanup
rm -f /tmp/sample_access.log

echo "=============================================="
echo "✅ Analysis Complete"
echo "=============================================="
echo ""
echo "💡 Key Takeaways:"
echo "   - Use grep to filter specific patterns"
echo "   - Use sort and uniq -c to count occurrences"
echo "   - Pipe (|) commands together for complex analysis"
echo "   - Look for anomalies: many failures, off-hours access"

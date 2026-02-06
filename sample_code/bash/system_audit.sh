#!/bin/bash
# ===========================================
# System Audit Script - Educational Example
# ===========================================
# Basic system checks for security review
#
# IMPORTANT: This is an educational script.
# In real environments, use proper security tools.
# ===========================================

echo "=============================================="
echo "🔍 SYSTEM SECURITY AUDIT"
echo "=============================================="
echo ""

# Current date and time
echo "📅 Audit Time: $(date)"
echo ""

# System information
echo "💻 SYSTEM INFO:"
echo "   Hostname: $(hostname)"
echo "   OS: $(uname -s) $(uname -r)"
echo "   User: $(whoami)"
echo ""

# Users with shell access
echo "👥 USERS WITH SHELL ACCESS:"
grep -E '/bin/(bash|sh|zsh)' /etc/passwd 2>/dev/null | cut -d: -f1 | while read user; do
    echo "   - $user"
done
echo ""

# Recently modified files in sensitive directories
echo "📁 RECENTLY MODIFIED (last 24h in /etc):"
find /etc -mtime -1 -type f 2>/dev/null | head -10 | while read file; do
    echo "   $file"
done
echo ""

# Open network ports
echo "🌐 LISTENING PORTS:"
netstat -tlnp 2>/dev/null | tail -n +3 | head -10 || ss -tlnp 2>/dev/null | tail -n +2 | head -10
echo ""

# Failed login attempts
echo "❌ RECENT FAILED LOGINS:"
lastb 2>/dev/null | head -5 || echo "   (lastb not available)"
echo ""

# Disk usage
echo "💾 DISK USAGE:"
df -h | head -5
echo ""

echo "=============================================="
echo "✅ Audit Complete"
echo "=============================================="

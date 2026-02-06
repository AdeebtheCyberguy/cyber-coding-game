/**
 * XSS Prevention - Educational Example
 * =====================================
 * Demonstrates safe HTML rendering to prevent Cross-Site Scripting.
 */

// ============================================
// THE PROBLEM: XSS Attacks
// ============================================

/*
Cross-Site Scripting (XSS) occurs when an attacker injects malicious
scripts into web pages viewed by other users.

Example:
If a user can submit comments, and you display them like this:
  element.innerHTML = userInput;

An attacker could submit:
  <script>stealCookies()</script>

And their script would run in every user's browser!
*/


// ============================================
// SAFE FUNCTIONS
// ============================================

/**
 * Escape HTML special characters to prevent XSS.
 * 
 * @param {string} text - Raw user input
 * @returns {string} - Safe HTML-escaped string
 */
function escapeHtml(text) {
    if (!text) return '';

    const escapeMap = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };

    return text.replace(/[&<>"']/g, char => escapeMap[char]);
}


/**
 * Safely set text content (preferred method).
 * 
 * @param {HTMLElement} element - DOM element
 * @param {string} text - Text to display
 */
function safeSetText(element, text) {
    // textContent is inherently safe - never interprets HTML
    element.textContent = text;
}


/**
 * Safely add user content to the page.
 * 
 * @param {string} containerId - ID of container element
 * @param {string} userInput - Raw user input
 */
function displayUserComment(containerId, userInput) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Create a safe text node
    const comment = document.createElement('div');
    comment.className = 'user-comment';

    // Use textContent, NOT innerHTML
    comment.textContent = userInput;

    container.appendChild(comment);
}


// ============================================
// EXAMPLES
// ============================================

function demoXssPrevention() {
    const maliciousInput = '<script>alert("XSS!")</script>';

    console.log('='.repeat(50));
    console.log('🛡️ XSS PREVENTION DEMO');
    console.log('='.repeat(50));
    console.log('');

    console.log('Malicious input:', maliciousInput);
    console.log('');

    console.log('❌ UNSAFE (innerHTML):');
    console.log('   element.innerHTML = maliciousInput');
    console.log('   Result: Script executes!');
    console.log('');

    console.log('✅ SAFE (textContent):');
    console.log('   element.textContent = maliciousInput');
    console.log('   Result:', maliciousInput, '(displayed as text, not executed)');
    console.log('');

    console.log('✅ SAFE (escape then innerHTML):');
    console.log('   element.innerHTML = escapeHtml(maliciousInput)');
    console.log('   Result:', escapeHtml(maliciousInput));
    console.log('');

    console.log('='.repeat(50));
    console.log('💡 Key Takeaway: NEVER use innerHTML with user input!');
    console.log('='.repeat(50));
}


// Run demo
demoXssPrevention();


// ============================================
// BEST PRACTICES SUMMARY
// ============================================

/*
XSS Prevention Checklist:

✅ DO:
  - Use textContent instead of innerHTML
  - Escape HTML entities when HTML is required
  - Validate and sanitize all user input
  - Use Content-Security-Policy headers
  - Use frameworks with built-in escaping (React, Vue)

❌ DON'T:
  - Never use innerHTML with user input
  - Never use eval() with user data
  - Never create script elements from user input
  - Never use document.write() with user data
*/


// Export for use in other modules
if (typeof module !== 'undefined') {
    module.exports = { escapeHtml, safeSetText, displayUserComment };
}

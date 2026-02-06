/**
 * API Configuration
 * 
 * Determines the backend URL based on the environment.
 * - In development: Uses the proxy set in vite.config.js (relative path)
 * - In production: Uses the VITE_API_URL environment variable provided by Render
 */

// If VITE_API_URL is set (production), use it. 
// Otherwise fall back to empty string to use the relative proxy path.
const BASE_URL = import.meta.env.VITE_API_URL || '';

/**
 * Helper to construct full API URLs
 * @param {string} endpoint - The API endpoint (e.g., '/api/missions')
 * @returns {string} The full URL
 */
export const getApiUrl = (endpoint) => {
    // Remove leading slash if present to avoid double slashes when joining
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint.substring(1) : endpoint;

    // Ensure BASE_URL doesn't have trailing slash if we're adding one
    const cleanBase = BASE_URL.endsWith('/') ? BASE_URL.slice(0, -1) : BASE_URL;

    // If no base URL (dev mode proxy), return relative path
    if (!cleanBase) return `/${cleanEndpoint}`;

    return `${cleanBase}/${cleanEndpoint}`;
};

export default getApiUrl;

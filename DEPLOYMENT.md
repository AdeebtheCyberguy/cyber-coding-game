# 🚀 Deployment Guide (Render.com)

This guide shows you how to deploy your **Cyber Coding Game** for free using Render.

---

## 1️⃣ Create a Render Account

1. Go to [dashboard.render.com](https://dashboard.render.com/).
2. Sign up with your **GitHub** account (this makes connecting your repo easy).

---

## 2️⃣ Connect Your Repository

1. Click the **"New +"** button (top right).
2. Select **"Blueprint"** (this is the magic option!).
3. Under "Connect a repository", find `cyber-coding-game` and click **Connect**.
4. Give Render permission if asked.

---

## 3️⃣ Deploy

1. Render will automatically find the `render.yaml` file we created.
2. It will show you two services it's going to build:
   - `cyber-game-backend` (Python)
   - `cyber-game-frontend` (Static Site)
3. Click **"Apply"** or **"Create Resources"**.

---

## 4️⃣ Wait for Build

Render will now build your app. This takes about 2-3 minutes.

- You can watch the logs streaming.
- Once done, you'll see a green **"Deploy Succeeded"** badge.

---

## 5️⃣ Play & Share

1. Go to your **Dashboard**.
2. Click on the `cyber-game-frontend` service.
3. Click the URL (e.g., `https://cyber-game-frontend.onrender.com`).
4. **Share that link with the world!** 🌍

---

### Troubleshooting

- **Build Failed?** Check the "Logs" tab to see what went wrong.
- **Backend Error?** Ensure the backend service is "Live" before checking the frontend.

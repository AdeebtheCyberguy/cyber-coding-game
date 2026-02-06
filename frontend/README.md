# ⚛️ Frontend - Cyber Coding Game

This is the React frontend for the Cyber Coding Game. It provides the user interface where players complete missions and learn cybersecurity through coding.

---

## 🚀 Quick Setup

### Prerequisites

- **Node.js 18+** — [Download here](https://nodejs.org/)

### Installation

```bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The app will be available at: **<http://localhost:5173>**

---

## 📁 Project Structure

```
frontend/
├── README.md           ← You are here!
├── package.json        ← Dependencies and scripts
├── vite.config.js      ← Vite configuration
├── index.html          ← Entry point
└── src/
    ├── main.jsx        ← React entry point
    ├── App.jsx         ← Main application component
    ├── components/     ← Reusable UI components
    │   ├── CodeEditor.jsx
    │   ├── TerminalView.jsx
    │   ├── LogViewer.jsx
    │   ├── MissionCard.jsx
    │   └── ProgressBar.jsx
    ├── pages/          ← Page components
    │   ├── HomePage.jsx
    │   ├── MissionListPage.jsx
    │   └── MissionDetailPage.jsx
    └── styles/
        └── main.css    ← Global styles
```

---

## 📦 Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |
| `npm run lint` | Run ESLint |

---

## 🎨 Design System

The UI uses a premium dark theme with:

- **Background**: Deep navy gradient (`#0a0f1a` → `#111827`)
- **Accent**: Cyan/turquoise (`#00d4aa`, `#06b6d4`)
- **Typography**: Inter font family
- **Effects**: Glassmorphism, subtle animations

---

## 🔒 Security Notes

### Frontend Security Rules

1. **Never use `eval()`** on any data
2. **Always escape user content** before rendering
3. **Validate on the client AND server** — client validation is for UX, server is for security
4. **Don't expose internal errors** — show generic messages to users

### Data Handling

- All code "execution" happens on the backend
- Frontend only displays results
- User input is validated before submission

---

## 🆘 Troubleshooting

### "Module not found"

```bash
rm -rf node_modules package-lock.json
npm install
```

### "Port 5173 already in use"

```bash
npm run dev -- --port 5174
```

### "CORS error"

Make sure the backend is running on port 8000.

---

## 🤝 Contributing

When modifying the frontend:

1. Follow the existing component patterns
2. Use CSS variables for theming
3. Keep components focused and small
4. Test on both desktop and mobile viewports

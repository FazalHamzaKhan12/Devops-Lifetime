const express = require("express");

const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send(`<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>DEVOPS-110</title>
    <style>
      :root {
        color-scheme: dark;
        --bg: #08111d;
        --panel: rgba(14, 24, 40, 0.9);
        --text: #eef4ff;
        --muted: #a7b8d1;
        --accent: #7cf0c7;
        --accent-2: #8aa8ff;
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        padding: 24px;
        font-family: Inter, Segoe UI, Arial, sans-serif;
        color: var(--text);
        background:
          radial-gradient(circle at top, rgba(124, 240, 199, 0.14), transparent 30%),
          radial-gradient(circle at bottom right, rgba(138, 168, 255, 0.12), transparent 28%),
          linear-gradient(135deg, #050a11, var(--bg));
      }

      .card {
        width: min(760px, 100%);
        padding: 48px;
        border-radius: 28px;
        background: var(--panel);
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 24px 80px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(12px);
      }

      .eyebrow {
        color: var(--accent);
        letter-spacing: 0.28em;
        text-transform: uppercase;
        font-size: 0.78rem;
        margin-bottom: 18px;
      }

      h1 {
        margin: 0;
        font-size: clamp(2.4rem, 7vw, 4.5rem);
        line-height: 0.95;
      }

      .accent {
        color: var(--accent);
      }

      .sub {
        margin: 20px 0 0;
        color: var(--muted);
        line-height: 1.75;
        font-size: 1.05rem;
      }

      .badge {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        margin-top: 28px;
        padding: 12px 18px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.05);
      }

      .dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 18px rgba(124, 240, 199, 0.75);
      }

      code {
        color: var(--accent-2);
      }
    </style>
  </head>
  <body>
    <main class="card">
      <div class="eyebrow">DEVOPS-110</div>
      <h1>Multi-Stage<br /><span class="accent">Docker Build</span></h1>
      <p class="sub">Node.js application is running successfully.</p>
      <div class="badge"><span class="dot"></span> Listening on port <code>${port}</code></div>
    </main>
  </body>
</html>`);
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Server listening on port ${port}`);
});


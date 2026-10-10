from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>DEVOPS-109</title>
        <style>
          :root {
            color-scheme: dark;
            --bg: #07111d;
            --panel: #0e1b2e;
            --text: #eef4ff;
            --muted: #9bb0ca;
            --accent: #6fe7c8;
            --accent-2: #85a7ff;
          }

          * {
            box-sizing: border-box;
          }

          body {
            margin: 0;
            min-height: 100vh;
            display: grid;
            place-items: center;
            font-family: Inter, Segoe UI, Arial, sans-serif;
            background:
              radial-gradient(circle at top, rgba(111, 231, 200, 0.14), transparent 35%),
              linear-gradient(135deg, #050b13, var(--bg));
            color: var(--text);
          }

          .card {
            width: min(720px, calc(100vw - 32px));
            padding: 48px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            background: rgba(14, 27, 46, 0.92);
            box-shadow: 0 20px 80px rgba(0, 0, 0, 0.35);
            backdrop-filter: blur(12px);
          }

          .eyebrow {
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.28em;
            font-size: 0.78rem;
            margin-bottom: 16px;
          }

          h1 {
            margin: 0;
            font-size: clamp(2.4rem, 7vw, 4.5rem);
            line-height: 0.96;
          }

          .accent {
            color: var(--accent);
          }

          p {
            margin: 20px 0 0;
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.7;
          }

          .meta {
            margin-top: 28px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 12px 16px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.05);
            color: var(--text);
          }

          .dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--accent);
            box-shadow: 0 0 16px rgba(111, 231, 200, 0.8);
          }
        </style>
      </head>
      <body>
        <main class="card">
          <div class="eyebrow">DEVOPS-109</div>
          <h1>Multi-Stage<br><span class="accent">Docker Application</span></h1>
          <p>Running successfully inside Docker.</p>
          <div class="meta"><span class="dot"></span> Flask service is live</div>
        </main>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

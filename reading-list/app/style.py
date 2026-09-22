from fasthtml.common import Style

css = Style(
    """
    :root {
        color-scheme: dark;
        --bg: #0b1117;
        --bg-elevated: #121b22;
        --bg-panel: rgba(18, 27, 34, 0.8);
        --bg-card: rgba(17, 24, 30, 0.95);
        --bg-soft: rgba(255, 255, 255, 0.04);
        --ink: #edf5f3;
        --ink-soft: #d0dfe3;
        --muted: #90a7af;
        --line: rgba(255, 255, 255, 0.08);
        --accent: #f4a261;
        --accent-strong: #f08c5d;
        --accent-soft: rgba(244, 162, 97, 0.14);
        --sage: rgba(96, 175, 139, 0.18);
        --sage-strong: #7ed7a2;
        --success: #9fe4bf;
        --shadow: 0 24px 60px rgba(0, 0, 0, 0.38);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
        margin: 0;
        background:
            radial-gradient(circle at top left, rgba(240, 140, 93, 0.18), transparent 24%),
            radial-gradient(circle at bottom right, rgba(126, 215, 162, 0.12), transparent 20%),
            var(--bg);
        color: var(--ink);
        font-family: "Inter", "SF Pro Display", "Segoe UI", sans-serif;
    }
    a { color: inherit; }
    .page-shell {
        min-height: 100vh;
        padding-bottom: 2rem;
    }
    .site-header {
        padding: 2.4rem max(1.25rem, calc((100vw - 1180px) / 2)) 1rem;
        background: linear-gradient(180deg, rgba(13, 18, 22, 0.96), rgba(11, 17, 23, 0.85));
        border-bottom: 1px solid var(--line);
    }
    .intro {
        max-width: 1180px;
        margin: 0 auto;
        display: grid;
        gap: 1.1rem;
    }
    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        max-width: 1180px;
        margin: 0 auto 1.1rem;
    }
    .topbar-link {
        color: var(--muted);
        text-decoration: none;
        font-size: 0.72rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        transition: color 180ms ease;
    }
    .topbar-link:hover { color: var(--ink); }
    .eyebrow, .section-label, label, .status, .book-count, .refresh-link, .stat-label, .pill, button {
        font-family: "Inter", "SF Pro Display", "Segoe UI", sans-serif;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        font-size: 0.72rem;
        font-weight: 700;
    }
    .eyebrow {
        margin: 0;
        color: var(--sage-strong);
    }
    h1 {
        margin: 0;
        max-width: 700px;
        font-size: clamp(2.8rem, 6vw, 5.4rem);
        font-weight: 700;
        letter-spacing: -0.07em;
        line-height: 0.92;
    }
    .intro h1 + p {
        margin: 0;
        max-width: 620px;
        color: var(--ink-soft);
        font-size: 1.06rem;
        line-height: 1.7;
        letter-spacing: -0.02em;
    }
    .header-pills {
        display: flex;
        gap: 0.55rem;
        flex-wrap: wrap;
    }
    .pill {
        display: inline-flex;
        align-items: center;
        background: rgba(255,255,255,0.04);
        color: var(--ink-soft);
        border: 1px solid var(--line);
        border-radius: 999px;
        padding: 0.5rem 0.8rem;
    }
    .pill.muted {
        background: rgba(255,255,255,0.02);
        color: var(--muted);
    }
    .main-shell {
        max-width: 1180px;
        margin: 0 auto;
        padding: 2rem max(1.25rem, calc((100vw - 1180px) / 2)) 2.5rem;
    }
    .dashboard-shell {
        display: grid;
        gap: 1.4rem;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(120px, 1fr));
        gap: 1rem;
    }
    .stat-card {
        background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        box-shadow: var(--shadow);
        transition: transform 200ms ease, border-color 200ms ease, box-shadow 200ms ease;
    }
    .stat-card:hover {
        transform: translateY(-3px);
        border-color: rgba(244, 162, 97, 0.5);
        box-shadow: 0 18px 34px rgba(0,0,0,0.16);
    }
    .stat-card.accent { background: linear-gradient(180deg, rgba(244,162,97,0.12), rgba(255,255,255,0.02)); }
    .stat-card.success { background: linear-gradient(180deg, rgba(126,215,162,0.12), rgba(255,255,255,0.02)); }
    .stat-card.subtle { background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02)); }
    .stat-label {
        margin: 0 0 0.7rem;
        color: var(--muted);
    }
    .stat-value {
        margin: 0;
        font-size: clamp(1.7rem, 2.4vw, 2.5rem);
        font-weight: 700;
        letter-spacing: -0.06em;
    }
    .content-grid {
        display: grid;
        grid-template-columns: minmax(290px, 0.72fr) minmax(0, 1.5fr);
        gap: 1.4rem;
        align-items: start;
    }
    .add-panel, .collection-panel {
        background: var(--bg-panel);
        backdrop-filter: blur(12px);
        border: 1px solid var(--line);
        border-radius: 24px;
        box-shadow: var(--shadow);
    }
    .add-panel {
        position: sticky;
        top: 1rem;
        padding: 1.3rem;
    }
    .section-label {
        margin: 0 0 1rem;
        color: var(--accent);
    }
    .book-form {
        display: grid;
        gap: 0.95rem;
    }
    .field {
        display: grid;
        gap: 0.48rem;
    }
    label {
        color: var(--ink-soft);
    }
    input, select {
        width: 100%;
        padding: 0.9rem 0.95rem;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        background: rgba(255,255,255,0.03);
        color: var(--ink);
        font: inherit;
        transition: border-color 180ms ease, box-shadow 180ms ease, transform 180ms ease;
    }
    input::placeholder { color: #7f8e95; }
    input:focus, select:focus {
        outline: none;
        border-color: rgba(244,162,97,0.7);
        box-shadow: 0 0 0 4px rgba(244,162,97,0.12);
    }
    .button {
        border: 0;
        padding: 0.9rem 1.1rem;
        border-radius: 12px;
        cursor: pointer;
        font-weight: 700;
        transition: transform 180ms ease, box-shadow 180ms ease, filter 180ms ease, opacity 180ms ease;
    }
    .button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 22px rgba(0,0,0,0.16);
        filter: brightness(1.03);
    }
    .button-primary {
        background: linear-gradient(135deg, var(--accent) 0%, var(--accent-strong) 100%);
        color: #180f0d;
        box-shadow: 0 12px 24px rgba(244, 162, 97, 0.22);
    }
    .button-quiet {
        background: rgba(244, 162, 97, 0.1);
        color: var(--accent);
        padding-inline: 1rem;
    }
    .button-wide {
        width: 100%;
        margin-top: 0.2rem;
    }
    .collection-panel {
        padding: 1.3rem 1.2rem 0.8rem;
    }
    .collection-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.2rem 0.2rem 1rem;
        border-bottom: 1px solid var(--line);
    }
    .section-heading {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 0.8rem;
        width: 100%;
    }
    .book-count {
        color: var(--muted);
        margin: 0;
    }
    .refresh-link {
        color: var(--accent);
        text-decoration: none;
        opacity: 0.9;
    }
    .book-list {
        display: grid;
        gap: 1rem;
        padding-top: 1.1rem;
    }
    .book-card {
        display: flex;
        justify-content: space-between;
        gap: 1.2rem;
        align-items: center;
        padding: 1.2rem 1.1rem;
        background: var(--bg-card);
        border: 1px solid var(--line);
        border-radius: 18px;
        box-shadow: 0 10px 26px rgba(0,0,0,0.12);
        transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
    }
    .book-card:hover {
        transform: translateY(-2px);
        border-color: rgba(244, 162, 97, 0.34);
        box-shadow: 0 18px 28px rgba(0,0,0,0.16);
    }
    .book-copy {
        min-width: 0;
        flex: 1;
    }
    .book-card h2 {
        margin: 0.48rem 0 0.5rem;
        font-size: clamp(1.3rem, 2vw, 1.8rem);
        font-weight: 600;
        letter-spacing: -0.04em;
        line-height: 1.2;
    }
    .book-author {
        margin: 0;
        color: var(--muted);
        font-size: 0.96rem;
    }
    .status {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 2rem;
        padding: 0.35rem 0.75rem;
        border-radius: 999px;
        background: rgba(126, 215, 162, 0.12);
        color: var(--success);
        border: 1px solid rgba(126, 215, 162, 0.18);
    }
    .status-reading {
        background: rgba(244, 162, 97, 0.12);
        color: #f9be8a;
        border-color: rgba(244, 162, 97, 0.24);
    }
    .status-finished {
        background: rgba(128, 170, 255, 0.12);
        color: #a6d4ff;
        border-color: rgba(128, 170, 255, 0.18);
    }
    .source-link {
        display: inline-block;
        margin-top: 0.8rem;
        color: var(--accent);
        text-decoration: none;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .source-link:hover { text-decoration: underline; }
    .book-actions {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 0.7rem;
        flex-shrink: 0;
    }
    .site-footer {
        padding: 1.1rem 1rem 0;
        text-align: center;
        color: var(--muted);
        font-size: 0.8rem;
    }
    @media (max-width: 760px) {
        .site-header { padding-top: 2rem; }
        .stats-grid { grid-template-columns: repeat(2, minmax(120px, 1fr)); }
        .content-grid { grid-template-columns: 1fr; }
        .add-panel { position: static; }
        .book-card {
            flex-direction: column;
            align-items: flex-start;
        }
        .book-actions {
            width: 100%;
            flex-direction: row;
            justify-content: flex-start;
            align-items: center;
            gap: 0.7rem;
        }
        .button-quiet { padding-inline: 0.9rem; }
    }
    """
)

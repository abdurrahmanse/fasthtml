from fasthtml.common import Style, serve

from app.database import app
from app import routes as _routes


app.hdrs = (
    Style(
        """
        :root {
            --ink: #17221c;
            --muted: #68736b;
            --paper: #f5f3ed;
            --panel: #fffdf8;
            --line: #d8ddd4;
            --accent: #d65d3a;
            --accent-dark: #a9432b;
            --sage: #dce8d9;
        }
        * { box-sizing: border-box; }
        body { margin: 0; background: var(--paper); color: var(--ink); font-family: Georgia, serif; }
        .page-shell { min-height: 100vh; }
        .site-header { padding: 3.5rem max(1.5rem, calc((100vw - 1120px) / 2)) 2.5rem; background: var(--ink); color: var(--paper); }
        .intro { max-width: 1120px; margin: auto; }
        .eyebrow, .section-label, label, .status, .book-count, .refresh-link, button { font-family: ui-sans-serif, system-ui, sans-serif; letter-spacing: .08em; text-transform: uppercase; font-size: .72rem; }
        .eyebrow { color: #a9c7a1; margin: 0 0 .9rem; }
        h1 { font-size: clamp(2.6rem, 7vw, 5.5rem); line-height: .95; max-width: 650px; margin: 0; font-weight: 400; }
        .intro h1 + p { color: #bbc6bd; font-family: ui-sans-serif, system-ui, sans-serif; margin: 1.25rem 0 0; }
        main { max-width: 1120px; margin: auto; padding: 2rem max(1.5rem, calc((100vw - 1120px) / 2)) 4rem; }
        .content-grid { display: grid; grid-template-columns: minmax(250px, .72fr) minmax(0, 1.4fr); gap: 3rem; align-items: start; }
        .add-panel { position: sticky; top: 1.5rem; }
        .section-label { color: var(--accent-dark); font-weight: 700; margin: 0 0 1rem; }
        .book-form { background: var(--panel); border: 1px solid var(--line); padding: 1.4rem; box-shadow: 8px 8px 0 var(--sage); }
        .field { display: grid; gap: .45rem; margin-bottom: 1rem; }
        label { color: var(--muted); font-weight: 700; }
        input, select { width: 100%; padding: .75rem .8rem; border: 1px solid var(--line); background: #fff; color: var(--ink); font: inherit; }
        input:focus, select:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
        .button { border: 0; padding: .75rem 1rem; cursor: pointer; font-weight: 700; }
        .button-primary { background: var(--accent); color: white; }
        .button-primary:hover { background: var(--accent-dark); }
        .button-quiet { background: transparent; color: var(--muted); padding-inline: 0; }
        .button-quiet:hover { color: var(--accent-dark); }
        .button-wide { width: 100%; margin-top: .4rem; }
        .collection-header { display: flex; align-items: baseline; justify-content: space-between; border-bottom: 2px solid var(--ink); }
        .section-heading { display: flex; align-items: baseline; gap: .8rem; }
        .book-count { color: var(--muted); }
        .refresh-link { color: var(--accent-dark); text-decoration: none; font-weight: 700; }
        .book-list { display: grid; gap: 1px; background: var(--line); border: 1px solid var(--line); }
        .book-card { display: flex; justify-content: space-between; gap: 1.5rem; padding: 1.4rem; background: var(--panel); }
        .book-copy { min-width: 0; }
        .book-card h2 { margin: .55rem 0 .3rem; font-size: 1.5rem; font-weight: 400; }
        .book-author { color: var(--muted); margin: 0; font-family: ui-sans-serif, system-ui, sans-serif; }
        .status { display: inline-block; padding: .3rem .45rem; background: var(--sage); color: #35503b; font-weight: 700; }
        .status-reading { background: #f4dfc8; color: #814b29; }
        .status-finished { background: #dce5eb; color: #3d5768; }
        .source-link { display: inline-block; margin-top: .8rem; color: var(--accent-dark); font-family: ui-sans-serif, system-ui, sans-serif; font-size: .82rem; }
        .book-actions { display: flex; flex-direction: column; align-items: end; gap: .7rem; flex-shrink: 0; }
        footer { padding: 1.5rem; color: var(--muted); text-align: center; font-family: ui-sans-serif, system-ui, sans-serif; font-size: .8rem; }
        @media (max-width: 720px) {
            .site-header { padding-top: 2.5rem; }
            .content-grid { grid-template-columns: 1fr; gap: 3rem; }
            .add-panel { position: static; }
            .book-card { flex-direction: column; }
            .book-actions { flex-direction: row; align-items: center; }
        }
        """
    ),
)


if __name__ == "__main__":
    serve(appname="reading-list")

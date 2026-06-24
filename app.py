"""
Streamlit UI for the Multi-Agent AI Research System.
Run with:  streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components
import re
from pathlib import Path
from pipeline import run_research_pipeline

# ── Page Config ──────────────────────────────────────────────────────────

st.set_page_config(
    page_title="MultiAgent Researcher",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Cosmic Dust Background ───────────────────────────────────────────────

import base64

cosmic_dust_path = Path(__file__).parent / "cosmic_dust.html"
cosmic_dust_html = cosmic_dust_path.read_text(encoding="utf-8")
cosmic_dust_b64 = base64.b64encode(cosmic_dust_html.encode("utf-8")).decode("utf-8")

# Inject the Three.js scene as a fixed full-page background iframe
st.markdown(
    f"""
    <style>
        .cosmic-bg-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            pointer-events: none;
        }}
        .cosmic-bg-container iframe {{
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
    <div class="cosmic-bg-container">
        <iframe src="data:text/html;base64,{cosmic_dust_b64}"
                scrolling="no" frameborder="0"></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Custom CSS ───────────────────────────────────────────────────────────

st.markdown("""
<style>
    /* ── Import Fonts ─────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ── Root Variables ───────────────────────────────────────────── */
    :root {
        --accent: #6c5ce7;
        --accent-light: #a855f7;
        --success: #10b981;
        --warning: #f59e0b;
        --glass: rgba(255, 255, 255, 0.04);
        --border: rgba(255, 255, 255, 0.06);
    }

    /* ── Transparent Backgrounds for Cosmic Dust ──────────────────── */
    .stApp {
        font-family: 'Inter', sans-serif;
        background: transparent !important;
    }

    .stApp > header {
        background: transparent !important;
    }

    .stMainBlockContainer,
    .block-container,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    section[data-testid="stSidebar"],
    .main .block-container {
        background: transparent !important;
    }

    /* Subtle glass overlay for readability */
    .main .block-container {
        background: rgba(0, 0, 0, 0.45) !important;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 16px;
        padding: 2rem !important;
        margin-top: 1rem;
    }

    /* ── Header ───────────────────────────────────────────────────── */
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: var(--glass);
        border: 1px solid var(--border);
        border-radius: 100px;
        padding: 6px 16px;
        font-size: 0.72rem;
        font-weight: 600;
        color: var(--accent-light);
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .hero-badge-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--accent-light);
        display: inline-block;
        animation: pulse-dot 2s ease-in-out infinite;
    }

    @keyframes pulse-dot {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.5); }
    }

    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.1;
        background: linear-gradient(135deg, #ff7a2a, #ffce5a, #ffc46b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0 0 8px 0;
    }

    .hero-sub {
        font-size: 1rem;
        color: #c0a08a;
        margin: 0;
        font-weight: 400;
    }

    /* ── Pipeline Steps ───────────────────────────────────────────── */
    .step-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin: 1.5rem 0;
    }

    .step-box {
        background: rgba(26, 10, 4, 0.55);
        border: 1px solid rgba(255, 122, 42, 0.12);
        border-radius: 14px;
        padding: 1.2rem 0.8rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        backdrop-filter: blur(6px);
    }

    .step-box.waiting { opacity: 0.4; }

    .step-box.running {
        border-color: #ff7a2a;
        opacity: 1;
        box-shadow: 0 0 20px rgba(255, 122, 42, 0.25), 0 0 60px rgba(255, 122, 42, 0.08);
        animation: glow-pulse 2s ease-in-out infinite;
    }

    @keyframes glow-pulse {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 122, 42, 0.25); }
        50% { box-shadow: 0 0 35px rgba(255, 122, 42, 0.4); }
    }

    .step-box.done {
        border-color: var(--success);
        opacity: 1;
        box-shadow: 0 0 16px rgba(16, 185, 129, 0.2);
    }

    .step-num {
        width: 36px;
        height: 36px;
        margin: 0 auto 8px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.85rem;
        font-weight: 700;
    }

    .waiting .step-num { background: rgba(255,255,255,0.05); color: #555; }
    .running .step-num { background: #ff7a2a; color: #fff; }
    .done .step-num    { background: var(--success); color: #fff; }

    .step-label {
        font-size: 0.82rem;
        font-weight: 600;
        margin-bottom: 2px;
    }

    .step-status {
        font-size: 0.68rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .waiting .step-status { color: #55556a; }
    .running .step-status { color: #ff9a5a; }
    .done .step-status    { color: var(--success); }

    /* ── Spinner ──────────────────────────────────────────────────── */
    .spinner {
        width: 18px; height: 18px;
        border: 2px solid rgba(255,255,255,0.3);
        border-top-color: #fff;
        border-radius: 50%;
        animation: spin 0.8s linear infinite;
        margin: 0 auto;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* ── Score Badge ──────────────────────────────────────────────── */
    .score-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff7a2a, #ffce5a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.6rem;
        font-weight: 800;
        padding: 4px 14px;
        border: 1px solid rgba(255, 122, 42, 0.3);
        border-radius: 8px;
    }

    /* ── Results Section Title ────────────────────────────────────── */
    .section-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #c0a08a;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }

    /* ── Streamlit Element Overrides for transparency ─────────────── */
    .stTextInput > div > div {
        background: rgba(26, 10, 4, 0.6) !important;
        border-color: rgba(255, 122, 42, 0.2) !important;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ff7a2a, #ffce5a) !important;
        border: none !important;
        color: #1a0a04 !important;
        font-weight: 700 !important;
    }

    .stButton > button[kind="primary"]:hover {
        box-shadow: 0 0 20px rgba(255, 122, 42, 0.4) !important;
    }

    div[data-testid="stExpander"] {
        background: rgba(26, 10, 4, 0.5) !important;
        border-color: rgba(255, 122, 42, 0.15) !important;
        border-radius: 12px;
        backdrop-filter: blur(4px);
    }

    .stAlert {
        background: rgba(26, 10, 4, 0.5) !important;
        backdrop-filter: blur(4px);
    }

    hr {
        border-color: rgba(255, 122, 42, 0.15) !important;
    }

    /* ── Responsive ───────────────────────────────────────────────── */
    @media (max-width: 768px) {
        .step-grid { grid-template-columns: repeat(2, 1fr); }
        .hero-title { font-size: 1.8rem; }
    }
</style>
""", unsafe_allow_html=True)


# ── Helper ───────────────────────────────────────────────────────────────

def safe_str(content):
    """Convert any LangChain content to a plain string."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                parts.append(block.get("text", str(block)))
            else:
                parts.append(str(block))
        return "\n".join(parts)
    return str(content)


def extract_score(text):
    """Pull 'Score: X/10' from critic feedback."""
    m = re.search(r"Score:\s*(\d+(?:\.\d+)?/\d+)", text, re.IGNORECASE)
    return m.group(1) if m else None


# ── Step Tracker HTML ────────────────────────────────────────────────────

STEP_META = [
    {"icon": "🔍", "label": "Search Agent"},
    {"icon": "🌐", "label": "Scraping Agent"},
    {"icon": "✍️",  "label": "Writer Agent"},
    {"icon": "🧐", "label": "Critic Agent"},
]

def render_steps(statuses):
    """Render the 4-step pipeline tracker."""
    boxes = ""
    for i, meta in enumerate(STEP_META):
        s = statuses[i]
        cls = s  # 'waiting', 'running', or 'done'

        if s == "running":
            num_html = '<div class="spinner"></div>'
            status_text = "Processing…"
        elif s == "done":
            num_html = "✓"
            status_text = "Complete"
        else:
            num_html = str(i + 1)
            status_text = "Waiting"

        boxes += f"""
        <div class="step-box {cls}">
            <div class="step-num">{num_html}</div>
            <div class="step-label">{meta['label']}</div>
            <div class="step-status">{status_text}</div>
        </div>"""

    st.markdown(f"""
    <div class="section-label">Pipeline Progress</div>
    <div class="step-grid">{boxes}</div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════
#  MAIN UI
# ══════════════════════════════════════════════════════════════════════════

# ── Header ───────────────────────────────────────────────────────────────

st.markdown("""
<div style="text-align:center; margin-bottom:2rem;">
    <h1 class="hero-title">MultiAgent Researcher</h1>
    <p class="hero-sub">Enter a topic and watch AI agents search, scrape, write, and critique a research report.</p>
</div>
""", unsafe_allow_html=True)

# ── Input ────────────────────────────────────────────────────────────────

col1, col2 = st.columns([5, 1])
with col1:
    topic = st.text_input(
        "Research Topic",
        placeholder="e.g.  Impact of quantum computing on cybersecurity",
        label_visibility="collapsed",
    )
with col2:
    start = st.button("🚀 Start Research", use_container_width=True, type="primary")

# ── Pipeline Execution ───────────────────────────────────────────────────

if start and topic.strip():
    statuses = ["waiting", "waiting", "waiting", "waiting"]
    tracker = st.empty()
    state = {}

    try:
        # ── Step 1: Search Agent ─────────────────────────────────────
        statuses[0] = "running"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        with st.status("🔍 **Step 1 — Search Agent** is finding information…", expanded=True) as s1:
            from agents import build_search_agent, build_scraping_agent, writer_chain, critic_chain

            search_agent = build_search_agent()
            search_result = search_agent.invoke({
                "messages": [("user", f"Find recent, reliable and detailed information on the topic: {topic}")]
            })
            state["search_result"] = safe_str(search_result["messages"][-1].content)
            st.markdown(state["search_result"])
            s1.update(label="🔍 **Step 1 — Search Agent** complete", state="complete", expanded=False)

        statuses[0] = "done"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        # ── Step 2: Scraping Agent ───────────────────────────────────
        statuses[1] = "running"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        with st.status("🌐 **Step 2 — Scraping Agent** is extracting data…", expanded=True) as s2:
            scraping_agent = build_scraping_agent()
            scraping_result = scraping_agent.invoke({
                "messages": [("user",
                    f"Based on the following search results about '{topic}',"
                    f"Pick the most relevant URL and scrape detailed information from it for deeper insights.\n\n"
                    f"Search Results:\n{state['search_result'][:800]}"
                )]
            })
            state["scraping_result"] = safe_str(scraping_result["messages"][-1].content)
            st.markdown(state["scraping_result"])
            s2.update(label="🌐 **Step 2 — Scraping Agent** complete", state="complete", expanded=False)

        statuses[1] = "done"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        # ── Step 3: Writer Agent ─────────────────────────────────────
        statuses[2] = "running"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        with st.status("✍️ **Step 3 — Writer Agent** is drafting the report…", expanded=True) as s3:
            research_combined = (
                f"SEARCH RESULTS: \n {state['search_result']} \n\n"
                f"SCRAPING RESULTS: \n {state['scraping_result']}"
            )
            state["report"] = writer_chain.invoke({
                "topic": topic,
                "research": research_combined
            })
            state["report"] = safe_str(state["report"])
            st.markdown(state["report"])
            s3.update(label="✍️ **Step 3 — Writer Agent** complete", state="complete", expanded=False)

        statuses[2] = "done"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        # ── Step 4: Critic Agent ─────────────────────────────────────
        statuses[3] = "running"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        with st.status("🧐 **Step 4 — Critic Agent** is reviewing the report…", expanded=True) as s4:
            state["feedback"] = critic_chain.invoke({
                "report": state["report"]
            })
            state["feedback"] = safe_str(state["feedback"])
            st.markdown(state["feedback"])
            s4.update(label="🧐 **Step 4 — Critic Agent** complete", state="complete", expanded=False)

        statuses[3] = "done"
        tracker.empty()
        with tracker.container():
            render_steps(statuses)

        # ── Final Report ─────────────────────────────────────────────

        st.divider()

        score = extract_score(state["feedback"])

        # Header row
        r1, r2 = st.columns([4, 1])
        with r1:
            st.markdown("### 📄 Final Research Report")
        with r2:
            if score:
                st.markdown(f'<div style="text-align:right"><span class="score-badge">{score}</span></div>',
                            unsafe_allow_html=True)

        st.markdown(state["report"])

        st.divider()

        st.markdown("### 🧐 Critic's Review")
        st.markdown(state["feedback"])

        st.success("✅ Research pipeline completed successfully!")

    except Exception as e:
        st.error(f"❌ Pipeline error: {e}")

elif start and not topic.strip():
    st.warning("⚠️ Please enter a research topic first.")

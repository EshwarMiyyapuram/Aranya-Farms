import streamlit as st
import os
import base64

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Aranya Farms – Luxury Farm Living",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── GLOBAL CSS ─────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=DM+Sans:wght@300;400;500;600&family=Cinzel:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        scroll-behavior: smooth;
    }
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    #MainMenu, footer, header { visibility: hidden; }

    :root {
        --forest:       #0e2318;
        --deep:         #1a3a2a;
        --mid:          #2d6a4f;
        --sage:         #4a8c68;
        --leaf:         #7abf94;
        --gold:         #c9a84c;
        --gold-light:   #e8c97e;
        --gold-pale:    #f5e9c5;
        --cream:        #faf7f0;
        --sand:         #f0ead8;
        --parchment:    #e8dfc8;
        --white:        #ffffff;
        --ink:          #1a2b1e;
        --moss:         #3d5a45;
        --mist:         #8fad96;
    }

    /* ══ NAV ══ */
    .top-nav {
        background: var(--forest);
        padding: 0 48px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 72px;
        position: sticky;
        top: 0;
        z-index: 999;
        border-bottom: 1px solid rgba(201,168,76,0.25);
    }
    .nav-brand {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .nav-brand-icon {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        flex-shrink: 0;
    }
    .nav-name {
        font-family: 'Cinzel', serif;
        color: var(--gold);
        font-size: 1.2rem;
        font-weight: 700;
        letter-spacing: 2px;
        line-height: 1.1;
    }
    .nav-sub {
        color: rgba(255,255,255,0.45);
        font-size: 0.6rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-weight: 300;
    }
    .nav-contact-pill {
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        color: var(--forest);
        padding: 9px 22px;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        text-decoration: none;
        display: inline-block;
    }

    /* ══ PAGE NAV ══ */
    .page-nav-wrap {
        background: var(--cream);
        border-bottom: 1px solid var(--parchment);
        padding: 0 48px;
        display: flex;
        align-items: center;
        gap: 4px;
        height: 52px;
    }

    /* Streamlit button overrides inside page-nav */
    div[data-testid="stHorizontalBlock"] .stButton > button {
        background: transparent !important;
        color: var(--moss) !important;
        border: none !important;
        border-radius: 0 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        padding: 8px 20px !important;
        box-shadow: none !important;
        height: 40px !important;
        transition: color 0.2s !important;
    }
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {
        color: var(--gold) !important;
        background: transparent !important;
        border-bottom: 2px solid var(--gold) !important;
    }

    /* ══ HERO ══ */
    .hero {
        background: linear-gradient(160deg, var(--forest) 0%, #142d1e 40%, var(--deep) 75%, #1f4a32 100%);
        padding: 110px 72px 100px;
        position: relative;
        overflow: hidden;
        min-height: 600px;
        display: flex;
        align-items: center;
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -200px; right: -150px;
        width: 700px; height: 700px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(201,168,76,0.12) 0%, transparent 60%);
        animation: shimmer 8s ease-in-out infinite;
    }
    .hero::after {
        content: '';
        position: absolute;
        bottom: -150px; left: -100px;
        width: 500px; height: 500px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(74,140,104,0.1) 0%, transparent 60%);
    }
    @keyframes shimmer {
        0%,100% { opacity: 0.7; transform: scale(1) rotate(0deg); }
        50% { opacity: 1; transform: scale(1.1) rotate(5deg); }
    }

    .hero-eyebrow {
        font-family: 'Cinzel', serif;
        font-size: 0.7rem;
        letter-spacing: 5px;
        color: var(--gold);
        text-transform: uppercase;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .hero-eyebrow::before, .hero-eyebrow::after {
        content: '';
        width: 40px;
        height: 1px;
        background: var(--gold);
        opacity: 0.5;
    }
    .hero-h1 {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.8rem, 5vw, 5rem);
        font-weight: 300;
        color: #ffffff;
        line-height: 1.1;
        margin-bottom: 24px;
        letter-spacing: -1px;
    }
    .hero-h1 em {
        color: var(--gold-light);
        font-style: italic;
    }
    .hero-para {
        color: rgba(255,255,255,0.65);
        font-size: 1.05rem;
        line-height: 1.8;
        max-width: 520px;
        margin-bottom: 44px;
        font-weight: 300;
    }

    /* Badges row */
    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 44px;
    }
    .stat-badge {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(201,168,76,0.3);
        border-radius: 6px;
        padding: 10px 18px;
        text-align: center;
        backdrop-filter: blur(8px);
    }
    .stat-badge .sb-val {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--gold-light);
        line-height: 1;
        display: block;
    }
    .stat-badge .sb-lbl {
        font-size: 0.65rem;
        color: rgba(255,255,255,0.5);
        letter-spacing: 1.5px;
        text-transform: uppercase;
        display: block;
        margin-top: 4px;
    }

    /* CTA Buttons */
    .btn-gold {
        background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
        color: var(--forest);
        padding: 15px 34px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.82rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 6px 24px rgba(201,168,76,0.4);
        transition: all 0.25s;
    }
    .btn-gold:hover { transform: translateY(-2px); box-shadow: 0 10px 32px rgba(201,168,76,0.55); }
    .btn-ghost {
        background: transparent;
        color: rgba(255,255,255,0.85);
        padding: 14px 32px;
        border-radius: 4px;
        font-weight: 500;
        font-size: 0.82rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        border: 1px solid rgba(255,255,255,0.35);
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        transition: all 0.25s;
    }
    .btn-ghost:hover { border-color: var(--gold); color: var(--gold); }
    .btn-green {
        background: linear-gradient(135deg, var(--mid) 0%, var(--deep) 100%);
        color: #fff;
        padding: 13px 30px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.82rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 4px 16px rgba(45,106,79,0.4);
    }
    .btn-wa {
        background: #25d366;
        color: #fff;
        padding: 13px 28px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.82rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 4px 14px rgba(37,211,102,0.4);
    }
    .btn-call {
        background: #1976d2;
        color: #fff;
        padding: 13px 28px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.82rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    .cta-row { display: flex; gap: 12px; flex-wrap: wrap; }

    /* ══ SECTION SHELLS ══ */
    .sec { padding: 88px 72px; }
    .sec-cream { background: var(--cream); }
    .sec-white { background: var(--white); }
    .sec-dark  { background: var(--forest); color: white; }
    .sec-sand  { background: var(--sand); }
    .sec-mid   { background: #f0ead8; }

    .eyebrow {
        font-family: 'Cinzel', serif;
        font-size: 0.65rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: 12px;
    }
    .sec-h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        font-weight: 300;
        color: var(--ink);
        line-height: 1.15;
        margin-bottom: 10px;
        letter-spacing: -0.5px;
    }
    .sec-h2 em { font-style: italic; color: var(--mid); }
    .sec-h2-white {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        font-weight: 300;
        color: #fff;
        line-height: 1.15;
        margin-bottom: 10px;
    }
    .sec-h2-white em { color: var(--gold-light); font-style: italic; }
    .rule {
        width: 56px;
        height: 2px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light));
        border-radius: 2px;
        margin: 16px 0 28px;
    }
    .rule-center { margin: 16px auto 28px; }
    .sec-lead {
        color: var(--moss);
        font-size: 1.02rem;
        line-height: 1.85;
        max-width: 640px;
        font-weight: 300;
    }

    /* ══ STATS STRIP ══ */
    .strip {
        background: var(--deep);
        padding: 36px 72px;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 24px;
        border-top: 1px solid rgba(201,168,76,0.2);
        border-bottom: 1px solid rgba(201,168,76,0.2);
    }
    .strip-item { text-align: center; }
    .strip-val {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        font-weight: 600;
        color: var(--gold-light);
        display: block;
        line-height: 1;
    }
    .strip-lbl {
        font-size: 0.68rem;
        color: rgba(255,255,255,0.5);
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 6px;
        display: block;
    }

    /* ══ FEATURE CARDS ══ */
    .feat-card {
        background: white;
        border-radius: 12px;
        padding: 36px 28px;
        box-shadow: 0 2px 20px rgba(26,58,42,0.07);
        border-top: 3px solid transparent;
        border-image: linear-gradient(90deg, var(--gold), var(--gold-light)) 1;
        text-align: center;
        height: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .feat-card:hover { transform: translateY(-6px); box-shadow: 0 16px 44px rgba(26,58,42,0.14); }
    .feat-icon { font-size: 2.4rem; margin-bottom: 18px; display: block; }
    .feat-card h4 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--ink);
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .feat-card p { color: var(--moss); font-size: 0.9rem; line-height: 1.75; margin: 0; }

    /* ══ AMENITY CHIPS ══ */
    .amenity-chip {
        display: flex;
        align-items: center;
        gap: 12px;
        background: var(--cream);
        border: 1px solid var(--parchment);
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 10px;
        transition: all 0.2s;
    }
    .amenity-chip:hover {
        background: white;
        border-color: var(--gold);
        box-shadow: 0 4px 16px rgba(201,168,76,0.15);
    }
    .ac-icon { font-size: 1.4rem; }
    .ac-name { color: var(--ink); font-size: 0.9rem; font-weight: 500; }

    /* ══ PROPERTY CARDS ══ */
    .prop-card {
        background: white;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 28px rgba(0,0,0,0.08);
        transition: transform 0.35s ease, box-shadow 0.35s ease;
        border: 1px solid rgba(0,0,0,0.04);
        height: 100%;
    }
    .prop-card:hover { transform: translateY(-8px); box-shadow: 0 24px 56px rgba(26,58,42,0.16); }
    .prop-badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        color: var(--forest);
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 5px 14px;
        border-radius: 50px;
        margin-bottom: 12px;
    }
    .prop-body { padding: 26px; }
    .prop-body h3 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--ink);
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .prop-price {
        color: var(--gold);
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 14px;
    }
    .prop-specs { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
    .spec-pill {
        background: var(--cream);
        color: var(--moss);
        font-size: 0.72rem;
        padding: 5px 12px;
        border-radius: 50px;
        border: 1px solid var(--parchment);
    }
    .prop-body p { color: var(--moss); font-size: 0.88rem; line-height: 1.7; }

    /* ══ CONTACT INFO BOX ══ */
    .contact-info-box {
        background: linear-gradient(160deg, var(--deep), var(--forest));
        border-radius: 16px;
        padding: 36px 32px;
        border: 1px solid rgba(201,168,76,0.2);
        height: 100%;
    }
    .contact-info-box h3 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--gold-light);
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 28px;
    }
    .contact-line {
        display: flex;
        gap: 14px;
        margin-bottom: 22px;
        align-items: flex-start;
    }
    .ci-icon { font-size: 1.2rem; margin-top: 2px; flex-shrink: 0; }
    .ci-text { color: rgba(255,255,255,0.75); font-size: 0.9rem; line-height: 1.7; }
    .ci-text strong { color: rgba(255,255,255,0.95); display: block; margin-bottom: 2px; }

    /* ══ LOCATION HIGHLIGHTS ══ */
    .loc-item {
        display: flex;
        gap: 16px;
        align-items: flex-start;
        padding: 18px 20px;
        background: white;
        border-radius: 10px;
        margin-bottom: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        border-left: 3px solid var(--gold);
        transition: box-shadow 0.2s;
    }
    .loc-item:hover { box-shadow: 0 6px 24px rgba(0,0,0,0.1); }
    .loc-icon-wrap { font-size: 1.3rem; flex-shrink: 0; }
    .loc-text h4 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--ink);
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 3px;
    }
    .loc-text p { color: var(--moss); font-size: 0.85rem; margin: 0; line-height: 1.55; }

    /* ══ MAP PLACEHOLDER ══ */
    .map-block {
        background: linear-gradient(135deg, #1a3a2a, #0e2318);
        border-radius: 16px;
        height: 380px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 1px dashed rgba(201,168,76,0.35);
        color: rgba(255,255,255,0.6);
        font-size: 0.85rem;
        text-align: center;
        padding: 30px;
        gap: 12px;
    }
    .map-block .mb-icon { font-size: 3.5rem; opacity: 0.45; }
    .map-block .mb-title { color: var(--gold-light); font-weight: 600; font-size: 1rem; }
    .map-block .mb-sub { font-size: 0.8rem; color: rgba(255,255,255,0.4); line-height: 1.6; }

    /* ══ GALLERY ══ */
    .gallery-category { margin-bottom: 52px; }
    .gallery-cat-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.4rem;
        color: var(--ink);
        font-weight: 600;
    }
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
    }
    .gallery-thumb {
        background: linear-gradient(135deg, var(--mid) 0%, var(--deep) 100%);
        border-radius: 10px;
        height: 175px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: rgba(255,255,255,0.55);
        font-size: 0.72rem;
        letter-spacing: 0.5px;
        gap: 8px;
        padding: 12px;
        text-align: center;
        border: 1px solid rgba(201,168,76,0.15);
    }
    .gt-icon { font-size: 2rem; opacity: 0.4; }
    .gt-label { color: rgba(255,255,255,0.65); font-size: 0.78rem; font-weight: 500; }
    .gt-sub { color: rgba(255,255,255,0.3); font-size: 0.68rem; }

    /* ══ FOOTER ══ */
    .footer {
        background: var(--forest);
        padding: 72px 72px 32px;
        border-top: 1px solid rgba(201,168,76,0.2);
    }
    .footer-logo {
        font-family: 'Cinzel', serif;
        color: var(--gold);
        font-size: 1.3rem;
        letter-spacing: 2px;
        margin-bottom: 6px;
    }
    .footer-tagline {
        font-family: 'Cormorant Garamond', serif;
        color: rgba(255,255,255,0.4);
        font-size: 0.85rem;
        letter-spacing: 3px;
        font-style: italic;
        margin-bottom: 18px;
    }
    .footer-copy {
        text-align: center;
        color: rgba(255,255,255,0.3);
        font-size: 0.78rem;
        padding-top: 28px;
        border-top: 1px solid rgba(255,255,255,0.08);
    }

    /* ══ QUOTE BLOCK ══ */
    .quote-block {
        background: linear-gradient(135deg, var(--deep), #1f4a32);
        border-radius: 14px;
        padding: 44px 48px;
        border-left: 4px solid var(--gold);
        margin: 40px 0;
    }
    .quote-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.55rem;
        font-weight: 300;
        font-style: italic;
        color: rgba(255,255,255,0.9);
        line-height: 1.65;
    }

    /* ══ PHILOSOPHY PILLARS ══ */
    .pillar-card {
        background: white;
        border-radius: 14px;
        padding: 40px 30px;
        box-shadow: 0 4px 24px rgba(26,58,42,0.08);
        text-align: center;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    .pillar-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light));
    }
    .pillar-card .pillar-icon { font-size: 3rem; margin-bottom: 20px; display: block; }
    .pillar-card h4 {
        font-family: 'Cinzel', serif;
        color: var(--ink);
        font-size: 1.1rem;
        letter-spacing: 2px;
        margin-bottom: 14px;
    }
    .pillar-card p { color: var(--moss); font-size: 0.9rem; line-height: 1.75; }

    /* ══ LIFESTYLE LIST ══ */
    .lifestyle-item {
        display: flex;
        gap: 18px;
        padding: 20px 24px;
        background: white;
        border-radius: 10px;
        margin-bottom: 14px;
        box-shadow: 0 2px 14px rgba(0,0,0,0.05);
    }
    .lifestyle-item .li-icon { font-size: 2rem; flex-shrink: 0; }
    .lifestyle-item h4 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--ink);
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .lifestyle-item p { color: var(--moss); font-size: 0.87rem; margin: 0; line-height: 1.65; }

    /* ══ DATA TABLE STYLING ══ */
    [data-testid="stDataFrame"] { border-radius: 10px; overflow: hidden; }

    /* ══ FORM STYLING ══ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 6px !important;
        border-color: var(--parchment) !important;
        font-family: 'DM Sans', sans-serif !important;
    }
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, var(--gold), var(--gold-light)) !important;
        color: var(--forest) !important;
        font-weight: 600 !important;
        letter-spacing: 1.5px !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 12px 24px !important;
    }

    /* ══ ENQUIRE BUTTON IN PROPERTY CARDS ══ */
    .stButton > button {
        border-radius: 4px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
    }

    </style>
    """, unsafe_allow_html=True)


# ─── HELPERS ────────────────────────────────────────────────────────────────
def load_img_b64(path):
    """Return (b64_string, mime_type) if file exists, else None."""
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    ext = path.rsplit(".", 1)[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    return data, mime

def img_tag(path, alt="", style="width:100%;display:block;"):
    result = load_img_b64(path)
    if result:
        b64, mime = result
        return f'<img src="data:{mime};base64,{b64}" alt="{alt}" style="{style}">'
    return None

def prop_image(path, alt="", height=240):
    """Return an image tag or None — never a visible placeholder."""
    result = load_img_b64(path)
    if result:
        b64, mime = result
        return f'<img src="data:{mime};base64,{b64}" alt="{alt}" style="width:100%;height:{height}px;object-fit:cover;display:block;">'
    return None

def gallery_thumb_html(label):
    return f"""
    <div class="gallery-thumb">
        <div class="gt-icon">📸</div>
        <div class="gt-label">{label}</div>
    </div>"""


# ─── NAV ────────────────────────────────────────────────────────────────────
def render_navbar():
    st.markdown("""
    <div class="top-nav">
        <div class="nav-brand">
            <div class="nav-brand-icon">🌿</div>
            <div>
                <div class="nav-name">Aranya Farms</div>
                <div class="nav-sub">Silver Oaks Agro Farms · Achampet, Toopran</div>
            </div>
        </div>
        <a class="nav-contact-pill" href="tel:+919999999999">📞 Call Now</a>
    </div>
    """, unsafe_allow_html=True)

PAGES = ["🏡 Home", "🌿 About", "🏘️ Properties", "📍 Location", "📞 Contact"]

def render_page_nav():
    st.markdown("<div style='background:var(--cream,#faf7f0);padding:8px 40px;border-bottom:1px solid #e8dfc8;'>", unsafe_allow_html=True)
    cols = st.columns(len(PAGES))
    for i, page in enumerate(PAGES):
        with cols[i]:
            label = page.split(" ", 1)[1] if " " in page else page
            if st.button(label, key=f"nav_{i}", use_container_width=True):
                st.session_state.page = page
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 1 — HOME
# ═══════════════════════════════════════════════════════════════════════════
def page_home():
    # ── HERO ──
    col1, col2 = st.columns([1.1, 0.9], gap="large")
    st.markdown('<div class="hero">', unsafe_allow_html=True)

    with col1:
        st.markdown("""
        <div style="position:relative;z-index:2;">
        <div class="hero-eyebrow">Silver Oaks Agro Farms Presents</div>
        <h1 class="hero-h1">Luxury Farm Living<br>at <em>Aranya Farms</em></h1>
        <p class="hero-para">
            Premium Farm Plots & 3-BHK Farm Houses at Achampet, Toopran.<br>
            Where nature meets refined living — your perfect weekend escape.
        </p>
        <div class="badge-row">
            <div class="stat-badge"><span class="sb-val">55</span><span class="sb-lbl">Acres</span></div>
            <div class="stat-badge"><span class="sb-val">Gated</span><span class="sb-lbl">Community</span></div>
            <div class="stat-badge"><span class="sb-val">3-BHK</span><span class="sb-lbl">Farm Houses</span></div>
            <div class="stat-badge"><span class="sb-val">5 min</span><span class="sb-lbl">From RRR</span></div>
            <div class="stat-badge"><span class="sb-val">30 min</span><span class="sb-lbl">From ORR</span></div>
            <div class="stat-badge"><span class="sb-val">₹49L+</span><span class="sb-lbl">Starting</span></div>
        </div>
        <div class="cta-row">
            <a class="btn-gold" href="#">📅 Book Site Visit</a>
            <a class="btn-ghost" href="#">🏘️ View Properties</a>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Try to show real image; otherwise show nothing (clean hero)
        hero_tag = None
        for _p in ["images/land1.png", "images/land1.jpg", "images/land2.png", "images/land2.jpg"]:
            hero_tag = img_tag(_p, "Aranya Farms", "width:100%;border-radius:16px;box-shadow:0 12px 56px rgba(0,0,0,0.4);")
            if hero_tag:
                break
        if hero_tag:
            st.markdown(f'<div style="position:relative;z-index:2;">{hero_tag}</div>', unsafe_allow_html=True)
        else:
            # Elegant decorative block instead of placeholder
            st.markdown("""
            <div style="position:relative;z-index:2;">
            <div style="border:1px solid rgba(201,168,76,0.3);border-radius:16px;padding:60px 40px;text-align:center;backdrop-filter:blur(4px);background:rgba(255,255,255,0.04);">
                <div style="font-family:'Cormorant Garamond',serif;font-size:3.5rem;color:var(--gold);opacity:0.4;line-height:1;">🌾</div>
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;font-style:italic;color:rgba(255,255,255,0.6);margin-top:16px;">Aranya Farms</div>
                <div style="font-size:0.7rem;color:rgba(255,255,255,0.3);letter-spacing:3px;text-transform:uppercase;margin-top:8px;">Achampet · Toopran</div>
            </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── STATS STRIP ──
    st.markdown("""
    <div class="strip">
        <div class="strip-item"><span class="strip-val">55+</span><span class="strip-lbl">Acres of Green</span></div>
        <div class="strip-item"><span class="strip-val">200+</span><span class="strip-lbl">Happy Families</span></div>
        <div class="strip-item"><span class="strip-val">15+</span><span class="strip-lbl">Amenities</span></div>
        <div class="strip-item"><span class="strip-val">₹49L</span><span class="strip-lbl">Starting Price</span></div>
        <div class="strip-item"><span class="strip-val">2024</span><span class="strip-lbl">Ready Possession</span></div>
    </div>
    """, unsafe_allow_html=True)

    # ── WHY ARANYA ──
    st.markdown("""
    <div class="sec sec-cream">
        <div class="eyebrow">Why Choose Us</div>
        <div class="sec-h2">The Aranya Farms <em>Difference</em></div>
        <div class="rule"></div>
        <p class="sec-lead">A unique blend of luxury living and nature's serenity — thoughtfully designed for families who seek more than just a home.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:var(--cream,#faf7f0);">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4, gap="medium")
        features = [
            ("🌿", "Pure Nature", "Nestled in lush greenery with fresh air, organic surroundings and breathtaking sunrise views."),
            ("🏡", "Premium Homes", "Thoughtfully designed 3-BHK farm houses with modern architecture and natural aesthetics."),
            ("🛡️", "Gated Security", "24×7 security, CCTV surveillance and managed entry for total peace of mind."),
            ("🌊", "Riverside Living", "Adjacent to the serene Haldi River — nature's own backyard at your doorstep."),
        ]
        for col, (icon, title, desc) in zip([c1, c2, c3, c4], features):
            with col:
                st.markdown(f"""
                <div class="feat-card">
                    <span class="feat-icon">{icon}</span>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── LAND PHOTOS (only if images exist) ──
    land_paths = [
        ("images/land1.png","Farm Land View 1"),("images/land1.jpg","Farm Land View 1"),
        ("images/land2.png","Farm Land View 2"),("images/land2.jpg","Farm Land View 2"),
        ("images/land3.png","Farm Land View 3"),("images/land3.jpg","Farm Land View 3"),
        ("images/land4.png","Farm Land View 4"),("images/land4.jpg","Farm Land View 4"),
    ]
    shown = {}
    imgs_html = ""
    for path, caption in land_paths:
        key = caption
        if key not in shown:
            result = load_img_b64(path)
            if result:
                b64, mime = result
                imgs_html += f"""
                <div style="position:relative;overflow:hidden;border-radius:12px;flex:1;min-width:0;">
                    <img src="data:{mime};base64,{b64}" alt="{caption}"
                         style="width:100%;height:260px;object-fit:cover;display:block;">
                    <div style="position:absolute;bottom:0;left:0;right:0;
                                background:linear-gradient(transparent,rgba(10,26,16,0.75));
                                padding:16px 14px 12px;">
                        <div style="color:rgba(255,255,255,0.85);font-size:0.73rem;letter-spacing:1px;">🌿 {caption}</div>
                    </div>
                </div>"""
                shown[key] = True

    if imgs_html:
        st.markdown(f"""
        <div style="background:#0d1f15;padding:60px 72px;">
            <div style="text-align:center;margin-bottom:32px;">
                <div class="eyebrow" style="text-align:center;color:var(--gold-light);">The Land</div>
                <div style="font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:300;color:#fff;">
                    Aranya Farms in its <em style="font-style:italic;color:var(--gold-light);">Natural Glory</em>
                </div>
                <div style="width:56px;height:2px;background:linear-gradient(90deg,var(--gold),var(--gold-light));margin:16px auto 0;"></div>
            </div>
            <div style="display:flex;gap:14px;align-items:stretch;">{imgs_html}</div>
        </div>""", unsafe_allow_html=True)

    # ── AMENITIES ──
    st.markdown("""
    <div class="sec sec-white">
        <div class="eyebrow">World-Class Amenities</div>
        <div class="sec-h2">Everything You Need to <em>Live Well</em></div>
        <div class="rule"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:white;">', unsafe_allow_html=True)
        amenities = [
            ("🏊","Swimming Pool"),("🎾","Sports Arena"),("🌿","Organic Farming"),
            ("🐄","Goshala"),("🌸","Gazebo & Gardens"),("🏋️","Fitness Centre"),
            ("🍽️","Clubhouse & Dining"),("🛕","Meditation Zone"),("🎠","Children's Play Area"),
            ("🌳","Tree Plantation"),("🚗","Ample Parking"),("💧","24×7 Water Supply"),
        ]
        rows = [amenities[i:i+4] for i in range(0, len(amenities), 4)]
        for row in rows:
            cols = st.columns(4, gap="small")
            for col, (icon, name) in zip(cols, row):
                with col:
                    st.markdown(f'<div class="amenity-chip"><span class="ac-icon">{icon}</span><span class="ac-name">{name}</span></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── CTA BANNER ──
    st.markdown("""
    <div class="sec sec-dark" style="text-align:center;">
        <div class="eyebrow" style="text-align:center;">Limited Plots Available</div>
        <div class="sec-h2-white">Ready to Find Your Perfect <em>Farm Plot?</em></div>
        <div class="rule rule-center"></div>
        <p style="color:rgba(255,255,255,0.6);font-size:1rem;margin-bottom:36px;font-weight:300;">
            Plots starting from ₹49 Lakhs. Register now for exclusive pre-launch pricing.
        </p>
        <div class="cta-row" style="justify-content:center;">
            <a class="btn-gold" href="#">📅 Book Free Site Visit</a>
            <a class="btn-ghost" href="#">📞 Talk to Expert</a>
            <a class="btn-ghost" href="#">📄 Download Brochure</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 2 — ABOUT
# ═══════════════════════════════════════════════════════════════════════════
def page_about():
    st.markdown("""
    <div class="hero" style="min-height:380px;padding:90px 72px;">
        <div style="position:relative;z-index:2;">
            <div class="hero-eyebrow">Our Story</div>
            <h1 class="hero-h1" style="font-size:3.8rem;">About <em>Aranya Farms</em></h1>
            <p class="hero-para">Play · Live · Celebrate — A new way to belong to nature.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Vision section
    st.markdown("""
    <div class="sec sec-cream">
        <div class="eyebrow">The Vision</div>
        <div class="sec-h2">Where Rural Richness Meets <em>Urban Comfort</em></div>
        <div class="rule"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:var(--cream,#faf7f0);">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1], gap="large")
        with col1:
            # Try images; skip if none
            about_img = None
            for _ap in ["images/land3.png","images/land3.jpg","images/land2.png","images/land2.jpg","images/land1.png","images/land1.jpg"]:
                t = img_tag(_ap, "Aranya Farms Land", "width:100%;height:360px;object-fit:cover;border-radius:14px;box-shadow:0 10px 40px rgba(0,0,0,0.15);")
                if t:
                    about_img = t
                    break
            if about_img:
                st.markdown(about_img, unsafe_allow_html=True)
            else:
                # Decorative quote block when no image
                st.markdown("""
                <div class="quote-block">
                    <div class="quote-text">"Every family deserves a sanctuary where they can breathe freely, grow organically, and celebrate life."</div>
                    <div style="color:var(--gold-light);font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;margin-top:20px;">— Silver Oaks Agro Farms</div>
                </div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="padding:10px 0;">
            <p style="color:var(--moss);font-size:1.05rem;line-height:1.9;margin-bottom:20px;font-weight:300;">
                <strong style="color:var(--ink);font-weight:600;">Aranya Farms</strong> is not just a real estate project — it is a lifestyle reimagined.
                Spread across <strong style="color:var(--ink);">55 lush acres</strong> in Achampet, Toopran, Aranya Farms brings together the
                warmth of rural living with the comforts of a premium gated community.
            </p>
            <p style="color:var(--moss);font-size:1.05rem;line-height:1.9;margin-bottom:20px;font-weight:300;">
                Conceived by <strong style="color:var(--ink);">Silver Oaks Agro Farms</strong>, a trusted name in managed farmland
                communities, this project is born from a simple belief: <em style="color:var(--mid);">every family deserves a sanctuary
                where they can breathe freely, grow organically, and celebrate life.</em>
            </p>
            <p style="color:var(--moss);font-size:1.05rem;line-height:1.9;font-weight:300;">
                Adjacent to the tranquil Haldi River and just 5 minutes from the Regional Ring Road (RRR),
                Aranya Farms is the perfect balance of accessibility and escape.
            </p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Philosophy pillars
    st.markdown("""
    <div class="sec sec-white" style="text-align:center;">
        <div class="eyebrow" style="text-align:center;">Our Philosophy</div>
        <div class="sec-h2" style="text-align:center;">Play · Live · <em>Celebrate</em></div>
        <div class="rule rule-center"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:white;">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3, gap="medium")
        pillars = [
            ("🎠","PLAY","Sports arenas, swimming pool, children's zones, nature trails — because life is meant to be enjoyed at every age, every weekend."),
            ("🏡","LIVE","Thoughtfully crafted farm houses and plots designed for wholesome family living. Wake up to birdsong, grow your own food, breathe clean air."),
            ("🎉","CELEBRATE","From festive gatherings at the clubhouse to quiet birthday mornings in the gazebo — every milestone is better amid nature."),
        ]
        for col, (icon, title, desc) in zip([c1, c2, c3], pillars):
            with col:
                st.markdown(f"""
                <div class="pillar-card">
                    <span class="pillar-icon">{icon}</span>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Lifestyle
    st.markdown("""
    <div class="sec sec-sand">
        <div class="eyebrow">Lifestyle & Wellness</div>
        <div class="sec-h2">Designed for Every <em>Chapter of Life</em></div>
        <div class="rule"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:var(--sand,#f0ead8);">', unsafe_allow_html=True)
        lifestyles = [
            ("👨‍👩‍👧‍👦","Family Lifestyle","Spacious plots with dedicated zones for kids, elders, and togetherness. A community where neighbours become extended family."),
            ("🧘","Wellness Retreat","Yoga pavilion, meditation zones, organic garden walks, and fresh-air mornings — your personal wellness sanctuary."),
            ("🏡","Weekend Homes","Just 30 minutes from ORR — the ideal weekend getaway that feels a world away. Rent-ready investment properties."),
            ("🌱","Organic Living","Farm-to-table living. Grow your own vegetables, herbs, and fruits on your private plot with managed farming support."),
        ]
        c1, c2 = st.columns(2, gap="medium")
        for i, (icon, title, desc) in enumerate(lifestyles):
            with (c1 if i % 2 == 0 else c2):
                st.markdown(f"""
                <div class="lifestyle-item">
                    <div class="li-icon">{icon}</div>
                    <div>
                        <h4>{title}</h4>
                        <p>{desc}</p>
                    </div>
                </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Developer
    st.markdown("""
    <div class="sec sec-dark" style="text-align:center;">
        <div class="eyebrow" style="text-align:center;">About the Developer</div>
        <div class="sec-h2-white" style="text-align:center;">Silver Oaks <em>Agro Farms</em></div>
        <div class="rule rule-center"></div>
        <p style="color:rgba(255,255,255,0.68);font-size:1rem;line-height:1.9;max-width:760px;margin:0 auto;font-weight:300;">
            Silver Oaks Agro Farms, operating under <strong style="color:var(--gold-light);">Silver Oaks Realty</strong>,
            is a Hyderabad-based premium farmland developer with a decade of experience in creating
            managed agro-communities. With a commitment to transparency, DTCP-approved layouts, and
            world-class amenities, Silver Oaks has helped over 500+ families find their perfect green sanctuary.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 3 — PROPERTIES
# ═══════════════════════════════════════════════════════════════════════════
def page_properties():
    st.markdown("""
    <div class="hero" style="min-height:360px;padding:90px 72px;">
        <div style="position:relative;z-index:2;">
            <div class="hero-eyebrow">Properties & Plots</div>
            <h1 class="hero-h1" style="font-size:3.8rem;">Find Your <em>Perfect Space</em></h1>
            <p class="hero-para">Farm plots, 3-BHK homes, premium villas — choose what suits your dream.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sec sec-cream">
        <div class="eyebrow">Available Properties</div>
        <div class="sec-h2">Explore Our <em>Offerings</em></div>
        <div class="rule"></div>
        <p class="sec-lead">All properties are within the 55-acre gated community with access to all amenities.</p>
    </div>
    """, unsafe_allow_html=True)

    properties = [
        {
            "badge": "Best Seller",
            "title": "Farm Plots",
            "price": "Starting ₹49 Lakhs",
            "specs": ["300 sq. yds", "605 sq. yds", "640 sq. yds", "753 sq. yds"],
            "desc": "Open farm plots in a gated, amenity-rich community. Build your dream home or enjoy managed farming. Clear titles, DTCP approved layout.",
            "img_paths": ["images/land1.png", "images/land1.jpg"],
        },
        {
            "badge": "Most Popular",
            "title": "3-BHK Farm Houses",
            "price": "Starting ₹65 Lakhs",
            "specs": ["685 sft BUA", "1480 sft BUA", "1500 sft BUA"],
            "desc": "Ready-to-move 3-BHK farm houses with contemporary architecture, private garden space, and complete modern amenities.",
            "img_paths": ["images/land2.png", "images/land2.jpg"],
        },
        {
            "badge": "Luxury",
            "title": "Premium Villas",
            "price": "Starting ₹90 Lakhs",
            "specs": ["2250 sft BUA", "Large Plot", "Private Garden"],
            "desc": "Exclusive premium villas with expansive built-up areas, landscaped private gardens, and premium finishes for the discerning buyer.",
            "img_paths": ["images/land3.png", "images/land3.jpg"],
        },
        {
            "badge": "Investment",
            "title": "Larger Farm Lands",
            "price": "On Request",
            "specs": ["1+ Acre", "Custom Layout", "Managed Option"],
            "desc": "Bulk farmland parcels ideal for families or investor groups looking for larger green footprints with full community access.",
            "img_paths": ["images/land4.png", "images/land4.jpg"],
        },
    ]

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:var(--cream,#faf7f0);">', unsafe_allow_html=True)
        c1, c2 = st.columns(2, gap="medium")
        for i, prop in enumerate(properties):
            with (c1 if i % 2 == 0 else c2):
                # Get image if it exists — no fallback placeholder shown
                card_img_html = ""
                for img_path in prop["img_paths"]:
                    t = prop_image(img_path, prop["title"], 240)
                    if t:
                        card_img_html = f'<div style="overflow:hidden;">{t}</div>'
                        break
                # If no image, card just starts with the body (clean look)
                specs_html = "".join(f'<span class="spec-pill">{s}</span>' for s in prop["specs"])
                st.markdown(f"""
                <div class="prop-card">
                    {card_img_html}
                    <div class="prop-body">
                        <div class="prop-badge">{prop["badge"]}</div>
                        <h3>{prop["title"]}</h3>
                        <div class="prop-price">{prop["price"]}</div>
                        <div class="prop-specs">{specs_html}</div>
                        <p>{prop["desc"]}</p>
                    </div>
                </div>""", unsafe_allow_html=True)
                st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
                if st.button(f"📩 Enquire — {prop['title']}", key=f"prop_btn_{i}", use_container_width=True):
                    st.session_state.page = "📞 Contact"
                    st.rerun()
                st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Plot size table
    st.markdown("""
    <div class="sec sec-white">
        <div class="eyebrow">Plot Dimensions</div>
        <div class="sec-h2">Plot Sizes at a <em>Glance</em></div>
        <div class="rule"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:white;">', unsafe_allow_html=True)
        import pandas as pd
        df = pd.DataFrame({
            "Type": ["Farm Plot – Compact","Farm Plot – Standard","Farm Plot – Large","Farm Plot – Premium","Farm House – 3 BHK (A)","Farm House – 3 BHK (B)","Farm House – 3 BHK (C)","Premium Villa"],
            "Plot Size": ["300 sq. yds","605 sq. yds","640 sq. yds","753 sq. yds","Included","Included","Included","Large"],
            "Built-up Area": ["—","—","—","—","685 sft","1480 sft","1500 sft","2250 sft"],
            "Starting Price": ["₹49 Lakhs","₹55 Lakhs","₹60 Lakhs","₹68 Lakhs","₹65 Lakhs","₹72 Lakhs","₹78 Lakhs","₹90 Lakhs"],
            "Status": ["Available","Limited","Available","Limited","Available","Ready Soon","Available","Pre-launch"],
        })
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 4 — LOCATION
# ═══════════════════════════════════════════════════════════════════════════
def page_location():
    st.markdown("""
    <div class="hero" style="min-height:360px;padding:90px 72px;">
        <div style="position:relative;z-index:2;">
            <div class="hero-eyebrow">Find Us</div>
            <h1 class="hero-h1" style="font-size:3.8rem;">Location & <em>Connectivity</em></h1>
            <p class="hero-para">Strategically located in Achampet, Toopran — nature close, city closer.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="eyebrow">How to Reach</div>
            <div class="sec-h2">Location <em>Highlights</em></div>
            <div class="rule"></div>
            """, unsafe_allow_html=True)

            highlights = [
                ("📍","Exact Location","Achampet Village, Toopran Mandal, Medchal-Malkajgiri District, Telangana"),
                ("🛣️","Near RRR","Only 5 minutes from the Regional Ring Road (RRR) entry point"),
                ("🔄","Near ORR","Approx. 30 minutes from the Outer Ring Road (ORR), Hyderabad"),
                ("🏙️","NH-44 Access","Adjacent to the Hyderabad–Medchal Highway (NH-44)"),
                ("🌊","Riverside","Adjacent to the scenic Haldi River — beautiful water views"),
                ("🏘️","Near Masaipet","Close to Masaipet town — easy access to local markets and services"),
                ("✈️","Airport","Approx. 40–50 minutes from Rajiv Gandhi International Airport"),
                ("🏥","Healthcare","Multiple hospitals and clinics within 15–20 km radius"),
            ]
            for icon, title, desc in highlights:
                st.markdown(f"""
                <div class="loc-item">
                    <div class="loc-icon-wrap">{icon}</div>
                    <div class="loc-text"><h4>{title}</h4><p>{desc}</p></div>
                </div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="eyebrow">Map</div>
            <div class="sec-h2">View on <em>Map</em></div>
            <div class="rule"></div>
            """, unsafe_allow_html=True)

            sat_result = load_img_b64("images/satellite.png") or load_img_b64("images/satellite.jpg")
            if sat_result:
                b64, mime = sat_result
                st.markdown(f"""
                <div style="position:relative;border-radius:16px;overflow:hidden;box-shadow:0 8px 40px rgba(0,0,0,0.18);">
                    <img src="data:{mime};base64,{b64}" alt="Satellite View – Aranya Farms"
                         style="width:100%;height:380px;object-fit:cover;display:block;">
                    <div style="position:absolute;bottom:0;left:0;right:0;
                                background:linear-gradient(transparent,rgba(14,35,24,0.88));
                                padding:20px 24px 18px;">
                        <div style="display:flex;align-items:center;gap:10px;">
                            <span style="font-size:1.4rem;">🛰️</span>
                            <div>
                                <div style="color:var(--gold-light);font-weight:600;font-size:0.85rem;letter-spacing:1px;">SATELLITE VIEW</div>
                                <div style="color:rgba(255,255,255,0.7);font-size:0.76rem;">Aranya Farms · Achampet, Toopran</div>
                            </div>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="map-block">
                    <div class="mb-icon">🗺️</div>
                    <div class="mb-title">Google Maps — Aranya Farms</div>
                    <div class="mb-sub">Achampet, Toopran<br>Medchal-Malkajgiri Dist., Telangana</div>
                </div>""", unsafe_allow_html=True)

            st.markdown("""
            <div style="margin-top:20px;">
                <a class="btn-green" href="https://maps.google.com/?q=Achampet+Toopran+Telangana" target="_blank" style="display:inline-block;">
                    🗺️ Open in Google Maps
                </a>
            </div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # Distance table
    st.markdown("""
    <div class="sec sec-white">
        <div class="eyebrow">Distances</div>
        <div class="sec-h2">Key Distances from <em>Aranya Farms</em></div>
        <div class="rule"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 72px 72px;background:white;">', unsafe_allow_html=True)
        import pandas as pd
        df = pd.DataFrame({
            "Destination": ["RRR (Regional Ring Road)","ORR (Outer Ring Road)","Kompally","Medchal Town","Hyderabad City Centre","RGIA Airport","Masaipet","Haldi River"],
            "Distance": ["~5 km","~30 km","~28 km","~18 km","~38 km","~48 km","~3 km","Adjacent"],
            "Travel Time": ["~5 mins","~30 mins","~28 mins","~18 mins","~40 mins","~50 mins","~5 mins","Walking"],
            "Via": ["State Highway","NH-44 + RRR","NH-44","NH-44","NH-44 + ORR","ORR + Shamshabad","Local Road","—"],
        })
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 5 — CONTACT
# ═══════════════════════════════════════════════════════════════════════════
def page_contact():
    st.markdown("""
    <div class="hero" style="min-height:360px;padding:90px 72px;">
        <div style="position:relative;z-index:2;">
            <div class="hero-eyebrow">Get in Touch</div>
            <h1 class="hero-h1" style="font-size:3.8rem;">Contact <em>Us</em></h1>
            <p class="hero-para">We'd love to hear from you. Let's find your perfect farm plot.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
        col1, col2 = st.columns([1.2, 0.8], gap="large")

        with col1:
            st.markdown("""
            <div class="eyebrow">Send Enquiry</div>
            <div class="sec-h2" style="font-size:2rem;">Let's <em>Talk</em></div>
            <div class="rule"></div>
            """, unsafe_allow_html=True)

            with st.form("enquiry_form", clear_on_submit=True):
                cf1, cf2 = st.columns(2)
                with cf1:
                    name = st.text_input("Full Name *", placeholder="Your full name")
                with cf2:
                    phone = st.text_input("Phone Number *", placeholder="+91 XXXXX XXXXX")

                email = st.text_input("Email Address", placeholder="your@email.com")
                interest = st.selectbox("Interested In *", [
                    "Select an option…",
                    "Farm Plot",
                    "3-BHK Farm House",
                    "Premium Villa",
                    "Larger Farm Land",
                    "Book Site Visit",
                    "Brochure Request",
                    "General Enquiry",
                ])
                message = st.text_area("Message", placeholder="Tell us more about what you're looking for…", height=120)
                submitted = st.form_submit_button("📩 Submit Enquiry", use_container_width=True)
                if submitted:
                    if not name or not phone or interest == "Select an option…":
                        st.error("Please fill in Name, Phone, and select your Interest.")
                    else:
                        st.success(f"✅ Thank you, {name}! Your enquiry has been received. Our team will call you within 24 hours.")
                        st.balloons()

            st.markdown("""
            <div style="margin-top:22px;display:flex;gap:12px;flex-wrap:wrap;">
                <a class="btn-wa" href="https://wa.me/919999999999?text=Hi!%20I%20am%20interested%20in%20Aranya%20Farms." target="_blank">💬 WhatsApp Us</a>
                <a class="btn-call" href="tel:+919999999999">📞 Call Now</a>
                <a class="btn-green" href="mailto:info@silveroaksrealty.com">📧 Email Us</a>
            </div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="contact-info-box">
                <h3>Silver Oaks Realty</h3>

                <div class="contact-line">
                    <div class="ci-icon">📍</div>
                    <div class="ci-text">
                        <strong>Corporate Office</strong>
                        2nd & 3rd Floor, 14-A,<br>
                        NCL Enclave Road, Petbasheerabad,<br>
                        Kompally, Hyderabad – 500067
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon">🏡</div>
                    <div class="ci-text">
                        <strong>Project Site Office</strong>
                        Aranya Farms, Achampet Village,<br>
                        Toopran Mandal, Medchal-Malkajgiri
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon">📞</div>
                    <div class="ci-text">
                        <strong>Phone / WhatsApp</strong>
                        +91 99999 99999<br>
                        +91 88888 88888
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon">📧</div>
                    <div class="ci-text">
                        <strong>Email</strong>
                        info@silveroaksrealty.com<br>
                        aranyafarms@silveroaks.in
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon">⏰</div>
                    <div class="ci-text">
                        <strong>Office Hours</strong>
                        Mon – Sat: 9:00 AM – 7:00 PM<br>
                        Sunday: 10:00 AM – 5:00 PM
                    </div>
                </div>

                <hr style="border:none;border-top:1px solid rgba(255,255,255,0.1);margin:24px 0;">
                <p style="color:rgba(255,255,255,0.5);font-size:0.82rem;line-height:1.7;margin:0;">
                    🌿 Site visits available 7 days a week.<br>
                    Complimentary pickup from Kompally for groups.
                </p>
            </div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════════════════
def render_footer():
    st.markdown("""
    <div class="footer">
        <div style="display:grid;grid-template-columns:2fr 1fr 1fr;gap:48px;margin-bottom:36px;">
            <div>
                <div class="footer-logo">🌿 Aranya Farms</div>
                <div class="footer-tagline">Play · Live · Celebrate</div>
                <p style="color:rgba(255,255,255,0.4);font-size:0.85rem;line-height:1.85;max-width:320px;font-weight:300;">
                    A premium gated farmland community by Silver Oaks Agro Farms, set across
                    55 acres of lush greenery at Achampet, Toopran, Telangana.
                </p>
            </div>
            <div>
                <p style="color:var(--gold-light);font-size:0.72rem;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px;font-family:'Cinzel',serif;">Pages</p>
                <p style="color:rgba(255,255,255,0.45);font-size:0.88rem;line-height:2.4;font-weight:300;">
                    Home<br>About<br>Properties<br>Location<br>Contact
                </p>
            </div>
            <div>
                <p style="color:var(--gold-light);font-size:0.72rem;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px;font-family:'Cinzel',serif;">Properties</p>
                <p style="color:rgba(255,255,255,0.45);font-size:0.88rem;line-height:2.4;font-weight:300;">
                    Farm Plots<br>3-BHK Farm Houses<br>Premium Villas<br>Farm Lands<br>Book Site Visit
                </p>
            </div>
        </div>
        <div class="footer-copy">
            © 2024 Aranya Farms by Silver Oaks Agro Farms · Silver Oaks Realty · Hyderabad, Telangana<br>
            <span style="font-size:0.7rem;opacity:0.45;">All dimensions and prices are indicative and subject to change. Please contact the sales team for current pricing.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════
def main():
    inject_css()

    if "page" not in st.session_state:
        st.session_state.page = "🏡 Home"

    render_navbar()
    render_page_nav()

    page = st.session_state.page

    if page == "🏡 Home":
        page_home()
    elif page == "🌿 About":
        page_about()
    elif page == "🏘️ Properties":
        page_properties()
    elif page == "📍 Location":
        page_location()
    elif page == "📞 Contact":
        page_contact()

    render_footer()


if __name__ == "__main__":
    main()

import streamlit as st

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Aranya Farms – Luxury Farm Living at Toopran",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── GLOBAL CSS ─────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Lato:wght@300;400;700&display=swap');

    /* ── Reset & Base ── */
    html, body, [class*="css"] {
        font-family: 'Lato', sans-serif;
        scroll-behavior: smooth;
    }
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    #MainMenu, footer, header { visibility: hidden; }

    /* ── Color Tokens ── */
    :root {
        --green-deep:   #1a3a2a;
        --green-mid:    #2d6a4f;
        --green-light:  #52b788;
        --gold:         #c9a84c;
        --gold-light:   #e8c97e;
        --beige:        #f5f0e8;
        --beige-dark:   #ede4d3;
        --white:        #ffffff;
        --text-dark:    #1a2b1e;
        --text-mid:     #3d5a45;
        --text-light:   #6b8c72;
    }

    /* ── TOP NAV BAR ── */
    .top-nav {
        background: var(--green-deep);
        padding: 0 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 68px;
        position: sticky;
        top: 0;
        z-index: 999;
        box-shadow: 0 2px 20px rgba(0,0,0,0.3);
    }
    .nav-logo {
        font-family: 'Playfair Display', serif;
        color: var(--gold);
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .nav-logo span { color: #fff; font-size: 0.7rem; display: block; letter-spacing: 3px; text-transform: uppercase; font-family: 'Lato', sans-serif; font-weight: 300; }

    /* ── SECTION WRAPPERS ── */
    .section { padding: 80px 60px; }
    .section-beige { background: var(--beige); }
    .section-white { background: var(--white); }
    .section-dark  { background: var(--green-deep); color: white; }
    .section-mid   { background: #f0ece3; }

    /* ── HEADINGS ── */
    .section-tag {
        font-size: 0.72rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 700;
        margin-bottom: 10px;
    }
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        font-weight: 700;
        color: var(--green-deep);
        line-height: 1.2;
        margin-bottom: 12px;
    }
    .section-title-white {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        font-weight: 700;
        color: #fff;
        line-height: 1.2;
        margin-bottom: 12px;
    }
    .section-subtitle {
        color: var(--text-mid);
        font-size: 1.05rem;
        line-height: 1.8;
        max-width: 680px;
        margin-bottom: 40px;
    }
    .gold-divider {
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light));
        border-radius: 2px;
        margin: 16px 0 28px;
    }

    /* ── HERO ── */
    .hero-section {
        background: linear-gradient(135deg, #0d2218 0%, #1a3a2a 45%, #2d6a4f 100%);
        padding: 100px 60px 90px;
        position: relative;
        overflow: hidden;
    }
    .hero-section::before {
        content: '';
        position: absolute;
        top: -100px; right: -100px;
        width: 500px; height: 500px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(201,168,76,0.12), transparent 70%);
    }
    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -80px; left: -80px;
        width: 400px; height: 400px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(82,183,136,0.1), transparent 70%);
    }
    .hero-tag {
        font-size: 0.72rem;
        letter-spacing: 5px;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 700;
        margin-bottom: 16px;
    }
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.2rem, 4vw, 3.8rem);
        font-weight: 900;
        color: #fff;
        line-height: 1.15;
        margin-bottom: 20px;
    }
    .hero-title em { color: var(--gold-light); font-style: normal; }
    .hero-subtitle {
        color: rgba(255,255,255,0.78);
        font-size: 1.1rem;
        margin-bottom: 40px;
        line-height: 1.7;
        max-width: 560px;
    }
    .hero-img-placeholder {
        background: linear-gradient(135deg, #2d6a4f, #1a3a2a);
        border: 2px dashed rgba(201,168,76,0.5);
        border-radius: 12px;
        height: 420px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: rgba(255,255,255,0.6);
        font-size: 0.85rem;
        letter-spacing: 1px;
    }
    .hero-img-placeholder .ph-icon { font-size: 3rem; margin-bottom: 12px; opacity: 0.5; }
    .hero-img-placeholder .ph-label { color: var(--gold-light); font-weight: 600; font-size: 0.9rem; }
    .hero-img-placeholder .ph-desc { color: rgba(255,255,255,0.45); font-size: 0.78rem; margin-top: 6px; }

    /* ── HIGHLIGHT BADGES ── */
    .highlights-row {
        display: flex;
        flex-wrap: wrap;
        gap: 14px;
        margin: 36px 0;
    }
    .highlight-badge {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(201,168,76,0.4);
        border-radius: 8px;
        padding: 12px 20px;
        text-align: center;
        backdrop-filter: blur(4px);
        min-width: 130px;
    }
    .highlight-badge .hb-value {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--gold-light);
    }
    .highlight-badge .hb-label {
        font-size: 0.72rem;
        color: rgba(255,255,255,0.65);
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* ── CTA BUTTONS ── */
    .cta-row { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 10px; }
    .btn-primary {
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        color: var(--green-deep);
        padding: 14px 30px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        transition: transform 0.2s, box-shadow 0.2s;
        box-shadow: 0 4px 16px rgba(201,168,76,0.35);
    }
    .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(201,168,76,0.5); }
    .btn-outline {
        background: transparent;
        color: #fff;
        padding: 13px 28px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: 2px solid rgba(255,255,255,0.5);
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        transition: all 0.2s;
    }
    .btn-outline:hover { border-color: var(--gold); color: var(--gold); }
    .btn-green {
        background: linear-gradient(135deg, var(--green-mid), var(--green-deep));
        color: #fff;
        padding: 13px 28px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.88rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 4px 14px rgba(45,106,79,0.4);
    }
    .btn-whatsapp {
        background: #25d366;
        color: #fff;
        padding: 13px 28px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.88rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        display: inline-block;
        box-shadow: 0 4px 14px rgba(37,211,102,0.4);
    }
    .btn-call {
        background: #2196f3;
        color: #fff;
        padding: 13px 28px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.88rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        display: inline-block;
    }

    /* ── FEATURE CARDS (About) ── */
    .feature-card {
        background: white;
        border-radius: 12px;
        padding: 32px 28px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.07);
        border-bottom: 4px solid var(--gold);
        text-align: center;
        height: 100%;
        transition: transform 0.25s, box-shadow 0.25s;
    }
    .feature-card:hover { transform: translateY(-4px); box-shadow: 0 12px 36px rgba(0,0,0,0.12); }
    .feature-card .fc-icon { font-size: 2.4rem; margin-bottom: 14px; }
    .feature-card h4 {
        font-family: 'Playfair Display', serif;
        color: var(--green-deep);
        font-size: 1.15rem;
        margin-bottom: 10px;
    }
    .feature-card p { color: var(--text-mid); font-size: 0.92rem; line-height: 1.7; margin: 0; }

    /* ── PROPERTY CARDS ── */
    .prop-card {
        background: white;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 28px rgba(0,0,0,0.09);
        transition: transform 0.25s, box-shadow 0.25s;
        height: 100%;
    }
    .prop-card:hover { transform: translateY(-5px); box-shadow: 0 16px 44px rgba(0,0,0,0.14); }
    .prop-img-placeholder {
        background: linear-gradient(135deg, #2d6a4f, #1a3a2a);
        height: 210px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 2px dashed rgba(201,168,76,0.4);
        color: rgba(255,255,255,0.55);
        font-size: 0.78rem;
        letter-spacing: 1px;
        gap: 8px;
    }
    .prop-img-placeholder .ph-icon2 { font-size: 2.4rem; opacity: 0.45; }
    .prop-img-placeholder .ph-label2 { color: var(--gold-light); font-size: 0.82rem; font-weight: 600; }
    .prop-badge {
        display: inline-block;
        background: var(--gold);
        color: var(--green-deep);
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .prop-body { padding: 24px; }
    .prop-body h3 {
        font-family: 'Playfair Display', serif;
        color: var(--green-deep);
        font-size: 1.25rem;
        margin-bottom: 6px;
    }
    .prop-body .price {
        color: var(--gold);
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 10px;
        font-family: 'Playfair Display', serif;
    }
    .prop-specs { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
    .spec-pill {
        background: var(--beige);
        color: var(--text-mid);
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 20px;
        border: 1px solid var(--beige-dark);
    }
    .prop-body p { color: var(--text-mid); font-size: 0.88rem; line-height: 1.65; }

    /* ── GALLERY GRID ── */
    .gallery-category {
        margin-bottom: 44px;
    }
    .gallery-cat-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        color: var(--green-deep);
        font-weight: 700;
        margin-bottom: 16px;
        padding-bottom: 8px;
        border-bottom: 2px solid var(--gold);
        display: inline-block;
    }
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
    }
    .gallery-thumb {
        background: linear-gradient(135deg, #2d6a4f 0%, #1a3a2a 100%);
        border-radius: 10px;
        height: 180px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 1.5px dashed rgba(201,168,76,0.45);
        cursor: pointer;
        transition: transform 0.2s, border-color 0.2s;
        gap: 8px;
    }
    .gallery-thumb:hover { transform: scale(1.02); border-color: var(--gold); }
    .gallery-thumb .gt-icon { font-size: 2rem; opacity: 0.5; }
    .gallery-thumb .gt-label { color: var(--gold-light); font-size: 0.78rem; font-weight: 600; letter-spacing: 1px; }
    .gallery-thumb .gt-sub { color: rgba(255,255,255,0.4); font-size: 0.7rem; }

    /* ── LOCATION ── */
    .loc-highlight {
        display: flex;
        align-items: flex-start;
        gap: 16px;
        padding: 18px 0;
        border-bottom: 1px solid var(--beige-dark);
    }
    .loc-icon { font-size: 1.6rem; min-width: 40px; }
    .loc-content h4 { color: var(--green-deep); font-size: 1rem; font-weight: 700; margin-bottom: 4px; }
    .loc-content p { color: var(--text-mid); font-size: 0.88rem; margin: 0; }
    .map-placeholder {
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        border: 2px dashed #81c784;
        border-radius: 12px;
        height: 380px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 14px;
        color: #388e3c;
    }
    .map-placeholder .mp-icon { font-size: 3.5rem; opacity: 0.6; }
    .map-placeholder .mp-label { font-size: 1rem; font-weight: 700; color: #2e7d32; }
    .map-placeholder .mp-desc { font-size: 0.82rem; color: #558b2f; text-align: center; max-width: 260px; }

    /* ── CONTACT FORM ── */
    .contact-card {
        background: white;
        border-radius: 16px;
        padding: 44px 40px;
        box-shadow: 0 8px 40px rgba(0,0,0,0.1);
    }
    .contact-info-box {
        background: linear-gradient(160deg, var(--green-deep), #2d6a4f);
        border-radius: 16px;
        padding: 40px 32px;
        color: white;
        height: 100%;
    }
    .contact-info-box h3 {
        font-family: 'Playfair Display', serif;
        color: var(--gold-light);
        font-size: 1.4rem;
        margin-bottom: 20px;
    }
    .contact-line {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        margin-bottom: 22px;
    }
    .contact-line .ci-icon { font-size: 1.3rem; min-width: 32px; margin-top: 2px; }
    .contact-line .ci-text { font-size: 0.9rem; color: rgba(255,255,255,0.85); line-height: 1.6; }
    .contact-line .ci-text strong { color: white; display: block; margin-bottom: 2px; }
    .stTextInput > div > div > input,
    .stSelectbox > div > div,
    .stTextArea > div > div > textarea {
        border: 1.5px solid #d8e8dc !important;
        border-radius: 8px !important;
        font-family: 'Lato', sans-serif !important;
        transition: border-color 0.2s !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--green-mid) !important;
        box-shadow: 0 0 0 3px rgba(45,106,79,0.12) !important;
    }
    .stButton > button {
        border-radius: 6px !important;
        font-family: 'Lato', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--gold), var(--gold-light)) !important;
        color: var(--green-deep) !important;
        border: none !important;
    }

    /* ── FOOTER ── */
    .footer {
        background: #0d1f15;
        color: rgba(255,255,255,0.6);
        padding: 50px 60px 30px;
    }
    .footer-logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        color: var(--gold);
        font-weight: 700;
        margin-bottom: 6px;
    }
    .footer-tagline {
        font-size: 0.75rem;
        letter-spacing: 3px;
        color: rgba(255,255,255,0.4);
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .footer-divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.1);
        margin: 28px 0;
    }
    .footer-copy { font-size: 0.8rem; text-align: center; color: rgba(255,255,255,0.35); }

    /* ── STATS STRIP ── */
    .stats-strip {
        background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 50%, var(--gold) 100%);
        padding: 40px 60px;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 20px;
    }
    .stat-item { text-align: center; }
    .stat-value {
        font-family: 'Playfair Display', serif;
        font-size: 2.4rem;
        font-weight: 900;
        color: var(--green-deep);
        line-height: 1;
    }
    .stat-label {
        font-size: 0.75rem;
        color: rgba(26,58,42,0.75);
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 6px;
    }

    /* ── AMENITIES ── */
    .amenity-chip {
        background: white;
        border: 1.5px solid var(--beige-dark);
        border-left: 4px solid var(--green-mid);
        border-radius: 8px;
        padding: 12px 16px;
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 0.88rem;
        color: var(--text-dark);
        font-weight: 500;
    }
    .amenity-chip .ac-icon { font-size: 1.2rem; }

    /* ── PAGE NAV PILLS ── */
    div[data-testid="stHorizontalBlock"] > div > div > div > button {
        border-radius: 4px !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.5px !important;
    }

    /* ── RESPONSIVE ── */
    @media (max-width: 768px) {
        .section { padding: 50px 20px; }
        .hero-section { padding: 60px 20px; }
        .footer { padding: 40px 20px 24px; }
        .gallery-grid { grid-template-columns: repeat(2,1fr); }
        .stats-strip { padding: 30px 20px; }
        .hero-title { font-size: 2rem; }
    }
    </style>
    """, unsafe_allow_html=True)


# ─── NAV BAR ────────────────────────────────────────────────────────────────
def render_navbar():
    import os
    logo_path = "images/logo.png"
    if os.path.exists(logo_path):
        import base64
        with open(logo_path, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
        logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height:44px;object-fit:contain;" alt="Aranya Farms Logo">'
    else:
        logo_html = '<div class="nav-logo">🌿 Aranya Farms<span>Silver Oaks Agro Farms · Achampet, Toopran</span></div>'

    st.markdown(f"""
    <div class="top-nav">
        <div style="display:flex;align-items:center;gap:14px;">
            {logo_html}
            <div>
                <div class="nav-logo" style="font-size:1.2rem;line-height:1.1;">Aranya Farms</div>
                <span style="color:#fff;font-size:0.62rem;letter-spacing:3px;text-transform:uppercase;font-family:'Lato',sans-serif;font-weight:300;opacity:0.7;">Silver Oaks Agro Farms · Achampet, Toopran</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── PAGE NAV BUTTONS ────────────────────────────────────────────────────────
PAGES = ["🏡 Home", "🌿 About", "🏘️ Properties", "📷 Gallery", "📍 Location", "📞 Contact"]

def render_page_nav():
    st.markdown("<div style='background:#f5f0e8; padding:10px 40px; border-bottom:1px solid #e0d8cc;'>", unsafe_allow_html=True)
    cols = st.columns(len(PAGES))
    for i, page in enumerate(PAGES):
        with cols[i]:
            if st.button(page, key=f"nav_{i}", use_container_width=True):
                st.session_state.page = page
    st.markdown("</div>", unsafe_allow_html=True)


# ─── HELPERS ─────────────────────────────────────────────────────────────────
def img_placeholder(label, desc="Add photo here", height=210, icon="🖼️"):
    return f"""
    <div class="prop-img-placeholder" style="height:{height}px;">
        <div class="ph-icon2">{icon}</div>
        <div class="ph-label2">{label}</div>
        <div style="color:rgba(255,255,255,0.4);font-size:0.7rem;">{desc}</div>
    </div>"""

def gallery_thumb(label, sub="Add photo"):
    return f"""
    <div class="gallery-thumb">
        <div class="gt-icon">📸</div>
        <div class="gt-label">{label}</div>
        <div class="gt-sub">{sub}</div>
    </div>"""


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 1 — HOME
# ═══════════════════════════════════════════════════════════════════════════
def page_home():
    # HERO
    st.markdown("""
    <div class="hero-section">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 0.9], gap="large")
    with col1:
        st.markdown("""
        <div class="hero-tag">🌿 Silver Oaks Agro Farms Presents</div>
        <h1 class="hero-title">Luxury Farm Living<br>at <em>Aranya Farms</em></h1>
        <p class="hero-subtitle">
            Premium Farm Plots & 3-BHK Farm Houses at Achampet, Toopran.<br>
            Where nature meets refined living — your perfect weekend escape.
        </p>
        <div class="highlights-row">
            <div class="highlight-badge"><div class="hb-value">55</div><div class="hb-label">Acres</div></div>
            <div class="highlight-badge"><div class="hb-value">Gated</div><div class="hb-label">Community</div></div>
            <div class="highlight-badge"><div class="hb-value">3-BHK</div><div class="hb-label">Farm Houses</div></div>
            <div class="highlight-badge"><div class="hb-value">5 min</div><div class="hb-label">From RRR</div></div>
            <div class="highlight-badge"><div class="hb-value">30 min</div><div class="hb-label">From ORR</div></div>
            <div class="highlight-badge"><div class="hb-value">₹49L+</div><div class="hb-label">Starting</div></div>
        </div>
        <div class="cta-row">
            <a class="btn-primary" href="#">📅 Book Site Visit</a>
            <a class="btn-outline" href="#">🏘️ View Properties</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        import os
        if os.path.exists("images/land1.jpg"):
            st.image("images/land1.jpg", use_container_width=True)
        else:
            st.markdown("""
            <div class="hero-img-placeholder">
                <div class="ph-icon">🌅</div>
                <div class="ph-label">Add images/land1.jpg</div>
                <div class="ph-desc">Upload land photos to images/ folder</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # STATS STRIP
    st.markdown("""
    <div class="stats-strip">
        <div class="stat-item"><div class="stat-value">55+</div><div class="stat-label">Acres of Green</div></div>
        <div class="stat-item"><div class="stat-value">200+</div><div class="stat-label">Happy Families</div></div>
        <div class="stat-item"><div class="stat-value">15+</div><div class="stat-label">Amenities</div></div>
        <div class="stat-item"><div class="stat-value">₹49L</div><div class="stat-label">Starting Price</div></div>
        <div class="stat-item"><div class="stat-value">2024</div><div class="stat-label">Ready Possession</div></div>
    </div>
    """, unsafe_allow_html=True)

    # WHY ARANYA FARMS
    st.markdown("""
    <div class="section section-beige">
        <div class="section-tag">Why Choose Us</div>
        <div class="section-title">The Aranya Farms Difference</div>
        <div class="gold-divider"></div>
        <p class="section-subtitle">
            A unique blend of luxury living and nature's serenity — thoughtfully designed for families
            who seek more than just a home.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding: 0 60px 60px; background: #f5f0e8;">', unsafe_allow_html=True)
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
                <div class="feature-card">
                    <div class="fc-icon">{icon}</div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # AMENITIES
    st.markdown("""
    <div class="section section-white">
        <div class="section-tag">World-Class Amenities</div>
        <div class="section-title">Everything You Need to <em style="font-style:normal;color:#2d6a4f;">Live Well</em></div>
        <div class="gold-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding: 0 60px 70px; background: white;">', unsafe_allow_html=True)
        amenities = [
            ("🏊", "Swimming Pool"), ("🎾", "Sports Arena"), ("🌿", "Organic Farming"),
            ("🐄", "Goshala"), ("🌸", "Gazebo & Gardens"), ("🏋️", "Fitness Centre"),
            ("🍽️", "Clubhouse & Dining"), ("🛕", "Meditation Zone"), ("🎠", "Children's Play Area"),
            ("🌳", "Tree Plantation"), ("🚗", "Ample Parking"), ("💧", "24×7 Water Supply"),
        ]
        rows = [amenities[i:i+4] for i in range(0, len(amenities), 4)]
        for row in rows:
            cols = st.columns(4, gap="small")
            for col, (icon, name) in zip(cols, row):
                with col:
                    st.markdown(f'<div class="amenity-chip"><span class="ac-icon">{icon}</span>{name}</div>', unsafe_allow_html=True)
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # QUICK CTA BANNER
    st.markdown("""
    <div class="section section-dark" style="text-align:center;">
        <div class="section-tag" style="text-align:center;">Limited Plots Available</div>
        <div class="section-title-white">Ready to Find Your Perfect Farm Plot?</div>
        <div class="gold-divider" style="margin:16px auto 28px;"></div>
        <p style="color:rgba(255,255,255,0.7);font-size:1.05rem;margin-bottom:36px;">
            Plots starting from ₹49 Lakhs. Register now for exclusive pre-launch pricing.
        </p>
        <div class="cta-row" style="justify-content:center;">
            <a class="btn-primary" href="#">📅 Book Free Site Visit</a>
            <a class="btn-outline" href="#">📞 Talk to Expert</a>
            <a class="btn-outline" href="#">📄 Download Brochure</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 2 — ABOUT
# ═══════════════════════════════════════════════════════════════════════════
def page_about():
    st.markdown("""
    <div class="hero-section" style="padding:70px 60px;">
        <div class="hero-tag">Our Story</div>
        <h1 class="hero-title" style="font-size:3rem;">About <em>Aranya Farms</em></h1>
        <p class="hero-subtitle">Play | Live | Celebrate — A new way to belong to nature.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section section-beige">
        <div class="section-tag">The Vision</div>
        <div class="section-title">Where Rural Richness Meets Urban Comfort</div>
        <div class="gold-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 60px 60px;background:#f5f0e8;">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1], gap="large")
        with col1:
            st.markdown(f"""
            {img_placeholder("About Us – Farm Aerial View", "Add aerial/landscape photo", 340, "🏞️")}
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="padding:20px 0;">
            <p style="color:#3d5a45;font-size:1.05rem;line-height:1.85;margin-bottom:20px;">
                <strong style="color:#1a3a2a;">Aranya Farms</strong> is not just a real estate project — it is a lifestyle reimagined.
                Spread across <strong>55 lush acres</strong> in Achampet, Toopran, Aranya Farms brings together the
                warmth of rural living with the comforts of a premium gated community.
            </p>
            <p style="color:#3d5a45;font-size:1.05rem;line-height:1.85;margin-bottom:20px;">
                Conceived by <strong style="color:#1a3a2a;">Silver Oaks Agro Farms</strong>, a trusted name in managed farmland
                communities, this project is born from a simple belief: <em>every family deserves a sanctuary
                where they can breathe freely, grow organically, and celebrate life.</em>
            </p>
            <p style="color:#3d5a45;font-size:1.05rem;line-height:1.85;">
                Adjacent to the tranquil Haldi River and just 5 minutes from the Ring Road (RRR),
                Aranya Farms is the perfect balance of accessibility and escape.
            </p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # PLAY LIVE CELEBRATE
    st.markdown("""
    <div class="section section-white" style="text-align:center;">
        <div class="section-tag" style="text-align:center;">Our Philosophy</div>
        <div class="section-title" style="text-align:center;">Play · Live · Celebrate</div>
        <div class="gold-divider" style="margin:16px auto 28px;"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 60px 60px;background:white;">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3, gap="medium")
        pillars = [
            ("🎠", "Play", "Sports arenas, swimming pool, children's zones, nature trails — because life is meant to be enjoyed at every age, every weekend."),
            ("🏡", "Live", "Thoughtfully crafted farm houses and plots designed for wholesome family living. Wake up to birdsong, grow your own food, breathe clean air."),
            ("🎉", "Celebrate", "From festive gatherings at the clubhouse to quiet birthday mornings in the gazebo — every milestone is better amid nature."),
        ]
        for col, (icon, title, desc) in zip([c1, c2, c3], pillars):
            with col:
                st.markdown(f"""
                <div class="feature-card" style="border-bottom-color:#2d6a4f;text-align:left;">
                    <div class="fc-icon">{icon}</div>
                    <h4 style="font-size:1.4rem;">{title}</h4>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # LIFESTYLE SECTION
    st.markdown("""
    <div class="section section-beige">
        <div class="section-tag">Lifestyle & Wellness</div>
        <div class="section-title">Designed for Every Chapter of Life</div>
        <div class="gold-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 60px 60px;background:#f5f0e8;">', unsafe_allow_html=True)
        lifestyles = [
            ("👨‍👩‍👧‍👦", "Family Lifestyle", "Spacious plots with dedicated zones for kids, elders, and togetherness. A community where neighbours become extended family."),
            ("🧘", "Wellness Retreat", "Yoga pavilion, meditation zones, organic garden walks, and fresh-air mornings — your personal wellness sanctuary."),
            ("🏡", "Weekend Homes", "Just 30 minutes from ORR — the ideal weekend getaway that feels a world away. Rent-ready investment properties."),
            ("🌱", "Organic Living", "Farm-to-table living. Grow your own vegetables, herbs, and fruits on your private plot with managed farming support."),
        ]
        c1, c2 = st.columns(2, gap="medium")
        for i, (icon, title, desc) in enumerate(lifestyles):
            with (c1 if i % 2 == 0 else c2):
                st.markdown(f"""
                <div style="display:flex;gap:16px;padding:20px;background:white;border-radius:10px;margin-bottom:14px;box-shadow:0 2px 12px rgba(0,0,0,0.06);">
                    <div style="font-size:2rem;min-width:44px;">{icon}</div>
                    <div>
                        <h4 style="color:#1a3a2a;font-family:'Playfair Display',serif;margin-bottom:6px;">{title}</h4>
                        <p style="color:#3d5a45;font-size:0.9rem;margin:0;line-height:1.65;">{desc}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # SILVER OAKS
    st.markdown("""
    <div class="section section-dark">
        <div class="section-tag" style="text-align:center;">About the Developer</div>
        <div class="section-title-white" style="text-align:center;">Silver Oaks Agro Farms</div>
        <div class="gold-divider" style="margin:16px auto 28px;"></div>
        <p style="color:rgba(255,255,255,0.75);font-size:1.05rem;line-height:1.85;max-width:760px;margin:0 auto;text-align:center;">
            Silver Oaks Agro Farms, operating under <strong style="color:#e8c97e;">Silver Oaks Realty</strong>,
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
    <div class="hero-section" style="padding:70px 60px;">
        <div class="hero-tag">Properties & Plots</div>
        <h1 class="hero-title">Find Your <em>Perfect Space</em></h1>
        <p class="hero-subtitle">Farm plots, 3-BHK homes, premium villas — choose what suits your dream.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section section-beige">
        <div class="section-tag">Available Properties</div>
        <div class="section-title">Explore Our Offerings</div>
        <div class="gold-divider"></div>
        <p class="section-subtitle">All properties are within the 55-acre gated community with access to all amenities.</p>
    </div>
    """, unsafe_allow_html=True)

    properties = [
        {
            "badge": "Best Seller",
            "icon": "🌾",
            "title": "Farm Plots",
            "price": "Starting ₹49 Lakhs",
            "specs": ["300 sq. yds", "605 sq. yds", "640 sq. yds", "753 sq. yds"],
            "desc": "Open farm plots in a gated, amenity-rich community. Build your dream home or enjoy managed farming. Clear titles, DTCP approved layout.",
            "note": "Plot photo — aerial / ground level",
        },
        {
            "badge": "Most Popular",
            "icon": "🏡",
            "title": "3-BHK Farm Houses",
            "price": "Starting ₹65 Lakhs",
            "specs": ["1480 sft BUA", "685 sft BUA", "1500 sft BUA"],
            "desc": "Ready-to-move 3-BHK farm houses with contemporary architecture, private garden space, and complete modern amenities.",
            "note": "Farm house exterior / interior photo",
        },
        {
            "badge": "Luxury",
            "icon": "🏰",
            "title": "Premium Villas",
            "price": "Starting ₹90 Lakhs",
            "specs": ["2250 sft BUA", "Large Plot", "Private Garden"],
            "desc": "Exclusive premium villas with expansive built-up areas, landscaped private gardens, and premium finishes for the discerning buyer.",
            "note": "Villa exterior / aerial photo",
        },
        {
            "badge": "Investment",
            "icon": "🌳",
            "title": "Larger Farm Lands",
            "price": "On Request",
            "specs": ["1+ Acre", "Custom Layout", "Managed Option"],
            "desc": "Bulk farmland parcels ideal for families or investor groups looking for larger green footprints with full community access.",
            "note": "Landscape / large plot photo",
        },
    ]

    with st.container():
        st.markdown('<div style="padding:0 60px 70px;background:#f5f0e8;">', unsafe_allow_html=True)
        c1, c2 = st.columns(2, gap="medium")
        for i, prop in enumerate(properties):
            with (c1 if i % 2 == 0 else c2):
                st.markdown(f"""
                <div class="prop-card">
                    {img_placeholder(prop["note"], "Add property photo here", 210, prop["icon"])}
                    <div class="prop-body">
                        <div class="prop-badge">{prop["badge"]}</div>
                        <h3>{prop["title"]}</h3>
                        <div class="price">{prop["price"]}</div>
                        <div class="prop-specs">
                            {"".join(f'<span class="spec-pill">{s}</span>' for s in prop["specs"])}
                        </div>
                        <p>{prop["desc"]}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
                if st.button(f"📩 Enquire About {prop['title']}", key=f"prop_btn_{i}", use_container_width=True):
                    st.session_state.page = "📞 Contact"
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # PLOT SIZE TABLE
    st.markdown("""
    <div class="section section-white">
        <div class="section-tag">Plot Dimensions</div>
        <div class="section-title">Plot Sizes at a Glance</div>
        <div class="gold-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 60px 60px;background:white;">', unsafe_allow_html=True)
        import pandas as pd
        df = pd.DataFrame({
            "Type": ["Farm Plot – Compact", "Farm Plot – Standard", "Farm Plot – Large", "Farm Plot – Premium", "Farm House – 3 BHK (A)", "Farm House – 3 BHK (B)", "Farm House – 3 BHK (C)", "Premium Villa"],
            "Plot Size": ["300 sq. yds", "605 sq. yds", "640 sq. yds", "753 sq. yds", "Included", "Included", "Included", "Large"],
            "Built-up Area": ["—", "—", "—", "—", "685 sft", "1480 sft", "1500 sft", "2250 sft"],
            "Starting Price": ["₹49 Lakhs", "₹55 Lakhs", "₹60 Lakhs", "₹68 Lakhs", "₹65 Lakhs", "₹72 Lakhs", "₹78 Lakhs", "₹90 Lakhs"],
            "Status": ["Available", "Limited", "Available", "Limited", "Available", "Ready Soon", "Available", "Pre-launch"],
        })
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 4 — GALLERY
# ═══════════════════════════════════════════════════════════════════════════
def page_gallery():
    st.markdown("""
    <div class="hero-section" style="padding:70px 60px;">
        <div class="hero-tag">Visual Tour</div>
        <h1 class="hero-title">Gallery — <em>Aranya Farms</em></h1>
        <p class="hero-subtitle">Explore our community through images. Real photos coming soon!</p>
    </div>
    """, unsafe_allow_html=True)

    import os

    # ── REAL LAND PHOTOS ──
    land_photos = [
        ("images/land1.jpg", "View 1 — Farm Land"),
        ("images/land2.jpg", "View 2 — Young Plantation"),
        ("images/land3.jpg", "View 3 — Coconut Grove"),
        ("images/land4.jpg", "View 4 — Saplings Row"),
    ]
    real_photos = [(p, c) for p, c in land_photos if os.path.exists(p)]

    st.markdown('<div class="section section-beige">', unsafe_allow_html=True)

    if real_photos:
        st.markdown("""
        <div class="gallery-category">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:18px;">
                <span style="font-size:1.6rem;">🌾</span>
                <span class="gallery-cat-title">Land — Aranya Farms, Achampet</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        cols = st.columns(len(real_photos), gap="small")
        for col, (path, caption) in zip(cols, real_photos):
            with col:
                st.image(path, caption=caption, use_container_width=True)
        st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    gallery_data = [
        ("🏰", "Villas & Farm Houses", ["Front Elevation", "Living Room", "Master Bedroom", "Kitchen", "Balcony View", "Rear Garden"]),
        ("🏛️", "Clubhouse", ["Lobby", "Lounge Area", "Dining Hall", "Event Space", "Meeting Room", "Terrace"]),
        ("🏊", "Pool & Guest Rooms", ["Main Pool", "Kids Pool", "Pool Deck", "Guest Room A", "Guest Room B", "Suite View"]),
        ("🏏", "Sports Arena", ["Cricket Pitch", "Badminton Court", "Tennis Court", "Volleyball", "Kids Play Zone", "Cycling Track"]),
        ("🌸", "Gazebo & Gardens", ["Main Gazebo", "Water Feature", "Flower Garden", "Organic Farm", "Walking Path", "Sunset Lawn"]),
        ("🐄", "Goshala", ["Goshala Entry", "Cows", "Organic Manure Unit", "Milking Area", "Calf Zone", "Feed Store"]),
        ("🗺️", "Layout Plan", ["Master Layout", "Phase 1 Plan", "Phase 2 Plan", "Zoning Map", "Amenities Map", "Road Network"]),
        ("📍", "Location Map", ["Google Map View", "Satellite View", "RRR Junction", "ORR Route", "Landmark View", "Entry Gate"]),
    ]

    for icon, cat, images in gallery_data:
        st.markdown(f"""
        <div class="gallery-category">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:18px;">
                <span style="font-size:1.6rem;">{icon}</span>
                <span class="gallery-cat-title">{cat}</span>
            </div>
            <div class="gallery-grid">
                {"".join(gallery_thumb(img, "Add photo") for img in images)}
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f5f0e8;padding:20px 60px 50px;text-align:center;">
        <p style="color:#6b8c72;font-size:0.9rem;">
            📸 <em>Actual photos and drone footage will be added here. Contact us for a virtual tour or to schedule an in-person site visit.</em>
        </p>
        <a class="btn-green" href="#" style="display:inline-block;margin-top:12px;">📅 Book a Site Visit</a>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 5 — LOCATION
# ═══════════════════════════════════════════════════════════════════════════
def page_location():
    st.markdown("""
    <div class="hero-section" style="padding:70px 60px;">
        <div class="hero-tag">Find Us</div>
        <h1 class="hero-title">Location & <em>Connectivity</em></h1>
        <p class="hero-subtitle">Strategically located in Achampet, Toopran — nature close, city closer.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section section-beige">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            st.markdown("""
            <div class="section-tag">How to Reach</div>
            <div class="section-title">Location Highlights</div>
            <div class="gold-divider"></div>
            """, unsafe_allow_html=True)

            highlights = [
                ("📍", "Exact Location", "Achampet Village, Toopran Mandal, Medchal-Malkajgiri District, Telangana"),
                ("🛣️", "Near RRR", "Only 5 minutes from the Regional Ring Road (RRR) entry point"),
                ("🔄", "Near ORR", "Approx. 30 minutes from the Outer Ring Road (ORR), Hyderabad"),
                ("🏙️", "NH-44 Access", "Adjacent to the Hyderabad–Medchal Highway (National Highway 44)"),
                ("🌊", "Riverside", "Project is adjacent to the scenic Haldi River — beautiful water views"),
                ("🏘️", "Near Masaipet", "Close to Masaipet town — easy access to local markets and services"),
                ("✈️", "Airport", "Approx. 40–50 minutes from Rajiv Gandhi International Airport"),
                ("🏥", "Healthcare", "Multiple hospitals and clinics within 15–20 km radius"),
            ]
            for icon, title, desc in highlights:
                st.markdown(f"""
                <div class="loc-highlight">
                    <div class="loc-icon">{icon}</div>
                    <div class="loc-content">
                        <h4>{title}</h4>
                        <p>{desc}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="section-tag">Map</div>
            <div class="section-title">View on Map</div>
            <div class="gold-divider"></div>
            """, unsafe_allow_html=True)

            # Placeholder map — replace with st.components.v1.iframe() for actual embed
            st.markdown("""
            <div class="map-placeholder">
                <div class="mp-icon">🗺️</div>
                <div class="mp-label">Google Maps – Aranya Farms</div>
                <div class="mp-desc">
                    Achampet, Toopran, Medchal-Malkajgiri Dist., Telangana<br><br>
                    <em>Embed Google Maps iframe here. Use:<br>
                    st.components.v1.iframe(src="MAPS_URL")</em>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="margin-top:20px;">
                <a class="btn-green" href="https://maps.google.com/?q=Achampet+Toopran+Telangana" target="_blank" style="display:inline-block;">
                    🗺️ Open in Google Maps
                </a>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # DISTANCE TABLE
    st.markdown("""
    <div class="section section-white">
        <div class="section-tag">Distances</div>
        <div class="section-title">Key Distances from Aranya Farms</div>
        <div class="gold-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 60px 60px;background:white;">', unsafe_allow_html=True)
        import pandas as pd
        df = pd.DataFrame({
            "Destination": ["RRR (Regional Ring Road)", "ORR (Outer Ring Road)", "Kompally", "Medchal Town", "Hyderabad City Centre", "RGIA Airport", "Masaipet", "Haldi River"],
            "Distance": ["~5 km", "~30 km", "~28 km", "~18 km", "~38 km", "~48 km", "~3 km", "Adjacent"],
            "Travel Time": ["~5 mins", "~30 mins", "~28 mins", "~18 mins", "~40 mins", "~50 mins", "~5 mins", "Walking"],
            "Via": ["State Highway", "NH-44 + RRR", "NH-44", "NH-44", "NH-44 + ORR", "ORR + Shamshabad", "Local Road", "—"],
        })
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 6 — CONTACT
# ═══════════════════════════════════════════════════════════════════════════
def page_contact():
    st.markdown("""
    <div class="hero-section" style="padding:70px 60px;">
        <div class="hero-tag">Get in Touch</div>
        <h1 class="hero-title">Contact <em>Us</em></h1>
        <p class="hero-subtitle">We'd love to hear from you. Let's find your perfect farm plot.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section section-beige">', unsafe_allow_html=True)
        col1, col2 = st.columns([1.2, 0.8], gap="large")

        with col1:
            st.markdown("""
            <div class="contact-card">
                <div class="section-tag">Send Enquiry</div>
                <div class="section-title" style="font-size:1.9rem;">Let's Talk</div>
                <div class="gold-divider"></div>
            """, unsafe_allow_html=True)

            with st.form("enquiry_form", clear_on_submit=True):
                c1f, c2f = st.columns(2)
                with c1f:
                    name = st.text_input("Full Name *", placeholder="Your full name")
                with c2f:
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

                submitted = st.form_submit_button("📩 Submit Enquiry", use_container_width=True, type="primary")
                if submitted:
                    if not name or not phone or interest == "Select an option…":
                        st.error("Please fill in Name, Phone, and select your Interest.")
                    else:
                        st.success(f"✅ Thank you, {name}! Your enquiry has been received. Our team will call you within 24 hours.")
                        st.balloons()

            st.markdown("</div>", unsafe_allow_html=True)

            # WhatsApp / Call buttons
            st.markdown("""
            <div style="margin-top:20px;display:flex;gap:14px;flex-wrap:wrap;">
                <a class="btn-whatsapp" href="https://wa.me/919999999999?text=Hi!%20I%20am%20interested%20in%20Aranya%20Farms." target="_blank">
                    💬 WhatsApp Us
                </a>
                <a class="btn-call" href="tel:+919999999999">
                    📞 Call Now
                </a>
                <a class="btn-primary" href="mailto:info@silveroaksrealty.com">
                    📧 Email Us
                </a>
            </div>
            <p style="color:#9aada0;font-size:0.78rem;margin-top:10px;">
                * Replace phone numbers and email above with actual contact details.
            </p>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="contact-info-box">
                <h3>Silver Oaks Realty</h3>

                <div class="contact-line">
                    <div class="ci-icon">📍</div>
                    <div class="ci-text">
                        <strong>Corporate Office</strong>
                        2nd & 3rd Floor, 14-A,<br>
                        NCL Enclave Road,<br>
                        Petbasheerabad, Kompally,<br>
                        Hyderabad, Telangana – 500067
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon">🏡</div>
                    <div class="ci-text">
                        <strong>Project Site Office</strong>
                        Aranya Farms, Achampet Village,<br>
                        Toopran Mandal, Medchal-Malkajgiri,<br>
                        Telangana
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

                <hr style="border:none;border-top:1px solid rgba(255,255,255,0.15);margin:24px 0;">

                <p style="color:rgba(255,255,255,0.6);font-size:0.82rem;line-height:1.7;">
                    🌿 Site visits are available 7 days a week.<br>
                    Complimentary pickup from Kompally available for groups.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════════════════
def render_footer():
    st.markdown("""
    <div class="footer">
        <div style="display:grid;grid-template-columns:2fr 1fr 1fr;gap:40px;margin-bottom:30px;flex-wrap:wrap;">
            <div>
                <div class="footer-logo">🌿 Aranya Farms</div>
                <div class="footer-tagline">Play · Live · Celebrate</div>
                <p style="color:rgba(255,255,255,0.5);font-size:0.88rem;line-height:1.8;max-width:320px;">
                    A premium gated farmland community by Silver Oaks Agro Farms, set across 55 acres
                    of lush greenery at Achampet, Toopran, Telangana.
                </p>
            </div>
            <div>
                <p style="color:var(--gold-light);font-size:0.8rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">Quick Links</p>
                <p style="color:rgba(255,255,255,0.5);font-size:0.88rem;line-height:2.2;">
                    Home<br>About<br>Properties<br>Gallery<br>Location<br>Contact
                </p>
            </div>
            <div>
                <p style="color:var(--gold-light);font-size:0.8rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;">Properties</p>
                <p style="color:rgba(255,255,255,0.5);font-size:0.88rem;line-height:2.2;">
                    Farm Plots<br>3-BHK Farm Houses<br>Premium Villas<br>Farm Lands<br>Book Site Visit
                </p>
            </div>
        </div>
        <hr class="footer-divider">
        <p class="footer-copy">
            © 2024 Aranya Farms by Silver Oaks Agro Farms · Silver Oaks Realty · Hyderabad, Telangana<br>
            <span style="font-size:0.72rem;opacity:0.5;">All dimensions and prices are indicative and subject to change. Please contact sales team for current pricing.</span>
        </p>
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
    elif page == "📷 Gallery":
        page_gallery()
    elif page == "📍 Location":
        page_location()
    elif page == "📞 Contact":
        page_contact()

    render_footer()


if __name__ == "__main__":
    main()

import streamlit as st
import os
import base64
import pandas as pd
from datetime import datetime

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Aranya Farms – Luxury Farm Living",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── GLOBAL CSS ─────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=Cinzel:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        scroll-behavior: smooth;
    }
    .main .block-container {
        padding: 0 0 40px 0 !important;
        max-width: 480px !important;
        margin: 0 auto !important;
    }
    #MainMenu, footer, header { visibility: hidden; }
    .stApp { background: #faf7f0; }

    :root {
        --forest:      #0a1f12;
        --deep:        #142d1e;
        --mid:         #2d6a4f;
        --sage:        #4a8c68;
        --leaf:        #7abf94;
        --gold:        #c9a84c;
        --gold-light:  #e8c97e;
        --gold-pale:   #f5e9c5;
        --cream:       #faf7f0;
        --sand:        #f0ead8;
        --parchment:   #e8dfc8;
        --white:       #ffffff;
        --ink:         #1a2b1e;
        --moss:        #3d5a45;
        --mist:        #8fad96;
    }

    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: var(--cream); }
    ::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 2px; }

    /* ══ TOP NAV MOBILE ══ */
    .top-nav {
        background: rgba(10,31,18,0.97);
        padding: 0 16px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 60px;
        position: sticky;
        top: 0;
        z-index: 999;
        border-bottom: 1px solid rgba(201,168,76,0.2);
        backdrop-filter: blur(12px);
        box-shadow: 0 2px 16px rgba(0,0,0,0.3);
        max-width: 480px;
        margin: 0 auto;
        width: 100%;
    }
    .nav-brand { display:flex; align-items:center; gap:10px; }
    .nav-brand-logo {
        width: 36px; height: 36px; border-radius: 50%;
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        display: flex; align-items: center; justify-content: center;
        font-size: 1rem; flex-shrink: 0;
        box-shadow: 0 2px 10px rgba(201,168,76,0.4);
    }
    .nav-name {
        font-family: 'Cinzel', serif; color: var(--gold);
        font-size: 1rem; font-weight: 700; letter-spacing: 1.5px; line-height: 1.1;
    }
    .nav-sub {
        color: rgba(255,255,255,0.38); font-size: 0.5rem;
        letter-spacing: 2px; text-transform: uppercase; font-weight: 300; margin-top: 2px;
    }
    .nav-wa-btn {
        background: rgba(37,211,102,0.15); border: 1px solid rgba(37,211,102,0.35);
        color: #25d366; padding: 7px 12px; border-radius: 50px;
        font-size: 0.7rem; font-weight: 600; text-decoration: none;
        display: inline-flex; align-items: center; gap: 4px;
    }

    /* ══ BOTTOM NAV — REMOVED ══ */
    .bottom-nav { display: none !important; }

    /* ══ HERO MOBILE ══ */
    .hero {
        background: linear-gradient(170deg, var(--forest) 0%, #0f2416 40%, #1a3d27 100%);
        padding: 40px 20px 36px;
        position: relative; overflow: hidden;
    }
    .hero::before {
        content: ''; position: absolute; top: -80px; right: -60px;
        width: 300px; height: 300px; border-radius: 50%;
        background: radial-gradient(circle, rgba(201,168,76,0.12) 0%, transparent 65%);
        animation: pulse-glow 9s ease-in-out infinite;
    }
    .hero-grid-lines {
        position: absolute; inset: 0;
        background-image:
            linear-gradient(rgba(201,168,76,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(201,168,76,0.04) 1px, transparent 1px);
        background-size: 40px 40px;
    }
    @keyframes pulse-glow {
        0%,100% { opacity:0.6; transform:scale(1); }
        50% { opacity:1; transform:scale(1.12); }
    }
    .hero-eyebrow {
        font-family: 'Cinzel', serif; font-size: 0.55rem;
        letter-spacing: 4px; color: var(--gold); text-transform: uppercase;
        margin-bottom: 14px; display: inline-flex; align-items: center; gap: 8px; opacity: 0.9;
    }
    .hero-eyebrow::before, .hero-eyebrow::after {
        content: ''; width: 20px; height: 1px;
        background: linear-gradient(90deg, transparent, var(--gold)); opacity: 0.6;
    }
    .hero-eyebrow::after { background: linear-gradient(90deg, var(--gold), transparent); }
    .hero-h1 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.6rem; font-weight: 300; color: #faf7f0;
        line-height: 1.1; margin-bottom: 16px; letter-spacing: -0.5px;
    }
    .hero-h1 em { color: var(--gold-light); font-style: italic; }
    .hero-para {
        color: rgba(250,247,240,0.75); font-size: 0.9rem;
        line-height: 1.8; margin-bottom: 24px; font-weight: 300;
    }

    /* ══ BADGE GRID ══ */
    .badge-grid {
        display: grid; grid-template-columns: repeat(3, 1fr);
        gap: 8px; margin-bottom: 28px;
    }
    .stat-badge {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(201,168,76,0.3);
        border-radius: 8px; padding: 10px 6px; text-align: center;
        backdrop-filter: blur(8px);
    }
    .stat-badge .sb-val {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem; font-weight: 700; color: #000000;
        line-height: 1; display: block;
    }
    .stat-badge .sb-lbl {
        font-size: 0.52rem; color: #000000;
        letter-spacing: 1.5px; text-transform: uppercase; display: block; margin-top: 3px;
    }

    /* ══ CTA BUTTONS ══ */
    .btn-gold {
        background: linear-gradient(135deg, var(--gold) 0%, #d4b05a 50%, var(--gold-light) 100%);
        color: var(--forest); padding: 14px 20px; border-radius: 6px;
        font-weight: 700; font-size: 0.72rem; letter-spacing: 2px;
        text-transform: uppercase; border: none; cursor: pointer;
        text-decoration: none; display: inline-flex; align-items: center;
        gap: 6px; box-shadow: 0 6px 20px rgba(201,168,76,0.45);
        font-family: 'Cinzel', serif; width: 100%; justify-content: center;
    }
    .btn-ghost {
        background: transparent; color: rgba(250,247,240,0.8);
        padding: 13px 20px; border-radius: 6px;
        font-weight: 500; font-size: 0.72rem; letter-spacing: 2px;
        text-transform: uppercase; border: 1px solid rgba(250,247,240,0.25);
        cursor: pointer; text-decoration: none; display: inline-flex;
        align-items: center; gap: 6px; width: 100%; justify-content: center;
        font-family: 'Cinzel', serif;
    }
    .btn-green {
        background: linear-gradient(135deg, var(--mid), var(--deep));
        color: #fff; padding: 13px 20px; border-radius: 6px;
        font-weight: 600; font-size: 0.72rem; letter-spacing: 1.5px;
        text-transform: uppercase; border: none; cursor: pointer;
        text-decoration: none; display: inline-flex; align-items: center;
        gap: 6px; width: 100%; justify-content: center;
        box-shadow: 0 4px 14px rgba(45,106,79,0.4);
    }
    .btn-wa {
        background: linear-gradient(135deg, #25d366, #1ebe5e);
        color: #fff; padding: 14px 20px; border-radius: 6px;
        font-weight: 600; font-size: 0.72rem; letter-spacing: 1.5px;
        text-transform: uppercase; border: none; cursor: pointer;
        text-decoration: none; display: inline-flex; align-items: center;
        gap: 6px; width: 100%; justify-content: center;
        box-shadow: 0 4px 14px rgba(37,211,102,0.4);
    }
    .btn-call {
        background: linear-gradient(135deg, #1565c0, #0d47a1);
        color: #fff; padding: 14px 20px; border-radius: 6px;
        font-weight: 600; font-size: 0.72rem; letter-spacing: 1.5px;
        text-transform: uppercase; border: none; cursor: pointer;
        text-decoration: none; display: inline-flex; align-items: center;
        gap: 6px; width: 100%; justify-content: center;
        box-shadow: 0 4px 12px rgba(21,101,192,0.4);
    }
    .btn-brochure {
        background: rgba(201,168,76,0.12); color: var(--gold-light);
        padding: 13px 20px; border-radius: 6px;
        font-weight: 600; font-size: 0.72rem; letter-spacing: 1.5px;
        text-transform: uppercase; border: 1px solid rgba(201,168,76,0.45);
        cursor: pointer; text-decoration: none; display: inline-flex;
        align-items: center; gap: 6px; width: 100%; justify-content: center;
        font-family: 'Cinzel', serif;
        transition: all 0.2s ease;
    }
    .btn-brochure:hover {
        background: rgba(201,168,76,0.2);
        border-color: rgba(201,168,76,0.7);
    }
    .cta-stack { display: flex; flex-direction: column; gap: 10px; }

    /* ══ SECTIONS ══ */
    .sec { padding: 36px 20px; }
    .sec-cream { background: var(--cream); }
    .sec-white { background: var(--white); }
    .sec-dark  { background: var(--forest); }
    .sec-sand  { background: var(--sand); }

    .eyebrow {
        font-family: 'Cinzel', serif; font-size: 0.58rem;
        letter-spacing: 4px; text-transform: uppercase; color: var(--gold);
        margin-bottom: 10px; display: flex; align-items: center; gap: 10px;
    }
    .eyebrow::before { content:''; width:18px; height:1px; background:var(--gold); opacity:0.6; }
    .eyebrow-center { justify-content: center; }
    .sec-h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem; font-weight: 300; color: var(--ink);
        line-height: 1.15; margin-bottom: 10px;
    }
    .sec-h2 em { font-style: italic; color: var(--mid); }
    .sec-h2-white {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem; font-weight: 300; color: #fff; line-height: 1.15; margin-bottom: 10px;
    }
    .sec-h2-white em { color: var(--gold-light); font-style: italic; }
    .rule { width: 40px; height: 2px; background: linear-gradient(90deg, var(--gold), var(--gold-light)); border-radius: 2px; margin: 12px 0 20px; }
    .rule-center { margin: 12px auto 20px; }
    .sec-lead { color: var(--moss); font-size: 0.92rem; line-height: 1.85; font-weight: 300; }

    /* ══ STATS STRIP MOBILE ══ */
    .stats-strip {
        background: linear-gradient(90deg, var(--deep), #1a3a2a, var(--deep));
        padding: 24px 16px;
        display: grid; grid-template-columns: repeat(3, 1fr);
        gap: 0; border-top: 1px solid rgba(201,168,76,0.2); border-bottom: 1px solid rgba(201,168,76,0.2);
    }
    .strip-item { text-align: center; padding: 6px 0; position: relative; }
    .strip-item:not(:last-child)::after {
        content:''; position:absolute; right:0; top:10%; height:80%;
        width:1px; background:rgba(201,168,76,0.2);
    }
    .strip-val {
        font-family: 'Cormorant Garamond', serif; font-size: 1.8rem;
        font-weight: 600; color: var(--gold-light); display: block; line-height: 1;
    }
    .strip-lbl {
        font-size: 0.52rem; color: rgba(255,255,255,0.45);
        letter-spacing: 1.5px; text-transform: uppercase; margin-top: 5px; display: block;
    }

    /* ══ FEATURE CARDS ══ */
    .feat-card {
        background: white; border-radius: 14px; padding: 24px 20px;
        box-shadow: 0 3px 16px rgba(26,58,42,0.07); text-align: center;
        margin-bottom: 14px; border: 1px solid rgba(201,168,76,0.1);
    }
    .feat-icon-wrap {
        width: 56px; height: 56px; border-radius: 50%;
        background: linear-gradient(135deg, rgba(201,168,76,0.12), rgba(201,168,76,0.05));
        border: 1px solid rgba(201,168,76,0.2);
        display: flex; align-items: center; justify-content: center;
        margin: 0 auto 14px; font-size: 1.5rem;
    }
    .feat-card h4 {
        font-family: 'Cinzel', serif; color: var(--ink);
        font-size: 0.82rem; font-weight: 600; letter-spacing: 1.5px; margin-bottom: 8px;
    }
    .feat-card p { color: var(--moss); font-size: 0.85rem; line-height: 1.75; margin: 0; font-weight: 300; }

    /* ══ AMENITY CHIPS ══ */
    .amenity-chip {
        display: flex; align-items: center; gap: 12px;
        background: var(--white); border: 1px solid rgba(201,168,76,0.15);
        border-radius: 10px; padding: 14px 16px; margin-bottom: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .ac-icon { font-size: 1.4rem; flex-shrink: 0; }
    .ac-name { color: var(--ink); font-size: 0.85rem; font-weight: 500; }

    /* ══ PROPERTY CARDS ══ */
    .prop-card {
        background: white; border-radius: 16px; overflow: hidden;
        box-shadow: 0 4px 24px rgba(0,0,0,0.08); margin-bottom: 20px;
        border: 1px solid rgba(201,168,76,0.1);
    }
    .prop-card-header {
        background: linear-gradient(160deg, var(--deep), #1f4a32);
        padding: 24px 20px 20px; position: relative; overflow: hidden;
    }
    .prop-card-header::before {
        content:''; position:absolute; top:-30px; right:-30px;
        width:120px; height:120px; border-radius:50%; background:rgba(201,168,76,0.08);
    }
    .prop-badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        color: var(--forest); font-family: 'Cinzel', serif;
        font-size: 0.55rem; font-weight: 700; letter-spacing: 2px;
        text-transform: uppercase; padding: 4px 12px; border-radius: 50px; margin-bottom: 10px;
        position: relative; z-index: 1;
    }
    .prop-card-header h3 {
        font-family: 'Cormorant Garamond', serif; color: white;
        font-size: 1.5rem; font-weight: 300; margin-bottom: 6px;
        position: relative; z-index: 1; line-height: 1.2;
    }
    .prop-card-header h3 em { font-style: italic; color: var(--gold-light); }
    .prop-price {
        font-family: 'Cormorant Garamond', serif; font-size: 1.3rem;
        font-weight: 600; color: var(--gold-light); position: relative; z-index: 1;
    }
    .prop-body { padding: 20px; }
    .prop-desc { color: var(--moss); font-size: 0.84rem; line-height: 1.75; margin-bottom: 14px; font-weight: 300; }
    .prop-specs { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
    .spec-pill {
        background: var(--cream); border: 1px solid var(--parchment);
        color: var(--ink); font-size: 0.68rem; padding: 4px 12px;
        border-radius: 50px; font-weight: 500;
    }
    .prop-features { display: flex; flex-direction: column; gap: 6px; margin-bottom: 18px; }
    .prop-feature-item { display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: var(--moss); }
    .prop-feature-item::before { content: '✓'; color: var(--gold); font-weight: 700; }

    /* ══ PILLAR CARDS ══ */
    .pillar-card {
        background: white; border-radius: 16px; padding: 32px 20px;
        box-shadow: 0 4px 20px rgba(26,58,42,0.07); text-align: center;
        margin-bottom: 14px; position: relative; overflow: hidden;
        border: 1px solid rgba(201,168,76,0.1);
    }
    .pillar-card::after {
        content:''; position:absolute; bottom:0; left:0; right:0; height:3px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light), var(--gold));
    }
    .pillar-num {
        font-family: 'Cormorant Garamond', serif; font-size: 4rem; font-weight: 700;
        color: rgba(201,168,76,0.08); position: absolute; top: -8px; right: 12px; line-height: 1;
    }
    .pillar-icon { font-size: 2.5rem; margin-bottom: 14px; display: block; }
    .pillar-card h4 {
        font-family: 'Cinzel', serif; color: var(--ink); font-size: 0.88rem;
        letter-spacing: 2.5px; margin-bottom: 12px; position: relative; z-index: 1;
    }
    .pillar-card p { color: var(--moss); font-size: 0.85rem; line-height: 1.78; font-weight: 300; }

    /* ══ LIFESTYLE ITEMS ══ */
    .lifestyle-item {
        display: flex; gap: 14px; padding: 18px 16px;
        background: white; border-radius: 12px; margin-bottom: 10px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05); border: 1px solid rgba(201,168,76,0.1);
    }
    .lifestyle-item .li-icon {
        font-size: 1.8rem; flex-shrink: 0; width: 48px; height: 48px;
        display: flex; align-items: center; justify-content: center;
        background: linear-gradient(135deg, rgba(201,168,76,0.1), rgba(201,168,76,0.05));
        border-radius: 10px; border: 1px solid rgba(201,168,76,0.15);
    }
    .lifestyle-item h4 {
        font-family: 'Cormorant Garamond', serif; color: var(--ink);
        font-size: 1rem; font-weight: 600; margin-bottom: 4px;
    }
    .lifestyle-item p { color: var(--moss); font-size: 0.83rem; margin: 0; line-height: 1.65; font-weight: 300; }

    /* ══ LOCATION ITEMS ══ */
    .loc-item {
        display: flex; gap: 14px; align-items: flex-start;
        padding: 16px; background: white; border-radius: 10px;
        margin-bottom: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.04);
        border-left: 3px solid var(--gold);
    }
    .loc-icon-wrap { font-size: 1.3rem; flex-shrink: 0; margin-top: 1px; }
    .loc-text h4 { font-family:'Cormorant Garamond',serif; color:var(--ink); font-size:0.95rem; font-weight:600; margin-bottom:2px; }
    .loc-text p { color:var(--moss); font-size:0.8rem; margin:0; line-height:1.55; font-weight:300; }

    /* ══ CONNECTIVITY CARDS ══ */
    .conn-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .conn-card {
        background: linear-gradient(135deg, rgba(201,168,76,0.08), rgba(201,168,76,0.03));
        border: 1px solid rgba(201,168,76,0.25); border-radius: 12px;
        padding: 18px 14px; text-align: center;
    }
    .conn-card .cc-icon { font-size: 1.6rem; margin-bottom: 8px; display: block; }
    .conn-card .cc-dest { font-family:'Cormorant Garamond',serif; color:var(--ink); font-size:0.95rem; font-weight:600; margin-bottom:3px; }
    .conn-card .cc-time { font-family:'Cinzel',serif; font-size:1.2rem; color:var(--gold); font-weight:600; display:block; margin:6px 0 3px; }
    .conn-card .cc-via { font-size:0.65rem; color:var(--mist); letter-spacing:1px; text-transform:uppercase; }

    /* ══ MAP BLOCK ══ */
    .map-embed-block { border-radius: 14px; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.15); border: 1px solid rgba(201,168,76,0.2); position: relative; }
    .map-embed-block iframe { display: block; border: none; }
    .map-overlay-badge {
        position: absolute; top: 12px; left: 12px;
        background: rgba(10,31,18,0.9); backdrop-filter: blur(8px);
        border: 1px solid rgba(201,168,76,0.35); border-radius: 8px;
        padding: 8px 12px; display: flex; align-items: center; gap: 8px;
    }
    .mob-dot { width:8px; height:8px; border-radius:50%; background:var(--gold); flex-shrink:0; box-shadow:0 0 8px rgba(201,168,76,0.7); }
    .mob-text { font-size:0.7rem; color:white; font-weight:500; line-height:1.4; }
    .mob-text small { color:rgba(255,255,255,0.55); font-size:0.6rem; display:block; }

    /* ══ QUOTE BLOCK ══ */
    .quote-block {
        background: linear-gradient(135deg, var(--deep), #1f4a32);
        border-radius: 16px; padding: 32px 24px;
        border: 1px solid rgba(201,168,76,0.2); margin-bottom: 20px;
    }
    .quote-text {
        font-family: 'Cormorant Garamond', serif; font-size: 1.25rem;
        font-style: italic; color: rgba(250,247,240,0.88); line-height: 1.7; font-weight: 300;
    }

    /* ══ DEVELOPER STRIP ══ */
    .developer-strip {
        background: rgba(255,255,255,0.05); border: 1px solid rgba(201,168,76,0.2);
        border-radius: 14px; padding: 24px 16px; margin-top: 28px;
        display: flex; flex-direction: column; align-items: center; gap: 16px;
    }
    .dev-icon { font-size: 2.5rem; }
    .dev-stats { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; width: 100%; }
    .dev-stat { text-align: center; }
    .ds-val { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:600; color:var(--gold-light); display:block; line-height:1; }
    .ds-lbl { font-size:0.58rem; color:rgba(255,255,255,0.45); letter-spacing:2px; text-transform:uppercase; margin-top:4px; display:block; }

    /* ══ FOOTER MOBILE ══ */
    .footer { background: var(--forest); padding: 40px 20px 24px; border-top: 1px solid rgba(201,168,76,0.15); }
    .footer-logo { font-family:'Cinzel',serif; color:var(--gold); font-size:1.2rem; font-weight:700; letter-spacing:2px; margin-bottom:4px; }
    .footer-tagline { font-family:'Cormorant Garamond',serif; color:rgba(255,255,255,0.35); font-size:0.78rem; letter-spacing:3px; font-style:italic; margin-bottom:14px; }
    .footer-divider { border:none; border-top:1px solid rgba(255,255,255,0.07); margin:24px 0 16px; }
    .footer-copy { text-align:center; color:rgba(255,255,255,0.28); font-size:0.7rem; line-height:1.8; }

    /* ══ FORMS ══ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 8px !important; border: 1px solid rgba(20,45,30,0.18) !important;
        font-family: 'DM Sans', sans-serif !important; font-size: 0.92rem !important;
        color: #142d1e !important; background: #ffffff !important;
        padding: 12px 14px !important; box-shadow: 0 1px 6px rgba(20,45,30,0.05) !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 3px rgba(201,168,76,0.15) !important; outline: none !important;
    }
    .stTextInput label, .stTextArea label, .stSelectbox label {
        color: #142d1e !important; font-family: 'DM Sans', sans-serif !important;
        font-size: 0.8rem !important; font-weight: 600 !important;
    }
    .stSelectbox > div > div {
        border-radius: 8px !important; border: 1px solid rgba(20,45,30,0.18) !important;
        background: #ffffff !important; color: #142d1e !important;
    }
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, var(--gold), var(--gold-light)) !important;
        color: var(--forest) !important; font-family: 'Cinzel', serif !important;
        font-weight: 700 !important; letter-spacing: 2px !important;
        font-size: 0.78rem !important; text-transform: uppercase !important;
        border: none !important; border-radius: 8px !important;
        padding: 14px !important; box-shadow: 0 4px 16px rgba(201,168,76,0.4) !important;
        width: 100% !important;
    }
    .stButton > button {
        border-radius: 8px !important; font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important; color: #142d1e !important;
        border: 1px solid rgba(20,45,30,0.22) !important; background: transparent !important;
        width: 100% !important;
    }

    /* ══ BROCHURE DOWNLOAD BUTTON ══ */
    [data-testid="stDownloadButton"] > button {
        background: rgba(201,168,76,0.12) !important;
        color: #e8c97e !important;
        border: 1px solid rgba(201,168,76,0.5) !important;
        border-radius: 6px !important;
        font-family: 'Cinzel', serif !important;
        font-weight: 600 !important;
        font-size: 0.72rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        padding: 14px 20px !important;
        width: 100% !important;
        transition: all 0.2s !important;
    }
    [data-testid="stDownloadButton"] > button:hover {
        background: rgba(201,168,76,0.22) !important;
        border-color: rgba(201,168,76,0.75) !important;
        color: #f5e9c5 !important;
    }

    /* ══ ADMIN ══ */
    .admin-stat-card {
        background: #fff; border-radius: 12px; padding: 18px 16px;
        border: 1px solid rgba(201,168,76,0.2); text-align: center;
        position: relative; overflow: hidden; margin-bottom: 10px;
    }
    .admin-stat-card::before {
        content:''; position:absolute; top:0; left:0; right:0; height:3px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light));
    }
    .admin-stat-card .asc-val { font-family:'Cormorant Garamond',serif; font-size:2.2rem; font-weight:700; color:#142d1e; line-height:1; display:block; }
    .admin-stat-card .asc-lbl { font-size:0.6rem; color:rgba(20,45,30,0.55); letter-spacing:2px; text-transform:uppercase; margin-top:4px; display:block; }
    .admin-preview-card { background:#fff; border-radius:12px; padding:16px 18px; border:1px solid rgba(201,168,76,0.2); margin-bottom:12px; }
    .admin-preview-card h4 { font-family:'Cinzel',serif; color:#142d1e; font-size:0.65rem; letter-spacing:2px; text-transform:uppercase; margin-bottom:10px; opacity:0.7; }
    .admin-preview-row { display:flex; justify-content:space-between; margin-bottom:6px; }
    .apr-label { font-size:0.7rem; color:rgba(20,45,30,0.5); font-weight:500; min-width:80px; }
    .apr-value { font-size:0.74rem; color:#142d1e; font-weight:500; text-align:right; flex:1; }
    .admin-section-title { font-family:'Cinzel',serif; color:#142d1e; font-size:0.65rem; letter-spacing:2.5px; text-transform:uppercase; margin:20px 0 10px; padding-bottom:8px; border-bottom:1px solid rgba(201,168,76,0.25); }
    .danger-zone { background:rgba(220,38,38,0.04); border:1px solid rgba(220,38,38,0.18); border-radius:10px; padding:16px; margin-top:8px; }

    /* ══ DATAFRAME ══ */
    [data-testid="stDataFrame"] { border-radius: 10px !important; overflow: hidden !important; }

    /* ══ HERO MINI ══ */
    .hero-mini {
        background: linear-gradient(170deg, var(--forest) 0%, #0f2416 40%, #1a3d27 100%);
        padding: 40px 20px 32px; position: relative; overflow: hidden;
    }
    .hero-mini .hero-grid-lines { position:absolute; inset:0; background-image: linear-gradient(rgba(201,168,76,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(201,168,76,0.04) 1px, transparent 1px); background-size:40px 40px; }
    .hero-mini h1 { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:300; color:#faf7f0; line-height:1.1; margin-bottom:10px; }
    .hero-mini h1 em { color:var(--gold-light); font-style:italic; }
    .hero-mini p { color:rgba(250,247,240,0.7); font-size:0.88rem; line-height:1.75; font-weight:300; margin:0; }

    /* ══ SECTION DIVIDER ══ */
    .sec-divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(201,168,76,0.2), transparent); margin: 0; }

    </style>
    """, unsafe_allow_html=True)


# ─── IMAGE HELPERS ───────────────────────────────────────────────────────────
def load_img_b64(path):
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

def get_first_img(paths, alt="", style=""):
    for p in paths:
        t = img_tag(p, alt, style)
        if t:
            return t
    return None


# ─── ENQUIRY STORAGE ─────────────────────────────────────────────────────────
ENQUIRY_FILE = "enquiries.csv"
ENQUIRY_COLUMNS = ["Full Name", "Phone Number", "Email Address", "Interested In", "Message", "Submission Date & Time"]
ADMIN_PASSWORD = "nagesh@1243"

def save_enquiry(name, phone, email, interest, message):
    new_row = {
        "Full Name": name, "Phone Number": phone, "Email Address": email,
        "Interested In": interest, "Message": message,
        "Submission Date & Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    if os.path.exists(ENQUIRY_FILE):
        df = pd.read_csv(ENQUIRY_FILE)
    else:
        df = pd.DataFrame(columns=ENQUIRY_COLUMNS)
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(ENQUIRY_FILE, index=False)

def load_enquiries():
    if os.path.exists(ENQUIRY_FILE):
        return pd.read_csv(ENQUIRY_FILE)
    return pd.DataFrame(columns=ENQUIRY_COLUMNS)


# ─── NAVIGATION ──────────────────────────────────────────────────────────────
PAGES = ["🏡 Home", "🌿 About", "🏘️ Properties", "📍 Location", "📞 Contact"]
PAGE_ICONS = ["🏡", "🌿", "🏘️", "📍", "📞"]
PAGE_LABELS = ["Home", "About", "Properties", "Location", "Contact"]

def render_navbar():
    st.markdown("""
    <div class="top-nav">
        <div class="nav-brand">
            <div class="nav-brand-logo">🌿</div>
            <div>
                <div class="nav-name">Aranya Farms</div>
                <div class="nav-sub">Silver Oaks Agro Farms</div>
            </div>
        </div>
        <a class="nav-wa-btn" href="https://wa.me/919640222237" target="_blank">💬 Chat</a>
    </div>
    """, unsafe_allow_html=True)

def render_bottom_nav():
    current = st.session_state.get("page", "🏡 Home")
    cols = st.columns(5)
    st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
    for i, (icon, label, page) in enumerate(zip(PAGE_ICONS, PAGE_LABELS, PAGES)):
        with cols[i]:
            active = "bnav-active" if current == page else ""
            if st.button(f"{icon}\n{label}", key=f"bnav_{i}", use_container_width=True):
                st.session_state.page = page
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ─── HERO MINI ───────────────────────────────────────────────────────────────
def hero_mini(eyebrow, title, subtitle):
    st.markdown(f"""
    <div class="hero-mini">
        <div class="hero-grid-lines"></div>
        <div style="position:relative;z-index:2;">
            <div class="hero-eyebrow">{eyebrow}</div>
            <h1 class="hero-h1" style="font-size:1.9rem;">{title}</h1>
            <p class="hero-para" style="font-size:0.86rem;">{subtitle}</p>
        </div>
    </div>""", unsafe_allow_html=True)

def section_header(eyebrow, title, subtitle=None, center=False, dark=False):
    align = "center" if center else "left"
    eyebrow_class = "eyebrow eyebrow-center" if center else "eyebrow"
    h2_class = "sec-h2-white" if dark else "sec-h2"
    lead_class = "sec-lead" + (" " if center else "") + ("" if not center else "")
    sub_html = f'<p class="{lead_class}" style="text-align:{align};">{subtitle}</p>' if subtitle else ""
    rule_html = '<div class="rule rule-center"></div>' if center else '<div class="rule"></div>'
    st.markdown(f"""
    <div style="text-align:{align};">
        <div class="{eyebrow_class}">{eyebrow}</div>
        <div class="{h2_class}">{title}</div>
        {rule_html}
        {sub_html}
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 1 — HOME
# ═══════════════════════════════════════════════════════════════════════════
def page_home():
    # HERO
    st.markdown("""
    <div class="hero">
        <div class="hero-grid-lines"></div>
        <div style="position:relative;z-index:2;">
            <div style="background:rgba(45,106,79,0.45);border:1px solid rgba(122,191,148,0.5);border-radius:10px;padding:12px 18px;margin-bottom:20px;display:inline-block;">
                <div style="font-family:'Cinzel',serif;font-size:0.55rem;letter-spacing:4px;color:rgba(255,255,255,0.65);text-transform:uppercase;margin-bottom:5px;">Welcome to</div>
                <div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:#7abf94;letter-spacing:1.5px;line-height:1.2;">&#127807; Silver Oak Agro Farms</div>
            </div>
            <div class="hero-eyebrow">Silver Oaks Agro Farms Presents</div>
            <h1 class="hero-h1">
                <strong style="color:#e8c97;">Luxury</strong>
                <span style="color:#f5e9c5;"> Farm Living</span><br>
                at <em>Aranya Farms</em>
            </h1>
            <p class="hero-para">A premium gated community across 55 acres of lush green land at Achampet, Toopran — where nature meets refined living.</p>
            <div class="badge-grid">
                <div class="stat-badge"><span class="sb-val" style="color:#e8c97e;">55</span><span class="sb-lbl" style="color:#f5e9c5;">Acres</span></div>
                <div class="stat-badge"><span class="sb-val" style="color:#e8c97e;">Gated</span><span class="sb-lbl" style="color:#f5e9c5;">Community</span></div>
                <div class="stat-badge"><span class="sb-val" style="color:#e8c97e;">3-BHK</span><span class="sb-lbl" style="color:#f5e9c5;">Farm Houses</span></div>
                <div class="stat-badge"><span class="sb-val" style="color:#e8c97e;">5 min</span><span class="sb-lbl" style="color:#f5e9c5;">From RRR</span></div>
                <div class="stat-badge"><span class="sb-val" style="color:#e8c97e;">30 min</span><span class="sb-lbl" style="color:#f5e9c5;">From ORR</span></div>
                <div class="stat-badge"><span class="sb-val" style="color:#e8c97e;">&#8377;49L+</span><span class="sb-lbl" style="color:#f5e9c5;">Starting</span></div>
            </div>
            <div class="cta-stack">
                <a class="btn-gold" href="tel:+919640222237">&#128197; Book Free Site Visit</a>
                <a class="btn-wa" href="https://wa.me/919640222237" target="_blank">&#128172; WhatsApp Us</a>
                <a class="btn-brochure" href="images/Aranya Farms - Brochure.pdf" download="Aranya_Farms_Brochure.pdf">&#128196; Download Brochure</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # STATS STRIP
    st.markdown("""
    <div class="stats-strip">
        <div class="strip-item"><span class="strip-val">55+</span><span class="strip-lbl">Acres</span></div>
        <div class="strip-item"><span class="strip-val">200+</span><span class="strip-lbl">Families</span></div>
        <div class="strip-item"><span class="strip-val">18+</span><span class="strip-lbl">Amenities</span></div>
    </div>
    """, unsafe_allow_html=True)

    # BROCHURE DOWNLOAD — uses Streamlit's native download_button for reliable file serving
    brochure_path = "images/Aranya Farms - Brochure.pdf"
    if os.path.exists(brochure_path):
        with open(brochure_path, "rb") as f:
            brochure_bytes = f.read()
        st.markdown('<div style="padding:16px 20px 0;">', unsafe_allow_html=True)
        st.download_button(
            label="📄  Download Brochure  —  Aranya Farms",
            data=brochure_bytes,
            file_name="Aranya_Farms_Brochure.pdf",
            mime="application/pdf",
            use_container_width=True,
            key="brochure_download_home",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # WHY ARANYA
    st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
    section_header("Why Choose Us", "The Aranya Farms <em>Difference</em>",
                   "A unique blend of luxury living and nature's serenity.")
    features = [
        ("🌿", "Pure Nature", "Lush greenery with fresh air, organic surroundings, and breathtaking sunrise views."),
        ("🏡", "Premium Homes", "Thoughtfully designed 3-BHK farm houses with modern architecture."),
        ("🛡️", "Gated Security", "24×7 security, CCTV surveillance, and managed access."),
        ("🌊", "Riverside Living", "Adjacent to the serene Haldi River — nature's own backyard."),
    ]
    for icon, title, desc in features:
        st.markdown(f"""
        <div class="feat-card">
            <div class="feat-icon-wrap">{icon}</div>
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # AMENITIES
    st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
    section_header("Amenities", "Everything You Need to <em>Live Well</em>")
    amenities = [
        ("🏊", "Swimming Pool"), ("🎾", "Sports Arena"),
        ("🌿", "Organic Farming"), ("🐄", "Goshala"),
        ("🌸", "Gazebo & Gardens"), ("🏋️", "Fitness Centre"),
        ("🍽️", "Clubhouse & Dining"), ("🛕", "Meditation Zone"),
        ("🎠", "Children's Play"), ("🌳", "Tree Plantation"),
        ("🚗", "Ample Parking"), ("💧", "24×7 Water Supply"),
    ]
    for icon, name in amenities:
        st.markdown(f'<div class="amenity-chip"><span class="ac-icon">{icon}</span><span class="ac-name">{name}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # CTA BANNER
    st.markdown("""
    <div class="sec sec-dark" style="text-align:center;">
        <div class="eyebrow eyebrow-center">Limited Plots Available</div>
        <div class="sec-h2-white" style="text-align:center;">Ready to Find Your <em>Farm Plot?</em></div>
        <div class="rule rule-center"></div>
        <p style="color:rgba(255,255,255,0.55);font-size:0.9rem;margin-bottom:24px;font-weight:300;line-height:1.8;">
            Plots starting from &#8377;49 Lakhs. Register now for exclusive pre-launch pricing.
        </p>
        <div class="cta-stack">
            <a class="btn-gold" href="tel:+919640222237">&#128197; Book Free Site Visit</a>
            <a class="btn-call" href="tel:+919640222237">&#128222; Talk to Expert</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 2 — ABOUT
# ═══════════════════════════════════════════════════════════════════════════
def page_about():
    hero_mini("Our Story", "About <em>Aranya Farms</em>", "Play · Live · Celebrate — A new way to belong to nature.")

    # VISION
    st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
    section_header("The Vision", "Where Rural Richness Meets <em>Urban Comfort</em>")
    about_img = get_first_img(
        ["images/land3.png","images/land3.jpg","images/land2.png","images/land2.jpg"],
        "Aranya Farms",
        "width:100%;border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,0.15);display:block;margin-bottom:20px;"
    )
    if about_img:
        st.markdown(about_img, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="quote-block" style="margin-bottom:20px;">
            <div class="quote-text">"Every family deserves a sanctuary where they can breathe freely, grow organically, and celebrate life amid nature's abundance."</div>
            <div style="color:var(--gold-light);font-family:'Cinzel',serif;font-size:0.6rem;letter-spacing:3px;text-transform:uppercase;margin-top:20px;padding-top:16px;border-top:1px solid rgba(201,168,76,0.2);">— Silver Oaks Agro Farms</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <p style="color:var(--moss);font-size:0.92rem;line-height:1.88;margin-bottom:14px;font-weight:300;">
        <strong style="color:var(--ink);font-weight:600;">Aranya Farms</strong> is not just a real estate project —
        it is a lifestyle reimagined. Spread across <strong style="color:var(--mid);">55 lush acres</strong> in Achampet, Toopran.
    </p>
    <p style="color:var(--moss);font-size:0.92rem;line-height:1.88;margin-bottom:14px;font-weight:300;">
        Conceived by <strong style="color:var(--ink);">Silver Oaks Agro Farms</strong>, this project is born from a simple belief:
        <em style="color:var(--mid);">every family deserves a sanctuary where they can breathe freely and celebrate life.</em>
    </p>
    <p style="color:var(--moss);font-size:0.92rem;line-height:1.88;font-weight:300;">
        Adjacent to the tranquil Haldi River and just 5 minutes from RRR — the perfect balance of accessibility and escape.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # PILLARS
    st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
    section_header("Our Philosophy", "Play · Live · <em>Celebrate</em>", center=True)
    pillars = [
        ("🎠", "01", "PLAY", "Sports arenas, swimming pool, children's zones, and nature trails — life is meant to be enjoyed at every age."),
        ("🏡", "02", "LIVE", "Thoughtfully crafted farm houses and plots designed for wholesome family living. Wake up to birdsong."),
        ("🎉", "03", "CELEBRATE", "From festive gatherings at the clubhouse to quiet birthday mornings in the gazebo — every milestone is better in nature."),
    ]
    for icon, num, title, desc in pillars:
        st.markdown(f"""
        <div class="pillar-card">
            <div class="pillar-num">{num}</div>
            <span class="pillar-icon">{icon}</span>
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # LIFESTYLE
    st.markdown('<div class="sec sec-sand">', unsafe_allow_html=True)
    section_header("Lifestyle", "Designed for Every <em>Chapter of Life</em>")
    lifestyles = [
        ("👨‍👩‍👧‍👦", "Family Lifestyle", "Spacious plots with dedicated zones for kids, elders, and togetherness."),
        ("🧘", "Wellness Retreat", "Yoga pavilion, meditation zones, organic garden walks, and fresh-air mornings."),
        ("🏡", "Weekend Homes", "Just 30 minutes from ORR — the ideal weekend getaway and investment."),
        ("🌱", "Organic Living", "Farm-to-table living. Grow your own vegetables, herbs, and fruits on your private plot."),
    ]
    for icon, title, desc in lifestyles:
        st.markdown(f"""
        <div class="lifestyle-item">
            <div class="li-icon">{icon}</div>
            <div><h4>{title}</h4><p>{desc}</p></div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # DEVELOPER
    st.markdown("""
    <div class="sec sec-dark" style="text-align:center;">
        <div class="eyebrow eyebrow-center">About the Developer</div>
        <div class="sec-h2-white" style="text-align:center;">Silver Oaks <em>Agro Farms</em></div>
        <div class="rule rule-center"></div>
        <p style="color:rgba(255,255,255,0.62);font-size:0.9rem;line-height:1.88;margin:0 0 28px;font-weight:300;">
            Silver Oaks Agro Farms, operating under <strong style="color:var(--gold-light);">Silver Oaks Realty</strong>,
            is a Hyderabad-based premium farmland developer with a decade of experience creating managed agro-communities.
        </p>
        <div class="developer-strip">
            <div class="dev-icon">🌳</div>
            <div class="dev-stats">
                <div class="dev-stat"><span class="ds-val">500+</span><span class="ds-lbl">Families Served</span></div>
                <div class="dev-stat"><span class="ds-val">10+</span><span class="ds-lbl">Years Experience</span></div>
                <div class="dev-stat"><span class="ds-val">5+</span><span class="ds-lbl">Projects Delivered</span></div>
                <div class="dev-stat"><span class="ds-val">DTCP</span><span class="ds-lbl">Approved Layouts</span></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 3 — PROPERTIES
# ═══════════════════════════════════════════════════════════════════════════
def page_properties():
    hero_mini("Properties & Plots", "Find Your <em>Perfect Space</em>",
              "Farm plots, 3-BHK homes, premium villas — each designed for a life well lived.")

    st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
    section_header("Available Properties", "Explore Our <em>Offerings</em>",
                   "All properties are within the 55-acre gated community with full access to world-class amenities.")

    properties = [
        {"badge": "Best Seller", "title": "Farm <em>Plots</em>", "price": "Starting &#8377;49 Lakhs",
         "specs": ["300 sq. yds", "605 sq. yds", "640 sq. yds", "753 sq. yds"],
         "features": ["DTCP Approved", "Clear Titles", "Gated Community", "All Amenities"],
         "desc": "Open farm plots in a fully gated, amenity-rich community. Clear titles, DTCP approved layout.", "idx": 0},
        {"badge": "Most Popular", "title": "3-BHK <em>Farm Houses</em>", "price": "Starting &#8377;65 Lakhs",
         "specs": ["685 sft BUA", "1480 sft BUA", "1500 sft BUA"],
         "features": ["3 Bedrooms", "Private Garden", "Modern Kitchen", "Ready Soon"],
         "desc": "Ready-to-move 3-BHK farm houses with contemporary architecture and private garden space.", "idx": 1},
        {"badge": "Luxury", "title": "Premium <em>Villas</em>", "price": "Starting &#8377;90 Lakhs",
         "specs": ["2250 sft BUA", "Large Plot", "Private Garden"],
         "features": ["Exclusive Layout", "Premium Finishes", "Landscaped Garden", "High Ceilings"],
         "desc": "Exclusive premium villas with expansive built-up areas and landscaped private gardens.", "idx": 2},
        {"badge": "Investment", "title": "Larger <em>Farm Lands</em>", "price": "On Request",
         "specs": ["1+ Acre", "Custom Layout", "Managed Option"],
         "features": ["Bulk Parcels", "Custom Design", "Managed Farming", "Community Access"],
         "desc": "Bulk farmland parcels for families or investor groups seeking larger green footprints.", "idx": 3},
    ]

    for prop in properties:
        specs_html = "".join(f'<span class="spec-pill">{s}</span>' for s in prop["specs"])
        feats_html = "".join(f'<div class="prop-feature-item">{f}</div>' for f in prop["features"])
        st.markdown(f"""
        <div class="prop-card">
            <div class="prop-card-header">
                <div class="prop-badge">{prop["badge"]}</div>
                <h3>{prop["title"]}</h3>
                <div class="prop-price">{prop["price"]}</div>
            </div>
            <div class="prop-body">
                <p class="prop-desc">{prop["desc"]}</p>
                <div class="prop-specs">{specs_html}</div>
                <div class="prop-features">{feats_html}</div>
            </div>
        </div>""", unsafe_allow_html=True)
        if st.button(f"📩 Enquire About This Property", key=f"prop_btn_{prop['idx']}", use_container_width=True):
            st.session_state.page = "📞 Contact"
            st.rerun()
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # PRICING TABLE
    st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
    section_header("Pricing", "Complete Pricing at a <em>Glance</em>")
    df = pd.DataFrame({
        "Type": ["Farm Plot – Compact", "Farm Plot – Standard", "Farm Plot – Large",
                 "Farm Plot – Premium", "Farm House – 3 BHK (A)", "Farm House – 3 BHK (B)",
                 "Farm House – 3 BHK (C)", "Premium Villa"],
        "Plot Size": ["300 sq. yds", "605 sq. yds", "640 sq. yds", "753 sq. yds",
                      "Included", "Included", "Included", "Large"],
        "Starting Price": ["₹49 Lakhs", "₹55 Lakhs", "₹60 Lakhs", "₹68 Lakhs",
                           "₹65 Lakhs", "₹72 Lakhs", "₹78 Lakhs", "₹90 Lakhs"],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div class="sec sec-dark" style="text-align:center;">
        <div class="eyebrow eyebrow-center">Exclusive Offer</div>
        <div class="sec-h2-white" style="text-align:center;">Get Pre-Launch <em>Pricing</em></div>
        <div class="rule rule-center"></div>
        <p style="color:rgba(255,255,255,0.55);font-size:0.9rem;line-height:1.8;margin-bottom:24px;font-weight:300;">
            Register your interest today for special pre-launch rates and a complimentary site visit.
        </p>
        <a class="btn-wa" href="https://wa.me/919640222237" target="_blank">&#128172; WhatsApp Us</a>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 4 — LOCATION
# ═══════════════════════════════════════════════════════════════════════════
def page_location():
    hero_mini("Find Us", "Location &amp; <em>Connectivity</em>",
              "Strategically placed in Achampet, Toopran — nature close, city even closer.")

    # LOCATION HIGHLIGHTS
    st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
    section_header("How to Reach", "Location <em>Highlights</em>")
    highlights = [
        ("📍", "Exact Location", "Achampet Village, Toopran Mandal, Medchal-Malkajgiri District, Telangana"),
        ("🛣️", "Near RRR", "Only 5 minutes from the Regional Ring Road (RRR)"),
        ("🔄", "Near ORR", "Approx. 30 minutes from the Outer Ring Road (ORR)"),
        ("🏙️", "NH-44 Access", "Adjacent to the Hyderabad–Medchal Highway (NH-44)"),
        ("🌊", "Riverside", "Adjacent to the scenic Haldi River — beautiful water views year-round"),
        ("✈️", "Airport", "Approx. 40–50 minutes from Rajiv Gandhi International Airport"),
    ]
    for icon, title, desc in highlights:
        st.markdown(f"""
        <div class="loc-item">
            <div class="loc-icon-wrap">{icon}</div>
            <div class="loc-text"><h4>{title}</h4><p>{desc}</p></div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # MAP
    st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
    section_header("Map", "View on <em>Map</em>")
    st.markdown("""
    <div class="map-embed-block">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3808.7!2d78.1!3d17.7!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb9c0000000001%3A0x1!2sAchampet%2C%20Toopran%2C%20Telangana!5e0!3m2!1sen!2sin!4v1700000000000"
            width="100%" height="280" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        <div class="map-overlay-badge">
            <div class="mob-dot"></div>
            <div class="mob-text">Aranya Farms<small>Achampet · Toopran</small></div>
        </div>
    </div>
    <div style="margin-top:14px;">
        <a class="btn-green" href="https://maps.google.com/?q=Achampet+Toopran+Telangana" target="_blank">&#128506; Open in Google Maps</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # CONNECTIVITY
    st.markdown('<div class="sec sec-sand">', unsafe_allow_html=True)
    section_header("Connectivity", "Key Distances from <em>Aranya Farms</em>", center=True)
    connections = [
        ("🛣️", "RRR", "~5 min", "State Highway"),
        ("🔄", "ORR", "~30 min", "NH-44 + RRR"),
        ("🏙️", "Kompally", "~28 min", "NH-44"),
        ("🏘️", "Medchal", "~18 min", "NH-44"),
        ("🌆", "Hyderabad", "~40 min", "NH-44 + ORR"),
        ("✈️", "Airport", "~50 min", "ORR"),
    ]
    conn_html = '<div class="conn-grid">'
    for icon, dest, time, via in connections:
        conn_html += f'<div class="conn-card"><span class="cc-icon">{icon}</span><div class="cc-dest">{dest}</div><span class="cc-time">{time}</span><div class="cc-via">{via}</div></div>'
    conn_html += '</div>'
    st.markdown(conn_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # DISTANCE TABLE
    st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
    section_header("Distances", "Full Distance <em>Reference</em>")
    df = pd.DataFrame({
        "Destination": ["RRR", "ORR", "Kompally", "Medchal", "Hyderabad City", "Airport RGIA", "Masaipet", "Haldi River"],
        "Distance": ["~5 km", "~30 km", "~28 km", "~18 km", "~38 km", "~48 km", "~3 km", "Adjacent"],
        "Time": ["~5 mins", "~30 mins", "~28 mins", "~18 mins", "~40 mins", "~50 mins", "~5 mins", "Walking"],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 5 — CONTACT
# ═══════════════════════════════════════════════════════════════════════════
def page_contact():
    hero_mini("Get in Touch", "Let's Find Your <em>Dream Plot</em>",
              "Our expert team is ready to guide you. Book a visit or simply send us an enquiry.")

    st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
    section_header("Send Enquiry", "Let's <em>Talk</em>")

    with st.form("enquiry_form", clear_on_submit=True):
        name = st.text_input("Full Name *", placeholder="Your full name")
        phone = st.text_input("Phone Number *", placeholder="+91 XXXXX XXXXX")
        email = st.text_input("Email Address", placeholder="your@email.com")
        interest = st.selectbox("Interested In *", [
            "Select an option…", "Farm Plot", "3-BHK Farm House",
            "Premium Villa", "Larger Farm Land", "Book Site Visit",
            "Brochure Request", "General Enquiry",
        ])
        message = st.text_area("Message", placeholder="Tell us more about what you're looking for…", height=100)
        submitted = st.form_submit_button("📩 Submit Enquiry", use_container_width=True)
        if submitted:
            if not name or not phone or interest == "Select an option…":
                st.error("Please fill in Name, Phone, and select your Interest.")
            else:
                save_enquiry(name, phone, email, interest, message)
                st.success("Thank you! Your enquiry has been submitted successfully.")
                st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

    # QUICK CONTACT
    st.markdown("""
    <div class="sec sec-dark">
        <div class="eyebrow">Quick Contact</div>
        <div class="sec-h2-white">Reach Us <em>Directly</em></div>
        <div class="rule"></div>
        <div class="cta-stack" style="margin-bottom:20px;">
            <a class="btn-wa" href="https://wa.me/919640222237" target="_blank">&#128172; WhatsApp: +91 96402 22237</a>
            <a class="btn-call" href="tel:+919640222237">&#128222; Call: +91 96402 22237</a>
        </div>
        <p style="color:rgba(255,255,255,0.45);font-size:0.8rem;line-height:1.8;">
            &#128344; Mon–Sat: 9AM – 7PM &nbsp;|&nbsp; Sunday: 10AM – 5PM<br>
            &#128140; info@silveroaksrealty.com
        </p>
    </div>
    """, unsafe_allow_html=True)

    render_admin_section()


# ═══════════════════════════════════════════════════════════════════════════
#  ADMIN SECTION
# ═══════════════════════════════════════════════════════════════════════════
def render_admin_section():
    with st.container():
        st.markdown('<div style="padding:32px 20px 48px;background:var(--sand);">', unsafe_allow_html=True)
        st.markdown("""
        <div style="margin-bottom:20px;">
            <div class="eyebrow">Admin Panel</div>
            <div class="sec-h2">Enquiry <em>Dashboard</em></div>
            <div class="rule"></div>
            <p class="sec-lead">Password-protected dashboard for managing customer enquiries.</p>
        </div>""", unsafe_allow_html=True)

        admin_pass = st.text_input("Admin Password", type="password", key="admin_password_input",
                                   placeholder="Enter password to access dashboard…")
        if not admin_pass:
            st.markdown("</div>", unsafe_allow_html=True)
            return
        if admin_pass != ADMIN_PASSWORD:
            st.error("⛔ Incorrect password. Please try again.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        df = load_enquiries()
        total = len(df)

        # STAT CARDS — 2x2 on mobile
        c1, c2 = st.columns(2, gap="small")
        today_str = datetime.now().strftime("%Y-%m-%d")
        today_count = df[df["Submission Date & Time"].str.startswith(today_str)].shape[0] if total > 0 else 0
        top_interest_short = df["Interested In"].value_counts().idxmax()[:14] + "…" if total > 0 else "—"
        this_week = 0
        if total > 0:
            try:
                df["_dt"] = pd.to_datetime(df["Submission Date & Time"], errors="coerce")
                cutoff = pd.Timestamp.now() - pd.Timedelta(days=7)
                this_week = df[df["_dt"] >= cutoff].shape[0]
                df.drop(columns=["_dt"], inplace=True)
            except Exception:
                pass

        with c1:
            st.markdown(f'<div class="admin-stat-card"><span class="asc-val">{total}</span><span class="asc-lbl">Total Enquiries</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="admin-stat-card"><span class="asc-val" style="font-size:1.1rem;padding-top:6px;">{top_interest_short}</span><span class="asc-lbl">Top Interest</span></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="admin-stat-card"><span class="asc-val">{today_count}</span><span class="asc-lbl">Today</span></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="admin-stat-card"><span class="asc-val">{this_week}</span><span class="asc-lbl">This Week</span></div>', unsafe_allow_html=True)

        if df.empty:
            st.info("📭 No enquiries yet.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        # LATEST
        latest = df.iloc[-1]
        st.markdown(f"""
        <div class="admin-preview-card">
            <h4>🕐 Latest Enquiry</h4>
            <div class="admin-preview-row"><span class="apr-label">Name</span><span class="apr-value">{latest.get("Full Name","—")}</span></div>
            <div class="admin-preview-row"><span class="apr-label">Phone</span><span class="apr-value">{latest.get("Phone Number","—")}</span></div>
            <div class="admin-preview-row"><span class="apr-label">Interest</span><span class="apr-value">{latest.get("Interested In","—")}</span></div>
            <div class="admin-preview-row"><span class="apr-label">Date</span><span class="apr-value">{latest.get("Submission Date & Time","—")}</span></div>
        </div>""", unsafe_allow_html=True)

        # SEARCH
        st.markdown('<div class="admin-section-title">🔍 Search</div>', unsafe_allow_html=True)
        search_query = st.text_input("Search enquiries", placeholder="Name, phone, email…", key="admin_search", label_visibility="collapsed")
        filter_interest = st.selectbox("Filter by interest", ["All"] + sorted(df["Interested In"].dropna().unique().tolist()), key="admin_filter_interest", label_visibility="collapsed")

        display_df = df.copy()
        if search_query:
            mask = display_df.apply(lambda row: search_query.lower() in " ".join(row.astype(str).values).lower(), axis=1)
            display_df = display_df[mask]
        if filter_interest != "All":
            display_df = display_df[display_df["Interested In"] == filter_interest]

        st.markdown('<div class="admin-section-title">📋 All Enquiries</div>', unsafe_allow_html=True)
        st.caption(f"Showing {len(display_df)} of {total} enquiries")
        st.dataframe(display_df.reset_index(drop=True), use_container_width=True, hide_index=True)

        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download as CSV", data=csv_data,
                           file_name=f"aranya_enquiries_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                           mime="text/csv", use_container_width=True)

        # DELETE
        st.markdown('<div class="admin-section-title">🗑️ Delete Enquiry</div>', unsafe_allow_html=True)
        if total > 0:
            enquiry_options = {f"#{i+1} — {row['Full Name']} | {row['Phone Number']}": i for i, row in df.iterrows()}
            selected_label = st.selectbox("Select to delete", list(enquiry_options.keys()), key="admin_delete_select", label_visibility="collapsed")
            selected_idx = enquiry_options[selected_label]
            if st.button("🗑️ Delete Selected", key="admin_delete_one", use_container_width=True, type="secondary"):
                sel_row = df.iloc[selected_idx]
                df_updated = df.drop(index=selected_idx).reset_index(drop=True)
                df_updated.to_csv(ENQUIRY_FILE, index=False)
                st.success(f"✅ Deleted enquiry from {sel_row.get('Full Name','—')}.")
                st.rerun()

        st.markdown('<div class="admin-section-title">⚠️ Danger Zone</div>', unsafe_allow_html=True)
        st.markdown('<div class="danger-zone">', unsafe_allow_html=True)
        st.markdown('<strong style="color:#dc2626;font-size:0.88rem;">Delete All Enquiries</strong><p style="color:rgba(20,45,30,0.6);font-size:0.8rem;margin:4px 0 0;">This will permanently erase all records. Cannot be undone.</p>', unsafe_allow_html=True)
        confirm_delete_all = st.checkbox("I understand — delete all enquiries permanently.", key="admin_confirm_delete_all")
        if confirm_delete_all:
            if st.button("🔥 Delete ALL Enquiries", key="admin_delete_all", use_container_width=True, type="secondary"):
                pd.DataFrame(columns=ENQUIRY_COLUMNS).to_csv(ENQUIRY_FILE, index=False)
                st.success("✅ All enquiries deleted.")
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════════════════
def render_footer():
    st.markdown("""
    <div class="footer">
        <div style="text-align:center;margin-bottom:20px;">
            <div class="footer-logo">🌿 Aranya Farms</div>
            <div class="footer-tagline">Play · Live · Celebrate</div>
            <p style="color:rgba(255,255,255,0.38);font-size:0.82rem;line-height:1.85;font-weight:300;max-width:320px;margin:0 auto 16px;">
                A premium gated farmland community by Silver Oaks Agro Farms, set across 55 acres at Achampet, Toopran, Telangana.
            </p>
            <div style="display:flex;gap:10px;justify-content:center;">
                <a href="https://wa.me/919640222237" target="_blank" style="width:36px;height:36px;border-radius:50%;background:rgba(37,211,102,0.15);border:1px solid rgba(37,211,102,0.3);display:flex;align-items:center;justify-content:center;font-size:1rem;text-decoration:none;">💬</a>
                <a href="tel:+919640222237" style="width:36px;height:36px;border-radius:50%;background:rgba(201,168,76,0.1);border:1px solid rgba(201,168,76,0.25);display:flex;align-items:center;justify-content:center;font-size:1rem;text-decoration:none;">📞</a>
                <a href="mailto:info@silveroaksrealty.com" style="width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;justify-content:center;font-size:1rem;text-decoration:none;">📧</a>
            </div>
        </div>
        <hr class="footer-divider">
        <div class="footer-copy">
            © 2024 Aranya Farms by Silver Oaks Agro Farms · Hyderabad, Telangana<br>
            <span style="font-size:0.65rem;opacity:0.55;">All prices are indicative and subject to change.</span>
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


import streamlit as st
import os
import base64
import pandas as pd
from datetime import datetime

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
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=Cinzel:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        scroll-behavior: smooth;
    }
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    #MainMenu, footer, header { visibility: hidden; }
    .stApp { background: #faf7f0; }

    :root {
        --forest:       #0a1f12;
        --deep:         #142d1e;
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
        --moss:         #1e3526;
        --mist:         #8fad96;
        --shadow-dark:  rgba(10, 31, 18, 0.18);
    }

    /* ══ SCROLLBAR ══ */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--cream); }
    ::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 3px; }

    /* ══ TOP NAV ══ */
    .top-nav {
        background: rgba(10, 31, 18, 0.97);
        padding: 0 56px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 76px;
        position: sticky;
        top: 0;
        z-index: 999;
        border-bottom: 1px solid rgba(201,168,76,0.2);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 4px 32px rgba(0,0,0,0.3);
    }
    .nav-brand {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .nav-brand-logo {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        flex-shrink: 0;
        box-shadow: 0 4px 16px rgba(201,168,76,0.4);
    }
    .nav-name {
        font-family: 'Cinzel', serif;
        color: var(--gold);
        font-size: 1.25rem;
        font-weight: 700;
        letter-spacing: 2.5px;
        line-height: 1.1;
    }
    .nav-sub {
        color: rgba(255,255,255,0.38);
        font-size: 0.58rem;
        letter-spacing: 3.5px;
        text-transform: uppercase;
        font-weight: 300;
        margin-top: 2px;
    }
    .nav-right {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .nav-wa-btn {
        background: rgba(37,211,102,0.15);
        border: 1px solid rgba(37,211,102,0.35);
        color: #25d366;
        padding: 8px 18px;
        border-radius: 50px;
        font-size: 0.73rem;
        font-weight: 600;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        transition: all 0.25s;
    }
    .nav-wa-btn:hover { background: rgba(37,211,102,0.25); }
    .nav-call-btn {
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        color: var(--forest);
        padding: 9px 24px;
        border-radius: 50px;
        font-size: 0.73rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        box-shadow: 0 4px 16px rgba(201,168,76,0.45);
        transition: all 0.25s;
    }
    .nav-call-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 24px rgba(201,168,76,0.55); }

    /* ══ PAGE NAV BAR ══ */
    .page-nav-outer {
        background: var(--white);
        border-bottom: 1px solid rgba(201,168,76,0.2);
        padding: 0 48px;
        box-shadow: 0 2px 16px rgba(0,0,0,0.05);
        position: sticky;
        top: 76px;
        z-index: 998;
    }
    div[data-testid="stHorizontalBlock"] .stButton > button {
        background: transparent !important;
        color: var(--moss) !important;
        border: none !important;
        border-radius: 0 !important;
        font-family: 'Cinzel', serif !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        padding: 18px 22px !important;
        box-shadow: none !important;
        height: 56px !important;
        transition: all 0.2s !important;
        border-bottom: 2px solid transparent !important;
    }
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {
        color: var(--gold) !important;
        background: transparent !important;
        border-bottom: 2px solid var(--gold) !important;
    }

    /* ══ HERO ══ */
    .hero {
       background: var(--cream);
        border-bottom: 1px solid rgba(201,168,76,0.15);
        padding: 120px 80px 110px;
        position: relative;
        overflow: hidden;
        min-height: 640px;
        display: flex;
        align-items: center;
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -180px; right: -120px;
        width: 750px; height: 750px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(201,168,76,0.13) 0%, transparent 65%);
        animation: pulse-glow 9s ease-in-out infinite;
    }
    .hero::after {
        content: '';
        position: absolute;
        bottom: -200px; left: -80px;
        width: 600px; height: 600px;
        border-radius: 50%;
       background: radial-gradient(circle, rgba(45,106,79,0.04) 0%, transparent 65%);
        animation: pulse-glow2 12s ease-in-out infinite;
    }
    .hero-grid-lines {
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(rgba(201,168,76,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(201,168,76,0.04) 1px, transparent 1px);
        background-size: 60px 60px;
    }
    @keyframes pulse-glow {
        0%,100% { opacity: 0.6; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.12); }
    }
    @keyframes pulse-glow2 {
        0%,100% { opacity: 0.5; transform: scale(1) rotate(0deg); }
        50% { opacity: 0.9; transform: scale(1.08) rotate(-5deg); }
    }
    .hero-eyebrow {
        font-family: 'Cinzel', serif;
        font-size: 0.65rem;
        letter-spacing: 6px;
        color: var(--gold);
        text-transform: uppercase;
        margin-bottom: 22px;
        display: inline-flex;
        align-items: center;
        gap: 14px;
        opacity: 0.9;
    }
    .hero-eyebrow::before, .hero-eyebrow::after {
        content: '';
        width: 36px;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--gold));
        opacity: 0.6;
    }
    .hero-eyebrow::after { background: linear-gradient(90deg, var(--gold), transparent); }
    .hero-h1 {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.8rem, 5.5vw, 5.5rem);
        font-weight: 300;
        color: var(--ink);
        line-height: 1.08;
        margin-bottom: 26px;
        letter-spacing: -0.5px;
    }
    .hero-h1 em {
        color: var(--gold);
        font-style: italic;
    }
    .hero-h1 strong {
        font-weight: 600;
        color: var(--ink);
    }
    .hero-para {
        color: var(--moss);
        font-size: 1.05rem;
        line-height: 1.85;
        max-width: 500px;
        margin-bottom: 40px;
        font-weight: 300;
    }

    /* ── BADGE ROW ── */
    .badge-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 44px;
    }
    .stat-badge {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(201,168,76,0.3);
        border-radius: 8px;
        padding: 10px 18px;
        text-align: center;
        backdrop-filter: blur(8px);
        transition: all 0.25s;
    }
    .stat-badge:hover {
        background: rgba(201,168,76,0.12);
        border-color: rgba(201,168,76,0.6);
        transform: translateY(-2px);
    }
    .stat-badge .sb-val {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        font-weight: 700;
        color: var(--gold);
        line-height: 1;
        display: block;
    }
    .stat-badge .sb-lbl {
        font-size: 0.6rem;
        color: var(--moss);
        letter-spacing: 2px;
        text-transform: uppercase;
        display: block;
        margin-top: 4px;
    }

    /* ── CTA BUTTONS ── */
    .btn-gold {
        background: linear-gradient(135deg, var(--gold) 0%, #d4b05a 50%, var(--gold-light) 100%);
        color:var(--forest) !important;
        padding: 15px 36px;
        border-radius: 4px;
        font-weight: 700;
        font-size: 0.78rem;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none 
        !important;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 8px 28px rgba(201,168,76,0.45);
        transition: all 0.3s;
        font-family: 'Cinzel', serif;
    }
    .btn-gold:hover {
        transform: translateY(-3px);
        box-shadow: 0 14px 40px rgba(201,168,76,0.6);
        color: var(--forest) !important;
    }
    .btn-ghost {
        background: transparent;
        color: #142d1e !important;
        padding: 14px 34px;
        border-radius: 4px;
        font-weight: 500;
        font-size: 0.78rem;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        border: 1px solid rgba(20,45,30,0.25) !important;
        cursor: pointer;
        text-decoration: none
        !important;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transition: all 0.3s;
        font-family: 'Cinzel', serif;
    }
    .btn-ghost:hover {
         border-color: var(--gold) !important;
        color: var(--gold) !important;
    }
    .btn-green {
        background: linear-gradient(135deg, var(--mid), var(--deep));
        color: #fff;
        padding: 13px 30px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.78rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 16px rgba(45,106,79,0.4);
        transition: all 0.25s;
    }
    .btn-green:hover { transform: translateY(-2px); }
    .btn-wa {
        background: linear-gradient(135deg, #25d366, #1ebe5e);
        color: #fff;
        padding: 13px 28px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.78rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 18px rgba(37,211,102,0.4);
        transition: all 0.25s;
    }
    .btn-wa:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(37,211,102,0.5); }
    .btn-call {
        background: linear-gradient(135deg, #1565c0, #0d47a1);
        color: #fff;
        padding: 13px 28px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.78rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border: none;
        cursor: pointer;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 14px rgba(21,101,192,0.4);
        transition: all 0.25s;
    }
    .btn-call:hover { transform: translateY(-2px); }
    .cta-row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }

    /* ══ SECTIONS ══ */
    .sec { padding: 96px 80px; }
    .sec-sm { padding: 64px 80px; }
    .sec-cream { background: var(--cream); }
    .sec-white { background: var(--white); }
    .sec-dark  { background: var(--forest); }
    .sec-deep  { background: var(--deep); }
    .sec-sand  { background: var(--sand); }

    .eyebrow {
        font-family: 'Cinzel', serif;
        font-size: 0.62rem;
        letter-spacing: 5px;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .eyebrow-center { justify-content: center; }
    .eyebrow::before {
        content: '';
        width: 24px;
        height: 1px;
        background: var(--gold);
        opacity: 0.6;
    }
    .sec-h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.2rem, 3.5vw, 3.2rem);
        font-weight: 300;
        color: var(--ink);
        line-height: 1.12;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }
    .sec-h2 em { font-style: italic; color: var(--mid); }
    .sec-h2-white {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.2rem, 3.5vw, 3.2rem);
        font-weight: 300;
        color: #fff;
        line-height: 1.12;
        margin-bottom: 12px;
    }
    .sec-h2-white em { color: var(--gold-light); font-style: italic; }
    .rule {
        width: 52px;
        height: 2px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light));
        border-radius: 2px;
        margin: 18px 0 32px;
    }
    .rule-center { margin: 18px auto 32px; }
    .sec-lead {
        color: var(--moss);
        font-size: 1.02rem;
        line-height: 1.9;
        max-width: 640px;
        font-weight: 300;
    }
    .sec-lead-center { text-align: center; margin: 0 auto; }

    /* ══ STATS STRIP ══ */
    .stats-strip {
        background: linear-gradient(90deg, var(--deep) 0%, #1a3a2a 50%, var(--deep) 100%);
        padding: 40px 80px;
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0;
        border-top: 1px solid rgba(201,168,76,0.2);
        border-bottom: 1px solid rgba(201,168,76,0.2);
    }
    .strip-item {
        text-align: center;
        padding: 8px 0;
        position: relative;
    }
    .strip-item:not(:last-child)::after {
        content: '';
        position: absolute;
        right: 0; top: 10%; height: 80%;
        width: 1px;
        background: rgba(201,168,76,0.2);
    }
    .strip-val {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.6rem;
        font-weight: 600;
        color: var(--gold-light);
        display: block;
        line-height: 1;
    }
    .strip-lbl {
        font-size: 0.63rem;
        color: rgba(255,255,255,0.45);
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-top: 8px;
        display: block;
    }

    /* ══ FEATURE CARDS ══ */
    .feat-card {
        background: white;
        border-radius: 16px;
        padding: 40px 30px;
        box-shadow: 0 4px 24px rgba(26,58,42,0.07);
        text-align: center;
        height: 100%;
        transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(201,168,76,0.1);
    }
    .feat-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light), var(--gold));
        transform: scaleX(0);
        transition: transform 0.35s ease;
    }
    .feat-card:hover { transform: translateY(-8px); box-shadow: 0 20px 52px rgba(26,58,42,0.15); }
    .feat-card:hover::before { transform: scaleX(1); }
    .feat-icon-wrap {
        width: 72px;
        height: 72px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(201,168,76,0.12), rgba(201,168,76,0.05));
        border: 1px solid rgba(201,168,76,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 22px;
        font-size: 1.8rem;
        transition: all 0.35s;
    }
    .feat-card:hover .feat-icon-wrap {
        background: linear-gradient(135deg, rgba(201,168,76,0.2), rgba(201,168,76,0.1));
        border-color: rgba(201,168,76,0.4);
        transform: scale(1.08);
    }
    .feat-card h4 {
        font-family: 'Cinzel', serif;
        color: var(--ink);
        font-size: 0.95rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        margin-bottom: 12px;
    }
    .feat-card p { color: var(--moss); font-size: 0.9rem; line-height: 1.8; margin: 0; font-weight: 300; }

    /* ══ AMENITY CHIPS ══ */
    .amenity-chip {
        display: flex;
        align-items: center;
        gap: 14px;
        background: var(--white);
        border: 1px solid rgba(201,168,76,0.15);
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 10px;
        transition: all 0.25s;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    .amenity-chip:hover {
        background: var(--cream);
        border-color: var(--gold);
        box-shadow: 0 6px 20px rgba(201,168,76,0.18);
        transform: translateX(4px);
    }
    .ac-icon { font-size: 1.5rem; flex-shrink: 0; }
    .ac-name { color: var(--ink); font-size: 0.88rem; font-weight: 500; letter-spacing: 0.3px; }

    /* ══ PROPERTY CARDS ══ */
    .prop-card {
        background: white;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 6px 32px rgba(0,0,0,0.08);
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        border: 1px solid rgba(201,168,76,0.1);
        height: 100%;
        position: relative;
    }
    .prop-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 28px 64px rgba(26,58,42,0.2);
    }
    .prop-card-header {
        background: linear-gradient(160deg, var(--deep), #1f4a32);
        padding: 36px 28px 32px;
        position: relative;
        overflow: hidden;
    }
    .prop-card-header::before {
        content: '';
        position: absolute;
        top: -40px; right: -40px;
        width: 160px; height: 160px;
        border-radius: 50%;
        background: rgba(201,168,76,0.08);
    }
    .prop-badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        color: var(--forest);
        font-family: 'Cinzel', serif;
        font-size: 0.6rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 5px 16px;
        border-radius: 50px;
        margin-bottom: 16px;
        position: relative;
        z-index: 1;
    }
    .prop-card-header h3 {
        font-family: 'Cormorant Garamond', serif;
        color: white;
        font-size: 1.8rem;
        font-weight: 300;
        margin-bottom: 8px;
        position: relative;
        z-index: 1;
        line-height: 1.15;
    }
    .prop-card-header h3 em { font-style: italic; color: var(--gold-light); }
    .prop-price {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.6rem;
        font-weight: 600;
        color: var(--gold-light);
        position: relative;
        z-index: 1;
    }
    .prop-body { padding: 28px; }
    .prop-desc { color: var(--moss); font-size: 0.88rem; line-height: 1.8; margin-bottom: 20px; font-weight: 300; }
    .prop-specs {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-bottom: 22px;
    }
    .spec-pill {
        background: var(--cream);
        border: 1px solid var(--parchment);
        color: var(--ink);
        font-size: 0.72rem;
        padding: 5px 14px;
        border-radius: 50px;
        font-weight: 500;
        letter-spacing: 0.5px;
        white-space: nowrap;
    }
    .prop-features {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-bottom: 24px;
    }
    .prop-feature-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.82rem;
        color: var(--moss);
    }
    .prop-feature-item::before {
        content: '✓';
        color: var(--gold);
        font-weight: 700;
        font-size: 0.85rem;
    }

    /* ══ PILLAR CARDS ══ */
    .pillar-card {
        background: white;
        border-radius: 18px;
        padding: 48px 32px;
        box-shadow: 0 6px 30px rgba(26,58,42,0.08);
        text-align: center;
        height: 100%;
        position: relative;
        overflow: hidden;
        transition: all 0.35s ease;
        border: 1px solid rgba(201,168,76,0.1);
    }
    .pillar-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light), var(--gold));
    }
    .pillar-card:hover { transform: translateY(-6px); box-shadow: 0 20px 50px rgba(26,58,42,0.14); }
    .pillar-num {
        font-family: 'Cormorant Garamond', serif;
        font-size: 5rem;
        font-weight: 700;
        color: rgba(201,168,76,0.1);
        position: absolute;
        top: -10px; right: 16px;
        line-height: 1;
        pointer-events: none;
    }
    .pillar-icon { font-size: 3rem; margin-bottom: 22px; display: block; }
    .pillar-card h4 {
        font-family: 'Cinzel', serif;
        color: var(--ink);
        font-size: 1rem;
        letter-spacing: 3px;
        margin-bottom: 16px;
        position: relative;
        z-index: 1;
    }
    .pillar-card p { color: var(--moss); font-size: 0.88rem; line-height: 1.82; font-weight: 300; }

    /* ══ LIFESTYLE ITEMS ══ */
    .lifestyle-item {
        display: flex;
        gap: 20px;
        padding: 24px 28px;
        background: white;
        border-radius: 14px;
        margin-bottom: 14px;
        box-shadow: 0 3px 18px rgba(0,0,0,0.05);
        transition: all 0.25s;
        border: 1px solid rgba(201,168,76,0.1);
    }
    .lifestyle-item:hover {
        box-shadow: 0 10px 36px rgba(26,58,42,0.1);
        border-color: rgba(201,168,76,0.3);
        transform: translateX(4px);
    }
    .lifestyle-item .li-icon {
        font-size: 2.2rem;
        flex-shrink: 0;
        width: 56px;
        height: 56px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, rgba(201,168,76,0.1), rgba(201,168,76,0.05));
        border-radius: 12px;
        border: 1px solid rgba(201,168,76,0.15);
    }
    .lifestyle-item h4 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--ink);
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .lifestyle-item p { color: var(--moss); font-size: 0.88rem; margin: 0; line-height: 1.7; font-weight: 300; }

    /* ══ LOCATION ITEMS ══ */
    .loc-item {
        display: flex;
        gap: 18px;
        align-items: flex-start;
        padding: 20px 24px;
        background: white;
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0 2px 14px rgba(0,0,0,0.04);
        border-left: 3px solid var(--gold);
        transition: all 0.25s;
    }
    .loc-item:hover {
        box-shadow: 0 8px 28px rgba(0,0,0,0.09);
        transform: translateX(4px);
    }
    .loc-icon-wrap { font-size: 1.4rem; flex-shrink: 0; margin-top: 2px; }
    .loc-text h4 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--ink);
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 3px;
    }
    .loc-text p { color: var(--moss); font-size: 0.84rem; margin: 0; line-height: 1.6; font-weight: 300; }

    /* ══ CONNECTIVITY CARDS ══ */
    .conn-card {
        background: linear-gradient(135deg, rgba(201,168,76,0.08), rgba(201,168,76,0.03));
        border: 1px solid rgba(201,168,76,0.25);
        border-radius: 14px;
        padding: 28px 24px;
        text-align: center;
        transition: all 0.3s;
        height: 100%;
    }
    .conn-card:hover {
        background: linear-gradient(135deg, rgba(201,168,76,0.15), rgba(201,168,76,0.07));
        border-color: rgba(201,168,76,0.5);
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(201,168,76,0.18);
    }
    .conn-card .cc-icon { font-size: 2rem; margin-bottom: 12px; display: block; }
    .conn-card .cc-dest {
        font-family: 'Cormorant Garamond', serif;
        color: var(--ink);
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .conn-card .cc-time {
        font-family: 'Cinzel', serif;
        font-size: 1.5rem;
        color: var(--gold);
        font-weight: 600;
        display: block;
        margin: 8px 0 4px;
    }
    .conn-card .cc-via {
        font-size: 0.72rem;
        color: var(--mist);
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* ══ MAP BLOCK ══ */
    .map-embed-block {
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 12px 48px rgba(0,0,0,0.18);
        border: 1px solid rgba(201,168,76,0.2);
        position: relative;
    }
    .map-embed-block iframe {
        display: block;
        border: none;
    }
    .map-overlay-badge {
        position: absolute;
        top: 20px; left: 20px;
        background: rgba(10,31,18,0.9);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(201,168,76,0.35);
        border-radius: 10px;
        padding: 10px 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .map-overlay-badge .mob-dot {
        width: 10px; height: 10px;
        border-radius: 50%;
        background: var(--gold);
        box-shadow: 0 0 0 3px rgba(201,168,76,0.25);
        animation: dot-pulse 2s infinite;
    }
    @keyframes dot-pulse {
        0%,100% { box-shadow: 0 0 0 3px rgba(201,168,76,0.25); }
        50% { box-shadow: 0 0 0 7px rgba(201,168,76,0.1); }
    }
    .mob-text { color: white; font-size: 0.78rem; font-weight: 500; line-height: 1.4; }
    .mob-text small { color: rgba(255,255,255,0.5); font-size: 0.65rem; letter-spacing: 1px; text-transform: uppercase; display: block; }

    /* ══ CONTACT ══ */
    .contact-info-box {
        background: linear-gradient(155deg, #142d1e 0%, #0a1f12 100%);
        border-radius: 20px;
        padding: 40px 36px;
        border: 1px solid rgba(201,168,76,0.18);
        height: 100%;
        box-shadow: 0 12px 48px rgba(0,0,0,0.25);
    }
    .contact-info-box h3 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--gold-light);
        font-size: 1.7rem;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .cib-tagline {
        color: rgba(255,255,255,0.38);
        font-size: 0.62rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 30px;
        display: block;
    }
    .contact-line {
        display: flex;
        gap: 16px;
        margin-bottom: 24px;
        align-items: flex-start;
        padding-bottom: 20px;
        border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .contact-line:last-of-type { border-bottom: none; }
    .ci-icon-wrap {
        width: 38px; height: 38px;
        border-radius: 10px;
        background: rgba(201,168,76,0.12);
        border: 1px solid rgba(201,168,76,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        flex-shrink: 0;
    }
    .ci-text { color: rgba(255,255,255,0.7); font-size: 0.88rem; line-height: 1.75; }
    .ci-text strong { color: rgba(255,255,255,0.95); display: block; margin-bottom: 3px; font-size: 0.82rem; letter-spacing: 0.5px; }

    /* ══ QUOTE BLOCK ══ */
    .quote-block {
        background: linear-gradient(135deg, var(--deep) 0%, #1f4a32 100%);
        border-radius: 18px;
        padding: 52px 56px;
        border-left: 4px solid var(--gold);
        position: relative;
        overflow: hidden;
    }
    .quote-block::before {
        content: '"';
        position: absolute;
        top: -20px; left: 32px;
        font-family: 'Cormorant Garamond', serif;
        font-size: 12rem;
        color: rgba(201,168,76,0.08);
        line-height: 1;
        pointer-events: none;
    }
    .quote-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.65rem;
        font-weight: 300;
        font-style: italic;
        color: rgba(255,255,255,0.9);
        line-height: 1.65;
        position: relative;
        z-index: 1;
    }

    /* ══ DEVELOPER CARD ══ */
    .developer-strip {
        display: flex;
        align-items: center;
        gap: 32px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(201,168,76,0.2);
        border-radius: 16px;
        padding: 32px 40px;
        max-width: 800px;
        margin: 0 auto;
    }
    .dev-icon { font-size: 4rem; }
    .dev-stats {
        display: flex;
        gap: 40px;
    }
    .dev-stat .ds-val {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.2rem;
        font-weight: 600;
        color: var(--gold-light);
        display: block;
        line-height: 1;
    }
    .dev-stat .ds-lbl {
        font-size: 0.65rem;
        color: rgba(255,255,255,0.4);
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 5px;
        display: block;
    }

    /* ══ COMPARISON TABLE ══ */
    .comparison-table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 28px rgba(0,0,0,0.08);
        font-size: 0.88rem;
    }
    .comparison-table thead tr {
        background: linear-gradient(90deg, var(--deep), #1f4a32);
    }
    .comparison-table thead th {
        color: var(--gold-light);
        font-family: 'Cinzel', serif;
        font-size: 0.68rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 18px 20px;
        font-weight: 600;
        text-align: left;
    }
    .comparison-table tbody tr {
        border-bottom: 1px solid rgba(201,168,76,0.1);
        transition: background 0.2s;
    }
    .comparison-table tbody tr:nth-child(even) { background: rgba(201,168,76,0.03); }
    .comparison-table tbody tr:hover { background: rgba(201,168,76,0.08); }
    .comparison-table tbody td {
        padding: 15px 20px;
        color: var(--ink);
        vertical-align: middle;
    }
    .comparison-table tbody td:first-child { font-weight: 500; }
    .td-price { color: var(--mid); font-weight: 600; font-family: 'Cormorant Garamond', serif; font-size: 1rem; }
    .td-badge {
        display: inline-block;
        padding: 3px 12px;
        border-radius: 50px;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .td-avail { background: rgba(74,140,104,0.15); color: #2d6a4f; }
    .td-limited { background: rgba(201,168,76,0.15); color: #8a6f1e; }
    .td-pre { background: rgba(26,58,42,0.1); color: var(--ink); }

    /* ══ FOOTER ══ */
    .footer {
        background: var(--forest);
        padding: 80px 80px 40px;
        border-top: 1px solid rgba(201,168,76,0.15);
    }
    .footer-logo {
        font-family: 'Cinzel', serif;
        color: var(--gold);
        font-size: 1.4rem;
        letter-spacing: 2.5px;
        margin-bottom: 6px;
    }
    .footer-tagline {
        font-family: 'Cormorant Garamond', serif;
        color: rgba(255,255,255,0.35);
        font-size: 0.82rem;
        letter-spacing: 4px;
        font-style: italic;
        margin-bottom: 20px;
    }
    .footer-divider {
        border: none;
        border-top: 1px solid rgba(255,255,255,0.07);
        margin: 36px 0 24px;
    }
    .footer-copy {
        text-align: center;
        color: rgba(255,255,255,0.28);
        font-size: 0.76rem;
        line-height: 1.8;
    }

    /* ══ FORM OVERRIDES ══ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 8px !important;
        border: 1px solid rgba(20,45,30,0.18) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.92rem !important;
        color: #142d1e !important;
        background: #ffffff !important;
        transition: border-color 0.2s, box-shadow 0.2s !important;
        padding: 12px 16px !important;
        box-shadow: 0 2px 8px rgba(20,45,30,0.05) !important;
    }
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(20,45,30,0.38) !important;
        font-style: italic !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 3px rgba(201,168,76,0.15), 0 2px 8px rgba(20,45,30,0.05) !important;
        outline: none !important;
    }
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label,
    .stNumberInput label {
        color: #142d1e !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.4px !important;
        margin-bottom: 4px !important;
    }
    .stSelectbox > div > div {
        border-radius: 8px !important;
        border: 1px solid rgba(20,45,30,0.18) !important;
        background: #ffffff !important;
        box-shadow: 0 2px 8px rgba(20,45,30,0.05) !important;
        color: #142d1e !important;
    }
    .stSelectbox > div > div:focus-within {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 3px rgba(201,168,76,0.15) !important;
    }
    .stSelectbox [data-baseweb="select"] > div {
        color: #142d1e !important;
    }
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, var(--gold), var(--gold-light)) !important;
        color: var(--forest) !important;
        font-family: 'Cinzel', serif !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        font-size: 0.78rem !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 14px 28px !important;
        box-shadow: 0 6px 22px rgba(201,168,76,0.4) !important;
        transition: all 0.25s !important;
    }
    [data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 32px rgba(201,168,76,0.55) !important;
    }

    /* ══ INNER PAGE BUTTONS ══ */
    .stButton > button {
        border-radius: 6px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        color: #142d1e !important;
        border: 1px solid rgba(20,45,30,0.22) !important;
        transition: all 0.2s !important;
        background: transparent !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        background: rgba(20,45,30,0.05) !important;
        border-color: rgba(20,45,30,0.4) !important;
    }

    /* ══ ADMIN DASHBOARD ══ */
    .admin-stat-card {
        background: #fff;
        border-radius: 14px;
        padding: 24px 28px;
        border: 1px solid rgba(201,168,76,0.2);
        box-shadow: 0 4px 20px rgba(20,45,30,0.07);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .admin-stat-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--gold), var(--gold-light));
    }
    .admin-stat-card .asc-val {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.8rem;
        font-weight: 700;
        color: #142d1e;
        line-height: 1;
        display: block;
    }
    .admin-stat-card .asc-lbl {
        font-size: 0.65rem;
        color: rgba(20,45,30,0.55);
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-top: 6px;
        display: block;
        font-weight: 500;
    }
    .admin-preview-card {
        background: #fff;
        border-radius: 14px;
        padding: 22px 26px;
        border: 1px solid rgba(201,168,76,0.2);
        box-shadow: 0 4px 20px rgba(20,45,30,0.06);
    }
    .admin-preview-card h4 {
        font-family: 'Cinzel', serif;
        color: #142d1e;
        font-size: 0.72rem;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 14px;
        opacity: 0.7;
    }
    .admin-preview-row {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 8px;
    }
    .apr-label {
        font-size: 0.73rem;
        color: rgba(20,45,30,0.5);
        font-weight: 500;
        letter-spacing: 0.3px;
        min-width: 100px;
    }
    .apr-value {
        font-size: 0.78rem;
        color: #142d1e;
        font-weight: 500;
        text-align: right;
        flex: 1;
    }
    .admin-section-title {
        font-family: 'Cinzel', serif;
        color: #142d1e;
        font-size: 0.7rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin: 28px 0 14px;
        padding-bottom: 10px;
        border-bottom: 1px solid rgba(201,168,76,0.25);
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .danger-zone {
        background: rgba(220,38,38,0.04);
        border: 1px solid rgba(220,38,38,0.18);
        border-radius: 12px;
        padding: 22px 24px;
        margin-top: 10px;
    }

    /* ══ DATAFRAME STYLING ══ */
    [data-testid="stDataFrame"] {
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 22px rgba(0,0,0,0.07) !important;
    }

    /* ══ RESPONSIVE ══ */
    @media (max-width: 768px) {
        .hero { padding: 80px 24px 70px; min-height: auto; }
        .sec { padding: 64px 24px; }
        .stats-strip { grid-template-columns: repeat(3, 1fr); padding: 32px 24px; gap: 20px; }
        .strip-item:not(:last-child)::after { display: none; }
        .footer { padding: 56px 24px 32px; }
        .top-nav { padding: 0 20px; }
        .hero-h1 { font-size: 2.4rem !important; }
    }
    </style>
    """, unsafe_allow_html=True)


# ─── IMAGE HELPERS ───────────────────────────────────────────────────────────
def load_img_b64(path):
    if not os.path.isabs(path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, path)
    else:
        full_path = path

    if not os.path.exists(full_path):
        return None
    with open(full_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    ext = full_path.rsplit(".", 1)[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    return data, mime


def img_tag(path, alt="", style="width:100%;display:block;"):
    result = load_img_b64(path)
    if result:
        b64, mime = result
        return f'<img src="data:{mime};base64,{b64}" alt="{alt}" style="{style}">'
    return None


def prop_image(path, alt="", height=240):
    result = load_img_b64(path)
    if result:
        b64, mime = result
        return f'<img src="data:{mime};base64,{b64}" alt="{alt}" style="width:100%;height:{height}px;object-fit:cover;display:block;">'
    return None


def get_first_img(paths, alt="", style=""):
    for p in paths:
        t = img_tag(p, alt, style)
        if t:
            return t
    return None


# ─── NAVIGATION ─────────────────────────────────────────────────────────────
PAGES = ["🏡 Home", "🌿 About", "🏘️ Properties", "📍 Location", "📞 Contact"]


def render_navbar():
    st.markdown("""
    <div class="top-nav">
        <div class="nav-brand">
            <div class="nav-brand-logo">🌿</div>
            <div>
                <div class="nav-name">Aranya Farms</div>
                <div class="nav-sub">Silver Oaks Agro Farms · Achampet, Toopran</div>
            </div>
        </div>
        <div class="nav-right">
            <a class="nav-wa-btn" href="https://wa.me/919640222237" target="_blank">
                💬 WhatsApp
            </a>
            <a class="nav-call-btn" href="tel:+919640222237">
                📞 +91 96402 22237
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_page_nav():
    st.markdown("<div class='page-nav-outer'>", unsafe_allow_html=True)
    cols = st.columns(len(PAGES))
    for i, page in enumerate(PAGES):
        with cols[i]:
            label = page.split(" ", 1)[1] if " " in page else page
            if st.button(label, key=f"nav_{i}", use_container_width=True):
                st.session_state.page = page
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ─── REUSABLE SECTION HELPERS ────────────────────────────────────────────────
def section_header(eyebrow, title, subtitle=None, center=False, dark=False):
    align = "center" if center else "left"
    eyebrow_class = "eyebrow eyebrow-center" if center else "eyebrow"
    h2_class = "sec-h2-white" if dark else "sec-h2"
    lead_class = "sec-lead sec-lead-center" if center else "sec-lead"
    sub_html = f'<p class="{lead_class}">{subtitle}</p>' if subtitle else ""
    rule_html = '<div class="rule rule-center"></div>' if center else '<div class="rule"></div>'
    st.markdown(f"""
    <div style="text-align:{align};">
        <div class="{eyebrow_class}">{eyebrow}</div>
        <div class="{h2_class}">{title}</div>
        {rule_html}
        {sub_html}
    </div>""", unsafe_allow_html=True)


def hero_mini(eyebrow, title, subtitle):
    st.markdown(f"""
    <div class="hero" style="min-height:380px;padding:100px 80px 90px;">
        <div class="hero-grid-lines"></div>
        <div style="position:relative;z-index:2;">
            <div class="hero-eyebrow">{eyebrow}</div>
            <h1 class="hero-h1" style="font-size:clamp(2.4rem,4vw,4.2rem);">{title}</h1>
            <p class="hero-para" style="max-width:480px;">{subtitle}</p>
        </div>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 1 — HOME
# ═══════════════════════════════════════════════════════════════════════════
def page_home():
    # ── HERO ──
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    st.markdown('<div class="hero-grid-lines"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.15, 0.85], gap="large")
    with col1:
        st.markdown("""
        <div style="position:relative;z-index:2;">
            <div class="hero-eyebrow">Silver Oaks Agro Farms Presents</div>
            <h1 class="hero-h1">
                <strong>Luxury</strong> Farm Living<br>at <em>Aranya Farms</em>
            </h1>
            <p class="hero-para">
                A premium gated community across 55 acres of lush green land at Achampet, Toopran —
                where nature's serenity meets refined, modern living.
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
        hero_img = get_first_img(
            ["images/land1.png","images/land1.jpg","images/land2.png","images/land2.jpg"],
            "Aranya Farms",
            "width:100%;border-radius:18px;box-shadow:0 20px 64px rgba(0,0,0,0.45);display:block;"
        )
        if hero_img:
            st.markdown(f'<div style="position:relative;z-index:2;">{hero_img}</div>', unsafe_allow_html=True)
            
            st.markdown("""
            <div style="position:relative;z-index:2;">
                <div style="border:1px solid rgba(201,168,76,0.3);border-radius:18px;padding:90px 32px;
                     text-align:center;background:#ffffff;box-shadow:0 20px 50px rgba(20,45,30,0.08);">
                    <div style="font-family:'Cormorant Garamond',serif;font-size:6.5rem;
                                color:var(--gold);opacity:0.25;line-height:1;margin-bottom:15px;">🌾</div>
                    <h2 style="font-family:'Cinzel',serif;font-size:3.5rem;font-weight:700;
                               color:var(--gold);letter-spacing:3px;margin:0 0 16px;line-height:1.1;">
                        Aranya Farms
                    </h2>
                  style="font-family:'DM Sans',sans-serif;font-size:1.15rem;color:var(--moss);
                              margin:0;letter-spacing:1px;font-weight:300;line-height:1.6;">
                        Silver Oaks Agro Farms &middot; Achampet, Toopran
                    </p>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── STATS STRIP ──
    st.markdown("""
    <div class="stats-strip">
        <div class="strip-item">
            <span class="strip-val">55+</span>
            <span class="strip-lbl">Acres of Green</span>
        </div>
        <div class="strip-item">
            <span class="strip-val">200+</span>
            <span class="strip-lbl">Happy Families</span>
        </div>
        <div class="strip-item">
            <span class="strip-val">18+</span>
            <span class="strip-lbl">World-Class Amenities</span>
        </div>
        <div class="strip-item">
            <span class="strip-val">₹49L</span>
            <span class="strip-lbl">Starting Price</span>
        </div>
        <div class="strip-item">
            <span class="strip-val">2024</span>
            <span class="strip-lbl">Ready Possession</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── WHY ARANYA ──
    with st.container():
        st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
        section_header("Why Choose Us", "The Aranya Farms <em>Difference</em>",
                       "A unique blend of luxury living and nature's serenity — thoughtfully designed for families who seek more than just a home.")
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:var(--cream);">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4, gap="medium")
        features = [
            ("🌿", "Pure Nature", "Lush greenery with fresh air, organic surroundings, and breathtaking sunrise views from your doorstep."),
            ("🏡", "Premium Homes", "Thoughtfully designed 3-BHK farm houses with modern architecture and natural aesthetics."),
            ("🛡️", "Gated Security", "24×7 security, CCTV surveillance, and managed access for total peace of mind."),
            ("🌊", "Riverside Living", "Adjacent to the serene Haldi River — nature's own backyard at your doorstep."),
        ]
        for col, (icon, title, desc) in zip([c1, c2, c3, c4], features):
            with col:
                st.markdown(f"""
                <div class="feat-card">
                    <div class="feat-icon-wrap">{icon}</div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── AMENITIES ──
    with st.container():
        st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
        section_header("World-Class Amenities", "Everything You Need to <em>Live Well</em>")
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:white;">', unsafe_allow_html=True)
        amenities = [
            ("🏊", "Swimming Pool"),     ("🎾", "Sports Arena"),
            ("🌿", "Organic Farming"),   ("🐄", "Goshala"),
            ("🌸", "Gazebo & Gardens"),  ("🏋️", "Fitness Centre"),
            ("🍽️", "Clubhouse & Dining"), ("🛕", "Meditation Zone"),
            ("🎠", "Children's Play Area"), ("🌳", "Tree Plantation"),
            ("🚗", "Ample Parking"),     ("💧", "24×7 Water Supply"),
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
        <div class="eyebrow eyebrow-center">Limited Plots Available</div>
        <div class="sec-h2-white" style="text-align:center;">
            Ready to Find Your Perfect <em>Farm Plot?</em>
        </div>
        <div class="rule rule-center"></div>
        <p style="color:rgba(255,255,255,0.55);font-size:1.02rem;margin-bottom:40px;
                  font-weight:300;max-width:560px;margin-left:auto;margin-right:auto;line-height:1.8;">
            Plots starting from ₹49 Lakhs. Register now for exclusive pre-launch pricing and a
            complimentary site visit.
st.markdown("""
   </p>
<div class="cta-row" style="justify-content:center;">
    <a class="btn-gold" href="tel:+919640222237">📅 Book Free Site Visit</a>

    <a class="btn-ghost" href="tel:+919640222237">
        📞 Talk to Expert
    </a>

with open("Aranya Farms - Brochure.pdf", "rb") as pdf_file:
    st.download_button(
        label="📄 Download Brochure",
        data=pdf_file,
        file_name="Aranya-Farms-Brochure.pdf",
        mime="application/pdf",
        use_container_width=False
    )
</div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 2 — ABOUT
# ═══════════════════════════════════════════════════════════════════════════
def page_about():
    hero_mini("Our Story", "About <em>Aranya Farms</em>", "Play · Live · Celebrate — A new way to belong to nature.")

    # ── VISION ──
    with st.container():
        st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            about_img = get_first_img(
                ["images/land3.png","images/land3.jpg","images/land2.png","images/land2.jpg","images/land1.png","images/land1.jpg"],
                "Aranya Farms Land",
                "width:100%;height:400px;object-fit:cover;border-radius:16px;box-shadow:0 12px 48px rgba(0,0,0,0.15);display:block;"
            )
            if about_img:
                st.markdown(about_img, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="quote-block">
                    <div class="quote-text">"Every family deserves a sanctuary where they can breathe freely, grow organically, and celebrate life amid nature's abundance."</div>
                    <div style="color:var(--gold-light);font-family:'Cinzel',serif;font-size:0.65rem;
                                letter-spacing:3px;text-transform:uppercase;margin-top:28px;
                                padding-top:20px;border-top:1px solid rgba(201,168,76,0.2);">
                        — Silver Oaks Agro Farms
                    </div>
                </div>""", unsafe_allow_html=True)

        with col2:
            section_header("The Vision", "Where Rural Richness Meets <em>Urban Comfort</em>")
            st.markdown("""
            <div style="padding-top:4px;">
                <p style="color:var(--moss);font-size:1.02rem;line-height:1.92;margin-bottom:20px;font-weight:300;">
                    <strong style="color:var(--ink);font-weight:600;">Aranya Farms</strong> is not just a real estate project —
                    it is a lifestyle reimagined. Spread across
                    <strong style="color:var(--mid);">55 lush acres</strong> in Achampet, Toopran, it brings together
                    the warmth of rural living with the comforts of a premium gated community.
                </p>
                <p style="color:var(--moss);font-size:1.02rem;line-height:1.92;margin-bottom:20px;font-weight:300;">
                    Conceived by <strong style="color:var(--ink);">Silver Oaks Agro Farms</strong>, a trusted name in
                    managed farmland communities, this project is born from a simple belief:
                    <em style="color:var(--mid);">every family deserves a sanctuary where they can breathe freely,
                    grow organically, and celebrate life.</em>
                </p>
                <p style="color:var(--moss);font-size:1.02rem;line-height:1.92;font-weight:300;">
                    Adjacent to the tranquil Haldi River and just 5 minutes from RRR, Aranya Farms
                    is the perfect balance of accessibility and escape — a home you will look forward
                    to returning to every single weekend.
                </p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── PHILOSOPHY PILLARS ──
    with st.container():
        st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
        section_header("Our Philosophy", "Play · Live · <em>Celebrate</em>", center=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:white;">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3, gap="medium")
        pillars = [
            ("🎠", "01", "PLAY",
             "Sports arenas, swimming pool, children's zones, and nature trails — because life is meant to be enjoyed at every age, every weekend, every season."),
            ("🏡", "02", "LIVE",
             "Thoughtfully crafted farm houses and plots designed for wholesome family living. Wake up to birdsong, grow your own food, breathe truly clean air."),
            ("🎉", "03", "CELEBRATE",
             "From festive gatherings at the clubhouse to quiet birthday mornings in the gazebo — every milestone is profoundly better amid nature."),
        ]
        for col, (icon, num, title, desc) in zip([c1, c2, c3], pillars):
            with col:
                st.markdown(f"""
                <div class="pillar-card">
                    <div class="pillar-num">{num}</div>
                    <span class="pillar-icon">{icon}</span>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── LIFESTYLE ──
    with st.container():
        st.markdown('<div class="sec sec-sand">', unsafe_allow_html=True)
        section_header("Lifestyle & Wellness", "Designed for Every <em>Chapter of Life</em>")
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:var(--sand);">', unsafe_allow_html=True)
        lifestyles = [
            ("👨‍👩‍👧‍👦", "Family Lifestyle",
             "Spacious plots with dedicated zones for kids, elders, and togetherness. A community where neighbours become extended family."),
            ("🧘", "Wellness Retreat",
             "Yoga pavilion, meditation zones, organic garden walks, and fresh-air mornings — your personal wellness sanctuary awaits."),
            ("🏡", "Weekend Homes",
             "Just 30 minutes from ORR — the ideal weekend getaway that feels a world away. Perfectly suited as rent-ready investments."),
            ("🌱", "Organic Living",
             "Farm-to-table living. Grow your own vegetables, herbs, and fruits on your private plot with full managed farming support."),
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

    # ── DEVELOPER ──
    st.markdown("""
    <div class="sec sec-dark" style="text-align:center;">
        <div class="eyebrow eyebrow-center">About the Developer</div>
        <div class="sec-h2-white" style="text-align:center;">Silver Oaks <em>Agro Farms</em></div>
        <div class="rule rule-center"></div>
        <p style="color:rgba(255,255,255,0.62);font-size:1rem;line-height:1.92;max-width:740px;
                  margin:0 auto 44px;font-weight:300;">
            Silver Oaks Agro Farms, operating under <strong style="color:var(--gold-light);">Silver Oaks Realty</strong>,
            is a Hyderabad-based premium farmland developer with a decade of experience in creating
            managed agro-communities. With a commitment to transparency, DTCP-approved layouts, and
            world-class amenities, Silver Oaks has helped over 500+ families find their perfect green sanctuary.
        </p>
        <div class="developer-strip">
            <div class="dev-icon">🌳</div>
            <div class="dev-stats">
                <div class="dev-stat">
                    <span class="ds-val">500+</span>
                    <span class="ds-lbl">Families Served</span>
                </div>
                <div class="dev-stat">
                    <span class="ds-val">10+</span>
                    <span class="ds-lbl">Years Experience</span>
                </div>
                <div class="dev-stat">
                    <span class="ds-val">5+</span>
                    <span class="ds-lbl">Projects Delivered</span>
                </div>
                <div class="dev-stat">
                    <span class="ds-val">DTCP</span>
                    <span class="ds-lbl">Approved Layouts</span>
                </div>
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

    # ── PROPERTY CARDS ──
    with st.container():
        st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
        section_header("Available Properties", "Explore Our <em>Offerings</em>",
                       "All properties are within the 55-acre gated community with full access to world-class amenities.")
        st.markdown("</div>", unsafe_allow_html=True)

    properties = [
        {
            "badge": "Best Seller",
            "title": "Farm <em>Plots</em>",
            "price": "Starting ₹49 Lakhs",
            "specs": ["300 sq. yds", "605 sq. yds", "640 sq. yds", "753 sq. yds"],
            "features": ["DTCP Approved", "Clear Titles", "Gated Community", "All Amenities Included"],
            "desc": "Open farm plots in a fully gated, amenity-rich community. Build your dream home or enjoy managed farming. Clear titles, DTCP approved layout.",
            "img_paths": ["images/land1.png", "images/land1.jpg"],
        },
        {
            "badge": "Most Popular",
            "title": "3-BHK <em>Farm Houses</em>",
            "price": "Starting ₹65 Lakhs",
            "specs": ["685 sft BUA", "1480 sft BUA", "1500 sft BUA"],
            "features": ["3 Bedrooms", "Private Garden", "Modern Kitchen", "Ready Soon"],
            "desc": "Ready-to-move 3-BHK farm houses with contemporary architecture, private garden space, and complete modern amenities for comfortable family living.",
            "img_paths": ["images/land2.png", "images/land2.jpg"],
        },
        {
            "badge": "Luxury",
            "title": "Premium <em>Villas</em>",
            "price": "Starting ₹90 Lakhs",
            "specs": ["2250 sft BUA", "Large Plot", "Private Garden"],
            "features": ["Exclusive Layout", "Premium Finishes", "Landscaped Garden", "High Ceilings"],
            "desc": "Exclusive premium villas with expansive built-up areas, landscaped private gardens, and premium finishes for the truly discerning buyer.",
            "img_paths": ["images/land3.png", "images/land3.jpg"],
        },
        {
            "badge": "Investment",
            "title": "Larger <em>Farm Lands</em>",
            "price": "On Request",
            "specs": ["1+ Acre", "Custom Layout", "Managed Option"],
            "features": ["Bulk Parcels", "Custom Design", "Managed Farming", "Community Access"],
            "desc": "Bulk farmland parcels ideal for families or investor groups seeking larger green footprints with full community access and managed farming support.",
            "img_paths": ["images/land4.png", "images/land4.jpg"],
        },
    ]

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:var(--cream);">', unsafe_allow_html=True)
        c1, c2 = st.columns(2, gap="large")
        for i, prop in enumerate(properties):
            with (c1 if i % 2 == 0 else c2):
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
                st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
                if st.button(f"📩 Enquire — {prop['title'].replace('<em>','').replace('</em>','')}", key=f"prop_btn_{i}", use_container_width=True):
                    st.session_state.page = "📞 Contact"
                    st.rerun()
                st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── COMPARISON TABLE ──
    with st.container():
        st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
        section_header("Plot Dimensions", "Complete Pricing at a <em>Glance</em>",
                       "All prices are indicative. Contact our sales team for current pricing and availability.")
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:white;">', unsafe_allow_html=True)
        df = pd.DataFrame({
            "Type": [
                "Farm Plot – Compact", "Farm Plot – Standard", "Farm Plot – Large",
                "Farm Plot – Premium", "Farm House – 3 BHK (A)", "Farm House – 3 BHK (B)",
                "Farm House – 3 BHK (C)", "Premium Villa"
            ],
            "Plot Size": ["300 sq. yds", "605 sq. yds", "640 sq. yds", "753 sq. yds",
                          "Included", "Included", "Included", "Large"],
            "Built-up Area": ["—", "—", "—", "—", "685 sft", "1480 sft", "1500 sft", "2250 sft"],
            "Starting Price": ["₹49 Lakhs", "₹55 Lakhs", "₹60 Lakhs", "₹68 Lakhs",
                               "₹65 Lakhs", "₹72 Lakhs", "₹78 Lakhs", "₹90 Lakhs"],
            "Availability": ["Available", "Limited", "Available", "Limited",
                             "Available", "Ready Soon", "Available", "Pre-launch"],
        })
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── BOTTOM CTA ──
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style="text-align:center;padding:60px 0 80px;background:var(--cream);">
                <div class="eyebrow eyebrow-center">Exclusive Offer</div>
                <div class="sec-h2" style="text-align:center;">Get Pre-Launch <em>Pricing</em></div>
                <div class="rule rule-center"></div>
                <p style="color:var(--moss);font-size:0.95rem;line-height:1.8;margin-bottom:28px;font-weight:300;">
                    Register your interest today for access to special pre-launch rates and complimentary site visit.
                </p>
                <div class="cta-row" style="justify-content:center;">
                    <a class="btn-gold" href="#">📅 Register Interest</a>
                    <a class="btn-wa" href="https://wa.me/919640222238" target="_blank">💬 WhatsApp Us</a>
                </div>
            </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 4 — LOCATION
# ═══════════════════════════════════════════════════════════════════════════
def page_location():
    hero_mini("Find Us", "Location & <em>Connectivity</em>",
              "Strategically placed in Achampet, Toopran — nature close, city even closer.")

    # ── LOCATION HIGHLIGHTS + MAP ──
    with st.container():
        st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            section_header("How to Reach", "Location <em>Highlights</em>")
            highlights = [
                ("📍", "Exact Location",
                 "Achampet Village, Toopran Mandal, Medchal-Malkajgiri District, Telangana"),
                ("🛣️", "Near RRR",
                 "Only 5 minutes from the Regional Ring Road (RRR) entry point"),
                ("🔄", "Near ORR",
                 "Approx. 30 minutes from the Outer Ring Road (ORR), Hyderabad"),
                ("🏙️", "NH-44 Access",
                 "Adjacent to the Hyderabad–Medchal Highway (NH-44)"),
                ("🌊", "Riverside",
                 "Adjacent to the scenic Haldi River — beautiful water views year-round"),
                ("🏘️", "Near Masaipet",
                 "Close to Masaipet town for easy access to local markets and services"),
                ("✈️", "Airport",
                 "Approx. 40–50 minutes from Rajiv Gandhi International Airport"),
            ]
            for icon, title, desc in highlights:
                st.markdown(f"""
                <div class="loc-item">
                    <div class="loc-icon-wrap">{icon}</div>
                    <div class="loc-text"><h4>{title}</h4><p>{desc}</p></div>
                </div>""", unsafe_allow_html=True)

        with col2:
            section_header("Interactive Map", "View on <em>Map</em>")
            sat_result = None
            for sp in ["images/satellite.png", "images/satellite.jpg"]:
                sat_result = load_img_b64(sp)
                if sat_result:
                    break
            if sat_result:
                b64, mime = sat_result
                st.markdown(f"""
                <div class="map-embed-block">
                    <img src="data:{mime};base64,{b64}" alt="Satellite View – Aranya Farms"
                         style="width:100%;height:420px;object-fit:cover;display:block;">
                    <div class="map-overlay-badge">
                        <div class="mob-dot"></div>
                        <div class="mob-text">
                            Aranya Farms
                            <small>Achampet · Toopran · Telangana</small>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="map-embed-block">
                    <iframe
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3808.7!2d78.1!3d17.7!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb9c0000000001%3A0x1!2sAchampet%2C%20Toopran%2C%20Telangana!5e0!3m2!1sen!2sin!4v1700000000000"
                        width="100%" height="420"
                        style="border:0;"
                        allowfullscreen="" loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                    <div class="map-overlay-badge">
                        <div class="mob-dot"></div>
                        <div class="mob-text">
                            Aranya Farms
                            <small>Achampet · Toopran · Telangana</small>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)

            st.markdown("""
            <div style="margin-top:20px;">
                <a class="btn-green" href="https://maps.google.com/?q=Achampet+Toopran+Telangana"
                   target="_blank" style="display:inline-flex;">
                    🗺️ Open in Google Maps
                </a>
            </div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── CONNECTIVITY CARDS ──
    with st.container():
        st.markdown('<div class="sec sec-white">', unsafe_allow_html=True)
        section_header("Connectivity", "Key Distances from <em>Aranya Farms</em>", center=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:white;">', unsafe_allow_html=True)
        connections = [
            ("🛣️", "RRR", "~5 min", "State Highway"),
            ("🔄", "ORR", "~30 min", "NH-44 + RRR"),
            ("🏙️", "Kompally", "~28 min", "NH-44"),
            ("🏘️", "Medchal", "~18 min", "NH-44"),
            ("🌆", "Hyderabad City", "~40 min", "NH-44 + ORR"),
            ("✈️", "Airport RGIA", "~50 min", "ORR + Shamshabad"),
        ]
        c1, c2, c3, c4, c5, c6 = st.columns(6, gap="small")
        for col, (icon, dest, time, via) in zip([c1,c2,c3,c4,c5,c6], connections):
            with col:
                st.markdown(f"""
                <div class="conn-card">
                    <span class="cc-icon">{icon}</span>
                    <div class="cc-dest">{dest}</div>
                    <span class="cc-time">{time}</span>
                    <div class="cc-via">{via}</div>
                </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── DISTANCE TABLE ──
    with st.container():
        st.markdown('<div class="sec sec-sand">', unsafe_allow_html=True)
        section_header("Distances", "Full Distance <em>Reference</em>")
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div style="padding:0 80px 88px;background:var(--sand);">', unsafe_allow_html=True)
        df = pd.DataFrame({
            "Destination": [
                "RRR (Regional Ring Road)", "ORR (Outer Ring Road)", "Kompally",
                "Medchal Town", "Hyderabad City Centre", "RGIA Airport",
                "Masaipet", "Haldi River"
            ],
            "Distance": ["~5 km", "~30 km", "~28 km", "~18 km", "~38 km", "~48 km", "~3 km", "Adjacent"],
            "Travel Time": ["~5 mins", "~30 mins", "~28 mins", "~18 mins", "~40 mins", "~50 mins", "~5 mins", "Walking"],
            "Route": ["State Highway", "NH-44 + RRR", "NH-44", "NH-44", "NH-44 + ORR", "ORR + Shamshabad", "Local Road", "—"],
        })
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  ENQUIRY STORAGE HELPERS
# ═══════════════════════════════════════════════════════════════════════════
ENQUIRY_FILE = "enquiries.csv"
ENQUIRY_COLUMNS = ["Full Name", "Phone Number", "Email Address", "Interested In", "Message", "Submission Date & Time"]
ADMIN_PASSWORD = "nagesh@1243"


def save_enquiry(name, phone, email, interest, message):
    """Save a new enquiry to enquiries.csv, creating the file if needed."""
    new_row = {
        "Full Name": name,
        "Phone Number": phone,
        "Email Address": email,
        "Interested In": interest,
        "Message": message,
        "Submission Date & Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    if os.path.exists(ENQUIRY_FILE):
        df = pd.read_csv(ENQUIRY_FILE)
    else:
        df = pd.DataFrame(columns=ENQUIRY_COLUMNS)
    new_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(ENQUIRY_FILE, index=False)


def load_enquiries():
    """Load all enquiries from CSV. Returns an empty DataFrame if file doesn't exist."""
    if os.path.exists(ENQUIRY_FILE):
        return pd.read_csv(ENQUIRY_FILE)
    return pd.DataFrame(columns=ENQUIRY_COLUMNS)


def render_admin_section():
    """Render the password-protected admin section below the contact form."""
    with st.container():
        st.markdown('<div style="padding:48px 80px 64px;background:var(--sand);">', unsafe_allow_html=True)
        st.markdown("""
        <div style="margin-bottom:24px;">
            <div class="eyebrow">Admin Panel</div>
            <div class="sec-h2">Enquiry <em>Dashboard</em></div>
            <div class="rule"></div>
            <p class="sec-lead">Password-protected dashboard for managing and reviewing all customer enquiries.</p>
        </div>""", unsafe_allow_html=True)

        admin_pass = st.text_input(
            "Admin Password",
            type="password",
            key="admin_password_input",
            placeholder="Enter password to access dashboard…",
        )

        if not admin_pass:
            st.markdown("</div>", unsafe_allow_html=True)
            return

        if admin_pass != ADMIN_PASSWORD:
            st.error("⛔ Incorrect password. Please try again.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        # ── ACCESS GRANTED ──
        df = load_enquiries()
        total = len(df)

        # ── STAT CARDS ──
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        sc1, sc2, sc3, sc4 = st.columns(4, gap="medium")
        with sc1:
            latest_date = df["Submission Date & Time"].iloc[-1] if total > 0 else "—"
            st.markdown(f"""
            <div class="admin-stat-card">
                <span class="asc-val">{total}</span>
                <span class="asc-lbl">Total Enquiries</span>
            </div>""", unsafe_allow_html=True)
        with sc2:
            today_str = datetime.now().strftime("%Y-%m-%d")
            today_count = 0
            if total > 0:
                today_count = df[df["Submission Date & Time"].str.startswith(today_str)].shape[0]
            st.markdown(f"""
            <div class="admin-stat-card">
                <span class="asc-val">{today_count}</span>
                <span class="asc-lbl">Today's Enquiries</span>
            </div>""", unsafe_allow_html=True)
        with sc3:
            top_interest = "—"
            if total > 0:
                top_interest = df["Interested In"].value_counts().idxmax()
                top_interest_short = top_interest[:16] + "…" if len(top_interest) > 16 else top_interest
            else:
                top_interest_short = "—"
            st.markdown(f"""
            <div class="admin-stat-card">
                <span class="asc-val" style="font-size:1.3rem;padding-top:4px;">{top_interest_short}</span>
                <span class="asc-lbl">Top Interest</span>
            </div>""", unsafe_allow_html=True)
        with sc4:
            this_week = 0
            if total > 0:
                try:
                    df["_dt"] = pd.to_datetime(df["Submission Date & Time"], errors="coerce")
                    cutoff = pd.Timestamp.now() - pd.Timedelta(days=7)
                    this_week = df[df["_dt"] >= cutoff].shape[0]
                    df.drop(columns=["_dt"], inplace=True)
                except Exception:
                    pass
            st.markdown(f"""
            <div class="admin-stat-card">
                <span class="asc-val">{this_week}</span>
                <span class="asc-lbl">This Week</span>
            </div>""", unsafe_allow_html=True)

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        if df.empty:
            st.info("📭 No enquiries have been submitted yet.")
            st.markdown("</div>", unsafe_allow_html=True)
            return

        # ── LATEST ENQUIRY PREVIEW ──
        latest = df.iloc[-1]
        st.markdown(f"""
        <div class="admin-preview-card">
            <h4>🕐 Latest Enquiry</h4>
            <div class="admin-preview-row">
                <span class="apr-label">Name</span>
                <span class="apr-value">{latest.get("Full Name","—")}</span>
            </div>
            <div class="admin-preview-row">
                <span class="apr-label">Phone</span>
                <span class="apr-value">{latest.get("Phone Number","—")}</span>
            </div>
            <div class="admin-preview-row">
                <span class="apr-label">Interest</span>
                <span class="apr-value">{latest.get("Interested In","—")}</span>
            </div>
            <div class="admin-preview-row">
                <span class="apr-label">Submitted</span>
                <span class="apr-value">{latest.get("Submission Date & Time","—")}</span>
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # ── SEARCH & FILTER ──
        st.markdown('<div class="admin-section-title">🔍 Search & Filter</div>', unsafe_allow_html=True)
        sf1, sf2 = st.columns([2, 1], gap="medium")
        with sf1:
            search_query = st.text_input(
                "Search enquiries",
                placeholder="Search by name, phone, email, or interest…",
                key="admin_search",
                label_visibility="collapsed",
            )
        with sf2:
            filter_interest = st.selectbox(
                "Filter by interest",
                ["All"] + sorted(df["Interested In"].dropna().unique().tolist()),
                key="admin_filter_interest",
                label_visibility="collapsed",
            )

        # Apply filters
        display_df = df.copy()
        if search_query:
            mask = display_df.apply(
                lambda row: search_query.lower() in " ".join(row.astype(str).values).lower(), axis=1
            )
            display_df = display_df[mask]
        if filter_interest != "All":
            display_df = display_df[display_df["Interested In"] == filter_interest]

        # ── ENQUIRY TABLE ──
        st.markdown('<div class="admin-section-title">📋 All Enquiries</div>', unsafe_allow_html=True)
        st.caption(f"Showing {len(display_df)} of {total} enquiries")
        st.dataframe(display_df.reset_index(drop=True), use_container_width=True, hide_index=True)

        # ── DOWNLOAD CSV ──
        csv_data = df.to_csv(index=False).encode("utf-8")
        dl_col, _ = st.columns([1, 2])
        with dl_col:
            st.download_button(
                label="⬇️ Download All as CSV",
                data=csv_data,
                file_name=f"aranya_enquiries_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv",
                use_container_width=True,
            )

        # ── DELETE SINGLE ENQUIRY ──
        st.markdown('<div class="admin-section-title">🗑️ Delete an Enquiry</div>', unsafe_allow_html=True)
        if total > 0:
            enquiry_options = {
                f"#{i+1} — {row['Full Name']} | {row['Phone Number']} | {row['Interested In']} | {row['Submission Date & Time']}": i
                for i, row in df.iterrows()
            }
            selected_label = st.selectbox(
                "Select enquiry to delete",
                list(enquiry_options.keys()),
                key="admin_delete_select",
                label_visibility="collapsed",
            )
            selected_idx = enquiry_options[selected_label]

            # Preview selected row
            sel_row = df.iloc[selected_idx]
            st.markdown(f"""
            <div style="background:rgba(220,38,38,0.04);border:1px solid rgba(220,38,38,0.15);
                        border-radius:10px;padding:14px 18px;margin:8px 0 14px;">
                <span style="font-size:0.72rem;color:rgba(20,45,30,0.55);letter-spacing:1px;
                             text-transform:uppercase;font-weight:600;">Selected for deletion:</span>
                <div style="margin-top:6px;font-size:0.85rem;color:#142d1e;">
                    <strong>{sel_row.get("Full Name","—")}</strong> &nbsp;·&nbsp;
                    {sel_row.get("Phone Number","—")} &nbsp;·&nbsp;
                    {sel_row.get("Interested In","—")} &nbsp;·&nbsp;
                    <span style="color:rgba(20,45,30,0.5);">{sel_row.get("Submission Date & Time","—")}</span>
                </div>
            </div>""", unsafe_allow_html=True)

            del_btn_col, _ = st.columns([1, 3])
            with del_btn_col:
                if st.button("🗑️ Delete Selected Enquiry", key="admin_delete_one",
                             use_container_width=True, type="secondary"):
                    df_updated = df.drop(index=selected_idx).reset_index(drop=True)
                    df_updated.to_csv(ENQUIRY_FILE, index=False)
                    st.success(f"✅ Enquiry from **{sel_row.get('Full Name','—')}** has been deleted.")
                    st.rerun()

        # ── DELETE ALL ENQUIRIES ──
        st.markdown('<div class="admin-section-title">⚠️ Danger Zone</div>', unsafe_allow_html=True)
        st.markdown('<div class="danger-zone">', unsafe_allow_html=True)
        st.markdown("""
        <div style="margin-bottom:12px;">
            <strong style="color:#dc2626;font-size:0.9rem;">Delete All Enquiries</strong>
            <p style="color:rgba(20,45,30,0.6);font-size:0.82rem;margin:4px 0 0;">
                This will permanently erase all enquiry records from the CSV file. This action cannot be undone.
            </p>
        </div>""", unsafe_allow_html=True)
        confirm_delete_all = st.checkbox(
            "I understand this is permanent and cannot be undone. Delete all enquiries.",
            key="admin_confirm_delete_all",
        )
        if confirm_delete_all:
            da_col, _ = st.columns([1, 3])
            with da_col:
                if st.button("🔥 Delete ALL Enquiries", key="admin_delete_all",
                             use_container_width=True, type="secondary"):
                    empty_df = pd.DataFrame(columns=ENQUIRY_COLUMNS)
                    empty_df.to_csv(ENQUIRY_FILE, index=False)
                    st.success("✅ All enquiries have been deleted. The file has been reset.")
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
#  PAGE 5 — CONTACT
# ═══════════════════════════════════════════════════════════════════════════
def page_contact():
    hero_mini("Get in Touch", "Let's Find Your <em>Dream Plot</em>",
              "Our expert team is ready to guide you. Book a visit or simply send us an enquiry.")

    with st.container():
        st.markdown('<div class="sec sec-cream">', unsafe_allow_html=True)
        col1, col2 = st.columns([1.3, 0.7], gap="large")

        with col1:
            section_header("Send Enquiry", "Let's <em>Talk</em>")

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
                        save_enquiry(name, phone, email, interest, message)
                        st.success("Thank you! Your enquiry has been submitted successfully.")
                        st.balloons()

            st.markdown("""
            <div style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap;">
                <a class="btn-wa" href="https://wa.me/919640222237?text=Hi!%20I%20am%20interested%20in%20Aranya%20Farms."
                   target="_blank">💬 WhatsApp Us</a>
                <a class="btn-call" href="tel:+919640222237">📞 Call Now</a>
                <a class="btn-green" href="mailto:info@silveroaksrealty.com">📧 Email Us</a>
            </div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="contact-info-box">
                <h3>Silver Oaks Realty</h3>
                <span class="cib-tagline">Aranya Farms Sales Office</span>

                <div class="contact-line">
                    <div class="ci-icon-wrap">📍</div>
                    <div class="ci-text">
                        <strong>Corporate Office</strong>
                        2nd & 3rd Floor, 14-A,<br>
                        NCL Enclave Road, Petbasheerabad,<br>
                        Kompally, Hyderabad – 500067
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon-wrap">🏡</div>
                    <div class="ci-text">
                        <strong>Project Site Office</strong>
                        Aranya Farms, Achampet Village,<br>
                        Toopran Mandal, Medchal-Malkajgiri
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon-wrap">📞</div>
                    <div class="ci-text">
                        <strong>Phone / WhatsApp</strong>
                        +91 96402 22237
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon-wrap">📧</div>
                    <div class="ci-text">
                        <strong>Email</strong>
                        info@silveroaksrealty.com<br>
                        aranyafarms@silveroaks.in
                    </div>
                </div>

                <div class="contact-line">
                    <div class="ci-icon-wrap">⏰</div>
                    <div class="ci-text">
                        <strong>Office Hours</strong>
                        Mon – Sat: 9:00 AM – 7:00 PM<br>
                        Sunday: 10:00 AM – 5:00 PM
                    </div>
                </div>

                <div style="margin-top:6px;padding:16px;background:rgba(201,168,76,0.08);
                            border-radius:10px;border:1px solid rgba(201,168,76,0.18);">
                    <p style="color:rgba(255,255,255,0.55);font-size:0.82rem;line-height:1.75;margin:0;">
                        🌿 Site visits available 7 days a week.<br>
                        Complimentary pickup from Kompally for groups of 4+.
                    </p>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── ADMIN SECTION ──
    render_admin_section()
# ═══════════════════════════════════════════════════════════════════════════
def render_footer():
    st.markdown("""
    <div class="footer">
        <div style="display:grid;grid-template-columns:2.2fr 1fr 1fr 1.2fr;gap:52px;margin-bottom:0;">
            <div>
                <div class="footer-logo">🌿 Aranya Farms</div>
                <div class="footer-tagline">Play · Live · Celebrate</div>
                <p style="color:rgba(255,255,255,0.38);font-size:0.84rem;line-height:1.9;
                          max-width:300px;font-weight:300;">
                    A premium gated farmland community by Silver Oaks Agro Farms, set across
                    55 acres of lush greenery at Achampet, Toopran, Telangana.
                </p>
                <div style="margin-top:24px;display:flex;gap:10px;">
                    <a href="https://wa.me/919640222237" target="_blank"
                       style="width:36px;height:36px;border-radius:50%;background:rgba(37,211,102,0.15);
                              border:1px solid rgba(37,211,102,0.3);display:flex;align-items:center;
                              justify-content:center;font-size:1rem;text-decoration:none;">💬</a>
                    <a href="tel:+919640222237"
                       style="width:36px;height:36px;border-radius:50%;background:rgba(201,168,76,0.1);
                              border:1px solid rgba(201,168,76,0.25);display:flex;align-items:center;
                              justify-content:center;font-size:1rem;text-decoration:none;">📞</a>
                    <a href="mailto:info@silveroaksrealty.com"
                       style="width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.05);
                              border:1px solid rgba(255,255,255,0.12);display:flex;align-items:center;
                              justify-content:center;font-size:1rem;text-decoration:none;">📧</a>
                </div>
            </div>
            <div>
                <p style="color:var(--gold-light);font-family:'Cinzel',serif;font-size:0.65rem;
                          letter-spacing:3px;text-transform:uppercase;margin-bottom:20px;">Pages</p>
                <p style="color:rgba(255,255,255,0.4);font-size:0.87rem;line-height:2.6;font-weight:300;">
                    Home<br>About<br>Properties<br>Location<br>Contact
                </p>
            </div>
            <div>
                <p style="color:var(--gold-light);font-family:'Cinzel',serif;font-size:0.65rem;
                          letter-spacing:3px;text-transform:uppercase;margin-bottom:20px;">Properties</p>
                <p style="color:rgba(255,255,255,0.4);font-size:0.87rem;line-height:2.6;font-weight:300;">
                    Farm Plots<br>3-BHK Farm Houses<br>Premium Villas<br>Farm Lands<br>Book Site Visit
                </p>
            </div>
            <div>
                <p style="color:var(--gold-light);font-family:'Cinzel',serif;font-size:0.65rem;
                          letter-spacing:3px;text-transform:uppercase;margin-bottom:20px;">Contact</p>
                <p style="color:rgba(255,255,255,0.4);font-size:0.87rem;line-height:2.0;font-weight:300;">
                    +91 96402 22238<br>
                    info@silveroaksrealty.com<br><br>
                    <span style="font-size:0.8rem;">Mon–Sat: 9AM – 7PM</span><br>
                    <span style="font-size:0.8rem;">Sunday: 10AM – 5PM</span>
                </p>
            </div>
        </div>
        <hr class="footer-divider">
        <div class="footer-copy">
            © 2024 Aranya Farms by Silver Oaks Agro Farms · Silver Oaks Realty · Hyderabad, Telangana<br>
            <span style="font-size:0.7rem;opacity:0.55;">
                All dimensions and prices are indicative and subject to change. Please contact our sales team for current pricing and availability.
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── MAIN ───────────────────────────────────────────────────────────────────
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


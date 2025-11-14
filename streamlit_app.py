import streamlit as st
import base64
import os
from app_sections import the_gift, the_guide, Cam


# Configurazione pagina
st.set_page_config(
    page_title="Happy Birthday Cam",
    page_icon="🎂",
    layout="centered"
)

# ---- Funzione per convertire la foto in base64 ----
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# Percorso della foto
image_path = os.path.join("images", "cam.png")
image_base64 = get_base64_image(image_path)

# ---- SIDEBAR: MENU A TENDINA ----
st.sidebar.markdown("### 🤍 Cam's B. Day")
page = st.sidebar.selectbox(
    "Navigate the menu:",
    ["Home", "The Gift", "The Guide", "Cam"],
)

# ---- CSS GLOBALE ----
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap" rel="stylesheet">

<style>
    .stApp {
        background: linear-gradient(135deg, #e6fff4, #c8f7e3, #a8e6cf, #74c69d);
        background-size: 400% 400%;
        animation: gradientMove 14s ease infinite;
        font-family: 'Quicksand', sans-serif;
    }

    @keyframes gradientMove {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .hero-container {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 4rem;
        margin-bottom: 2rem;
    }

    .hero-card {
        background: rgba(255, 255, 255, 0.86);
        border-radius: 32px;
        padding: 3rem 3.5rem 2.2rem 3.5rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        text-align: center;
        max-width: 750px;
        backdrop-filter: blur(8px);
        animation: fadeIn 1.4s ease-out;
    }

    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(15px);}
        100% {opacity: 1; transform: translateY(0);}
    }

    .hero-badge {
        display: inline-block;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        background: rgba(64, 145, 108, 0.15);
        color: #1b4332;
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 1.2rem;
        font-weight: 600;
    }

    .hero-title {
        font-size: 3.1rem;
        line-height: 1.1;
        margin-bottom: 1rem;
        color: #1b4332;
        font-weight: 700;
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #2b6b4a;
        margin-bottom: 0.8rem;
        font-weight: 500;
    }

    .hero-body {
        font-size: 1rem;
        color: #3f7054;
        margin-top: 0.9rem;
        line-height: 1.6;
    }

    .hero-photo {
        margin-top: 1.0rem;
        border-radius: 24px;
        max-width: 100%;
        height: auto;
        box-shadow: 0 12px 32px rgba(0,0,0,0.18);
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1b4332;
        margin-top: 3rem;
        margin-bottom: 0.5rem;
        text-align: left;
    }

    .section-sub {
        color: #2b6b4a;
        margin-bottom: 1.5rem;
        font-size: 0.98rem;
        text-align: left;
    }

    .dest-card {
        background: rgba(255,255,255,0.88);
        border-radius: 20px;
        padding: 0.8rem 0.9rem 1rem 0.9rem;
        box-shadow: 0 8px 18px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 0.95rem;
        color: #2b6b4a;
        margin-bottom: 1.5rem;
    }

    .dest-title {
        font-weight: 700;
        margin-top: 0.4rem;
        margin-bottom: 0.2rem;
        color: #1b4332;
    }

    .dest-text {
        font-size: 0.85rem;
    }

    @media (max-width: 600px) {
        .hero-card {
            padding: 2.2rem 1.6rem 1.8rem 1.6rem;
            margin: 0 1rem;
        }
        .hero-title {
            font-size: 2.3rem;
        }
        .hero-subtitle {
            font-size: 1.1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ---- FUNZIONE PER LA HOME ----
def render_home():
    st.markdown(f"""
    <div class="hero-container">
        <div class="hero-card">
            <div class="hero-badge">
                • A gift from Cecilia •
            </div>
            <div class="hero-title">
                HAPPY BIRTHDAY CAM!
            </div>
            <div class="hero-subtitle">
                May your 27th year be as stunning as the sunsets you have shared with me
            </div>
            <img src="data:image/png;base64,{image_base64}" class="hero-photo" />
        </div>
    </div>
    """, unsafe_allow_html=True)


    # Citazione sotto la card, fuori dal box bianco
    st.markdown("""
        <p style="margin-top:1.5rem; font-style:italic; text-align:center; color:#000000;">
            Amor, ch’a nullo amato amar perdona.<br>
            - Dante Alighieri (Inferno, V)
        </p>
        """, unsafe_allow_html=True)

# ---- LOGICA PAGINE ----
if page == "Home":
    render_home()
elif page == "The Gift":
    the_gift.render()
elif page == "The Guide":
    the_guide.render()
elif page == "Cam":
    Cam.render()
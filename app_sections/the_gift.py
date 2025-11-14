# pages/the_gift.py
import streamlit as st
import os
import base64

def _get_base64_image(path: str) -> str:
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def render():
    # Stato per mostrare / nascondere i dettagli dopo il click
    if "show_gift_details" not in st.session_state:
        st.session_state["show_gift_details"] = False

    # CSS extra
    st.markdown("""
    <style>
        .dest-img {
            width: 100%;
            height: 220px;          /* stessa altezza per tutte */
            object-fit: cover;      /* ritaglia l'immagine mantenendo il focus */
            border-radius: 18px;
            display: block;
        }
        .dest-text-black {
            color: #000000;
        }
        .final-text-black {
            color: #000000;
            font-style: italic;
        }
    </style>
    """, unsafe_allow_html=True)

    # ---------- CARD BIANCA "THE GIFT" ----------
    st.markdown("""
    <div class="hero-container">
        <div class="hero-card">
            <div class="hero-badge">
                Limited edition offer
            </div>
            <div class="hero-title">
                THE GIFT 🎁
            </div>
            <div class="hero-subtitle">
                A magical weekend together, designed just for you.
            </div>
            <div class="hero-body">
    Think red rocks and desert skies, or ocean waves and city skylines,<br>
    all with good Italian music in the background (don’t worry, Kali Uchis will join us too),<br>
    too many photos, good food, cuddles, and those embarrassing moments<br>
    where I can’t quite explain myself and just mumble nonsense in English.<br><br>
    This is your birthday gift: a weekend away together,<br>
    planned around whatever makes you feel most alive and at peace.<br><br>
    No pressure, no rush: just you and me.
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- BOTTONE "I'M IN" ----------
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("I'm in 💚"):
            st.session_state["show_gift_details"] = True
            st.balloons()  # 🎈

    if not st.session_state["show_gift_details"]:
        return
    
    

    # Messaggio nero dopo il click
    st.markdown(
        "<p style='text-align:center; color:#000000; font-weight:600; margin-top:0.5rem;'>"
        "Perfect. Then it's a date. 🌵✨"
        "</p>",
        unsafe_allow_html=True
    )

    # ---------- SEZIONE DETTAGLI ----------
    st.markdown(
        '<div class="section-title">Let’s find out what this is all about! </div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-sub">'
        "The destination can change depending on the birthday girl\'s mood. "
        "Some options (just to start dreaming) are:"
        '</div>',
        unsafe_allow_html=True
    )

    # Percorsi immagini (cartella 'images' nella root del progetto)
    img_south_utah = _get_base64_image(os.path.join("images", "southutah.jpg"))
    img_west      = _get_base64_image(os.path.join("images", "west.png"))
    img_arizona   = _get_base64_image(os.path.join("images", "arizona.jpg"))
    img_nevada    = _get_base64_image(os.path.join("images", "nevada.jpg"))
    img_colorado  = _get_base64_image(os.path.join("images", "colorado.png"))

    cols = st.columns(3)

    with cols[0]:
        st.markdown(
            f"""
            <div class="dest-card">
                <img src="data:image/jpeg;base64,{img_south_utah}" class="dest-img" />
                <div class="dest-title">Southern Utah</div>
                <div class="dest-text dest-text-black">
                    Red rocks, desert sunsets, and starry nights. 🌵
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with cols[1]:
        st.markdown(
            f"""
            <div class="dest-card">
                <img src="data:image/png;base64,{img_west}" class="dest-img" />
                <div class="dest-title">West Coast</div>
                <div class="dest-text dest-text-black">
                    Ocean breeze, coastal walks, and cozy city corners. 🌊
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with cols[2]:
        st.markdown(
            f"""
            <div class="dest-card">
                <img src="data:image/jpeg;base64,{img_arizona}" class="dest-img" />
                <div class="dest-title">Arizona</div>
                <div class="dest-text dest-text-black">
                    Canyons, desert roads, and heart-melting sunsets. 🧡
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    cols2 = st.columns(2)

    with cols2[0]:
        st.markdown(
            f"""
            <div class="dest-card">
                <img src="data:image/jpeg;base64,{img_nevada}" class="dest-img" />
                <div class="dest-title">Nevada</div>
                <div class="dest-text dest-text-black">
                    Desert highways and maybe a touch of Vegas. 🎲
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with cols2[1]:
        st.markdown(
            f"""
            <div class="dest-card">
                <img src="data:image/png;base64,{img_colorado}" class="dest-img" />
                <div class="dest-title">Colorado</div>
                <div class="dest-text dest-text-black">
                    Mountains, fresh air, and slow scenic days. 🏔️
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "<br><span class='final-text-black'>"
        "The final destination will simply depend on whatever makes you smile the most"
        "</span>",
        unsafe_allow_html=True
    )

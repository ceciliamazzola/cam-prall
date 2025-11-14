# pages/cam.py
import streamlit as st
import os
import base64

def _get_base64_image(path: str) -> str:
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def render():
    # Stato per mostrare / nascondere il quiz dopo il click
    if "show_cam_quiz" not in st.session_state:
        st.session_state["show_cam_quiz"] = False

    # CSS extra (testo nero)
    st.markdown("""
    <style>
        .cam-text-black {
            color: #000000;
        }
        body, .stApp, p, label, .section-title, .section-sub {
            color: #000000 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # ---------- CARD BIANCA "CAM" ----------
    st.markdown("""
    <div class="hero-container">
        <div class="hero-card">
            <div class="hero-badge">
                Compatibility check (very scientific)
            </div>
            <div class="hero-title">
                CAM – Cute Answer Machine 💭
            </div>
            <div class="hero-subtitle">
                Tiny questions, big clues about your heart, your brain, and your future adventures.
            </div>
            <div class="hero-body">
    Answer honestly. Your answers may or may not be used to plan suspiciously perfect dates, playlists, road trips,  and a slightly ridiculous amount of cuddles.<br><br>
    No grades, no wrong answers: just your vibes on record.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- BOTTONE "LET'S PLAY" ----------
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Okay, let's play 💚"):
            st.session_state["show_cam_quiz"] = True
            st.balloons()  # 🎈

    if not st.session_state["show_cam_quiz"]:
        return

    # ---------- 1. ABOUT YOU (HER SECTION) ----------
    st.markdown(
        '<div class="section-title cam-text-black">1 · About you (tiny autobiography) ✨</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-sub cam-text-black">'
        "Just a few questions all about you – little pieces of your story."
        '</div>',
        unsafe_allow_html=True
    )

    # 1a) Town where she was born
    st.markdown(
        '<p class="cam-text-black"><b>The town where you were born is called...</b></p>',
        unsafe_allow_html=True
    )
    city = st.text_input(
        "Town of birth",
        key="cam_birth_city",
        label_visibility="collapsed",
        placeholder="Write the town name here..."
    )
    if city:
        st.success(f"Saved! You wrote: **{city}** 💌")

    # 1b) Childhood memory
    st.markdown(
        '<p class="cam-text-black" style="margin-top:1rem;"><b>'
        "If you think about your childhood, what’s the very first memory that comes to mind?"
        "</b></p>",
        unsafe_allow_html=True
    )
    childhood = st.text_area(
        "Childhood memory",
        key="cam_childhood_memory",
        label_visibility="collapsed",
        placeholder="A place, a smell, a person, a tiny moment…",
        height=120
    )

    # 1c) Three words
    st.markdown(
        '<p class="cam-text-black" style="margin-top:1rem;"><b>'
        "If you had to describe yourself in three words, what would they be?"
        "</b></p>",
        unsafe_allow_html=True
    )
    three_words = st.text_input(
        "Three words",
        key="cam_three_words",
        label_visibility="collapsed",
        placeholder="Soft chaos? Golden retriever energy? Your choice. 😌"
    )

    # 1d) Small thing that makes her feel better
    st.markdown(
        '<p class="cam-text-black" style="margin-top:1rem;"><b>'
        "What’s a small thing that never fails to make you feel at least a little bit better?"
        "</b></p>",
        unsafe_allow_html=True
    )
    tiny_comfort = st.text_area(
        "Tiny comfort",
        key="cam_tiny_comfort",
        label_visibility="collapsed",
        placeholder="A song, a drink, a person, a hug, a walk…",
        height=120
    )

    
    # ---------- 2. WOULD YOU RATHER (TRAVEL / VIBES) ----------
    st.markdown(
        '<div class="section-title cam-text-black">2 · Would you rather… (travel edition) ✈️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="cam-text-black"><b>Would you rather:</b></p>',
        unsafe_allow_html=True
    )
    q1 = st.radio(
        "Beach or mountain",
        ["Beach day", "Mountain hike"],
        key="cam_beach_mountain",
        index=None,
        label_visibility="collapsed"
    )
    st.caption("(*Have you ever even properly been to the sea? No, right? Omg? 😱*)")

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "For food forever, you’d choose:"
        "</b></p>",
        unsafe_allow_html=True
    )
    q2 = st.radio(
        "Sweet or salty",
        ["Sweet", "Savory", "I refuse to choose, I want both"],
        key="cam_sweet_salty",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "On a random Friday night you’d prefer:"
        "</b></p>",
        unsafe_allow_html=True
    )
    q3 = st.radio(
        "Friday vibe",
        [
            "Movie night on the couch",
            "Going out dancing",
            "Board games & snacks",
            "Spontaneous late-night drive"
        ],
        key="cam_friday_vibe",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "Sleep schedule energy:"
        "</b></p>",
        unsafe_allow_html=True
    )
    q4 = st.radio(
        "Sleep energy",
        ["Early bird", "Night owl", "Chaotic neutral (depends on the day)"],
        key="cam_sleep_type",
        index=None,
        label_visibility="collapsed"
    )

    # --- extra wild questions ---
    st.markdown(
        '<p class="cam-text-black" style="margin-top:1.0rem;"><b>'
        "For a weekend, you’d rather:"
        "</b></p>",
        unsafe_allow_html=True
    )
    q5 = st.radio(
        "Wild vs spa",
        [
            "Sleep in the car on a chaotic, wild road trip",
            "Have a slow, relaxing weekend in a spa hotel"
        ],
        key="cam_wild_vs_spa",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "If you had to give up one forever (I’m sorry):"
        "</b></p>",
        unsafe_allow_html=True
    )
    q6 = st.radio(
        "Give up food",
        [
            "Pickles",
            "Pizza",
            "Peanut butter",
            "I refuse this question and I walk out"
        ],
        key="cam_food_sacrifice",
        index=None,
        label_visibility="collapsed"
    )

    # commento speciale per la risposta "walk out"
    if q6 == "I refuse this question and I walk out":
        st.warning("Danger zone detected. Someone clearly cares a *little too much* about food. 😈🍕")

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
            "For a whole day, you’d rather:"
        "</b></p>",
        unsafe_allow_html=True
    )
    q7 = st.radio(
        "Weird day",
        [
            "Speak only in Italian",
            "Speak only in memes and random sounds",
            "Whisper everything",
            "Talk in that weird half-whisper people use when they argue in a library"
        ],
        key="cam_weird_day",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "Travel style you secretly vibe with more:"
        "</b></p>",
        unsafe_allow_html=True
    )
    q8 = st.radio(
        "Travel style",
        [
            "No plan, just vibes and see what happens",
            "Detailed spreadsheet, schedule and backup plans",
            "I say I’m chill but I actually like having a soft plan",
        ],
        key="cam_travel_style",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "If you could go back to one period of your life, which one would you choose?"
        "</b></p>",
        unsafe_allow_html=True
    )
    q9 = st.radio(
        "Life period",
        [
            "Elementary school",
            "High school",
            "College / university",
            "Right now"
        ],
        key="cam_life_period",
        index=None,
        label_visibility="collapsed"
    )

    # commento speciale per "Right now"
    if q9 == "Right now":
        st.success("This is the only acceptable answer. 😌✨")

    st.markdown("---")

    # ---------- 3. TINY PERSONALITY QUIZ ----------
    st.markdown(
        '<div class="section-title cam-text-black">3 · Tiny personality scan 🔍</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="cam-text-black"><b>Which one sounds more like you?</b></p>',
        unsafe_allow_html=True
    )
    q5 = st.radio(
        "Personality style",
        [
            "I overthink everything but still somehow wing it",
            "I pretend to be chill but I have 47 feelings per minute",
            "I’m actually organised (like… with lists and calendars and stuff)",
            "Chaos but cute"
        ],
        key="cam_personality",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "Ideal cuddle weather:"
        "</b></p>",
        unsafe_allow_html=True
    )
    q6 = st.radio(
        "Cuddle weather",
        [
            "Thunderstorm outside, soft lights inside",
            "Snowy day, big blanket, hot drink",
            "Summer night with windows open and distant noises",
            "Honestly, any weather is cuddle weather"
        ],
        key="cam_cuddle_weather",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown("---")

    # ---------- 4. IDEAL WEEKEND DAY ----------
    st.markdown(
        '<div class="section-title cam-text-black">4 · Your ideal weekend ☀️</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-sub cam-text-black">'
        "Describe a perfect day during the weekend, with zero responsibilities."
        '</div>',
        unsafe_allow_html=True
    )

    ideal_day = st.text_area(
        "Ideal weekend",
        key="cam_ideal_weekend",
        label_visibility="collapsed",
        placeholder="Slow morning? Road trip? Picnic? Movies? Mountains? Tell me everything... 🫶",
        height=180
    )

    if ideal_day.strip():
        st.info("Noted. This may or may not inspire future plans. 😌")

    st.markdown("---")

    # ---------- 5. RAPID FIRE PREFERENCES ----------
    st.markdown(
        '<div class="section-title cam-text-black">5 · Rapid fire preferences ⚡</div>',
        unsafe_allow_html=True
    )

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            '<p class="cam-text-black"><b>Dream companion:</b></p>',
            unsafe_allow_html=True
        )
        pet = st.radio(
            "Pet",
            ["Dog", "Cat", "Both", "Something chaotic like a raccoon"],
            key="cam_pet",
            index=None,
            label_visibility="collapsed"
        )

    with col_right:
        st.markdown(
            '<p class="cam-text-black"><b>Comfort drink:</b></p>',
            unsafe_allow_html=True
        )
        drink = st.radio(
            "Drink",
            ["Coffee", "Tea", "Hot chocolate", "Sparkling water girlie"],
            key="cam_drink",
            index=None,
            label_visibility="collapsed"
        )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "Movie snack of choice:"
        "</b></p>",
        unsafe_allow_html=True
    )
    snack = st.radio(
        "Snack",
        ["Popcorn", "Chocolate", "Chips", "Pizza slice", "All of the above"],
        key="cam_snack",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown(
        '<p class="cam-text-black" style="margin-top:0.8rem;"><b>'
        "Music in the car:"
        "</b></p>",
        unsafe_allow_html=True
    )
    music = st.radio(
        "Car music",
        [
            "Screaming all the lyrics dramatically",
            "Soft songs & deep talks",
            "Random playlist chaos",
            "Podcasts & existential crises"
        ],
        key="cam_music",
        index=None,
        label_visibility="collapsed"
    )

    st.markdown("---")

# ---------- 6. CURRENT MOOD SLIDER ----------
    st.markdown(
        '<div class="section-title cam-text-black">6 · Mood check right now 🫣 → 🤩</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-sub cam-text-black">'
        'On a scale from “embarrassed” to “excited / happy”, where are you right now?'
        '</div>',
        unsafe_allow_html=True
    )

    mood = st.slider(
        "Mood slider",
        min_value=0,
        max_value=100,
        value=50,
        key="cam_mood",
        label_visibility="collapsed"
    )

    st.markdown(
        "<div style='display:flex; justify-content:space-between; color:#000000; font-size:0.9rem;'>"
        "<span>Embarrassed</span>"
        "<span>Excited / happy</span>"
        "</div>",
        unsafe_allow_html=True
    )

    if mood >= 65:
        st.success("DAJEEEE 🤩")
    elif mood <= 35:
        st.info("I know, this is all a bit too much… and you haven’t even seen the next question yet. 😈")

    st.markdown("---")


    # ---------- 7. ITALY QUESTION ----------
    st.markdown(
        '<div class="section-title cam-text-black">7 · Important: Italy plans 🇮🇹</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="section-sub cam-text-black">'
        'When do you want to come to Italy with me?'
        '</div>',
        unsafe_allow_html=True
    )

    italy_choice = st.radio(
        "Choose your destiny:",
        ["March", "April", "May", "June", "This is madness"],
        key="cam_italy_month",
        index=None,
        label_visibility="visible"
    )

    if italy_choice is not None:
        if italy_choice == "This is madness":
            st.markdown(
                "<p class='cam-text-black'>"
                "Absolutely yes, but isn’t it exactly this kind of madness that makes life make sense?!"
                "</p>",
                unsafe_allow_html=True
            )
        else:
            st.success("Perfect. Your personal travel planner will organise the trip as soon as humanly possible. ✈️")

    # ---------- FOOTER ----------
    st.markdown("---")
    st.markdown(
        "<span class='cam-text-black'><i>"
        "This page doesn’t judge you. It just quietly collects data to know you better. 💌"
        "</i></span>",
        unsafe_allow_html=True
    )

import streamlit as st
import time
import random
import json
from typing import List, Dict
from datetime import datetime

# Constants
LOVELY_COLORS = {
    'primary': '#FF1493',
    'secondary': '#FF69B4',
    'background': '#FFF0F5',
    'border': '#FFB6C1',
    'accent': '#FF1493'
}

NO_BUTTON_RESPONSES = [
    "🔥 Playing hard to get? I like that...",
    "😏 That's not what your eyes are saying...",
    "💋 Are you sure? I can be very persuasive...",
    "😈 The 'No' button is just foreplay...",
    "🎭 Testing me? Two can play that game...",
    "✨ Your resistance only makes me want you more...",
    "💝 I love it when you're feisty...",
    "🌙 The night is young, and so are we...",
    "🎪 This button is just for show, like your hesitation...",
    "🎯 Missing on purpose? I can help with your aim...",
    "🌟 Being naughty? Santa's watching... but I won't tell 😘",
    "🎨 This button is as resistible as I am... not at all!",
    "💫 Your mouse seems to have slipped... like my intentions 😏"
]

ROMANTIC_MESSAGES = [
    "I've been thinking about you... probably more than I should 😏",
    "You make my heart race in all the right ways... 💓",
    "Just seeing you makes me feel... things 😘",
    "Ready for a Valentine's Day you won't forget? 😉",
    "They say good things come to those who wait... 💋",
    "I promise to make it worth your while... 😈",
    "Let's make this Valentine's Day memorable... 🔥",
    "I've got some special plans in mind... 💝"
]

REASONS_TO_SAY_YES = [
    "I know exactly how to make you smile... and other things 😏",
    "We have the kind of chemistry that sets off fireworks 🎆",
    "I promise to keep you up all night... talking, of course 😉",
    "Our adventures together are always... exciting 💫",
    "I know all your favorite spots... to get coffee ☕",
    "We make magic together in more ways than one ✨",
    "I love the way you bite me for no reason :)",
    "Our 'Netflix and chill' sessions are legendary 📺",
    "You bring out my wild side 🐯",
    "I know exactly what you like... for dinner 🍽️",
    "We're both thinking the same thing right now 💭",
    "I promise to keep you... entertained 🎭"
]

VALENTINE_FACTS = [
    "In Ancient Rome, Valentine's Day celebrations lasted all night long... for good luck, of course 😏",
    "Chocolate releases the same chemicals as... intense exercise 💦",
    "The Victorians had secret messages in their Valentine's cards... quite spicy ones actually 🔥",
    "Red roses aren't the only things that get hearts racing on Valentine's Day 💓",
    "Some cultures celebrate Valentine's Day with breakfast... the morning after 😘",
    "They say kissing burns calories... want to work out? 💋",
    "Champagne isn't the only thing that gets bubbly on Valentine's Day 🍾",
    "The heart isn't the only organ affected by love... your brain gets quite excited too 🧠",
    "Historical fact: Valentine's Day was once celebrated in bedchambers... for tradition! 🛏️",
    "Studies show couples who play together... stay together 😈"
]

MEMORIES = [
    "Remember our first glance? The spark was undeniable... 👀",
    "That time we couldn't stop laughing... about everything 😆",
    "Our late-night conversations that never seemed to end... 🌙",
    "The way you make my heart race every time... 💓",
    "All those 'accidental' touches that weren't so accidental... 😏"
]

QUIZ_QUESTIONS = {
    "What's your ideal date night?": [
        "Netflix and... chill 😏",
        "Romantic dinner 🍷",
        "Adventure together 🌟",
        "Dancing all night 💃"
    ],
    "What's your love language?": [
        "Physical Touch 💋",
        "Words of Affirmation 💝",
        "Quality Time 🌙",
        "Giving Gifts 🎁"
    ],
    "What's your idea of perfect romance?": [
        "Spontaneous and wild 🔥",
        "Sweet and tender 💕",
        "Playful and fun 😋",
        "Deep and passionate 💘"
    ]
}


def load_custom_css():
    """Load custom CSS styles for the app."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&display=swap');

        .title-font {
            font-size: 3.5rem !important;
            font-weight: bold;
            text-align: center;
            color: """ + LOVELY_COLORS['primary'] + """;
            margin-bottom: 2rem;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.1);
            animation: float 3s infinite ease-in-out;
            font-family: 'Dancing Script', cursive;
        }

        .message-font {
            font-size: 1.75rem !important;
            text-align: center;
            color: #333;
            margin: 1.25rem 0;
            animation: fadeIn 1.5s ease-in;
            font-family: 'Dancing Script', cursive;
        }

        .stButton>button {
            background-color: """ + LOVELY_COLORS['secondary'] + """;
            color: white;
            border-radius: 25px;
            padding: 0.75rem 2rem;
            font-size: 1.2rem;
            border: none;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }

        .content-box {
            background-color: """ + LOVELY_COLORS['background'] + """;
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            border: 2px solid """ + LOVELY_COLORS['border'] + """;
            animation: fadeIn 1s ease-in;
        }

        .memory-book {
            background: #fff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin: 2rem 0;
        }

        .page {
            background: #fffaf0;
            padding: 1.5rem;
            border-radius: 5px;
            margin: 1rem 0;
            transform-origin: center left;
            transition: transform 0.5s ease;
        }

        .page:hover {
            transform: rotateY(10deg);
        }

        .mood-selector {
            background: """ + LOVELY_COLORS['background'] + """;
            padding: 1rem;
            border-radius: 15px;
            margin: 1rem 0;
            text-align: center;
            border: 2px dashed """ + LOVELY_COLORS['border'] + """;
        }

        .custom-message {
            font-family: 'Dancing Script', cursive;
            font-size: 1.5rem;
            color: """ + LOVELY_COLORS['primary'] + """;
            text-align: center;
            margin: 1rem 0;
        }

        .special-message {
            font-size: 1.2rem;
            color: """ + LOVELY_COLORS['accent'] + """;
            text-align: center;
            margin: 1rem 0;
            padding: 1rem;
            border: 2px dashed """ + LOVELY_COLORS['border'] + """;
            border-radius: 10px;
            animation: pulse 2s infinite;
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        </style>
    """, unsafe_allow_html=True)


def calculate_love_percentage():
    """Calculate a 'love percentage' based on various factors."""
    current_time = datetime.now()
    factors = [
        random.randint(85, 100),  # Base attraction
        current_time.second % 20 + 80,  # Time-based factor
        random.randint(90, 100)  # Random chemistry
    ]
    return sum(factors) / len(factors)


def display_love_meter():
    """Display an animated love meter."""
    love_percentage = calculate_love_percentage()
    st.markdown("""
        <div class="content-box">
            <h3 style='text-align:center;'>💘 Love Meter 💘</h3>
            <div class="love-meter">
                <div class="love-meter-fill" style="width: {}%;"></div>
            </div>
            <p style='text-align:center;'>Chemistry Level: {:.1f}%</p>
        </div>
    """.format(love_percentage, love_percentage), unsafe_allow_html=True)


def display_special_message():
    """Display a special personalized message."""
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        time_message = "Good morning, gorgeous! Ready for breakfast in bed? ☀️"
    elif 12 <= current_hour < 17:
        time_message = "Afternoon delight? I mean... hello! 🌸"
    elif 17 <= current_hour < 22:
        time_message = "The night is young, and so are we... 🌙"
    else:
        time_message = "Late night thoughts keeping you up too? ✨"

    st.markdown(f"""
        <div class="special-message">
            {time_message}<br>
            You make my imagination run wild! 💖
        </div>
    """, unsafe_allow_html=True)


def display_typewriter_messages(messages: List[str], delay: float = 0.5):
    """Display messages with a typewriter effect."""
    for msg in messages:
        st.markdown(f'<p class="message-font">{msg}</p>', unsafe_allow_html=True)
        time.sleep(delay)


def create_memory_book():
    """Create an interactive memory book section."""
    st.markdown("""
        <div class="memory-book">
            <h3 style='text-align:center; color:""" + LOVELY_COLORS['primary'] + """'>
                📖 Our Story So Far... 📖
            </h3>
    """, unsafe_allow_html=True)

    for memory in MEMORIES:
        st.markdown(f"""
            <div class="page">
                {memory}
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def create_mood_selector():
    """Create an interactive mood selector."""
    st.markdown("""
        <div class="mood-selector">
            <h3>Set the Mood 🌟</h3>
        </div>
    """, unsafe_allow_html=True)

    mood = st.select_slider(
        "How spicy are you feeling?",
        options=["Mild 😊", "Flirty 😏", "Spicy 🔥", "Extra Spicy 🌶️"],
        value="Flirty 😏"
    )

    return mood


def create_custom_message_section():
    """Create a section for custom messages."""
    st.markdown("<div class='custom-message'>", unsafe_allow_html=True)

    message_type = st.selectbox(
        "Choose your message style:",
        ["Sweet & Romantic 💝", "Playful & Flirty 😏", "Hot & Spicy 🔥"]
    )

    custom_message = st.text_area(
        "Add your personal touch:",
        placeholder="Write something special..."
    )

    if st.button("💌 Send Love Note"):
        if custom_message:
            st.success("Message sent with love! 💘")
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)


def create_love_quiz():
    """Create an interactive love quiz."""
    st.markdown("""
        <div class="content-box">
            <h3 style='text-align:center'>💘 Love Connection Quiz 💘</h3>
        </div>
    """, unsafe_allow_html=True)

    quiz_answers = {}
    for question, options in QUIZ_QUESTIONS.items():
        quiz_answers[question] = st.radio(question, options)

    if st.button("💘 Calculate Our Chemistry"):
        compatibility = random.randint(85, 100)
        st.success(f"Our chemistry is off the charts! {compatibility}% compatible! 🔥")
        st.balloons()


def display_reasons_section():
    """Display the reasons section with animation."""
    st.markdown("""
        <div class="content-box">
            <h3 style='text-align:center; color:""" + LOVELY_COLORS['primary'] + """'>
                ✨ Why We Would Be Perfect Together ✨
            </h3>
            <ul style='font-size:1.1rem; margin:1.25rem 0;'>
    """, unsafe_allow_html=True)

    for reason in random.sample(REASONS_TO_SAY_YES, 5):
        st.markdown(f"<li>{reason}</li>", unsafe_allow_html=True)

    st.markdown("</ul></div>", unsafe_allow_html=True)


def display_valentine_facts():
    """Display random Valentine's Day facts."""
    st.markdown("""
        <div class="content-box" style='background-color:#FFE4E1'>
            <h3 style='text-align:center; color:""" + LOVELY_COLORS['primary'] + """'>
                🌟 Sweet Valentine's Facts 🌟
            </h3>
            <ul style='font-size:1.1rem; margin:1.25rem 0;'>
    """, unsafe_allow_html=True)

    for fact in random.sample(VALENTINE_FACTS, 4):
        st.markdown(f"<li>{fact}</li>", unsafe_allow_html=True)


def main():
    # Page configuration
    st.set_page_config(
        page_title="Be My Valentine? 💝",
        page_icon="💝",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    load_custom_css()

    # Header with floating hearts animation
    st.markdown("""
        <div class="title-font">
            ❤️ Will You Be My Valentine? ❤️
        </div>
    """, unsafe_allow_html=True)

    # Display special personalized message
    display_special_message()

    # Introduction messages
    display_typewriter_messages(random.sample(ROMANTIC_MESSAGES, 3))

    # Love Meter
    display_love_meter()

    # Main proposal section
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if "proposal_clicked" not in st.session_state:
            st.session_state.proposal_clicked = False

        if st.button("💝 Open Your Valentine's Message 💝", key="main_button") or st.session_state.proposal_clicked:
            st.session_state.proposal_clicked = True
            st.balloons()
            st.markdown(
                '<p class="title-font" style="font-size:2.5rem !important;">'
                'Will you make me the happiest person and be my Valentine?</p>',
                unsafe_allow_html=True
            )

            # Create two columns for the Yes and No buttons
            col_yes, col_no = st.columns(2)

            with col_yes:
                yes_clicked = st.button("Yes! 💖", key="yes_button")
            with col_no:
                no_clicked = st.button("No 😢", key="no_button")

            # Now, outside the button row, display the message in a new row if Yes is clicked
            if yes_clicked:
                st.snow()
                st.markdown(
                    """
                    <div class="content-box" style="background-color: #FFE4E1; text-align: center; padding: 2rem; margin: 1.5rem 0;">
                        <h2 style="color: #FF1493; font-size: 2.2rem; margin-bottom: 1.5rem; font-family: 'Dancing Script', cursive;">
                            🎉 You've Made My Day! 🎉
                        </h2>
                        <div style="margin: 2rem 0;">
                            <p style="font-size: 1.4rem; color: #333; margin-bottom: 1rem;">
                                Get ready for the most magical Valentine's ever! ✨
                            </p>
                            <p style="font-size: 1.2rem; color: #666; font-style: italic;">
                                Every moment with you is going to be absolutely amazing! 💫
                            </p>
                        </div>
                        <div style="margin-top: 1.5rem;">
                            <span style="font-size: 1.8rem;">💝 💖 💕</span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            if no_clicked:
                st.markdown(random.choice(NO_BUTTON_RESPONSES))

    # Additional sections with improved styling
    if st.checkbox("💫 Why You Should Say Yes! 💫"):
        display_reasons_section()

    if st.button("💝 Discover Valentine's Magic! 💝"):
        display_valentine_facts()

    # Footer with pulsing heart
    st.markdown("---")
    st.markdown("""
        <p style="text-align:center; font-size:1rem; color:""" + LOVELY_COLORS['secondary'] + """">
            Created with 💖 and endless hope<br>
            <span style="font-size:0.8rem;">Every click brings us closer together</span>
        </p>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

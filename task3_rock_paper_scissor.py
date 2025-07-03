import streamlit as st
import random

st.set_page_config(page_title="Rock-Paper-Scissors", layout="centered")

# Initialize session states
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = ""
if 'computer_choice' not in st.session_state:
    st.session_state.computer_choice = ""
if 'round_result' not in st.session_state:
    st.session_state.round_result = ""

# Title
st.title("✊ Rock - 🖐 Paper - ✌ Scissors")

# Radio button for user's choice
user_move = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

# Play button
if st.button("Play"):
    st.session_state.user_choice = user_move
    st.session_state.computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    user = st.session_state.user_choice
    computer = st.session_state.computer_choice

    if user == computer:
        st.session_state.round_result = "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        st.session_state.round_result = "🎉 You win this round!"
        st.session_state.user_score += 1
    else:
        st.session_state.round_result = "💻 Computer wins this round!"
        st.session_state.computer_score += 1

# Display results
if st.session_state.round_result:
    st.subheader("Result:")
    st.markdown(f"*You chose:* {st.session_state.user_choice}")
    st.markdown(f"*Computer chose:* {st.session_state.computer_choice}")
    st.success(st.session_state.round_result)

# Scoreboard
st.markdown("### 🔢 Scoreboard")
st.write(f"*You:* {st.session_state.user_score}")
st.write(f"*Computer:* {st.session_state.computer_score}")

# Reset button
if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.user_choice = ""
    st.session_state.computer_choice = ""
    st.session_state.round_result = ""
    st.rerun()

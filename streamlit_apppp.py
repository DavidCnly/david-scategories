import streamlit as st
import random
import time
from collections import deque
import string

# Full list of categories
all_categories = [
    "boys name", "girls name", "animal", "song", "movie", "clothing brand", "shop",
    "food", "fruit/vegetable", "positive adjective", "negative adjective", 
    "four letter word", "7+ letter word", "country", "city", "place in your city", 
    "something that is black", "something that is red", "something that is green", 
    "something that is blue", "something that is yellow", "something that is pink",
    "offensive word", "term of endearment", "reason for a bank loan", "mode of transport", 
    "things at a zoo", "tourist attraction", "politician", "plant", "religious figure", 
    "Halloween costume", "part of the body", "colour", "alcoholic beverage", 
    "non-alcoholic beverage", "pizza topping", "sea creature", "reason to call the cops", 
    "tv show", "male actor", "actress", "male singer", "female singer", "sportsperson", 
    "something found in the kitchen", "something found in the bathroom", 
    "something found in the living room", "something found in the bedroom", 
    "historical figure", "crimes", "something related to Christmas", "something you plug in", 
    "car brand", "item of clothing", "language", "things to do at a party", "disease/injury",
    "job", "book title", "game", "body of water", "insect", "brand", 
    "something found in a school", "a common fear", "something recyclable", 
    "superhero/supervillain", "fictional character", "pet peeve", "slang word", 
    "name for a dog", "excuse for being late", "excuse for missing work", 
    "good first date idea", "bad first date idea", "reason to break up with someone"
]

num_emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']

all_letters = list(string.ascii_uppercase)

if 'recently_used' not in st.session_state:
    st.session_state.recently_used = deque(maxlen=20)
if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = []
if 'selected_letter' not in st.session_state:
    st.session_state.selected_letter = None
if 'timer_duration' not in st.session_state:
    st.session_state.timer_duration = 30
if 'timer_started' not in st.session_state:
    st.session_state.timer_started = False
if 'timer_end_time' not in st.session_state:
    st.session_state.timer_end_time = None

def shuffle_animation(all_options, display_spot, number, duration=1, speed=0.05):
    start_time = time.time()
    while time.time() - start_time < duration:
        choice = random.choice(all_options)
        display_spot.markdown(f"### {num_emojis[number]}:  {choice}")
        time.sleep(speed)
    return choice

def select_new_categories(num=5):
    available = list(set(all_categories) - set(st.session_state.recently_used))
    final_selections = []
    st.markdown("## 🔁 Picking categories...")
    for i in range(num):
        placeholder = st.empty()
        picked = shuffle_animation(available, placeholder, number=i)
        final_selections.append(picked)
        st.session_state.recently_used.append(picked)
        available.remove(picked)
    st.session_state.selected_categories = final_selections

def letter_animation(all_options, display_spot, duration=1, speed=0.05):
    start_time = time.time()
    while time.time() - start_time < duration:
        choice = random.choice(all_options)
        display_spot.markdown(f"### Letter: {choice}")
        time.sleep(speed)
    return choice

# UI
st.title("Stop the Bus ✋🚌")

st.radio("⏱️ Choose Timer Duration:", [30, 45, 60], horizontal=True, key="timer_duration")

if st.button("Let's Play!"):
    select_new_categories()
    st.divider()
    placeholder = st.empty()
    letter = letter_animation(all_letters, placeholder)
    st.session_state.selected_letter = letter
    st.session_state.timer_started = False
    st.session_state.timer_end_time = None

if st.session_state.selected_categories:
    #st.subheader("Your Categories:")
    #for cat in st.session_state.selected_categories:
     #   st.write(f"- {cat}")
     pass

if st.session_state.selected_letter:
    st.markdown(f"### 🔤 Letter: **{st.session_state.selected_letter}**")

    if not st.session_state.timer_started:
        if st.button("🕒 Start Timer"):
            st.session_state.timer_started = True
            st.session_state.timer_end_time = time.time() + st.session_state.timer_duration

    if st.session_state.timer_started:
        time_left = int(st.session_state.timer_end_time - time.time())
        if time_left > 0:
            mins, secs = divmod(time_left, 60)
            st.markdown(f"### ⏳ Time Remaining: {mins}:{secs:02d}")
            st.experimental_rerun()  # rerun every second to update timer
        else:
            st.markdown("### 🛎️ Time's up!")
            st.session_state.timer_started = False
            st.session_state.timer_end_time = None

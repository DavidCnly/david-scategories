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

# Persistent storage across reruns
if 'recently_used' not in st.session_state:
    st.session_state.recently_used = deque(maxlen=20)

if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = []

if 'selected_letter' not in st.session_state:
    st.session_state.selected_letter = None

if 'timer_duration' not in st.session_state:
    st.session_state.timer_duration = 30  # default timer seconds

if 'timer_started' not in st.session_state:
    st.session_state.timer_started = False



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
        #with st.spinner(f"Selecting category {i+1}..."):
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

def run_timer(duration):
    timer_placeholder = st.empty()
    for remaining in range(duration, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_placeholder.markdown(f"### ⏳ Time Remaining: {mins}:{secs:02d}")
        time.sleep(1)
    timer_placeholder.markdown("### 🛎️ Time's up!")
    st.session_state.timer_started = False  # Reset after timer ends

# UI
st.title("Stop the Bus ✋🚌")
st.radio("⏱️ Choose Timer Duration:", [30, 45, 60], horizontal=True, key="timer_duration")



if st.button("Let's Play!"):
    select_new_categories()
    st.divider()
    placeholder = st.empty()
    letter = letter_animation(all_letters, placeholder)
    st.session_state.selected_letter = letter
    st.session_state.timer_started = False  # Reset timer start on new play

if st.session_state.selected_categories:
    #st.divider()
    #for cat in st.session_state.selected_categories:
     #   st.write(f"### - {cat}")
     pass

if st.session_state.selected_letter:
    #st.markdown(f"### 🔤 Letter: 
    # **{st.session_state.selected_letter}**")
    st.divider()


    if not st.session_state.timer_started:
        if st.button("🕒 Start Timer"):
            st.session_state.timer_started = True
    if st.session_state.timer_started:
        run_timer(st.session_state.timer_duration)

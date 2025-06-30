import streamlit as st
import random
import time
from collections import deque

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

# Persistent storage across reruns
if 'recently_used' not in st.session_state:
    st.session_state.recently_used = deque(maxlen=20)

if 'selected_categories' not in st.session_state:
    st.session_state.selected_categories = []

def shuffle_animation(all_options, display_spot, duration=1.5, speed=0.05):
    start_time = time.time()
    while time.time() - start_time < duration:
        choice = random.choice(all_options)
        display_spot.markdown(f"### 🎲 {choice}")
        time.sleep(speed)
    return choice

def select_new_categories(num=5):
    available = list(set(all_categories) - set(st.session_state.recently_used))
    
    if len(available) < num:
        st.info("Not enough unique categories left. Resetting cooldown list.")
        st.session_state.recently_used.clear()
        available = all_categories[:]
    
    final_selections = []
    st.markdown("## 🔁 Picking categories...")

    for i in range(num):
        with st.spinner(f"Selecting category {i+1}..."):
            placeholder = st.empty()
            picked = shuffle_animation(available, placeholder)
            final_selections.append(picked)
            st.session_state.recently_used.append(picked)
            available.remove(picked)

    st.session_state.selected_categories = final_selections

# UI
st.title("🎉 Stop The Bus / Scategories Picker")

if st.button("🎰 Pick New Categories"):
    select_new_categories()

if st.session_state.selected_categories:
    st.subheader("📝 Your Categories:")
    for cat in st.session_state.selected_categories:
        st.write(f"- {cat}")


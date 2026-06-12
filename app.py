import streamlit as st
from leetcode_api import get_clean_stats   # bring in our data function

# --- Page setup ---
st.set_page_config(
    page_title="LeetCode Weakness Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar: where the user chooses what to see ---
with st.sidebar:
    st.title("⚙️ Controls")
    st.caption("Choose what to analyze")
    username = st.text_input("LeetCode Username", placeholder="e.g. Krina_Paghadar")
    view = st.radio(
        "View",
        ["Overview", "Topic Breakdown", "Weak Areas", "AI Study Plan"]
    )

# --- Main area ---
st.title("📊 LeetCode Weakness Analyzer")
st.markdown("##### Turn your solve history into a personalized study plan")
st.divider()

# Only fetch + show data once a username is typed
if username:
    stats = get_clean_stats(username)

    if stats is None:
        st.error(f"❌ Couldn't find user '{username}'. Check the spelling?")
    else:
        st.subheader(f"Solved Problems — {username}")

        # Show the 4 numbers as metric cards in a row
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total", stats.get("All", 0))
        col2.metric("Easy", stats.get("Easy", 0))
        col3.metric("Medium", stats.get("Medium", 0))
        col4.metric("Hard", stats.get("Hard", 0))
else:
    st.info("👈 Enter your username in the sidebar to get started.")
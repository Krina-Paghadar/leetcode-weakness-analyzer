import streamlit as st

# --- Page setup ---
st.set_page_config(
    page_title="LeetCode Weakness Analyzer",
    page_icon="📊",
    layout="wide",                 # use full width, feels bold & spacious
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

st.info("👈 Enter your username and pick a view to get started. (Data coming in the next build step.)")
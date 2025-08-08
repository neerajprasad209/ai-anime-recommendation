from utils.logger import get_logger
from utils.custom_exception import CustomException
from pipeline.pipeline import AnimeRecommenderPipeline
from dotenv import load_dotenv
from pathlib import Path
import streamlit as st

import sys


logger = get_logger(__name__)
load_dotenv()

st.set_page_config(page_title="Anime Recommender", page_icon="📺", layout="centered")

@st.cache_resource
def get_anime_recommender_pipeline():
    return AnimeRecommenderPipeline()

pipeline = get_anime_recommender_pipeline()

# Load CSS from file
with open("app/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


banner_path = Path("images/img.jpg")

if banner_path.exists():
    st.image(str(banner_path), use_container_width=True)
else:
    st.warning("Banner image not found. Make sure 'assets/img.jpg' exists.")


# ----- App UI -----
st.title("Anime Recommender")

query = st.text_input("🔍 Enter Anime Name:")

if st.button("🎯 Process"):
    if query.strip():
        with st.spinner("Fetching your anime recommendations... ✨"):
            response = pipeline.recommend(query)
            st.markdown("## 📜 Recommendations")
            st.write(response)
            
    else:
        st.warning("⚠️ Please enter an anime name before processing.")

st.markdown("""
    <div class="footer">
        <hr>
        <p>✨ Made by <strong>Neeraj Prasad</strong> ✨</p>
        <div class="footer-icons">
            <a href="https://github.com/neerajprasad209" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="25">
            </a>
            <a href="https://www.linkedin.com/in/neeraj-prasad-86a89b202/" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="25">
            </a>
            <a href="https://neerajprasad.netlify.app/" target="_blank">🌐</a>
            <a href="mailto:neerajprasad.209@gmail.com" target="_blank">📧</a>
        </div>
    </div>
""", unsafe_allow_html=True)
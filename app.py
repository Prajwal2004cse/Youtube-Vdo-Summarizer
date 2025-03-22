import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Ensure the module is found
from extract_transcript import get_video_transcript
import streamlit as st
import urllib.parse
from summarization import summarize_text

# ---- PAGE CONFIG ----
st.set_page_config(page_title="YouTube Summarizer", page_icon="📹", layout="centered")

# ---- CUSTOM STYLING ----
st.markdown("""
    <style>
        /* Background Image */
        .stApp {
            background: url('https://www.google.com/search?sca_esv=21396e216036fcb0&rlz=1C1CHBD_enIN1153IN1153&sxsrf=AHTn8zq4jhPPLCEHH6aF4ffr-8ZXVrdJ9Q:1742628462440&q=background+image+for+ai+youtube+summarizer&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBkzPWUS0OtApxR2914vrjk4ZqZZ4I2IkJifuoUeV0iQtecxn2V84znwGHaFIyj59zgvou5woM9zYUJv8brzSrqdiUGFZ1SbY4s6m4wQTixVY5hsWxIn_k7Jj9b18zG4GTK4uu2Z-HvxGs_iEur0xNf6ldnEaTj0IMKr6b5ARoL-8LC8ZXA&sa=X&ved=2ahUKEwjgtOrzlJ2MAxXExTgGHdqCE-8QtKgLegQIFBAB&biw=1366&bih=633&dpr=1#vhid=v74LfQYh219ovM&vssid=mosaic') no-repeat center fixed;
            background-size: cover;
        }

        /* Overlay for Readability */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.5);  /* Dark overlay */
            z-index: -1;
        }

        /* Header Styling */
        .title {
            font-size: 35px; font-weight: bold;
            color: #ffcc00; text-align: center;
        }
        .subtitle {
            text-align: center; color: white;
            font-size: 18px; margin-bottom: 20px;
        }

        /* Stylish Input Box */
        input[type="text"] {
            border-radius: 10px !important;
            padding: 12px !important;
            font-size: 16px !important;
            background: rgba(255, 255, 255, 0.8);
            border: 1px solid #ddd;
        }
        
        /* Summary Box */
        .summary-box {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px; border-radius: 12px;
            box-shadow: 2px 2px 15px rgba(255, 255, 255, 0.2);
            font-size: 18px; line-height: 1.5;
        }

        /* Centering */
        .stTextInput, .stButton, .stExpander { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown("<p class='title'>📹 YouTube Video Summarizer</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Get AI-powered summaries for YouTube videos in seconds! 🚀</p>", unsafe_allow_html=True)

# ---- INPUT BOX ----
video_url = st.text_input("🔗 Enter YouTube Video URL:", placeholder="Paste the YouTube link here...")

# ---- EXTRACT VIDEO ID FUNCTION ----
def extract_video_id(url):
    parsed_url = urllib.parse.urlparse(url)
    if "youtube.com" in parsed_url.netloc:
        query_params = urllib.parse.parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")
    return None

# ---- SUMMARIZATION PROCESS ----
if st.button("🔍 Summarize Video"):
    video_id = extract_video_id(video_url)

    if video_id:
        with st.spinner("🔄 Fetching transcript..."):
            transcript = get_video_transcript(video_id)

        if not transcript or "Error" in transcript:
            st.error("❌ Could not fetch transcript. Try another video.")
        else:
            with st.spinner("✍️ Generating summary..."):
                summary = summarize_text(transcript)

            # ---- COLLAPSIBLE FULL TRANSCRIPT ----
            with st.expander("📜 Full Transcript"):
                st.write(transcript)

            # ---- DISPLAY SUMMARY ----
            st.subheader("✨ Summary:")
            st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

    else:
        st.error("⚠️ Invalid YouTube URL. Please enter a correct link.")

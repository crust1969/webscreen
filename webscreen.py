import streamlit as st

st.set_page_config(layout="wide")

# Spotify embed
spotify_url = "https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M"

# YouTube embed
youtube_url = "https://www.youtube.com/embed/VIDEO_ID"

st.title("Spotify and YouTube Side by Side")

col1, col2 = st.columns(2)

with col1:
    st.header("Spotify")
    st.markdown(f'<iframe src="{spotify_url}" width="100%" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

with col2:
    st.header("YouTube")
    st.markdown(f'<iframe width="100%" height="380" src="{youtube_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)

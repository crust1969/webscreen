import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'
SPOTIPY_REDIRECT_URI = 'your_spotify_redirect_uri'

st.set_page_config(layout="wide")

st.sidebar.title("Spotify Login")

# Spotify authentication
if 'spotify_token' not in st.session_state:
    sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope='user-library-read')
    token_info = sp_oauth.get_access_token()
    st.session_state['spotify_token'] = token_info['access_token']

# Spotify embed
spotify_url = "https://open.spotify.com/embed/playlist/37i9dQZF1DXcBWIGoYBM5M"

st.title("Spotify Access")

st.markdown(f'<iframe src="{spotify_url}" width="100%" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)

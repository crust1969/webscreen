import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Spotify credentials
SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'
SPOTIPY_REDIRECT_URI = 'your_spotify_redirect_uri'

# Google credentials
GOOGLE_CLIENT_SECRETS_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

st.set_page_config(layout="wide")

st.sidebar.title("Login")

# Spotify authentication
if 'spotify_token' not in st.session_state:
    sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope='user-library-read')
    token_info = sp_oauth.get_access_token()
    st.session_state['spotify_token'] = token_info['access_token']

# Google authentication
if 'google_token' not in st.session_state:
    flow = InstalledAppFlow.from_client_secrets_file(GOOGLE_CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    st.session_state['google_token'] = credentials.token

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

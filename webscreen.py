import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials
SPOTIPY_CLIENT_ID = '7e10a9ddde3d4fdfad5a805ade9f9dc8'
SPOTIPY_CLIENT_SECRET = '0ef98f30900144e190acc6f7c3f3c639'
SPOTIPY_REDIRECT_URI = 'https://webscreen-uzxkxiyk3sbvw2cesdyfqn.streamlit.app/'

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

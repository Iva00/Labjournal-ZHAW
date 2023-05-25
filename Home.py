import streamlit as st
import pandas as pd
from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Logo/Name setzen für Tab in Google, so dass nicht "local" steht
st.set_page_config(
    page_title="Laborjournal ZHAW"
)

# -------- load secrets for jsonbin.io --------
jsonbin_secrets = st.secrets["jsonbin"]
api_key = jsonbin_secrets["api_key"]
bin_id = jsonbin_secrets["bin_id"]

# -------- user login --------
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

fullname, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == True:   # login successful
    authenticator.logout('Logout', 'main')   # show logout button
elif authentication_status == False:
    st.error('Username/password is incorrect')
    st.stop()
elif authentication_status == None:
    st.warning('Please enter your username and password')
    st.stop()






data = load_key(api_key, bin_id, username)

data = {"test": [2,2]}

save_key(api_key, bin_id, username, data)





# Seitenleiste-Kommentar erstellen
st.sidebar.success("Wähle einen Tab.")

# Kolone erstellen, um den Titel links zu setzen und nicht in der Mitte
col1, col2, col3 = st.columns([1,2,1])
col1.markdown(' # :blue[_Welcome to our App Laborjournal ZHAW_] :test_tube:')

# Untertitel 
st.subheader('Die Laborjournal ZHAW App unterstützt dich bei deinen Labortpraktika bzw. Experimenten während deines Studiums. Hier kannst du deine Experimente dokumentieren, Notizen erstellen oder Berechnungen durchführen.')

#Bild in der 3. Kolone setzen
col3.image('https://pixy.org/src/94/946218.gif')

# Caption erstellen 
st.caption('Erstellt von BMLD Studentinnen: Lea Gugganig, Michèle Pfister und Ivana Vujinovic')
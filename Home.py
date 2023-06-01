import streamlit as st
import pandas as pd
from jsonbin import load_key, save_key
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import datetime

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


# -------- helper functions ------
def experiment(experiment, data, api_key, bin_id, username):
    # Kolone erstellen, dass Titel links und Emoji rechts
    col1, col2, col3 = st.columns([1,2,1])
    st.markdown(' # :blue[_Experiment 1_]')
    col3.header(':test_tube:')
    # Trennungslinie hinzufügen
    st.write("---")
    # Eingabe Titel
    title1 = st.text_input('Titel Experiment')
    # Kalender hinzufügen
    d = st.date_input(
        "Datum des Experiments",
        datetime.date(2023, 3, 31),
        key='date_experiment'
    )
    # Input Eingabe
    title2 = st.text_input('Durchgeführt von', key='performed_by')
    title3 = st.text_input('Studiengang', key='course')
    # Multiselektion
    options = st.multiselect(
        'Verwendetes Material',
        ['Erlenmeyerkolben', 'Messzylinder', 'Trichter', 'Polylöffel', 'Becherglas', 'Magnetstab mit Fischli', 'Messkolben', 'Bürette', 'Thermometer', 'Glasstab','Anderes'],
        ['Erlenmeyerkolben', 'Messzylinder'],
        key='material'
    )
    # Input Text
    txt1 = st.text_area('Verwendete Chemikalien: ', key='chemicals')
    st.write('Output:',txt1)

    txt2 = st.text_area('Ablauf des Experiments: ', key='experiment_flow')
    st.write('Ablauf Output:',txt2)

    txt3 = st.text_area('Schlussfolgerungen: ', key='conclusions')
    st.write('Schlussfolgerungen Output:',txt3)

    data[experiment] = {
        "Titel Experiment" : title1,
        "Datum des Experiments" : str(d),
        "Durchgeführt" : title2,
        "Studiengang" : title3,
        "Verwendetes Material" : options,
        "Verwendete Chemikalien" : txt1,
        "Ablauf des Experiments" : txt2,
        "Schlussfolgerung" : txt3
    }
    
    return data

def get_experiment_data(data, experiment):
    experiment_data = data.get(experiment, {})
    return pd.DataFrame(experiment_data)



# ------- APP -------
# existierende daten laden
data = load_key(api_key, bin_id, username)
st.sidebar.header("Navigation")
selected_tab = st.sidebar.radio("Go to", ["Details", "Experiment 1", "Experiment 2", "Experiment 3", "Notizen", "Periodensystem", "Rechner", "Info Experiment"])

if selected_tab == "Details":
    # Kolone erstellen, dass Titel links und Emoji rechts angezeigt wird
    col1, col2, col3 = st.columns([1,2,1])
    col1.markdown(' # :blue[_Informationen über die App_]')
    col3.header(':test_tube:')
    # Trennungslinie hinzufügen
    st.write("---")
    # Titel
    st.header('Herzlich willkommen auf unserer App! Du befindest dich unter "Details".')
    # Untertitel
    st.subheader('Links in der Sidebar findest du alle Tools, welche du verwenden kannst.')
    st.subheader('Unter "Experiment" findest du eine Vorlage für dein Protokoll. Du kannst Folgendes ausfüllen: Datum, Visum, Titel, Material, Chemikalien, Durchführung...')
    st.subheader('Das Tool "Notizen" dient dir für persönliche Notizen und unter dem Tool "PSE und Formeln", haben wir für dich alle chemischen Elemente und die wichtigsten Formeln zusammengestellt.')
    st.subheader('Zu guter Letzt hilft dir "Rechner" mit deinen Umrechnungen.')
    st.subheader('Nun wünschen wir dir viel Erfolg bei deinen Experimenten und viel Spaß!')

elif selected_tab == "Experiment 1":
    data_exp = experiment("Experiment 1",data, api_key, bin_id, username)
    if st.button('Save'):
        save_key(api_key, bin_id, username, data_exp)

elif selected_tab == "Experiment 2":
    data_exp = experiment("Experiment 2",data, api_key, bin_id, username)
    if st.button('Save'):
        save_key(api_key, bin_id, username, data_exp)

elif selected_tab == "Experiment 3":
    data_exp = experiment("Experiment 3",data, api_key, bin_id, username)
    if st.button('Save'):
        save_key(api_key, bin_id, username, data_exp)

elif selected_tab == "Notizen":
    # Kolone erstellen, dass Titel links und Emoji rechts
    col1, col2, col3 = st.columns([1,2,1])
    col1.markdown(' # :blue[_Notizen_]')
    col3.header(':test_tube:')
    # Trennungslinie hinzufügen
    st.write("---")
    # Input Text
    txt = st.text_area('Deine Notizen: ', key='personal_notes')
    st.write('Notizen Output:',txt)
    
    data["Deine Notizen"] = txt
    #data_notes = {"Deine Notizen" : txt}
    if st.button('Save'):
        save_key(api_key, bin_id, username, data)

elif selected_tab == "Periodensystem":
    # Kolone erstellen, dass Titel links und Emoji rechts
    col1, col2, col3 = st.columns([1,2,1])
    col1.markdown(' # :blue[_Periodensystem_]')
    col3.header(':test_tube:')
    # Trennungslinie hinzufügen
    st.write("---")
    # Caption
    st.caption('Hier ist eine kleine Hilfe, falls du das PSE oder eine Formel gerade nicht zur Hand hast.')
    st.caption('Außerdem findest du unter diesem Link alle H- und P-Sätze: https://gestis.dguv.de')
    # Bilder hinzufügen mit Hilfe von Kolonen
    col1, col2, col3 = st.columns([1,2,1])
    col2.image('https://assets.serlo.org/5e96d795cbc3f_de178b5c2f79577bb099490f0253c95b377d2fce.png')
    col2.image('https://www.biologie-schule.de/img/molare-masse.gif')
    col2.image('https://www.thetutorteam.com/wp-content/uploads/2021/12/titration-formula-triange.png')

elif selected_tab == "Rechner":
    # Kolone erstellen, dass Titel links und Emoji rechts
    col1, col2, col3 = st.columns([1,2,1])
    col1.markdown(' # :blue[_Rechner_]')
    col3.header(':test_tube:')
    # Trennungslinie hinzufügen
    st.write("---")
    # input 1
    num1 = st.number_input(label="Erste Zahl")
    # input 2
    num2 = st.number_input(label="Zweite Zahl")
    # Operation wählen
    operation = st.radio("Wähle eine Operation:", ("+", "-", "*", "/"))

    ans = 0
    # Funktion definieren für Rechner
    def calculate():
        if operation == "+":
            ans = num1 + num2
        elif operation == "-":
            ans = num1 - num2
        elif operation == "*":
            ans = num1 * num2
        elif operation == "/" and num2 != 0:
            ans = num1 / num2
        else:
            st.warning("Division durch 0: Fehler. Bitte eine Zahl wählen, die nicht 0 ist.")
            ans = "Nicht definiert"

        st.success(f"Antwort = {ans}")

    if st.button("Rechnen"):
        calculate()
        
        
elif selected_tab == "Info Experiment":
    experiment_options = ["Experiment 1", "Experiment 2", "Experiment 3"]
    selected_experiment = st.selectbox("Select an experiment", experiment_options)
    if selected_experiment:
        experiment_data = get_experiment_data(data, selected_experiment)
        st.dataframe(experiment_data)


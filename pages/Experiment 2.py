import streamlit as st
import datetime 

# Kolone erstellen, dass TItel links und Emoji rechts
col1, col2, col3 = st.columns([1,2,1])
st.markdown(' # :blue[_Experiment 2_]')
col3.header(':test_tube:')

# Trennungslinie hinzufügen
st.write("---")

# Eingabe Titel
title1 = st.text_input('Titel Experiment', ' ')

# Kalender hinzufügen
d = st.date_input(
    "Datum des Experiments",
    datetime.date(2023, 3, 31))

# Input Eingabe
title2 = st.text_input('Durchgeführt von', ' ')

title3 = st.text_input('Studiengang', ' ')

# Multiselektion
options = st.multiselect(
    'Verwendetes Material',
    ['Erlenmeyerkolben', 'Messzylinder', 'Trichter', 'Polylöffel', 'Becherglas', 'Magnetstab mit Fischli', 'Messkolben', 'Bürette', 'Thermometer', 'Glasstab','Anderes'],
    ['Erlenmeyerkolben', 'Messzylinder'])

# Input Text
txt1 = st.text_area('Verwendete Chemikalien: ')
st.write('Output:',txt1)

txt2 = st.text_area('Ablauf des Experiments: ')
st.write('Ablauf Output:',txt2)

txt3 = st.text_area('Schlussfolgerungen: ')
st.write('Schlussfolgerungen Output:',txt3)

data = {"Titel Experiment" : title1,
        "Datum des Experiments" : d,
        "Durchgeführt": title2,
        "Studiengang" : title3,
        "Verwendetes Material" : options,
        "Verwendete Chemikalien" : txt1,
        "Ablauf des Experiments" : txt2,
        "Schlussfolgerung" : txt3,
        }

if st.button('Save'):
    save_key(api_key, bin_id, username, data)
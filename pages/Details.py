import streamlit as st

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
st.subheader('Nun wünschen wir dir viel Erfolg bei deinen Experimenten und viel Spass!')
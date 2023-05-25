import streamlit as st

# Kolone erstellen, dass Titel links und Emoji rechts
col1, col2, col3 = st.columns([1,2,1])
col1.markdown(' # :blue[_Periodensystem_]')
col3.header(':test_tube:')


# Trennungslinie hinzufügen
st.write("---")

# Caption
st.caption('Hier ist eine kleine Hilfe, falls du das PSE oder eine Formel gerade nicht zur Hand hast.')
st.caption('Ausserdem findest du unter diesem Link alle H- und P-Sätze: https://gestis.dguv.de')

# Bilder hinzufügen mit Hilfe von Kolonen
col1, col2, col3 = st.columns([1,2,1])

col2.image('https://assets.serlo.org/5e96d795cbc3f_de178b5c2f79577bb099490f0253c95b377d2fce.png')

col2.image('https://www.biologie-schule.de/img/molare-masse.gif')

col2.image('https://www.thetutorteam.com/wp-content/uploads/2021/12/titration-formula-triange.png')


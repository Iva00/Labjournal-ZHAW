import streamlit as st

# Kolone erstellen, dass TItel links und Emoji rechts
col1, col2, col3 = st.columns([1,2,1])
col1.markdown(' # :blue[_Notizen_]')
col3.header(':test_tube:')

# Trennungslinie hinzufügen
st.write("---")

# Input Text
txt = st.text_area('Deine Notizen: ')
st.write('Notizen Output:',txt)

data = {"Deine Notizen" : txt
         }

if st.button('Save'):
    save_key(api_key, bin_id, username, data)
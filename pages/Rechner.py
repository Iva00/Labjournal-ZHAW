import streamlit as st

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
operation = st.radio("Wähle eine Operation:",
                    ("+", "-", "*", "/"))
 
ans = 0
 
# Funktion definieren für Rechner
def calculate():
    if operation == "+":
        ans = num1 + num2
    elif operation == "-":
        ans = num1 - num2
    elif operation == "*":
        ans = num1 * num2
    elif operation=="/" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("Division durch 0: Fehler. Bitte eine Zahl wählen, die nicht 0 ist.")
        ans = "Nicht definiert"
 
    st.success(f"Antwort = {ans}")
 
if st.button("Rechnen"):
    calculate()





    
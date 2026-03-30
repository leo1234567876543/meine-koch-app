import streamlit as st
import random
import os

# Deine HTL-Funktionen (fast wie im Original)
def hole_zufall(dateiname, zuf):
    if os.path.exists(dateiname):
        with open(dateiname, "r", encoding="utf-8") as f:
            text = f.read()
            woerter = text.strip().split(",")
            # Entfernt Leerzeichen am Anfang/Ende jedes Wortes
            woerter = [w.strip() for w in woerter if w.strip()]
            zuf = random.choice
            
            return zuf(woerter)
    return "Datei nicht gefunden!"

def hole_zufall1(dateiname, zuf):
    if os.path.exists(dateiname):
        with open(dateiname, "r", encoding="utf-8") as f:
            text = f.read()
            woerter = text.strip().split(",")
            # Entfernt Leerzeichen am Anfang/Ende jedes Wortes
            woerter = [w.strip() for w in woerter if w.strip()]
            
            
            return zuf(woerter)
    return "Datei nicht gefunden!"

# --- Streamlit Oberfläche (Das "Frontend") ---
st.title("🍴 Ricardas Zufallsessen")
st.write("Wähle eine Kategorie aus, um einen Vorschlag zu erhalten:")

# Deine 3 Kategorien als schicke Buttons
if st.button("🍰 1. Kuchen"):
    ergebnis = hole_zufall("kuchen.txt", random.choice)
    st.success(f"Der Zufallskuchen ist ein **{ergebnis}**")
if st.button("Rezept"):
    ergebnis1=hole_zufall1("kuchen_rezepte.txt", random.choice)
    st.success(f"Hier ist das Rezept:**{ergebnis1}**")

if st.button("🍝 2. Essen unter der Woche"):
    ergebnis = hole_zufall("essen_unter.txt")
    st.info(f"Das Zufallswochentagsessen ist **{ergebnis}**")

if st.button("🍗 3. Essen am Wochenende"):
    ergebnis = hole_zufall("essen_wochenende.txt")
    st.warning(f"Das Zufallswochenendsessen ist **{ergebnis}**")

# Kleiner Info-Text für den Lehrer
st.sidebar.write("HTL Projekt v1.0")

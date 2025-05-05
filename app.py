import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("🌆 Mapa de Residuos en las 10 Ciudades más Pobladas de Colombia")

with open("mapa_ciudades_poligonos.html", "r", encoding="utf-8") as file:
    html_content = file.read()

components.html(html_content, height=600, scrolling=True)


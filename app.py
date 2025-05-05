import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Datos de ciudades (deben coincidir con los del mapa HTML)
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
            "Cúcuta", "Soacha", "Ibagué", "Bucaramanga", "Soledad"]
residuos_toneladas = [6582, 2183, 2034, 1083, 875, 678, 633, 555, 494, 489]
data = list(zip(ciudades, residuos_toneladas))
df = pd.DataFrame(data, columns=["Ciudad", "Toneladas/día"])

st.set_page_config(layout="wide")
st.title("🌆 Mapa de Residuos en las 10 Ciudades más Pobladas de Colombia")

# Filtros
st.sidebar.header("🎯 Filtros")
ciudades_seleccionadas = st.sidebar.multiselect("Selecciona ciudades", ciudades, default=ciudades)
residuos_minimos = st.sidebar.checkbox("Solo mostrar ciudades con > 500 toneladas/día")

# Mostrar datos filtrados
df_filtrado = df[df["Ciudad"].isin(ciudades_seleccionadas)]
if residuos_minimos:
    df_filtrado = df_filtrado[df_filtrado["Toneladas/día"] > 500]

# Mostrar tabla
st.subheader("📊 Resumen de ciudades seleccionadas")
st.dataframe(df_filtrado, use_container_width=True)

# Mostrar mapa si hay ciudades seleccionadas
if not df_filtrado.empty:
    with open("mapa_ciudades_poligonos.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    components.html(html_content, height=600, scrolling=True)
else:
    st.warning("⚠️ No hay ciudades que cumplan con los filtros seleccionados.")

# Firma
st.markdown("---")
st.markdown("📍 **Elaborado por Danny Ibarra Vega, PhD.**")

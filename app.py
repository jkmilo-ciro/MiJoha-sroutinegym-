import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración visual de la página
st.set_page_config(page_title="Mi Rutina Pro", page_icon="💪")

# 1. Definición de las Rutinas
rutinas = {
    "Pecho y Tríceps": ["Press de Banca", "Aperturas con mancuernas", "Extensión de tríceps", "Flexiones"],
    "Espalda y Bíceps": ["Dominadas", "Remo con barra", "Curl de bíceps", "Martillo"],
    "Pierna": ["Sentadillas", "Prensa", "Extensión de cuádriceps", "Peso muerto"],
    "Cardio y Abdomen": ["Correr 20 min", "Plancha", "Crunch abdominal", "Burpees"]
}

st.title("💪 Mi Diario de Entrenamiento")
st.write("Selecciona tu rutina y registra tus avances de hoy.")

# 2. Selección de Rutina
dia_entrenamiento = st.selectbox("¿Qué toca entrenar hoy?", list(rutinas.keys()))

st.subheader(f"Rutina: {dia_entrenamiento}")

# 3. Formulario de entrada de datos
datos_hoy = []
for ejercicio in rutinas[dia_entrenamiento]:
    with st.container():
        st.markdown(f"#### {ejercicio}")
        col1, col2 = st.columns(2)
        with col1:
            peso = st.number_input(f"Peso (kg)", key=f"p_{ejercicio}", min_value=0.0, step=0.5)
        with col2:
            reps = st.number_input(f"Repeticiones", key=f"r_{ejercicio}", min_value=0, step=1)
        datos_hoy.append({"Ejercicio": ejercicio, "Peso": peso, "Reps": reps})
        st.divider()

# 4. Botón de Guardado
if st.button("✅ Registrar Entrenamiento"):
    df = pd.DataFrame(datos_hoy)
    df['Fecha'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Mostrar resumen al usuario
    st.success("¡Entrenamiento registrado con éxito!")
    st.balloons()
    st.table(df)
  

import streamlit as st
import pandas as pd

# 1. Configuramos la página para que ocupe toda la pantalla (layout="wide")
st.set_page_config(page_title="Cosmopolitan Tower", page_icon="🏢", layout="wide")

# 2. Encabezado con imagen y título usando columnas
col_img, col_tit = st.columns([1, 4])
with col_img:
    # Jalamos una foto de la torre desde Wikipedia
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Cosmopolitan_Twarda_2_4.jpg/400px-Cosmopolitan_Twarda_2_4.jpg", use_container_width=True)
with col_tit:
    st.title("🏙️ Análisis Estructural - Cosmopolitan Twarda 2/4")
    st.markdown("### **Feria de Ingeniería - Universidad Nacional de Ingeniería (UNI)**")

st.divider() # Línea separadora elegante

# 3. Dividimos el área de trabajo en dos columnas (Izquierda para controles, Derecha para gráficas)
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("⚙️ Parámetros de Simulación")
    st.info("Ajuste los valores para simular las cargas actuando sobre la estructura.")
    
    velocidad_viento = st.slider("Velocidad del Viento (km/h)", min_value=0, max_value=250, value=120)
    peso_losa = st.number_input("Carga Muerta por piso (kN)", value=500.0, step=50.0)
    
    # Cálculo
    fuerza_base = (velocidad_viento ** 2) * 0.004 * 44
    
    # st.metric crea un número grande y llamativo, estilo "dashboard" financiero
    st.metric(label="Cortante Basal Total Estimado", value=f"{fuerza_base:,.2f} kN")

with col_der:
    st.subheader("📊 Distribución de Fuerzas por Piso")
    
    pisos = list(range(1, 45))
    fuerzas = [fuerza_base * (p / 44) for p in pisos]
    datos = pd.DataFrame({"Piso": pisos, "Fuerza Lateral (kN)": fuerzas})
    
    # Gráfica de barras (le ponemos color rojo para que resalte más)
    st.bar_chart(datos, x="Piso", y="Fuerza Lateral (kN)", color="#FF4B4B")
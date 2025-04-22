import streamlit as st

# Titulo de la aplicación
st.title("Calculadora de las Leyes de los Gases")

# Selección de la ley
ley = st.selectbox(
    "Selecciona la ley de los gases que deseas usar:",
    ("Ley de Charles", "Ley de Boyle", "Ley de Gay-Lussac")
)

# Ingreso de datos
if ley == "Ley de Charles":
    st.subheader("Ley de Charles: V1/T1 = V2/T2")
    T1 = st.number_input("Temperatura 1 (K)", min_value=0.01)
    V1 = st.number_input("Volumen 1 (L)", min_value=0.01)
    T2 = st.number_input("Temperatura 2 (K)", min_value=0.01)
    if st.button("Calcular Volumen 2 (V2)"):
        V2 = V1 * T2 / T1
        st.success(f"El volumen 2 (V2) es: {V2:.3f} L")

elif ley == "Ley de Boyle":
    st.subheader("Ley de Boyle: P1 * V1 = P2 * V2")
    P1 = st.number_input("Presión 1 (atm)", min_value=0.01)
    V1 = st.number_input("Volumen 1 (L)", min_value=0.01)
    P2 = st.number_input("Presión 2 (atm)", min_value=0.01)
    if st.button("Calcular Volumen 2 (V2)"):
        V2 = (P1 * V1) / P2
        st.success(f"El volumen 2 (V2) es: {V2:.3f} L")

elif ley == "Ley de Gay-Lussac":
    st.subheader("Ley de Gay-Lussac: P1/T1 = P2/T2")
    P1 = st.number_input("Presión 1 (atm)", min_value=0.01)
    T1 = st.number_input("Temperatura 1 (K)", min_value=0.01)
    P2 = st.number_input("Presión 2 (atm)", min_value=0.01)
    if st.button("Calcular Temperatura 2 (T2)"):
        T2 = (P2 * T1) / P1
        st.success(f"La temperatura 2 (T2) es: {T2:.3f} K")

import PyPDF2
import re
from collections import defaultdict
from datetime import datetime
import streamlit as st

# Título de la aplicación
st.title("Procesador de PDFs para Ventas")

# Subida de archivo PDF
uploaded_file = st.file_uploader("Sube un archivo PDF", type="pdf")

if uploaded_file is not None:
    # Procesar el archivo PDF
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    # Limpieza del texto
    text = re.sub(r'\s+', ' ', text)

    # Patrón para capturar fechas y valores
    pattern = r"(\d{2}-\d{2}-\d{4}).*?\$(\d[\d.,]*)\s*\$([-\d.,]*)\s*\$([-\d.,]*)"
    matches = re.findall(pattern, text)

    # Procesar los datos
    ventas_por_fecha = defaultdict(float)
    for match in matches:
        fecha = match[0]
        valor_neto = match[3]  # Último valor como valor neto
        try:
            valor_limpio = valor_neto.replace('.', '').replace(',', '.').replace('$', '')
            ventas_por_fecha[fecha] += float(valor_limpio)
        except ValueError:
            continue

    # Ordenar las ventas por fecha
    sorted_ventas = sorted(ventas_por_fecha.items(), key=lambda x: datetime.strptime(x[0], '%d-%m-%Y'))

    # Mostrar los resultados
    st.subheader("Resultados")
    if sorted_ventas:
        st.write("Ventas totales por fecha:")
        for fecha, total in sorted_ventas:
            st.write(f"Fecha: {fecha} - Total ventas netas: ${total:,.2f}")
    else:
        st.write("No se encontraron datos en el archivo PDF.")


import PyPDF2

# Abre el archivo PDF
with open('/Users/franciscoandreudegasperi/Downloads/MercadoPago.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Lee el texto de cada página
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

    # Imprime el texto extraído
    print(text)
# Datos de ventas: Una lista de tuplas (fecha, valor)
ventas = [
    ("07-11-2024", 72.89283),
    ("07-11-2024", 27.71220),
    ("07-11-2024", 30.97245),
    ("07-11-2024", 37.42704),
    ("08-11-2024", 36.13604),
    ("08-11-2024", 34.32924),
    ("09-11-2024", 45.61855),
    ("09-11-2024", 81.88274),
    # Agrega más datos según sea necesario
]

# Crear un diccionario para almacenar las sumas de ventas por fecha
ventas_por_fecha = {}

# Recorremos la lista de ventas
for fecha, valor in ventas:
    # Si la fecha ya existe en el diccionario, sumamos el valor a la venta existente
    if fecha in ventas_por_fecha:
        ventas_por_fecha[fecha] += valor
    else:
        # Si no existe, creamos una nueva entrada con el valor de la venta
        ventas_por_fecha[fecha] = valor

# Imprimir los resultados
for fecha, total_ventas in ventas_por_fecha.items():
    print(f"Fecha: {fecha} - Total de ventas: ${total_ventas:.2f}")


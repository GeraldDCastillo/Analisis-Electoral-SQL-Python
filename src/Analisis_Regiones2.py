import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
from openpyxl import load_workbook  # <--- NUEVO: El editor de Excel
from openpyxl.drawing.image import Image  # <--- NUEVO: El pegamento de imágenes

# ---------------------------------------------------------
# BLOQUE 1: CONEXIÓN (Igual que siempre)
# ---------------------------------------------------------
print("🔌 Conectando a SQL Server...")
server = 'LAPTOP-MSNVOJJO'
database = 'CursoSQL'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

try:
    conexion = pyodbc.connect(conn_str)

    # ---------------------------------------------------------
    # BLOQUE 2: EXTRAER DATOS (Tu JOIN ganador)
    # ---------------------------------------------------------
    query = """
            SELECT R.Zona, \
                   SUM(V.Votos) AS Total_Votos
            FROM dbo.votos AS V
                     INNER JOIN dbo.Regiones AS R
                                ON V.ENTIDAD = R.Estado
            GROUP BY R.Zona
            ORDER BY Total_Votos DESC \
            """

    df_zonas = pd.read_sql(query, conexion)

    # ---------------------------------------------------------
    # BLOQUE 3: CREAR EL EXCEL BÁSICO
    # ---------------------------------------------------------
    nombre_excel = "../data/Reporte_Electoral_Final.xlsx"
    print(f"💾 Creando archivo: {nombre_excel}...")
    df_zonas.to_excel(nombre_excel, index=False)

    # ---------------------------------------------------------
    # BLOQUE 4: GENERAR Y GUARDAR LA GRÁFICA (LA FOTO)
    # ---------------------------------------------------------
    print("🎨 Pintando y guardando la gráfica...")
    plt.figure(figsize=(10, 6))

    barras = plt.bar(df_zonas['Zona'], df_zonas['Total_Votos'], color='orange')
    plt.title('Votos Totales por Región')
    plt.xlabel('Región')
    plt.ylabel('Votos (Millones)')
    plt.ticklabel_format(style='plain', axis='y')
    plt.bar_label(barras, fmt='%d')

    # TRUCO: Guardamos la gráfica como imagen antes de mostrarla
    nombre_imagen = "grafica_temporal.png"
    plt.savefig(nombre_imagen, bbox_inches='tight')
    print("📸 ¡Foto de la gráfica tomada!")

    # ---------------------------------------------------------
    # BLOQUE 5: EL PEGAMENTO MÁGICO (Insertar imagen en Excel)
    # ---------------------------------------------------------
    print("📎 Insertando la gráfica dentro del Excel...")

    # 1. Abrimos el Excel que acabamos de crear
    libro = load_workbook(nombre_excel)
    hoja = libro.active  # Seleccionamos la primera hoja

    # 2. Preparamos la imagen
    img = Image(nombre_imagen)

    # 3. La pegamos en la celda D2 (al lado de la tabla)
    hoja.add_image(img, 'D2')

    # 4. Guardamos los cambios
    libro.save(nombre_excel)

    print("\n" + "=" * 40)
    print(f"🚀 ¡LISTO! Abre el archivo '{nombre_excel}'")
    print("   Verás los datos Y la gráfica adentro.")
    print("=" * 40)

    # Opcional: Mostrarla también en PyCharm
    plt.show()

except Exception as e:
    print("❌ Error:", e)
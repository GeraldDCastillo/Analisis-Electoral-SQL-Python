import pandas as pd
import random
from datetime import datetime, timedelta
import os

# --- 1. CONFIGURACIÓN DEL NEGOCIO ---
# Simulamos una distribuidora nacional
NUM_ENVIOS = 1000
RUTAS_LOGISTICAS = [
    'Centro-Norte (Managua-Estelí)',
    'Pacífico (Managua-León)',
    'Sur (Granada-Rivas)',
    'Occidente (Chinandega-Corinto)',
    'Caribe (Rama-Bluefields)'
]
FLOTA_CAMIONES = ['Camión C-001', 'Camión C-002', 'Camión Frio-01', 'Panel-Express', None]

print("🏭 INICIANDO GENERACIÓN DE DATA WAREHOUSE...")

data = []

# --- 2. MOTOR DE SIMULACIÓN ---
for i in range(NUM_ENVIOS):
    # Fechas dinámicas (últimos 3 meses)
    fecha_operacion = datetime.now() - timedelta(days=random.randint(0, 90))

    registro = {
        'Tracking_ID': f"TRK-{i + 5000}",  # IDs más realistas
        'Fecha_Despacho': fecha_operacion.strftime("%Y-%m-%d"),
        'Ruta_Asignada': random.choice(RUTAS_LOGISTICAS),
        'Unidad_Transporte': random.choice(FLOTA_CAMIONES),
        'Carga_KG': random.randint(50, 5000),
        'Costo_Operativo': round(random.uniform(100, 1200), 2),
        'Estatus_Entrega': random.choice(['Entregado_A_Tiempo', 'En_Transito', 'Retrasado', 'Siniestrado', 'Cancelado'])
    }

    # --- 3. INYECCIÓN DE ERRORES (Para limpiar en Databricks) ---
    # Simulamos que el sensor de peso falló en algunos casos
    if random.random() < 0.08:
        registro['Carga_KG'] = None

    # Simulamos error humano en el costo
    if random.random() < 0.05:
        registro['Costo_Operativo'] = -50.00  # Costos negativos (Imposible, hay que limpiar)

    data.append(registro)

# --- 4. EXPORTACIÓN ---
df = pd.DataFrame(data)

# Ruta relativa inteligente
ruta_destino = '../data'
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

archivo_excel = os.path.join(ruta_destino, 'SupplyChain_Raw_Data.xlsx')

try:
    df.to_excel(archivo_excel, index=False)
    print(f"✅ DATASET GENERADO CON ÉXITO:")
    print(f"   📂 Archivo: {archivo_excel}")
    print(f"   📊 Registros: {len(df)}")
except Exception as e:
    print(f"❌ Error guardando Excel (¿Falta openpyxl?): {e}")
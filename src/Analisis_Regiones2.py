import pandas as pd
import matplotlib.pyplot as plt
import pyodbc
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import os

# --- 1. CONFIGURATION & SETUP ---
SERVER = '.'
DATABASE = 'CursoSQL'

EXCEL_FILE = '../data/Reporte_Electoral_Final.xlsx'
IMAGE_FILE = '../img/chart_temp.png'

print("🔌 Connecting to SQL Server...")

try:
    # Secure connection
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;'

    conn = pyodbc.connect(connection_string)

    # --- LOGIC RESTORED: COMPLEX JOIN QUERY ---
    # We join 'votos' with 'Regiones' to aggregate by Zone instead of State
    query = """
            SELECT R.Zona, SUM(V.Votos) AS Total_Votos
            FROM dbo.votos AS V
                     INNER JOIN dbo.Regiones AS R
                                ON V.ENTIDAD = R.Estado
            GROUP BY R.Zona
            ORDER BY Total_Votos DESC \
            """

    df = pd.read_sql(query, conn)
    conn.close()

    print("✅ Data extracted successfully (By Region).")
    print(df.head())

except Exception as e:
    print(f"❌ CRITICAL ERROR: Database connection failed. {e}")
    exit()

# --- 2. DATA PROCESSING (Pandas) ---
print("⚙️ Processing data...")

# Note: The SQL Query already grouped the data, so we don't need to groupby here.
# We just save the result.
report = df

# Export to Excel
report.to_excel(EXCEL_FILE, index=False)
print(f"📄 Excel created at: {EXCEL_FILE}")

# --- 3. DATA VISUALIZATION (Matplotlib) ---
print("📊 Generating business charts...")

plt.figure(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Now we plot 'Zona' vs 'Total_Votos' (The original requirement)
plt.bar(report['Zona'], report['Total_Votos'], color=colors)

plt.title('Total Votes by Region (Generated via Python)')
plt.xlabel('Region')
plt.ylabel('Votes (Millions)')
plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation=45)

plt.savefig(IMAGE_FILE, bbox_inches='tight')
print(f"📸 Chart saved at: {IMAGE_FILE}")

# --- 4. REPORT GENERATION (OpenPyXL) ---
print("📎 Integrating chart into final Excel report...")

try:
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active

    img = Image(IMAGE_FILE)
    ws.add_image(img, 'D2')

    wb.save(EXCEL_FILE)

    print("=" * 50)
    print(f"🚀 SUCCESS! Full Pipeline finished.")
    print(f"📂 Output: {EXCEL_FILE}")
    print("=" * 50)

except Exception as e:
    print(f"❌ Error during Excel integration: {e}")
    print("⚠️ HINT: Close the Excel file if it is open!")
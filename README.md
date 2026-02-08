# 📊 Análisis Electoral: Pipeline de Datos (SQL + Python + Power BI)

Este proyecto implementa un flujo de trabajo completo de Ingeniería de Datos y Análisis para procesar resultados electorales, clasificarlos por zonas geográficas y visualizar los hallazgos.

---

## 🚀 Tecnologías Utilizadas
El proyecto integra tres herramientas clave:
* **SQL Server:** Para el almacenamiento, limpieza y agregación masiva de datos (Vistas y Queries).
* **Python (Pandas & Matplotlib):** Para la conexión a base de datos, automatización de reportes en Excel y generación de gráficas estáticas.
* **Power BI:** Para la visualización interactiva y el storytelling de los datos.

---

## 📂 Estructura del Proyecto

| Archivo | Descripción |
| :--- | :--- |
| `Script_Base_Datos.sql` | Código SQL para crear tablas, insertar datos y generar la Vista de Regiones (Norte, Sur, Centro). |
| `Analisis_Regiones2.py` | Script principal de Python. Conecta a SQL, extrae la data y genera el Excel final con gráficas. |
| `Dashboard_Electoral.pbix` | Tablero interactivo de Power BI con mapas y filtros dinámicos. |
| `Reporte_Electoral_Final.xlsx` | Resultado final del proceso automatizado. |

---

## ⚙️ Funcionalidades Clave

### 1. Clasificación Regional (SQL)
Se implementó una lógica de negocio en SQL para agrupar los estados en zonas económicas:
* **Norte:** Nuevo León, Sinaloa, etc.
* **Centro:** CDMX, Puebla, Estado de México.
* **Sur/Bajío/Occidente:** Resto de entidades.

### 2. Automatización (Python)
El script de Python ejecuta:
* Conexión segura mediante `pyodbc`.
* Extracción de datos de la vista SQL.
* Cálculo de estadísticas de participación.
* Exportación automática a reportes de Excel.

### 3. Visualización (Power BI)
El dashboard permite responder preguntas como:
* ¿Qué zona geográfica tuvo mayor participación?
* ¿Cómo se distribuyen los votos por partido en cada región?

---

## 👤 Autor
**Gerald David Castillo Soto**
* Estudiante de Administración de Empresas & Data Engineering.
* Universidad Nacional Politécnica (UNP).

---
*Este proyecto es parte de mi portafolio profesional de análisis de datos.*
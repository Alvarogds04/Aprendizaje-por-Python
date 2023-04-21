import pandas as pd
import pyodbc

# establecer la conexión a la base de datos
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=178.60.208.154,4523;DATABASE=BLUE100M_PT;UID=HLCODISYS;PWD=Nol@s3.18')

# crear una lista de los nombres de las bases de datos
bases_de_datos = ['BLUE100M_PT', 'MPTG100', 'PEPETACO_PT', 'TGBPT', 'PANTHER_PT', 'MULTIMARCA_PT']

# crear un diccionario para almacenar los datos de cada base de datos
datos = {}

# iterar sobre las bases de datos y obtener los datos
for db in bases_de_datos:
    # ejecutar la consulta y obtener los datos
    query = f"SELECT t.COD, t.DES, h.COD, h.DES, '{db}' as MARCA FROM {db}.dbo.MANHGD$$ d INNER JOIN {db}.dbo.manhgt$$ t ON t.cod=d.COD INNER JOIN {db}.dbo.manhpt$$ h ON h.cod=d.hip"
    datos[db] = pd.read_sql(query, conn)

# crear un objeto ExcelWriter para escribir en el archivo Excel
writer = pd.ExcelWriter('locales.xlsx')

# iterar sobre los datos y escribirlos en hojas separadas en el archivo Excel
for db in bases_de_datos:
    datos[db].to_excel(writer, sheet_name=db, index=False)

# guardar el archivo Excel
writer.save()

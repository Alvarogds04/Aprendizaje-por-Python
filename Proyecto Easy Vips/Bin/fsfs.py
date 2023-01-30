import sqlite3
from tkinter import filedialog

def import_db():
    file_path = filedialog.askopenfilename(filetypes=[("DB files", "*.db")])
    if file_path:
        con = sqlite3.connect(file_path)
        return con

conn = import_db()
if conn:
    cursor = conn.cursor()

    # Obtener nombres de todas las tablas en la base de datos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = cursor.fetchall()

    # Agregar una columna "ping" a cada tabla
    for table in tables:
        table_name = table[0]
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN ping INTEGER DEFAULT 0;")

    # Guardar los cambios en la base de datos
    conn.commit()

    # Cerrar la conexión a la base de datos
    conn.close()
else:
    print("No se seleccionó ningún archivo")

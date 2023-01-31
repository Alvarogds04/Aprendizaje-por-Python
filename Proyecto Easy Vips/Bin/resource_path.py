import os
import sys
from tkinter import *
from Bin.SQLite import *


def resource_path_temporal(relative_path):
    #obtener ruta de carpeta temporal
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
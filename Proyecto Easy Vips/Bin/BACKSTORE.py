import sqlite3


import fileinput
import subprocess


global file_path
con = sqlite3.connect(file_path)
cur = con.cursor()
cur.execute("SELECT * FROM table_name WHERE column = 'value'")
row = cur.fetchone()
new_text = row[0]
start_run_exe_and_change_txt_thread(line_number, new_text)


def change_txt_line(file_path, line_number, new_line):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for i, line in enumerate(file):
            if i == line_number:
                print(new_line)
            else:
                print(line, end='')

def open_exe(file_path):
    subprocess.Popen(file_path, shell=True)

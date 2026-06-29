
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QListWidget,
                             QPushButton, QLineEdit, QListWidgetItem, QGridLayout)
from PyQt5.QtGui import *
from funciones_app2 import (agregartarea, checks, num_tareas, mover_tareas, 
                            guardar_tareas, cargar_tareas, eliminar2)

import json
import os

app = QApplication ([])

main_win = QWidget()
main_win.setWindowTitle("Lista de tareas")
main_win.move(300,300)
main_win.resize(500,500)


list_widget = QListWidget()
button1 = QPushButton("agregar tarea")
linea_tarea = QLineEdit('')
linea_tarea.setPlaceholderText('escribe la tarea')

#-----lista completadas

mensaje = QLabel("actualiza tu progreso")

list_completadas = QListWidget()
label1 = QLabel("Tareas completadas")

label2 = QLabel("Tareas pendientes")

#personalización ------------

main_win.setFont(QFont("Playfair Display", 12))

'''button1.setStyleSheet("""
QPushButton {
    background-color: #2596be;
                      }      
QPushButton:hover {
    background-color: black;}                                      """)
'''

#--------guardar en archivos json

file_tareas = "lista_tareas4.json"

all_tareas = cargar_tareas(file_tareas)
if isinstance(all_tareas, list):
    tareas= all_tareas
else:
    tareas = []

completadas = [t["tarea"] for t in tareas if t.get("estado") == True]
pendientes = [t["tarea"] for t in tareas if t.get("estado") == False]


for tarea_dict in tareas:
    item = QListWidgetItem(tarea_dict["tarea"])
    if tarea_dict.get("estado") == True:
        item.setCheckState(Qt.Checked)
    else:
        item.setCheckState(Qt.Unchecked)
    list_widget.addItem(item)

#------



num_pendientes = len(pendientes)
num_completas = len(completadas)
total_tareas = len(tareas)





texto_num_tareas = QLabel("")

texto_num_tareas.setText(f"tienes {num_pendientes} tareas por realizar")



button1.clicked.connect(lambda item:
                        agregartarea(linea_tarea, list_widget, tareas, pendientes, file_tareas))

list_widget.itemChanged.connect(lambda item:
                                checks(item, tareas, pendientes, completadas, list_widget, list_completadas, file_tareas))

list_widget.itemChanged.connect(lambda:
                                num_tareas(tareas, pendientes, completadas, texto_num_tareas))

list_widget.itemChanged.connect(lambda:
                                mover_tareas(completadas, list_completadas))

'''list_completadas.itemChanged.connect(lambda item:
                                     eliminar2(item, completadas, pendientes, list_widget, list_completadas))
'''

#------LAYOUT

layout = QGridLayout()
#--- 1ra lista
layout.addWidget(linea_tarea, 1, 0)
layout.addWidget(button1, 1, 1)
layout.addWidget(list_widget, 3, 0)
layout.addWidget(label2, 2, 0)

 #--2da lista
layout.addWidget(label1, 2, 1 )
layout.addWidget(list_completadas, 3, 1)

layout.addWidget(texto_num_tareas, 0, 0, 1, 2, alignment=Qt.AlignCenter)
layout.addWidget(mensaje, 4, 0, 1, 2, alignment=Qt.AlignCenter)


main_win.setLayout(layout)










main_win.show()
app.exec()
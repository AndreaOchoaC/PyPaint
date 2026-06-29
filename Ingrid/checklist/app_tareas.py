
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QLineEdit, QListWidgetItem, QGridLayout
from PyQt5.QtGui import *
from funciones_app import agregartarea, checks, num_tareas, mover_tareas

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

list_completadas = QListWidget()
label1 = QLabel("Tareas completadas")

label2 = QLabel("Tareas pendientes")

#personalización ------------

main_win.setFont(QFont("Times", 12, QFont.Bold))

'''button1.setStyleSheet("""
QPushButton {
    background-color: #2596be;
                      }      
QPushButton:hover {
    background-color: black;}                                      """)
'''







#-----LISTA DE TAREAS

tareas = ["Jugar con sky", "Leer Blue lock", "Tarea de español", "Tarea de química"]

for tarea in tareas:
    item = QListWidgetItem(tarea)
    item.setCheckState(Qt.Unchecked)
    list_widget.addItem(item)




completadas = []
pendientes = tareas.copy()
num_pendientes = len(pendientes)
num_completas = len(completadas)
total_tareas = len(tareas)





texto_num_tareas = QLabel("")
texto_num_tareas.setText(f"tienes {num_pendientes} tareas por realizar")



button1.clicked.connect(lambda item:
                        agregartarea(linea_tarea, list_widget, tareas))

list_widget.itemChanged.connect(lambda item:
                                checks(item, pendientes, completadas, list_widget, list_completadas))

list_widget.itemChanged.connect(lambda item:
                                num_tareas(tareas, pendientes, completadas, texto_num_tareas))




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

main_win.setLayout(layout)










main_win.show()
app.exec()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QLineEdit, QListWidgetItem, QGridLayout
from PyQt5.QtGui import *



def agregartarea(linea_tarea, list_widget, tareas):
    todo = linea_tarea.text()
    print(f"tarea guardada: {todo}")
    if todo.strip():

        tareas.append(todo)
    
        item = QListWidgetItem(todo)
        item.setCheckState(Qt.Unchecked)
        list_widget.addItem(item)
        linea_tarea.clear()


def mover_tareas(list_completadas, completadas):
    for tarea in completadas:
        item = QListWidgetItem(tarea)
    list_completadas.addItem(item)


def checks(item, pendientes, completadas, list_widget, list_completadas):
    if item.checkState() == Qt.Checked:
        print(f"{item.text()} completada")
        completadas.append(item.text())
        pendientes.remove(item.text())
        mover_tareas(list_completadas, completadas)
    else:
        print(f"{item.text()} está pendiente")
        pendientes.append(item.text())

    print("tareas completadas:", completadas)
    print("tareas pendientes:", pendientes)

def num_tareas(tareas, pendientes, completadas, texto_num_tareas):
    num_pendientes = len(pendientes)
    num_completas = len(completadas)
    total_tareas = len(tareas)
    texto_num_tareas.setText(f"has completado {num_completas} tareas de {total_tareas} tareas")


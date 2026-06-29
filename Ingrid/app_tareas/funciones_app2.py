from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QLineEdit, QListWidgetItem, QGridLayout
from PyQt5.QtGui import *
import json
import os


def guardar_tareas(tareas, archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(tareas, f, indent=4, ensure_ascii=False)
        print(f"tareas guardadas en {archivo}")    
    except Exception as e:
        print(f"error")
        

def cargar_tareas(archivo="lista_tareas4.json"):
    try:
        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        else:
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
        

def agregartarea(linea_tarea, list_widget, tareas, pendientes, archivo):
    todo = linea_tarea.text()
    print(f"tarea guardada: {todo}")
    if todo.strip():
        task = {
            "tarea": todo,
            "estado": False 
        }
        tareas.append(task)
        pendientes.append(todo)

        guardar_tareas(tareas, archivo)

        item = QListWidgetItem(todo)
        item.setCheckState(Qt.Unchecked)
        list_widget.addItem(item)
        linea_tarea.clear()






def mover_tareas(completadas, list_completadas):
    list_completadas.clear()
    for tarea in completadas:
        item = QListWidgetItem(tarea)
        list_completadas.addItem(item)
        '''item.setCheckState(Qt.Checked)

'''

def checks(item, tareas, pendientes, completadas, list_widget, list_completadas, archivo):
    estado = item.checkState()
    tarea_texto = item.text()
    
    tarea_dict = next((t for t in tareas if t["tarea"] == tarea_texto), None)

    if tarea_dict:

        if estado == Qt.Checked:
            print(f"{item.text()} completada")
            tarea_dict["estado"] = True
            if tarea_texto in pendientes:
                pendientes.remove(tarea_texto)
            if tarea_texto not in completadas:
                completadas.append(tarea_texto)
        else:
            print(f"{item.text()} está pendiente")
            tarea_dict["estado"] = False
            if tarea_texto in completadas:
                completadas.remove(tarea_texto)
            if tarea_texto not in pendientes:
                pendientes.append(tarea_texto)

        
        guardar_tareas(tareas, archivo)
        mover_tareas(completadas, list_completadas)

    print("tareas completadas:", completadas)
    print("tareas pendientes:", pendientes)




def num_tareas(tareas, pendientes, completadas, texto_num_tareas):
    num_pendientes = len(pendientes)
    num_completas = len(completadas)
    total_tareas = num_completas + num_pendientes
    texto_num_tareas.setText(f"has completado {num_completas} tareas de {total_tareas} tareas")

def eliminar_tarea(completadas, pendientes, list_widget):
    for tarea in completadas:
        item = QListWidgetItem(tarea)
        if item.checkState == Qt.Unchecked:
            completadas.remove(item)
            pendientes.append(item)
            row = list_widget.currentRow()
            item = list_widget.takeItem(row)
            del item
    


def mensajes(tareas, pendientes, mensaje, num_tareas, completadas):
    if len(completadas) >=3:
        texto_mensaje = "vas bien"
    

def eliminar2(item, completadas, pendientes, list_widget, list_completadas):
    for tarea in completadas:
        if item.checkState() == Qt.Unchecked:
            completadas.remove(item)
            pendientes.append(item)
            row = list_completadas.takeItem(row)
            del item
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MoveFileHandler(FileSystemEventHandler):
  def on_modified(self, event):
    files = os.listdir(src_dir)
    for file_name in files:
        extension = get_ext(file_name)
        if extension != '':
            final_file = change_name(file_name, extension)
            dstntion_path = os.path.join(new_path(extension), final_file)
            shutil.move(new_path(final_file), dstntion_path)

def new_path(file):
    new_path = f'{src_dir}\{file}'
    return new_path

def get_ext(file_name):
    ext = os.path.splitext(file_name)[1] #Obtener extension, [1] para omitir el nombre
    format_ext = ext.replace('.','') #Quitar el '.' del nombre de la extension
    if format_ext != '':   #En caso de que este vacio omitir, vacio por carpetas
        if not os.path.exists(new_path(format_ext)):
            os.mkdir(new_path(format_ext))    #Si no existe el folder, crearlo con el nombre formateado del paso anterior
    return format_ext

def change_name(file_name, extension):
    count = 1
    solo_name = os.path.splitext(file_name)[0]      #Obtiene solo el nombre del archivo
    dstntion = new_path(extension)                  # Ruta de destino
    final_file = f'{solo_name}_{count}.{extension}'      #Nombre final del archivo
    dstntion_path = os.path.join(dstntion, final_file)   #Ruta de destino del archivo
    
    while os.path.exists(dstntion_path):
        count += 1
        final_file = f'{solo_name}_{count}.{extension}'     #Cambia el nombre solo de 'count'
        dstntion_path = os.path.join(dstntion, final_file)  #Actualiza la ruta de destino
    os.rename(new_path(file_name), new_path(final_file))
    return final_file

if __name__ == "__main__":
    global src_dir 
    src_dir = 'D:\Estudio\Python_labs\lab_move_file' #ruta de la carpeta

    #Creamos el manejador de eventos
    event_handler = FileSystemEventHandler() #manejador de eventos
    #calling functions
    event_handler = MoveFileHandler()

    #Creamos el observador
    observer = Observer()
    observer.schedule(event_handler, src_dir, recursive=True)
    #Iniciamos el observador
    observer.start()

    try:
        # Mantenemos el programa en ejecución mientras el observador esté activo    
        print("Monitoring")
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        # Detenemos el observador cuando el usuario presione Ctrl+C
        observer.stop()
    observer.join()
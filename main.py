import logging
from api import PixabayAPI
from mainThreads import HiloDescarga
import threading
# from contraste-rotacion-redimensiona import *
import concatenacion
import archivos


imagenesEntotal = 5
semaforo = threading.Semaphore(imagenesEntotal)
carpeta_imagenes = './imagenes'
query = 'computadoras'
api = PixabayAPI('15310764-bd15e0c149f0eebab022bf004', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, imagenesEntotal)
nombresArchivos = []
for u in urls:
  t = HiloDescarga(u,semaforo,api)
  t.start()
  nombresArchivos.append(u.split('/')[-1])
print(nombresArchivos[0])
print(nombresArchivos[1])
imagen1 = archivos.leer_imagen('./'+nombresArchivos[0])
imagen2 = archivos.leer_imagen('./'+nombresArchivos[1])
print(imagen1)
print(imagen2)
archivos.escribir_imagen('concatenada-vertical.jpg', concatenacion.concatenar_vertical([imagen1, imagen2]))      
# concatenacion.concatenar_horizontal([nombresArchivos[0],nombresArchivos[1]])

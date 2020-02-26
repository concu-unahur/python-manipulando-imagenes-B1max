import logging
from api import PixabayAPI
import threading

class HiloDescarga(threading.Thread):
  logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
  semaforo = threading.Semaphore()
  url = ''
  def __init__(self,_url,_semaforo,_api):
    super().__init__()
    self.semaforo = _semaforo
    self.url = _url
    self.api = _api

  def descargar(self,url):
    # logging.info(f'Descargando {url}')
    self.semaforo.acquire()
    try:
      self.api.descargar_imagen(url)
    finally:
      self.semaforo.release()
  def run(self):
    self.descargar(self.url)
from archivos import leer_imagen2, escribir_imagen2
# from skimage import exposure, transform, io
from skimage import exposure, transform, io



def contraste_adaptativo(img):
  # Contraste adaptativo: https://en.wikipedia.org/wiki/Adaptive_histogram_equalization
  img_adapteq = exposure.equalize_adapthist(img, clip_limit=0.03)
  return img_adapteq

def rotacion(img, angulo):
  img_rot = transform.rotate(img,angulo)
  return img_rot

def redimensiona(img, ancho, alto):
  img_resc = transform.resize(img,(ancho,alto))
  return img_resc

imagen1 = leer_imagen2('1.jpg')

escribir_imagen2('contraste.jpg', contraste_adaptativo(imagen1))    
escribir_imagen2('rotacion.jpg', rotacion(imagen1,25))    
escribir_imagen2('redim.jpg', redimensiona(imagen1,500,500))

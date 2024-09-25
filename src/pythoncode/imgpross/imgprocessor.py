import numpy as np
from matplotlib import pyplot as plt
import cv2
import pandas as pd

"""
Clase para manejar algunos procesos en imgs
"""
class ImgProcessor:
    def __init__(self, rutaImg,kernelX, kernelY):
        self.kernel_gaussian = (kernelX, kernelY)
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelX, kernelY))
        self.img = cv2.imread(rutaImg, cv2.IMREAD_GRAYSCALE)


    """
    Dilatacion morfologica:
    Conectar objetos o rellenar pequeños huecos.
    """
    def dilation(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"
        dilation = cv2.dilate(self.img, self.kernel, iterations=1)

        return dilation
    
    """
    Dilatacion morfologica:
    Conectar objetos o rellenar pequeños huecos.
    """
    def img_dilation(self, imagen):
        if imagen is None:
            return f"No se pudo cargar la imagen: {imagen}"
        dilation = cv2.dilate(imagen, self.kernel, iterations=1)

        return dilation

    """
    Gradiente morfologico:
    Detecta bordes de objetos en imgs binarias.
    """
    def grad(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"

        gradient = cv2.morphologyEx(self.img, cv2.MORPH_GRADIENT, self.kernel)
        
        return gradient
    
    """
    Gradiente morfologico:
    Detecta bordes de objetos en imgs binarias.
    """
    def img_grad(self, imagen):
        if imagen is None:
            return f"No se pudo cargar la imagen: {imagen}"

        gradient = cv2.morphologyEx(imagen, cv2.MORPH_GRADIENT, self.kernel)
        
        return gradient

    def img_closing(self, imagen):
        if imagen is None:
            return f"No se pudo cargar la imagen: {imagen}"
        
        closing = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, self.kernel)

        return closing


    """
    Apertura morfologica:
    Elimina pequeños objetos o ruido, pero mantiene la forma general de los objetos más grandes.
    """
    def opening(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"
        
        opening = cv2.morphologyEx(self.img, cv2.MORPH_OPEN, self.kernel)

        return opening

    """
    Apertura morfologica:
    Elimina pequeños objetos o ruido, pero mantiene la forma general de los objetos más grandes.
    """
    def img_opening(self, imagen):
        if imagen is None:
            return f"No se pudo cargar la imagen: {imagen}"
        
        opening = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, self.kernel)

        return opening

    """
    Erosion morfologica:
    Remover ruido o separar objetos conectados.
    """
    def erosion(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"
        
        #Erosion
        erosion = cv2.erode(self.img, self.kernel, iterations = 1)

        return erosion
    
    """
    Erosion morfologica:
    Remover ruido o separar objetos conectados.
    """
    def img_erosion(self, imagen):
        if imagen is None:
            return f"No se pudo cargar la imagen: {imagen}"
        
        #Erosion
        erosion = cv2.erode(imagen, self.kernel, iterations = 1)

        return erosion
    
    """
    Img data:
    Obtiene la informacion basica de la imagen.
    """
    def obtn_img_data(self):
        if self.img is None:
            print("No se pudo cargar la imagen.")
            return None
        
        h,w = self.img.shape
        channels = 1

        data_type = self.img.dtype

        img_size = self.img.size * self.img.itemsize

        info = {
                "width": w,
                "heigth":h,
                "channels": channels,
                "data_type": data_type,
                "image_size_bytes": img_size
                }

        return info

    """
    Img data:
    Obtiene la informacion basica de la imagen.
    """
    def img_data(self, imagen):
        if imagen is None:
            return f"No se pudo cargar la imagen: {imagen}"
        
        h,w = imagen.shape
        channels = 1

        data_type = imagen.dtype

        img_size = imagen.size * imagen.itemsize

        info = {
                "width": w,
                "heigth":h,
                "channels": channels,
                "data_type": data_type,
                "image_size_bytes": img_size
                }

        return info

    def threshold_otsu(self):
        _,thresh = cv2.threshold(self.img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh

    def img_threshold_otsu(self, imagen):
        _,thresh = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh


    """
    thresholding img:
    convertir una imagen en escala de grises en una imagen binaria.
    """
    def threshold(self):
        if self.img is None:
            return f"No se puede cargar la imagen: {self.img}"
        _, thresh = cv2.threshold(self.img, 128,255, cv2.THRESH_BINARY_INV)

        return thresh
    
    """
    thresholding img:
    convertir una imagen en escala de grises en una imagen binaria.
    """
    def img_threshold(self, imagen):
        if imagen is None:
            return f"No se puede cargar la imagen: {imagen}"
        _, thresh = cv2.threshold(imagen, 128,255, cv2.THRESH_BINARY_INV)

        return thresh


    """
    GaussianBlur:
    Aplicacion de filtro reduccion de ruido
    """
    def filtro_suave(self):
        blurred_img = cv2.GaussianBlur(self.img, self.kernel_gaussian,0)
        return blurred_img


    """
    GaussianBlur:
    Aplicacion de filtro reduccion de ruido
    """
    def img_filtro_suave(self, imagen):
        blurred_img = cv2.GaussianBlur(imagen, self.kernel_gaussian,0)
        return blurred_img



'''
DElimitar una

morph_close v2

ser mas descriptivo en mi documento

27 de septiembre, juntas de 5 a 7

proceso - luego luego en enero

manuscrito
presentacion
'''

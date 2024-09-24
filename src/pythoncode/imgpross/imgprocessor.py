import numpy as np
from matplotlib import pyplot as plt
import cv2
import pandas as pd


class ImgProcessor:
    def __init__(self, rutaImg):
        self.rutaImg = rutaImg
        self.kernel = np.ones((20,20), np.uint8)
        self.img = cv2.imread(self.rutaImg)

    def img_dilation(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"
        dilation = cv2.dilate(self.img, self.kernel, iterations=1)

        return dilation

    def img_grad(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"

        gradient = cv2.morphologyEx(self.img, cv2.MORPH_GRADIENT, self.kernel)
        
        return gradient

    def img_opening(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"
        
        opening = cv2.morphologyEx(self.img, cv2.MORPH_OPEN, self.kernel)
        print(opening)

        return opening

    def img_erosion(self):
        if self.img is None:
            return f"No se pudo cargar la imagen: {self.img}"
        
        #Erosion
        erosion = cv2.erode(self.img, self.kernel, iterations = 1)

        return erosion

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

    def img_gradient(self):
        laplacian = cv2.Laplacian(self.img, cv2.CV_64F)

        plt.subplot(2,2,1),plt.imshow(self.img,cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        
        plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
        plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

        plt.show()

    def img_threshold(self):
        if self.img is None:
            return f"No se puede cargar la imagen: {self.img}"
        _, thresh = cv2.threshold(self.img, 128,255, cv2.THRESH_BINARY_INV)

        return thresh

    def img_seg_thresholding(self):
        umbral_adaptativo = cv2.adaptiveThreshold(self.img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)
        return umbral_adaptativo


'''
DElimitar una

morph_close v2

ser mas descriptivo en mi documento

27 de septiembre, juntas de 5 a 7

proceso - luego luego en enero

manuscrito
presentacion
'''

import numpy as np
from matplotlib import pyplot as plt
import cv2
import pandas as pd
from .imgprocessor import ImgProcessor

"""
Clase para manejar las operaciones de segmentaciojn
"""
class SegImg:

    def __init__(self, imagen):
        self.imagenCV2Read = ImgProcessor(imagen,5,5)
        self.images_dic = {}

    def seg_img_morph(self):
        self.images_dic['Original']=self.imagenCV2Read.img

        img_blurred = self.imagenCV2Read.filtro_suave()
        self.images_dic['Blurred Image'] = img_blurred

        threshImg = self.imagenCV2Read.img_threshold_otsu(img_blurred)
        self.images_dic['Theshold Image']= threshImg

        opening = self.imagenCV2Read.img_opening(threshImg)
        self.images_dic['Opening Image']=opening

        closing = self.imagenCV2Read.img_closing(opening)
        self.images_dic['Closing Image']=closing

        contours,_ = cv2.findContours(closing,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        segmented_img = cv2.drawContours(self.imagenCV2Read.img.copy(), contours,-1, (0,255,0),2)
        self.images_dic['Segmented Image']= segmented_img

        return self.images_dic

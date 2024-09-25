import sys
from imgpross.imgprocessor import ImgProcessor
from plots.imgplots.imgplots import ImgPlots
from imgpross.seg_mastografia import SegImg
import cv2

def infoMap(info):
    if info:
        print("Informacion de la imagen")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No se pudo obtener la informacion de la imagen.")


if __name__ == "__main__":
    # Obtiene la imagen pasada por terminal
    img = sys.argv[1]

    imgOrig = cv2.imread(img)
    segImgPross = SegImg(img)

    morphImg = segImgPross.seg_img_morph()

    plotOrgMorph = ImgPlots()

    #graficar imagen original y la morphologica
    plotOrgMorph.graficar_imagenes_dic(morphImg)




import sys
from matplotlib import pyplot as plt
from imgpross.imgprocessor import ImgProcessor
from plots.imgplots.imgplots import ImgPlots

def infoMap(info):
    if info:
        print("Informacion de la imagen")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No se pudo obtener la informacion de la imagen.")


if __name__ == "__main__":
    img_prossR = ImgProcessor(sys.argv[1])
    img_prossL = ImgProcessor(sys.argv[2])
    
    plotsImgs =  ImgPlots(img_prossR.img, img_prossL.img)

    plotsImgs.orig_dilation(img_prossR.img_dilation(),img_prossL.img_dilation())


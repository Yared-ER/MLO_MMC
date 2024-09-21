import sys
from matplotlib import pyplot as plt
from imgpross.imgprocessor import ImgProcessor

def main():
    img_prossr = ImgProcessor(sys.argv[1])
    #infoMap(img_prossr.obtn_img_data())
    #thres_orig(img_prossr.img,img_prossr.img_seg_thresholding())
    #erros_orig(img_prossr.img,img_prossr.img_erosion())
    #open_orig(img_prossr.img, img_prossr.img_opening())
    #dil_orig(img_prossr.img, img_prossr.img_dilation())
    #orig_grad(img_prossr.img, img_prossr.img_grad())

def thres_orig(original, umbral):
    plt.figure('Imagen original')
    plt.imshow(original, cmap='gray')
    plt.title('Imagen original')
    plt.axis('off')


    #umbral
    plt.figure('Imagen Umbral')
    plt.imshow(umbral, cmap='gray')
    plt.title('Imagen Umbral')
    plt.axis('off')

    plt.show()

def orig_grad(original, gradiente):
    plt.subplot(121),plt.imshow(original),plt.title('Original')

    plt.subplot(122),plt.imshow(gradiente),plt.title('Gradiente')

    plt.show()

def dil_orig(original, dilation):
    plt.subplot(121),plt.imshow(original),plt.title('Original')

    plt.subplot(122),plt.imshow(dilation),plt.title('Dilation')
    plt.show()

def erros_orig(original, erosion):
    # imagen original
    plt.subplot(121),plt.imshow(original),plt.title('Original')

    # imagen erosionada
    plt.subplot(122),plt.imshow(erosion),plt.title('Erosion')

    plt.show()


def open_orig(original, opening):
    plt.subplot(121),plt.imshow(original),plt.title('Original')
    plt.subplot(122), plt.imshow(opening),plt.title('Openning')
    plt.show()


def infoMap(info):
    if info:
        print("Informacion de la imagen")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("No se pudo obtener la informacion de la imagen.")


if __name__ == "__main__":
    img_prossr = ImgProcessor(sys.argv[1])
    erros_orig(img_prossr.img, img_prossr.img_erosion())

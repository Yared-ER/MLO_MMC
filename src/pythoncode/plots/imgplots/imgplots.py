from matplotlib import pyplot as plt
import math
class ImgPlots:

    def graficar_org_mdf(self, imagenOrg, tituloOrg, imagenMdf, tituloMdf):
        plt.subplot(2,2,1)
        plt.imshow(imagenOrg)
        plt.title(tituloOrg)

        plt.subplot(2,2,2)
        plt.imshow(imagenMdf)
        plt.title(tituloMdf)

        plt.tight_layout()
        plt.show()

    def graficar_IMG(self, imagen, titulo):
        plt.imshow(imagen, cmap='gray')
        plt.title(titulo)
        plt.show()

    def graficar_4_img(self, img1, img2, img3, img4, titulo1, titulo2, titulo3, titulo4):
        plt.subplot(2,2,1)
        plt.imshow(img1)
        plt.title(titulo1)

        plt.subplot(2,2,2)
        plt.imshow(img2)
        plt.title(titulo2)
    
        plt.subplot(2,2,3)
        plt.imshow(img3)
        plt.title(titulo3)

        plt.subplot(2,2,4)
        plt.imshow(img4)
        plt.title(titulo4)

        plt.tight_layout()
        plt.show()

    def graficar_imagenes_dic(self, diccionarioImagenes):
        if diccionarioImagenes is None:
            return f"No contiene valores el diccionario: {diccionarioImagenes}"
        
        num_images = len(diccionarioImagenes)
        rows = math.ceil(num_images / 2)

        plt.figure(figsize=(10,5 * rows))

        for i,(title, imagen) in enumerate(diccionarioImagenes.items()):
            plt.subplot(rows, 2,i + 1)
            plt.title(title)

            if len(imagen.shape) == 2:
                plt.imshow(imagen, cmap='gray')
            else:
                plt.imshow(imagen)
            plt.axis('off')
        plt.tight_layout()
        plt.show()
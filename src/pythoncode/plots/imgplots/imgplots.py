from matplotlib import pyplot as plt

class ImgPlots:

    def __init__(self, originalR, originalL):
        self.imgOriginalR = originalR
        self.imgOriginalL = originalL

    def orig_gradiente(self, gradienteR, gradienteL):
        plt.subplot(2,2,1)
        plt.imshow(self.imgOriginalR)
        plt.title('Original Derecha')

        plt.subplot(2,2,2)
        plt.imshow(gradienteR)
        plt.title('IMG Gradiente Derecha')

        plt.subplot(2,2,3)
        plt.imshow(self.imgOriginalL)
        plt.title('Original Izquierda')

        plt.subplot(2,2,4)
        plt.imshow(gradienteL)
        plt.title('IMG Gradiente Izquierda')

        plt.tight_layout()
        plt.show()

    def orig_dilation(self, dilationR, dilationL):
        plt.subplot(2,2,1)
        plt.imshow(self.imgOriginalR)
        plt.title('Original Derecha')

        plt.subplot(2,2,2)
        plt.imshow(dilationR)
        plt.title('IMG Dilation Derecha')

        plt.subplot(2,2,3)
        plt.imshow(self.imgOriginalL)
        plt.title('Original Izquierda')

        plt.subplot(2,2,4)
        plt.imshow(dilationL)
        plt.title('IMG Dilation Izquierda')

        plt.tight_layout()
        plt.show()

    def orig_erosion(self, erosionR, erosionL):
        plt.subplot(2,2,1)
        plt.imshow(self.imgOriginalR)
        plt.title('Original Derecha')

        plt.subplot(2,2,2)
        plt.imshow(erosionR)
        plt.title('IMG Erosion Derecha')

        plt.subplot(2,2,3)
        plt.imshow(self.imgOriginalL)
        plt.title('Original Izquierda')

        plt.subplot(2,2,4)
        plt.imshow(erosionL)
        plt.title('IMG Erosion Izquierda')

        plt.tight_layout()
        plt.show()

    def orig_open(self, openingR, openingL):
        plt.subplot(2,2,1)
        plt.imshow(self.imgOriginalR)
        plt.title('Original Derecha')

        plt.subplot(2,2,2)
        plt.imshow(openingR)
        plt.title('IMG Opening Derecha')

        plt.subplot(2,2,3)
        plt.imshow(self.imgOriginalL)
        plt.title('Original Izquierda')

        plt.subplot(2,2,4)
        plt.imshow(openingL)
        plt.title('IMG Opening Izquierda')

        plt.tight_layout()
        plt.show()



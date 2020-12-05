# -*- coding: utf-8 -*-
#Spatial Image Enhancement
#  Enhance the three given images by three spatial image enhancement techniques:
#    power-law (gamma) correction
import numpy as np
import cv2
import os
from ImageProcessingMethod import ImageEnhancementMethod
from matplotlib import pyplot as plt

def main():
    FileName = os.path.realpath(__file__)
    DirName = os.path.dirname(FileName)
    BMPPath = DirName + '\\TestImage\\Lena.bmp'  #Cameraman.bmp, Peppers.bmp

    ProcessImage = cv2.imread(BMPPath)
    gamma = 0.2
    for i in range(1, 5):
        plt.subplot(2, 2, i)
        plt.title('gamma:'+ str(gamma*i))
        plt.imshow(ImageEnhancementMethod().GammaCorrection(ProcessImage, 1, gamma*i)) #0.2拉開暗部 => 0.5不變 => 0.8拉開亮部

    plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)
    plt.show()


if __name__ == "__main__":
    main()

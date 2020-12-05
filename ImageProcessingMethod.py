import numpy as np


class ImageEnhancementMethod:
    def GammaCorrection(self, InputImage, c, gamma):
        ResultImage = (c*InputImage/255)**gamma
        return ResultImage



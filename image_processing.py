import abc
import numpy as np
import cv2


class ImageFilter(abc.ABC):

    @staticmethod
    def get_filter(image, params):
        filter = params['filter']

        if filter == "resize":
            return Resize(image, params)
        elif filter == "gray":
            return Gray(image, params)
        
        raise ValueError(f"filter '{filter}' not found")

    @abc.abstractmethod
    def apply_filter(self):
        raise ValueError(f'Not implemented')



class Resize(ImageFilter):
    def __init__(self, image, params):
            self.image = image
            self.params = params

            if params['scale'] <= 0:
                raise ValueError(f'scale cannot have such a meaning')

    def apply_filter(self):

        kernel = np.ones((3, 3), np.float32) / 9
        blur = cv2.filter2D(self.image, -1, kernel)
        scale = self.params['scale']
        resize_image = blur[::scale, ::scale]

        return resize_image
        


class Gray(ImageFilter):
    def __init__(self, image, params):
            self.image = image
            self.params = params

    def apply_filter(self):
        b = self.image[:, :, 0]
        g = self.image[:, :, 1]
        r = self.image[:, :, 2]

        gray_image = 







        



class Vignette(ImageFilter):
    def __init__(self, image, params):
        super().__init__(image, params)

    def apply_filter(self):
        return super().apply_filter()


class Pixelation(ImageFilter):
    def __init__(self, image, params):
        super().__init__(image, params)

    def apply_filter(self):
        return super().apply_filter()


class ColorBorder(ImageFilter):
    def __init__(self, image, params):
        super().__init__(image, params)

    def apply_filter(self):
        return super().apply_filter()


class FigureBorder(ImageFilter):
    def __init__(self, image, params):
        super().__init__(image, params)

    def apply_filter(self):
        return super().apply_filter()


class CameraGlare(ImageFilter):
    def __init__(self, image, params):
        super().__init__(image, params)

    def apply_filter(self):
        return super().apply_filter()
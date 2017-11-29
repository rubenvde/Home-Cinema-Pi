from debug import Debugger


class ImageLoader:
    imagefolder = None

    @staticmethod
    def set_folder(imagefolder):
        ImageLoader.imagefolder = imagefolder

    @staticmethod
    def get_image(name):
        return ImageLoader.imagefolder + "/" + name

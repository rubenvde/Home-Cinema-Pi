from os import listdir
from os.path import isfile, join, splitext
from debug import Debugger

class FontLoader:
    array_of_fonts = []
    fontfolder = None

    @staticmethod
    def set_folder(fontfolder):
        FontLoader.fontfolder = fontfolder
        onlyfiles = [f for f in listdir(fontfolder) if isfile(join(fontfolder, f))]
        fontfiles = [k for k in onlyfiles if '.ttf' in k]
        fontnames = [splitext(each)[0] for each in fontfiles]
        FontLoader.array_of_fonts = fontnames
        Debugger.back_print("Found " + str(len(FontLoader.array_of_fonts)) + " fonts")

    @staticmethod
    def get_font(name):
        if name in FontLoader.array_of_fonts:
            return FontLoader.fontfolder + "/" + name + '.ttf'
        else:
            raise NameError('Font not found')

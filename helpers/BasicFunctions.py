class BasicFunctions:
    __root__ = None

    @staticmethod
    def hex_to_rgb(hex):
        localhex = hex.lstrip('#')
        localfloats = []
        for color in tuple(int(localhex[i:i + 2], 16) for i in (0, 2, 4)):
            localfloats.append(color / 255.0)
        return localfloats

    @staticmethod
    def get_root():
        return BasicFunctions.__root__

    @staticmethod
    def set_root(root):
        BasicFunctions.__root__ = root
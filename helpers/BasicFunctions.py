class BasicFunctions:
    @staticmethod
    def hex_to_rgb(hex):
        localhex = hex.lstrip('#')
        return tuple(int(localhex[i:i + 2], 16) for i in (0, 2, 4))

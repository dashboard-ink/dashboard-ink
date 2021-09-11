
class Plugin:
    def __init__(self, startX, startY):
        self.startX = startX
        self.startY = startY

    def draw(self, black_layer, red_layer):
        raise NotImplementedError

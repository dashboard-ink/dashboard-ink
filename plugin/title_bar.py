from datetime import datetime
from .plugin import Plugin
from core import fonts

class TitleBar(Plugin):
    def draw(self, black_layer, red_layer):
        current_date = datetime.now()
        black_layer.text((self.startX + 2, self.startY), current_date.strftime('%Y-%m-%d'), font = fonts.font24, fill = 0)
        black_layer.text((self.startX + 310, self.startY), 'Updated at: ' + current_date.strftime("%Y-%m-%d %H:%M:%S"), font = fonts.font12, fill = 0)

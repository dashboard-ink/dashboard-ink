from datetime import datetime
from ./plugin import Plugin

class TitleBar(Plugin):
    def draw(black_layer, red_layer):
        current_date = datetime.now()
        black_layer.text((self.maxX + 2, self.maxY), current_date.strftime('%Y-%m-%d'), font = fonts.font24, fill = 0)
        black_layer.text((self.maxX + 310, self.maxY), 'Updated at: ' + current_date.strftime("%Y-%m-%d %H:%M:%S"), font = fonts.font12, fill = 0)
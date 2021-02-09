class Bike:

    def __init__(self, manufacturer, model, description, buy_cost, sell_price, stock_level, mark_up=None, id=None):
        self.manufacturer = manufacturer
        self.model = model
        self.description = description
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.stock_level = stock_level
        self.mark_up = round((((float(self.sell_price) - float(self.buy_cost)) / float(self.buy_cost)) * 100), 2) 
        self.id = id

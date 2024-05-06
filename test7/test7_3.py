

class OutOfStack(Exception):
    pass

class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        try:
            if self.stock[color]==0:
                raise   OutOfStack
            else:
                self.stock[color] = self.stock[color]-1
                print(f"购买成功,库存为{self.stock[color]}")
        except OutOfStack as e:
            print("超出库存",e)



candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
while(1):
    x=input("请输入您想买的颜色\n")
    if x=="no":
        print("购买结束")
        break
    else:
        candle_shop.buy(x)

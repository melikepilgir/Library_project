class product:
    def __init__(self, name, price , isActive):
        self.name = name
        self.price = price
        self.isActive = isActive


p1 = product("Iphone 15", 50000, True)
p2 = product("Samsung S24", 60000, True)
p3 = product( "MK", 70000, False)

urunler = [p1, p2, p3]

for urun in urunler:
    if urun.isActive:
        print(f"ürün adı: {urun.name} ürün fiyatı: {urun.price} ")


sonuc = p2.name

print(sonuc)
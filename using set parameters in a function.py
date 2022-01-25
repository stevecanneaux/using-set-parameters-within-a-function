def GrossPrice(netPrice, vat = 17.5):
    gross = netPrice * (vat/100)
    return gross

result = GrossPrice(100.00)
print("total is:" , result)
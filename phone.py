import phoneclass as pc

phone1 = pc.phone()
phone2 = pc.phone()

phone1.set_manufact(7777777)
phone1.set_model('iphone')
phone1.set_retail_price(760)

phone2.set_manufact(555555)
phone2.set_model('android')
phone2.set_retail_price(550)

print(phone1.get_manufact(), phone1.get_model(), phone1.get_retail_price())
print(phone2.get_manufact(), phone2.get_model(), phone2.get_retail_price())
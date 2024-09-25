panjang = float(input("panjang = "))
lebar = float(input("lebar = "))
satuan = str(input("satuan (meter/inch) = "))
# 1 inch = 0.0254 meter
if satuan == "meter":
    luas_meter = panjang * lebar
    print("luas dengan satuan meter adalah","", luas_meter, "m^2")
elif satuan == "inch":
    one_inch = 0.0254
    p_inch = panjang * one_inch 
    l_inch = lebar * one_inch 
    luas_inch = p_inch * l_inch
    print("luas dengan satuan inch adalah","",luas_inch, "m^2")
else:
    print("anda harus memilih satuan")

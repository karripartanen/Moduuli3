Year = int(input("Antaisitko haluamasi vuosiluvun, kerron onko se karkausvuosi: "))

if Year % 4 == 0 or Year % 100 == 0 and Year % 400 == 0:
    print("Vuosi "+str(Year)+" on karkausvuosi")
else:
    print("Vuosi "+str(Year)+" ei ole karkausvuosi")









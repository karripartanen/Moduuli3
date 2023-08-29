Hytti = input("Kertoisitko varaamasi laivan "
              "hyttiluokan (A, B, C tai LUX): ")

HyttiA = "A on ikkunallinen hytti autokannen yläpuolella."
HyttiB = "B on ikkunaton hytti autokannen yläpuolella."
HyttiC = "C on ikkunaton hytti autokannen alapuolella."
HyttiLUX = "LUX on parvekkeellinen hytti yläkannella."

if Hytti == "A" or Hytti == "a":
    print(""+HyttiA+"")
elif Hytti == "B" or Hytti == "b":
    print(""+HyttiB+"")
elif Hytti == "C" or Hytti == "c":
    print(""+HyttiC+"")
elif Hytti == "LUX" or Hytti == "lux" or Hytti == "Lux":
    print(""+HyttiLUX+"")
else:
    print("Virheellinen hyttiluokka")




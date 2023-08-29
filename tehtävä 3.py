Gender = str(input("Antaisitko sukupuolesi (Mies/Nainen): "))
HG_Reading = int(input("Antaisitko hemoglobiiniarvosi (g/l): "))
GenderID = ""

if Gender == "Mies" or Gender == "mies":
    GenderID = "M"
elif Gender == "Nainen" or Gender == "nainen":
    GenderID = "F"

if GenderID == "M" and 134<=HG_Reading>=195:
    print("Hemoglobiiniarvosi on normaali.")
elif GenderID == "M" and 195<HG_Reading:
    print("Hemoglobiiniarvosi on koholla.")
elif GenderID == "M" and 134>HG_Reading:
    print("Hemoglobiiniarvosi on alhainen.")

if GenderID == "F" and 117<=HG_Reading>=175:
    print("Hemoglobiiniarvosi on normaali.")
elif GenderID == "F" and 175<HG_Reading:
    print("Hemoglobiiniarvosi on koholla.")
elif GenderID == "F" and 117>HG_Reading:
    print("Hemoglobiiniarvosi on alhainen.")




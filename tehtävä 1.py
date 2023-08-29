Kuha = float(input("Antaisitko saamasi kuhan pituuden senttimetreinä: "))
if Kuha < 37:
    print("Kuhasi on alamittainen ja se täytyy palauttaa vesistöön. "
          "Kuhan sallitusta pituudesta puuttuu "+str((37-Kuha))+ " senttimetriä")
else:
    print("Kuhasi on sallituissa mitoissa. Voit pitää kalan!")



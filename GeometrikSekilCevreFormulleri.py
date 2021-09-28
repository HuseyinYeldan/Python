print("Geometrik Şekil Çevre Formüllerine Hoşgeldiniz! Lütfen Seçim Yapınız.")
print("---------------------------------------------------------------")
print("")
print("Kare Formülü için '1' yazınız. ")
print("Dikdörtgen Formülü için '2' yazınız. ")
print("Çember Formülü için '3' yazınız. ")
print("Üçgen Formülü için '4' yazınız. ")
print("Düzgün Çokgen Formülü için '5' yazınız. ")
print("")
print("---------------------------------------------------------------")
formul = input("Lütfen seçim yapınız: ")

print("")

pi = 3.14

if formul == "1":
    karekenaruzunlugu = float(input("Karenizin bir kenar uzunluğunu giriniz: "))

    kareformul = karekenaruzunlugu*4

    print("Sonuç: ",kareformul)

elif formul == "2":
    dikdortgenkisa = float(input("Dikdörtgeninizin kısa olan kenarının uzunluğunu giriniz: "))
    dikdortgenuzun = float(input("Dikdörtgeninizin uzun olan kenarının uzunluğunu giriniz: "))

    if dikdortgenkisa>=dikdortgenuzun:
        print("Dikdörtgenin kısa kenarı uzun kenarından yüksek veya eşit bir değere sahip olamaz.")
    else:
        dikdortgenformul = (dikdortgenkisa*2)+(dikdortgenuzun*2)
        print("Sonuç: ",dikdortgenformul)

elif formul == "3":

    cemberyaricap = float(input("Çemberinizin yarı çapını(r) giriniz: "))
    cemberformul = 2*pi*cemberyaricap
    print("Sonuç: ",cemberformul)

elif formul == "4":

    ucgen1 = float(input("Üçgeninizin ilk kenarını giriniz: "))
    ucgen2 = float(input("Üçgeninizin ikinci kenarını giriniz: "))
    ucgen3 = float(input("Üçgeninizin üçüncü kenarını giriniz: "))

    ucgenformul= ucgen1*ucgen2*ucgen3

    print("Sonuç: ",ucgenformul)

elif formul=="5":

    duzguncokgenkenar = float(input("Düzgün çokgeninizin kaç kenarı olduğunu giriniz: "))
    cokgenuzunlugu = float(input("Çokgeninizin bir kenarının uzunluğunu giriniz: "))

    cokgenformul= duzguncokgenkenar*cokgenuzunlugu
    
    print("Sonuç: "+cokgenformul)

else:
    print("Hatalı Giriş yaptınız!")
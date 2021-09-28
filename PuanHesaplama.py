isim = input("Ad ve Soyadınızı giriniz: ")
dersismi = input("Ders ismini giriniz:")
odevpuan= float(input("Ödev Puanınızı Giriniz:"))
vizepuan= float(input("Vize Puanınızı Giriniz:"))
finalpuan= float(input("Final Puanınızı Giriniz:"))

#Ödev puanı = %20
#Vize puanı = %30
#Final puanı = %50

odevsonuc = (odevpuan*20)/100
vizesonuc = (vizepuan*30)/100
finalsonuc = (finalpuan*50)/100

toplampuan = odevsonuc + vizesonuc + finalsonuc

print("")


if toplampuan<50 and toplampuan>=0:

 print("---------------------------------------------")
 print("Sayın", isim, "toplam puanınız: ", toplampuan)
 print("Malesef", dersismi,"dersinden kaldınız.")
 print("---------------------------------------------")


elif toplampuan>=50 and toplampuan<=100:
 print("---------------------------------------------")
 print("Sayın", isim, "toplam puanınız: ", toplampuan)
 print("Tebrikler", dersismi,"dersini geçtiniz!")
 print("---------------------------------------------")

elif odevpuan > 100 or odevpuan<0:
 print("---------------------------------------------")
 print("Hatalı bir giriş yaptınız! Lütfen tekrar deneyiniz!")
 print("---------------------------------------------")

elif vizepuan > 100 or vizepuan<0:
 print("---------------------------------------------")
 print("Hatalı bir giriş yaptınız! Lütfen tekrar deneyiniz!")
 print("---------------------------------------------")

elif finalpuan > 100 or vizepuan <0:
 print("---------------------------------------------")
 print("Hatalı bir giriş yaptınız! Lütfen tekrar deneyiniz!")
 print("---------------------------------------------")

else:
 print("---------------------------------------------")
 print("Hatalı bir giriş yaptınız! Lütfen tekrar deneyiniz!")
 print("---------------------------------------------")   

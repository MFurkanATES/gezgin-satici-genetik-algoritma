import numpy as np
import random as rd
import time

#jenerasyon: populasyon elemanlarinin olusturdugu topluluk
#populasyon: jenerasyonu olusturan her bir eleman

#koordinat noktalarinin sayisi
koordinat_sayisi = 15

#olusturulmasi istenilen jenerasyon sayisi
jenerasyon_sayisi = 100

#olusturulmasi istenilen populasyon sayisi
populasyon_sayisi = 20

#caprazlanmasi istenilen noktaların orani
caprazlama_orani = 20

#populasyonda istenilen mutasyon orani
mutasyon_orani = 10

#hesaplanan en kisa rotanin listesi
en_kisa_koordinatlar_listesi = np.zeros(populasyon_sayisi,dtype=int)

#hesaplanan en kisa rotanin uzunlugu
en_kisa_rota_menzili = 9999999999

#toplam_yol degiskeni- dongu icerisinde mesafeleri hesaplarken degisiyor bu degisken
toplam_yol = 0

#en kisa rotaya sahip jenerasyonun kacinci jenerasyon oldugunun numarasi
en_iyi_jenerasyon_numarasi = 0

#bulunan jenerasyonda olusturulan populasyonlarin kendi yol uzunlugunu bulunduran liste
populasyon_menzil_listesi = np.zeros((populasyon_sayisi,1),dtype = float)

#populasyonu olusturuyoruz
populasyon = np.empty((populasyon_sayisi,koordinat_sayisi),dtype = int) 

#rastgele olusturulan koordinat listesi ,gercek uygulamada normal koordinatlar verilecek
noktalar_x_y_z = np.random.randint(200,size=((koordinat_sayisi,3)))
#olusturulan koordinatlarin kontrolu
#print (noktalar_x_y_z)

#loop zamani baslangici,anlik zamani aliyoruz
loop_ilk_zaman = time.time()

#populasyon listesi rastgele,sirali olmadan diziliyor
for i in range(0,populasyon_sayisi):             
        populasyon[i] = np.random.permutation(koordinat_sayisi)
#olusturulan populasyonu kontrol  
#print (np.shape(populasyon_menzil_listesi))

#populasyonda bulunan koordinatlarin mesafe hesaplari
for i in range(0,populasyon_sayisi):
  for j in range(0,koordinat_sayisi-1):
    x = noktalar_x_y_z[populasyon[i,j],0] - noktalar_x_y_z[populasyon[i,j+1],0]
    y = noktalar_x_y_z[populasyon[i,j],1] - noktalar_x_y_z[populasyon[i,j+1],1]
    z = noktalar_x_y_z[populasyon[i,j],2] - noktalar_x_y_z[populasyon[i,j+1],2]
    #print(x,y,z)
    toplam_yol = toplam_yol + np.sqrt(x**2 + y**2 + z**2)
  populasyon_menzil_listesi[i] = toplam_yol
  if(toplam_yol < en_kisa_rota_menzili):
    en_kisa_rota_menzili = toplam_yol
    en_kisa_koordinatlar_listesi = populasyon[i,:]
  toplam_yol = 0
  #print (populasyon_menzil_listesi)
#koordinat_listesi = []
#for i in range(0,koordinat_sayisi):
#  koordinat_listesi.append(i)
#kontrol_listesi_1 =np.zeros((koordinat_sayisi,1),dtype = int)
#kontrol_listesi_2 =np.zeros((koordinat_sayisi,1),dtype = int)
#print (koordinat_listesi,kontrol2[2])

#kontrol icin koordinat listesinin yapilmasi
#tekrarli koordinatlari bulmak icin olusturuldu
koordinat_listesi = np.arange(0,koordinat_sayisi,1)

for s in range(0,jenerasyon_sayisi):
  #caprazlama oranina gore kac tane koordinat caprazlanacaksa 
  caprazlanacak_populasyon_sayisi = int(populasyon_sayisi * caprazlama_orani/100)
  if (caprazlanacak_populasyon_sayisi % 2 == 1): 
    caprazlanacak_populasyon_sayisi +=  1
  caprazlanacak_koordinatlar = np.random.choice(populasyon_sayisi , size = caprazlanacak_populasyon_sayisi , replace = False)
  for i in range(0,caprazlanacak_populasyon_sayisi,2):
    caprazlama_noktasi = np.random.choice(koordinat_sayisi ,1) 
    #print(caprazlama_noktasi)
    kontrol_listesi_1 = np.copy(koordinat_listesi)
    #print (kontrol_listesi_1)
    kontrol_listesi_2 = np.copy(koordinat_listesi) 
    #capramazlama noktasindan sonrasini kopyaliyor,pythonda degiskenler dinamik degistigi için boyle ayri bir degiskene attik
    kopyalama_noktasi = np.copy(populasyon[caprazlanacak_koordinatlar[i],caprazlama_noktasi[0]:koordinat_sayisi])
    #print(kopyalama_noktasi)
    populasyon[caprazlanacak_koordinatlar[i],caprazlama_noktasi[0]:koordinat_sayisi] = populasyon[caprazlanacak_koordinatlar[i+1],caprazlama_noktasi[0]:koordinat_sayisi]
    populasyon[caprazlanacak_koordinatlar[i+1],caprazlama_noktasi[0]:koordinat_sayisi] = kopyalama_noktasi
    #tekrarli olan elemanlari kontrol etmek icin in1d kullaildi eger iki dizide ayni eleman varsa true dondurdu
    #tekrarsiz eleman listede olmayan yani yerine tekrarli baska bir eleman var demektir
        
    dinamik_liste_1 = np.in1d( koordinat_listesi, populasyon[caprazlanacak_koordinatlar[i],:])         
    dinamik_liste_2 = np.in1d( koordinat_listesi, populasyon[caprazlanacak_koordinatlar[i+1],:])
    index_1 = np.argwhere(dinamik_liste_1 == True )
    kontrol_listesi_1 =np.delete(kontrol_listesi_1 , index_1)
    #print (kontrol_listesi_1)
    index_2 = np.argwhere(dinamik_liste_2 == True )
    kontrol_listesi_2 =np.delete(kontrol_listesi_2 , index_2)
    #print (kontrol_listesi_2)
    for t in range(0,caprazlama_noktasi[0]):
      for r in range(caprazlama_noktasi[0],koordinat_sayisi):
        if(populasyon[caprazlanacak_koordinatlar[i],t] == populasyon[caprazlanacak_koordinatlar[i],r]):
          #print (populasyon[caprazlanacak_koordinatlar[i],:],"populasyon-1-kontrol_listesi_1",kontrol_listesi_1)
          populasyon[caprazlanacak_koordinatlar[i],t] = np.random.choice(kontrol_listesi_1,1)
          kontrol_listesi_1 = np.delete(kontrol_listesi_1,np.argwhere(kontrol_listesi_1 == populasyon[caprazlanacak_koordinatlar[i],t]))
          #print (populasyon[caprazlanacak_koordinatlar[i],:],"populasyon-1-son-")
        if(populasyon[caprazlanacak_koordinatlar[i+1],t] == populasyon[caprazlanacak_koordinatlar[i+1],r]):
          #print (populasyon[caprazlanacak_koordinatlar[i+1],:],"populasyon-2-kontrol_listesi_2",kontrol_listesi_2)
          populasyon[caprazlanacak_koordinatlar[i+1],t] = np.random.choice(kontrol_listesi_2,1)
          kontrol_listesi_2 = np.delete(kontrol_listesi_2,np.argwhere(kontrol_listesi_2 == populasyon[caprazlanacak_koordinatlar[i+1],t]))
          #print (populasyon[caprazlanacak_koordinatlar[i+1],:],"populasyon-2-son-\n") 

   #mutasyon 
  mutasyonlu_koordinat_sayisi = int(populasyon_sayisi * koordinat_sayisi * mutasyon_orani / 100)
  if(mutasyonlu_koordinat_sayisi % 2 == 1):
    mutasyonlu_koordinat_sayisi += 1
  #print "mutasyonlu_koordinat_sayisi", mutasyonlu_koordinat_sayisi
  for i in range(0,mutasyonlu_koordinat_sayisi ,2):
    mutasyon_populasyon_elemani = np.random.choice(populasyon_sayisi,1)
    mutasyon_degistirme_koordinatlari = np.random.choice(koordinat_sayisi,2)
    #print "mutasyon_populasyon_elemani",mutasyon_populasyon_elemani,mutasyon_degistirme_koordinatlari[0],mutasyon_degistirme_koordinatlari[1]
    degisken = np.copy(populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_koordinatlari[0]])
    populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_koordinatlari[0]] = populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_koordinatlari[1]]
    populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_koordinatlari[1]] = degisken
    #print populasyon
  for i in range(0,populasyon_sayisi):
    for j in range(0,koordinat_sayisi-1):
      x = noktalar_x_y_z[populasyon[i,j],0] - noktalar_x_y_z[populasyon[i,j+1],0]
      y = noktalar_x_y_z[populasyon[i,j],1] - noktalar_x_y_z[populasyon[i,j+1],1]
      z = noktalar_x_y_z[populasyon[i,j],2] - noktalar_x_y_z[populasyon[i,j+1],2]
      #print(x,y,z)
      toplam_yol = toplam_yol + np.sqrt(x**2 + y**2 + z**2)
    populasyon_menzil_listesi[i] = toplam_yol
    if(toplam_yol < en_kisa_rota_menzili):
      en_kisa_rota_menzili = toplam_yol
      en_kisa_koordinatlar_listesi = populasyon[i,:]
      en_iyi_jenerasyon_numarasi = s
    toplam_yol = 0
  print ("jenerasyon numarasi",en_iyi_jenerasyon_numarasi,"en iyi rota uzunlugu",en_kisa_rota_menzili,"en iyi rota",en_kisa_koordinatlar_listesi)
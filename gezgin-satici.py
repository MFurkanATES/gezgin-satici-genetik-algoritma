import numpy as np
import random as rd
import time
nokta_sayisi = 35
jenerasyon =  1000
populasyon_sayisi = 20
caprazlama_orani = 20
mutasyon_orani = 5
en_iyi_rota = np.zeros(nokta_sayisi,dtype=int)
en_iyi_yol = 99999999999 
toplam_yol = 0 
en_iyi_jenerasyon = 0
toplam_nokta_uzakliklari = np.zeros((populasyon_sayisi,1))
populasyon = np.empty((populasyon_sayisi,nokta_sayisi),dtype = int) 
noktalar_x_y = np.random.randint(200,size=((nokta_sayisi,2)))
a = time.time()
#print noktalar_x_y
for i in range(0,populasyon_sayisi):             
        populasyon[i] = np.random.permutation(nokta_sayisi)
#print populasyon,"\n","populasyon"print index
for i in range(0,populasyon_sayisi):
        for j in range(0,nokta_sayisi-1):
                x = noktalar_x_y[populasyon[i,j],0] - noktalar_x_y[populasyon[i,j+1],0]
                y = noktalar_x_y[populasyon[i,j],1] - noktalar_x_y[populasyon[i,j+1],1]
                toplam_yol = toplam_yol + np.sqrt( x**2 + y**2)
        toplam_nokta_uzakliklari[i] = toplam_yol
        if(toplam_yol < en_iyi_yol):
                en_iyi_yol = toplam_yol
                en_iyi_rota = populasyon[i,:]
        toplam_yol = 0
#print "toplam_nokta_uzakliklari\n", toplam_nokta_uzakliklari,"\n","en_iyi_rota", en_iyi_rota,"\n","en_iyi_yol", en_iyi_yol
print "toplam_nokta_uzakliklari\n", toplam_nokta_uzakliklari,"\n","en_iyi_rota", en_iyi_rota,"\n","en_iyi_yol", en_iyi_yol,"\n"
nokta_listesi = []
for i in range(0,nokta_sayisi):
        nokta_listesi.append(i)
kontrol_listesi_1 =np.zeros((nokta_sayisi,1),dtype = int)
kontrol_listesi_2 =np.zeros((nokta_sayisi,1),dtype = int)
#print nokta_listesi
#caprazlama islemi
for s in range(0,jenerasyon):
        caprazlanacak_nokta_sayisi = int(populasyon_sayisi*caprazlama_orani/100)
        if (caprazlanacak_nokta_sayisi%2 == 1): caprazlanacak_nokta_sayisi +=  1 
        #print "caprazlanacak_nokta_sayisi ", caprazlanacak_nokta_sayisi
        caprazlanacak_noktalar = np.random.choice(populasyon_sayisi , size = caprazlanacak_nokta_sayisi ,replace = False )
        #print "caprazlanacak_noktalar ", caprazlanacak_noktalar
        #print "pop\n",populasyon,"\n"
        for i in range(0,caprazlanacak_nokta_sayisi,2):
                caprazlama_noktasi = np.random.choice(nokta_sayisi ,1,)
                #print  "caprazlama_noktasi",caprazlama_noktasi
                kontrol_listesi_1 = np.copy(nokta_listesi)
                kontrol_listesi_2 = np.copy(nokta_listesi)               
                nokta = np.copy(populasyon[caprazlanacak_noktalar[i],caprazlama_noktasi[0]:nokta_sayisi])
                populasyon[caprazlanacak_noktalar[i],caprazlama_noktasi[0]:nokta_sayisi] = populasyon[caprazlanacak_noktalar[i+1],caprazlama_noktasi[0]:nokta_sayisi]
                populasyon[caprazlanacak_noktalar[i+1],caprazlama_noktasi[0]:nokta_sayisi] = nokta         
                dinamik_liste_1 = np.in1d( nokta_listesi, populasyon[caprazlanacak_noktalar[i],:])
                dinamik_liste_2 = np.in1d( nokta_listesi, populasyon[caprazlanacak_noktalar[i+1],:])
                #print dinamik_liste_1,"dinamik1-------------------------------",populasyon[i,:],"\n",dinamik_liste_2,"dinamik2-------------------------------",populasyon[i+1,:]
                index_1 = np.argwhere(dinamik_liste_1 == True )
                kontrol_listesi_1 =np.delete(kontrol_listesi_1 , index_1)
                #print kontrol_listesi_1
                index_2 = np.argwhere(dinamik_liste_2 == True )
                kontrol_listesi_2 =np.delete(kontrol_listesi_2 , index_2)
                #print kontrol_listesi_2
                for t in range(0,caprazlama_noktasi[0]):
                        for r in range(caprazlama_noktasi[0],nokta_sayisi):
                                if(populasyon[caprazlanacak_noktalar[i],t] == populasyon[caprazlanacak_noktalar[i],r]):
                                        #print "\n"
                                        #print populasyon[caprazlanacak_noktalar[i],:],"populasyon-1----------kontrol_listesi_1",kontrol_listesi_1
                                        populasyon[caprazlanacak_noktalar[i],t] = np.random.choice(kontrol_listesi_1,1)
                                        kontrol_listesi_1 = np.delete(kontrol_listesi_1,np.argwhere(kontrol_listesi_1 == populasyon[caprazlanacak_noktalar[i],t]))
                                        #print populasyon[caprazlanacak_noktalar[i],:],"populasyon-1-son------"
                        
                                if(populasyon[caprazlanacak_noktalar[i+1],t] == populasyon[caprazlanacak_noktalar[i+1],r]):
                                        #print populasyon[caprazlanacak_noktalar[i+1],:],"populasyon-2---------kontrol_listesi_2",kontrol_listesi_2
                                        populasyon[caprazlanacak_noktalar[i+1],t] = np.random.choice(kontrol_listesi_2,1)
                                        kontrol_listesi_2 = np.delete(kontrol_listesi_2,np.argwhere(kontrol_listesi_2 == populasyon[caprazlanacak_noktalar[i+1],t]))
                                        #print populasyon[caprazlanacak_noktalar[i+1],:],"populasyon-2-son------\n"                       
        #print "--------------------------------------------------------------------------------------------------------------"                  
        #print "pop\n",populasyon        
        #mutasyon 
        mutasyonlu_nokta_sayisi = populasyon_sayisi * nokta_sayisi * mutasyon_orani / 100
        if(mutasyonlu_nokta_sayisi%2 ==1): mutasyonlu_nokta_sayisi += 1
        #print "mutasyonlu_nokta_sayisi", mutasyonlu_nokta_sayisi
        for i in range(0,mutasyonlu_nokta_sayisi ,2):
                mutasyon_populasyon_elemani = np.random.choice(populasyon_sayisi,1)
                mutasyon_degistirme_noktalari = np.random.choice(nokta_sayisi,2)
                #print "mutasyon_populasyon_elemani",mutasyon_populasyon_elemani,mutasyon_degistirme_noktalari[0],mutasyon_degistirme_noktalari[1]
                degisken = np.copy(populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_noktalari[0]])
                populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_noktalari[0]] = populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_noktalari[1]]
                populasyon[mutasyon_populasyon_elemani,mutasyon_degistirme_noktalari[1]] = degisken
                #print populasyon
        for i in range(0,populasyon_sayisi):
                for j in range(0,nokta_sayisi-1):
                        x = noktalar_x_y[populasyon[i,j],0] - noktalar_x_y[populasyon[i,j+1],0]
                        y = noktalar_x_y[populasyon[i,j],1] - noktalar_x_y[populasyon[i,j+1],1]
                        toplam_yol +=  np.sqrt( x**2 + y**2)
                toplam_nokta_uzakliklari[i] = toplam_yol
                if(toplam_yol < en_iyi_yol):
                        en_iyi_yol = toplam_yol
                        en_iyi_rota = populasyon[i,:]
                        en_iyi_jenerasyon = s
                toplam_yol = 0
        #print "toplam_nokta_uzakliklari\n", toplam_nokta_uzakliklari,"\n","en_iyi_rota", en_iyi_rota,"\n","en_iyi_yol", en_iyi_yol
print "en_iyi_rota", en_iyi_rota,"\nen_iyi_yol", en_iyi_yol,"\nen_iyi_jenerasyon",en_iyi_jenerasyon,"\nzaman(s)",time.time() - a

















                


                        
                        
                        
                        

                
                    
                       


    






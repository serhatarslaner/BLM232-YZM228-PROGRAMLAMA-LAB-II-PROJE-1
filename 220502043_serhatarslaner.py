import pygame
import sys
from savascilar import *

pygame.init()
clock = pygame.time.Clock()

Siyah = (0, 0, 0)
Beyaz = (255, 255, 255)
Kirmizi = (255, 0, 0)
Mavi = (0, 0, 255)
Yesil = (0, 255, 0)
Sari = (255, 255, 0)

gir = int(input("Boyut Gir 16x16 (Tam Sayı Giriniz Örnek 16)= "))
karenkonumu=dict()
kare_boyutu = 35
MxM = gir
uzunluk = kare_boyutu*MxM
genislik = uzunluk + 240


pencere = pygame.display.set_mode((genislik, uzunluk))
pygame.display.set_caption("LORDS OF THE POLYWARPHISM")

oyuncuList = ["M1", "M2", "M3", "M4"]
renkler = [Kirmizi, Mavi, Yesil, Sari]
matris1 = [[0 for _ in range(MxM)] for _ in range(MxM)]
matris1[0][0] = 1
matris1[0][MxM-1] = 2
matris1[MxM-1][0] = 3
matris1[MxM-1][MxM-1] = 4

def matrisPanel():
    for row in matris1:
        print(row)

font2 = pygame.font.SysFont(None, 25)

def konumlandirici():

    for row in range(len(matris1)):
        for col in range(len(matris1)):            
            xkord = col * kare_boyutu
            ykord = row * kare_boyutu
            karenkonumu[(row,col)]= (xkord,ykord)
    
def kareCizdirme():
    kareBoyutu = 35
    for satir in range(MxM):
        for sutun in range(MxM):
            pygame.draw.rect(pencere, Beyaz, (satir * kareBoyutu, sutun * kareBoyutu, kareBoyutu, kareBoyutu), 1)
            font = pygame.font.SysFont(None, 20)
            oyuncu_sirasi_text = font.render("   .   ", True, Beyaz)
            pencere.blit(oyuncu_sirasi_text, (satir * kareBoyutu, sutun * kareBoyutu))


def karerenkdegistir(ekran, rengi,isim,satir,sutun): 
    noktatext = font2.render(isim, True, (255,255,255))
    pygame.draw.rect(ekran,rengi,(karenkonumu[(satir,sutun)][0],karenkonumu[(satir,sutun)][1],kare_boyutu,kare_boyutu))
    text_rect = noktatext.get_rect(center=(karenkonumu[(satir,sutun)][0] + kare_boyutu // 2, karenkonumu[(satir,sutun)][1] + kare_boyutu // 2))
    pencere.blit(noktatext, text_rect)
    pygame.draw.rect(ekran,rengi,(karenkonumu[(satir,sutun)][0],karenkonumu[(satir,sutun)][1],kare_boyutu,kare_boyutu),1)
    matris1[satir ][sutun]=isim
    pygame.display.flip()  


def oyuncuCiz():
    kareBoyutu = 35
    for i in range(len(oyuncuList)):
        pygame.draw.rect(pencere, renkler[i], (i % 2 * (uzunluk - kareBoyutu), i // 2 * (uzunluk - kareBoyutu), kareBoyutu, kareBoyutu))
        font = pygame.font.SysFont(None, 20)
        text = font.render(oyuncuList[i], True, Siyah)
        pencere.blit(text, (i % 2 * (uzunluk - kareBoyutu) + 5, i // 2 * (uzunluk - kareBoyutu) + 5))


def oyuncuSirasi(suanki_oyuncu):
    font = pygame.font.SysFont(None, 30)
    pygame.draw.rect(pencere, Siyah, (uzunluk, 0, 200, 30))
    suanki_oyuncu_text = font.render("Oyuncu Sirasi: {}".format(oyuncuList[suanki_oyuncu]), True, renkler[suanki_oyuncu])
    pencere.blit(suanki_oyuncu_text, (uzunluk, 0))


def ArayuzTasarlama(renk):
    okcu1 = Okcu()
    topcu1 = Topcu()
    atli1 = Atli()
    muhafiz1 = Muhafiz()
    saglikci1 = Saglikci()
    
    font = pygame.font.SysFont(None, 20)
    kaynaks = font.render("OYUNCU KAYNAK: +10",True,Beyaz)
    muhafız = font.render("Muhafiz:  {}".format(muhafiz1.kaynak), True, renk)
    okcu = font.render("Okcu:  {}".format(okcu1.kaynak), True, renk)
    topcu = font.render("Topcu:  {}".format(topcu1.kaynak), True, renk)
    atli = font.render("Atli:  {}".format(atli1.kaynak), True, renk)
    saglikci = font.render("Saglikci:  {}".format(saglikci1.kaynak), True, renk)
    pencere.blit(kaynaks,(uzunluk,35))
    pencere.blit(muhafız, (uzunluk, 65))
    pencere.blit(okcu, (uzunluk, 125))
    pencere.blit(topcu, (uzunluk, 185))
    pencere.blit(atli, (uzunluk, 245))
    pencere.blit(saglikci, (uzunluk, 305))
    pygame.draw.rect(pencere, Beyaz, (uzunluk+110, 60, 20, 20),1)
    pygame.draw.rect(pencere, Beyaz, (uzunluk+110, 120, 20, 20),1)
    pygame.draw.rect(pencere, Beyaz, (uzunluk+110, 180, 20, 20),1)
    pygame.draw.rect(pencere, Beyaz, (uzunluk+110, 240, 20, 20),1)
    pygame.draw.rect(pencere, Beyaz, (uzunluk+110, 300, 20, 20),1)
    addW = font.render("+",True,Beyaz)
    pencere.blit(addW,(uzunluk+115,60))
    pencere.blit(addW,(uzunluk+115,120))
    pencere.blit(addW,(uzunluk+115,180))
    pencere.blit(addW,(uzunluk+115,240))
    pencere.blit(addW,(uzunluk+115,300))

def AnlikKoordinat():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    satir = mouse_y // kare_boyutu
    sutun = mouse_x // kare_boyutu
    
    return satir,sutun
   


def OynamaSirasi(suanki_oyuncu):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    satir = mouse_y // kare_boyutu
    sutun = mouse_x // kare_boyutu

    if 0 <= satir < MxM and 0 <= sutun < MxM:  
        if matris1[satir][sutun] == 0:  
            for i in range(-1, 2):  
                for j in range(-1, 2):  
                    if 0 <= satir + i < MxM and 0 <= sutun + j < MxM:  
                        if matris1[satir + i][sutun + j] == suanki_oyuncu + 1:  
                            matris1[satir][sutun] = suanki_oyuncu + 1  
                            pygame.draw.rect(pencere, renkler[suanki_oyuncu], (sutun * kare_boyutu, satir * kare_boyutu, 35, 35))  
                            return True, (satir, sutun)  
            return False, None  
        else:  
            return False, None  
    else:  
        return False, None  



M_sayi=1
O_sayi=1
T_sayi=1
S_sayi=1
A_sayi=1
sayilist=[M_sayi,O_sayi,T_sayi,A_sayi,S_sayi]
tiklandiM=False    
tiklandiO=False    
tiklandiT=False    
tiklandiS=False    
tiklandiA=False 
sayac=0 
def savasciYerlestirme(suanki_oyuncu):
    global tiklandiM
    global tiklandiO
    global tiklandiT
    global tiklandiS
    global tiklandiA
    global A_sayi
    global S_sayi
    global O_sayi
    global T_sayi
    global M_sayi
    global sayac
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if uzunluk+110 <= mouse_x <= uzunluk+130 and 60 <= mouse_y <= 80 and pygame.mouse.get_pressed()[0] or tiklandiM:
        
        tiklandiM=True
        satir,sutun=AnlikKoordinat()
        if pygame.mouse.get_pressed()[2] and matris1[satir][sutun]!="." :
            
            karerenkdegistir(pencere,renkler[suanki_oyuncu],"M"+str(sayilist[0]),satir,sutun)
            konumlar=yerlesme_menzil(satir,sutun)
            for i in konumlar:
                karerenkdegistir(pencere,renkler[suanki_oyuncu],".",i[0],i[1])
            sayilist[0]+=1
            matrisPanel()
            tiklandiM=False
            if sayac==2:
                print("hey")
                pasGecme()
                sayac=0
            sayac+=1
      
    elif uzunluk+110 <= mouse_x <= uzunluk+130 and 120 <= mouse_y <= 140 and pygame.mouse.get_pressed()[0]or tiklandiO:
         
        tiklandiO=True
        satir,sutun=AnlikKoordinat()
        if pygame.mouse.get_pressed()[2] and matris1[satir][sutun]!="." :
            karerenkdegistir(pencere,renkler[suanki_oyuncu],"O"+str(sayilist[1]),satir,sutun)
            konumlar=yerlesme_menzil(satir,sutun)
            for i in konumlar:
                karerenkdegistir(pencere,renkler[suanki_oyuncu],".",i[0],i[1])
            sayilist[1]+=1
            matrisPanel()
            tiklandiO=False
        
    elif uzunluk+110 <= mouse_x <= uzunluk+130 and 180 <= mouse_y <= 200 and pygame.mouse.get_pressed()[0]or tiklandiT:
        
        tiklandiT=True
        satir,sutun=AnlikKoordinat()
        if pygame.mouse.get_pressed()[2] and matris1[satir][sutun]!=".":
            karerenkdegistir(pencere,renkler[suanki_oyuncu],"T"+str(sayilist[2]),satir,sutun)
            konumlar=yerlesme_menzil(satir,sutun)
            for i in konumlar:
                karerenkdegistir(pencere,renkler[suanki_oyuncu],".",i[0],i[1])
            sayilist[2]+=1
            matrisPanel()
            tiklandiT=False
        
    elif uzunluk+110 <= mouse_x <= uzunluk+130 and 240 <= mouse_y <= 260 and pygame.mouse.get_pressed()[0]or tiklandiA:
            
        tiklandiA=True
        satir,sutun=AnlikKoordinat()
        if pygame.mouse.get_pressed()[2] and matris1[satir][sutun]!="." :
            karerenkdegistir(pencere,renkler[suanki_oyuncu],"A"+str(sayilist[3]),satir,sutun)
            konumlar=yerlesme_menzil(satir,sutun)
            for i in konumlar:
                karerenkdegistir(pencere,renkler[suanki_oyuncu],".",i[0],i[1])
            sayilist[3]+=1
            matrisPanel()
            tiklandiA=False
        
    elif uzunluk+110 <= mouse_x <= uzunluk+130 and 300 <= mouse_y <= 320 and pygame.mouse.get_pressed()[0]or tiklandiS:
             
        tiklandiS=True
        satir,sutun=AnlikKoordinat()
        if pygame.mouse.get_pressed()[2] and matris1[satir][sutun]!=".":
            karerenkdegistir(pencere,renkler[suanki_oyuncu],"S"+str(sayilist[4]),satir,sutun)
            konumlar=yerlesme_menzil(satir,sutun)
            for i in konumlar:
                karerenkdegistir(pencere,renkler[suanki_oyuncu],".",i[0],i[1])
            sayilist[4]+=1
            matrisPanel()
            tiklandiS=False

def yerlesme_menzil(satir,sutun):
        indexler=[]
        
        for x in range(max(0, satir - 1), min(satir + 2, len(matris1))):
            for y in range(max(0, sutun - 1), min(sutun + 2, len(matris1[0]))):
                if (x, y) != (satir, sutun):
                    indexler.append((x, y))
        return indexler
                    
                    
    

def pasGecme():
    mouse_x, mouse_y = pygame.mouse.get_pos()    
    font = pygame.font.SysFont(None, 30)
    pygame.draw.rect(pencere, Beyaz, (uzunluk+170, uzunluk-50, MxM*4, MxM*3),1)
    pasGec = font.render("PAS", True, Beyaz)
    pencere.blit(pasGec, (uzunluk+180, uzunluk-40))
    if uzunluk+170 <= mouse_x <= uzunluk+170+(MxM*4) and uzunluk-50 <= mouse_y <= (uzunluk-50) + MxM*3 and pygame.mouse.get_pressed()[0]:
        return True  
    return False  


def matrisPanel():
    for row in matris1:
        print(row)


def ArayuzTasarlamaGosterge(renk):
    kareBoyutu = 35
    for satir in range(MxM):
        for sutun in range(MxM):
            if matris1[satir][sutun] == 0:  
                for i in range(-1, 2):  
                    for j in range(-1, 2):  
                        if 0 <= satir + i < MxM and 0 <= sutun + j < MxM:  
                            if matris1[satir + i][sutun + j] == renkler.index(renk) + 1:  
                                pygame.draw.rect(pencere, tuple(c * 0.9 for c in renk), (sutun * kareBoyutu, satir * kareBoyutu, kareBoyutu, kareBoyutu), 2)


def mainGame():
    suanki_oyuncu = 0
    player_attempts = 0
    
    konumlandirici()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if pasGecme(): 
                        player_attempts = 0  
                        suanki_oyuncu = (suanki_oyuncu + 1) % len(oyuncuList)
                        oyuncuSirasi(suanki_oyuncu)
                        print("Oyuncu ", oyuncuList[suanki_oyuncu-1]," PAS Geçti")
                    else:
                        move_valid, position = OynamaSirasi(suanki_oyuncu)  
                        if move_valid:
                            player_attempts += 1
                            if player_attempts >= 2:  
                                player_attempts = 0  
                                suanki_oyuncu = (suanki_oyuncu + 1) % len(oyuncuList)  
                            oyuncuSirasi(suanki_oyuncu)
                            matrisPanel()  
                            if position:  
                                print("Tiklanan karenin pozisyonu:", position)

        
        savasciYerlestirme(suanki_oyuncu)
        ArayuzTasarlama(Beyaz)
        ArayuzTasarlamaGosterge(renkler[suanki_oyuncu])  
        pasGecme()
        kareCizdirme()
        oyuncuCiz()
        oyuncuSirasi(suanki_oyuncu)
        pygame.display.flip()
        clock.tick(10)

mainGame()
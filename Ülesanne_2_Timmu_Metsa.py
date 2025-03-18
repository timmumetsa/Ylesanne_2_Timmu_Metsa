import pygame  # PyGame'i mooduli importimine.
import sys  # Süsteemimooduli importimine programmi sulgemiseks.

# Algseadistus.
pygame.init()  # PyGame'i käivitamine (initsialiseerimine).
ekraani_laius, ekraani_kõrgus = 640, 480  # Ekraani mõõtmed (laius x kõrgus).
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_kõrgus))  # Mänguakna loomine.
pygame.display.set_caption("Ülesanne 2")  # Akna pealkirja määramine.

# Piltide laadimine ja suuruse kohandamine.
taust = pygame.image.load("bg_shop.png")  # Taustapildi laadimine.
muujaja = pygame.image.load("seller.png")  # Poemüüja pildi laadimine.
muujaja = pygame.transform.scale(muujaja, (265, 306))  # Muudab poemüüja suurust.
jutumull = pygame.image.load("chat.png")  # Jutumulli pildi laadimine.
jutumull = pygame.transform.scale(jutumull, (258, 203))  # Muudab jutumulli suurust.

# Fondi seaded.
font = pygame.font.SysFont("Arial", 24)  # Fondi seadistamine (Arial, suurus 24).
tekst = font.render("Tere, olen Timmu", True, (255, 255, 255))  # Teksti renderdamine valges värvis (RGB 255, 255, 255).

# Mängu tsükkel.
kell = pygame.time.Clock()  # Kella objekt mängutsükli kiiruse kontrollimiseks
töös = True  # Mängu tsükkel on aktiivne.

while töös:  # Peamine mängutsükkel.
    for event in pygame.event.get():  # Läbitakse kõik sündmused (nt klahvivajutused, akna sulgemine).
        if event.type == pygame.QUIT:  # Kui kasutaja sulgeb akna
            töös = False  # Mängutsükkel lõpetatakse.

    # Tausta ja elementide kuvamine ekraanil.
    ekraan.blit(taust, (0, 0))  # Taustapildi kuvamine ekraani ülemises vasakus nurgas (koordinaadid 0, 0).
    ekraan.blit(muujaja, (102, 158))  # Poemüüja kuvamise koordinaadid.
    ekraan.blit(jutumull, (245, 65))  # Jutumulli kuvamise koordinaadid.
    ekraan.blit(tekst, (290, 134))  # Teksti kuvamise koordinaadid jutumulli sees.

    pygame.display.flip()  # Ekraani värskendamine, et näidata muudatusi.
    kell.tick(30)  # Kaadrisageduse piiramine 30 kaadrile sekundis (FPS).

pygame.quit()  # PyGame'i lõpetamine.
sys.exit()  # Programmi lõpetamine.
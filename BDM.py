#!/usr/bin/env python

import pygame, sys,os, random
from pygame.locals import *

def instructions(screen, font, white, width, height):
    screen.fill((0, 0, 0))
    text1=font.render("As explained, please bid on each of the following items",1,white)
    text2=font.render("by clicking on the amount on the bar below",1,white)
    text3=font.render("Please click to continue..",1,white)
    textpos1=text1.get_rect(centerx=width/2, centery=height/2-40)
    textpos2=text2.get_rect(centerx=width/2, centery=height/2)
    textpos3=text3.get_rect(centerx=width/2, centery=height/2+60)
    screen.blit(text1, textpos1)
    screen.blit(text2, textpos2)
    screen.blit(text3, textpos3)
    pygame.display.flip()
    while 1:
        event=pygame.event.poll()
        if event.type==MOUSEBUTTONDOWN:
            pygame.event.clear()
            break

def display_trial(stim, pos, rect, screen, font, white, blue, width, height):
    file = os.path.join("Images",stim)       #was "stim" and changed
    file = os.path.abspath(file)
    pic=pygame.image.load(file).convert()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, white, rect)
    text=font.render("0    1     2     3     4     5     6     7     8     9    10",1,white)
    text4=font.render("NIS",1,white)
    textpos=text.get_rect(centerx=width/2, centery=height-30)
    textpos4=text.get_rect(centerx=width/2+520, centery=height-30)
    screen.blit(text, textpos)
    screen.blit(text4, textpos4)
    screen.blit(pic,pic.get_rect(centerx=width/2, centery=height/2))
    draw_marker(pos, screen, height, blue)
    pygame.display.flip()

def draw_marker(pos, screen, height, blue):
    marker = pygame.Rect(pos-2,(height-75),4,30)
    pygame.draw.rect(screen, blue, marker)
    pygame.display.flip()

def get_response(width, height, stim, rect, screen, font, white, blue):
    pygame.event.clear()
    while 1:
        event=pygame.event.poll()
        pos = pygame.mouse.get_pos()
        if pos[0] > width/2-225 and pos[0] < width/2+225 and pos[1]>height-70 and pos[1]<height-50:
            display_trial(stim,pos[0], rect, screen, font, white, blue, width, height)
        
        
        if pygame.key.get_pressed()[K_LSHIFT] and pygame.key.get_pressed()[K_BACKQUOTE]:
            raise SystemExit
        if pygame.key.get_pressed()[K_LSHIFT] and pygame.key.get_pressed()[K_EQUALS]:
            save_image()
        if event.type==MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] > width/2-225 and pos[0] < width/2+225 and pos[1]>height-70 and pos[1]<height-50:
                bet=(pos[0]-(width/2-225))/45.0
                return bet
                break

def write_header(subjid):
    sd=("Trial"+'\t'+"StimName"+'\t'+"Bid"+'\t'+"RT"+'\n')
    sepname=subjid+"_BDM1.txt"
    # sep_path=os.path.join(r"C:\Users\wolfi\Documents\PythonCourse\Final_project\Python-Hackathon\Output",sepname)
    sep_path = os.path.join("Output", sepname)
    sepfile=open(sep_path, "a")
    sepfile.write(sd)
    sepfile.close()
    return sep_path


def write_response(trial,bet,rt, stim, subjid):
    sd=(str(trial)+'\t'+stim+'\t'+str(bet)+'\t'+str(rt)+'\n')
    sepname=subjid+"_BDM1.txt"
    sep_path=os.path.join("Output",sepname)
    sepfile=open(sep_path, "a")
    sepfile.write(sd)
    sepfile.close()

def intertrial(screen, font2, white, width, height):
    screen.fill((0, 0, 0))
    text=font2.render("+",1,white)
    textpos=text.get_rect(centerx=width/2, centery=height/2)
    screen.blit(text, textpos)
    pygame.display.flip()
    pygame.time.wait(1000)

def end(screen, font2, width, height, yellow):
    screen.fill((0, 0, 0))
    text=font2.render("Thank you! Please get the experimenter.",1,yellow)
    textpos=text.get_rect(centerx=width/2, centery=height/2)
    screen.blit(text, textpos)
    pygame.display.flip()
    pygame.time.wait(5000)

def main(subjid):
    # subjid=sys.argv[1]

    pygame.init()

    # Set up variables
    screen = pygame.display.set_mode((1280,800), FULLSCREEN)
    # screen = pygame.display.set_mode((1920,1080))
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    blue=(0,0,255)
    height=screen.get_height()
    width=screen.get_width()
    font = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 72)
    rect = pygame.Rect((width/2-225),(height-70),450,20)

    #JR=["jollyrancherblue", "jollyranchergreen", "jollyrancherpurple", "jollyrancherred"]
    #random.shuffle(JR)
    #Pringles=[ "Pringles", "PringlesRed", "pringlescheezums"]
    #random.shuffle(Pringles)
    #keebler=["keeblerfudgestripes", "keeblerrainbow"]
    #random.shuffle(keebler)

    #stimulus list of 60 items
    # stimlist=["Apropo.bmp", "BabyDoll.bmp", "BagaleShtuhim.bmp", "Bamba.bmp", "BambaNugat.bmp", "BambaSweet.bmp", "BisliGrill.bmp", "BisliOnion.bmp", "BisliPizza3.bmp", "Bounty.bmp", "Cheetos.bmp", "ChocolateParaCookies5.bmp", "ChocolateParaMarir2.bmp", "ChocolateParaMilk3.bmp", "ChocolateParaSucariotKoftzot2.bmp", "ClickBalls5.bmp", "ClickBisquit2.bmp", "ClickBlackWhite3.bmp", "ClickXLbrown4.bmp", "ClickXLwhite4.bmp", "CrunchBisquitBrown3.bmp", "CrunchBisquitWhite2.bmp", "CrunchShokoVanil.bmp", "DoritosGrill.bmp", "DoritosNatural.bmp", "DoritosSourSpicy.bmp", "Dubonim.bmp", "Egozi.bmp", "GumiSnakes3.bmp", "GumiWine2.bmp", "Halva2.bmp", "HappyHippo.bmp", "HispusimShatiah.bmp", "Hit.bmp", "KashitSour.bmp", "Keifli.bmp", "KifkefMaklot2.bmp", "KinderBuenoBrown3.bmp", "KinderBuenoWhite2.bmp", "KinderJoy.bmp", "Kitkat.bmp", "Loacker.bmp", "Mars.bmp", "Mekupelet.bmp", "Mentos.bmp", "PesekZman.bmp", "Popco.bmp", "Shugi.bmp", "SkittlesFruits2.bmp", "SkittlesSour4.bmp", "Smarties.bmp", "Snickers.bmp", "Taami.bmp", "Tapuchips.bmp", "TapuchipsCrunch.bmp", "Tictac.bmp", "Tortit.bmp", "Twist.bmp", "Twix.bmp", "WerthersOriginal.bmp"]
    stimlist = ["bamba.jpg", "bisli.jpg", "doritos.jpg", "kitkat.jpg", "mars.jpg", "snickers.jpg"]
    random.shuffle(stimlist)

    trial=1

    instructions(screen, font, white, width, height)
    output_file_path = write_header(subjid)
    for stim in stimlist:

        pygame.mouse.set_pos(width/2,height/2)

        stimonset=pygame.time.get_ticks()
        display_trial(stim,(width/2), rect, screen, font, white, blue, width, height)

        pygame.time.wait(500)

        bet=get_response(width, height, stim, rect, screen, font, white, blue)
        rt=pygame.time.get_ticks()-stimonset
        write_response(trial,bet,rt, stim, subjid)

        intertrial(screen, font2, white, width, height)
        trial=trial+1
    end(screen, font2, width, height, yellow)
    pygame.quit()
    return output_file_path



import random
from viata.toate_patratele import *
import ast
import pygame
import sys

def verifica_suprapunerea(arg,i,l,width,height):
    patrate=arg[0]
    ok=1
    for j in range(0,l):
            
            if j!=i and pygame.Rect(patrate[i].x,patrate[i].y,patrate[i].size,patrate[i].size).colliderect(pygame.Rect(patrate[j].x,patrate[j].y,patrate[j].size,patrate[j].size)):
                patrate[i].x=random.randint(0,350)
                patrate[i].y=random.randint(0,350)
                ok=0
            if j!=i and patrate[i].x<0:patrate[i].x+=1;ok=0
            if j!=i and patrate[i].x>height:patrate[i].x-=1;ok=0
            if j!=i and patrate[i].y<0:patrate[i].y+=1;ok=0
            if j!=i and patrate[i].y>width:patrate[i].y-=1;ok=0
    arg[0]=patrate
    arg[1]=ok

def creare_muve_impuls():
    impuls=[round(random.random(),2),
            round(random.random(),2),
            round(random.random(),2),
            round(random.random(),2),
            round(random.random(),2)]
    
    return impuls


def creaza(nr_patrate,width,height):
    patrate=[]
    l=0
    i=0
    while i<=nr_patrate:

        muve_impuls=creare_muve_impuls()
        muve_stimul=1
        speed=1
        size=50
        x=random.randint(1,height-50)
        y=random.randint(1,width-50)
        patrate.append(patrat(muve_impuls,muve_stimul,
                              speed,size,x,y))
        print(i,patrate[i].muve_impuls)
        l+=1
        if l!=1:
            
            arg=[patrate,1]
            verifica_suprapunerea(arg,i,l,width,height)
            while arg[1]==0: verifica_suprapunerea(arg,i,l,width,height)
            patrate=arg[0]
        i+=1
        
    return patrate

def next(nr_patrate,width,height):
    patrate=[]
    linii=[]
    nr_linii=0
    with open("biblioteca.txt","r") as fisier:
        tot=fisier.readlines()
        for i in tot:
            linii.append(ast.literal_eval(i.strip()))
            nr_linii+=1
    l=0
    i=0
        


    if nr_linii<=1: return 0
    while i<nr_patrate:
        t=random.randint(0,nr_linii-1)
        m=random.randint(0,nr_linii-1)
        while m==t:
            m=random.randint(0,nr_linii-1)
        impuls=[round(random.uniform(linii[t][0],linii[m][0]),2),
                round(random.uniform(linii[t][1],linii[m][1]),2),
                round(random.uniform(linii[t][2],linii[m][2]),2),
                round(random.uniform(linii[t][3],linii[m][3]),2),
                round(random.uniform(linii[t][4],linii[m][4]),2)]
        for k in range(0,5):
            x=1-impuls[k]
            ok=2
            if x<0.1:
                ok=0
            elif impuls[k]<0.1:
                ok=1
            if ok==0:
                y=random.choice([-0.1,x])
                impuls[k]=round(impuls[k]+y,2)
            elif ok==1:
                y=random.choice([impuls[k],0.1])
                impuls[k]=round(impuls[k]+y,2)
            else:
                y=random.choice([-0.1,0.1])
                impuls[k]=round(impuls[k]+y,2)
        linii.append(impuls)
        
        print(i,linii[i])
        patrate.append(patrat(linii[nr_linii],1,1,50,random.randint(1,350),random.randint(1,350)))

        if i>nr_linii:
            nr_linii+=1

        arg=[patrate,1]
        verifica_suprapunerea(arg,i,l,width,height)
        while arg[1]==0: verifica_suprapunerea(arg,i,l,width,height)
        patrate=arg[0]
        l+=1
        i+=1
    return patrate
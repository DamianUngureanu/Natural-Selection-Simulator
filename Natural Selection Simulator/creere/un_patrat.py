import random

def COLISION(patrate,nr_patrate,actual,width,height):
    dr=1;st=1;top=1;bot=1
    if patrate[actual].x+patrate[actual].size>width:
        dr=0
    if patrate[actual].x<0:
        st=0
    if patrate[actual].y<0:
        top=0
    if patrate[actual].y+patrate[actual].size>height:
        bot=0
    
    for i in range(0,nr_patrate):
        if i!=actual:
            if patrate[actual].y+patrate[actual].size==patrate[i].y and ((patrate[actual].x+patrate[actual].size>=patrate[i].x and patrate[actual].x+patrate[actual].size<=patrate[i].x+patrate[i].size) or (patrate[actual].x<=patrate[i].x+patrate[i].size and patrate[actual].x>=patrate[i].x)):
                bot=0
            if patrate[actual].y==patrate[i].y+patrate[i].size and ((patrate[actual].x+patrate[actual].size>=patrate[i].x and patrate[actual].x+patrate[actual].size<=patrate[i].x+patrate[i].size) or (patrate[actual].x<=patrate[i].x+patrate[i].size and patrate[actual].x>=patrate[i].x)):
                top=0
            if patrate[actual].x==patrate[i].x+patrate[i].size and ((patrate[actual].y+patrate[actual].size>=patrate[i].y and patrate[actual].y+patrate[actual].size<=patrate[i].y+patrate[i].size) or (patrate[actual].y<=patrate[i].y+patrate[i].size and patrate[actual].y>=patrate[i].y)):
                st=0
            if patrate[actual].x+patrate[actual].size==patrate[i].x and ((patrate[actual].y+patrate[actual].size>=patrate[i].y and patrate[actual].y+patrate[actual].size<=patrate[i].y+patrate[i].size) or (patrate[actual].y<=patrate[i].y+patrate[i].size and patrate[actual].y>=patrate[i].y)):
                dr=0

    return [st,top,dr,bot]


def MUVE(patrat,width,height,ponderi):
    var=0
    move_reactie=[0,0]
    ponderi.append(1)
    for i in range(0,5):
        ponderi[i]*=patrat.muve_impuls[i]

    unde=[[-patrat.speed,0],[0,-patrat.speed],[patrat.speed,0],[0,patrat.speed],[0,0]]
    move_reactie=random.choices(unde,ponderi)[0]
    return move_reactie


def LUME(patrate,nr_patrate,width,height):
    for i in range(0,nr_patrate):
        if patrate[i].muve_stimul==1:
            colision_info=COLISION(patrate,nr_patrate,i,width,height)
            unde=MUVE(patrate[i],width,height,colision_info)
            patrate[i].x+=unde[0]
            patrate[i].y+=unde[1]

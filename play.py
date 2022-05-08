import turtle
import time
import random

oyunekranı=turtle.Screen()
oyunekranı.tracer()
oyunekranı.setup(600,600)
oyunekranı.bgcolor("black")

yılan=turtle.Turtle()

yılan.shape("square")
yılan.color("white")
yılan.speed(0)
yılan.penup()
yılan.goto(-200,0)
yılan.yön ="dur"

yem=turtle.Turtle()

yem.shape("square")
yem.color("green")
yem.speed(0)
yem.penup()
yem.goto(0,0)
yem.yön ="dur"

def yukari():
    if yılan.yön!="aşağı":
        yılan.yön="yukarı"
def aşağı():
    if yılan.yön!="yukarı":
        yılan.yön="aşağı"
def sola():
    if yılan.yön!="sağa":
        yılan.yön="sola"
def sağa():
    if yılan.yön!="sola":
        yılan.yön="sağa"
        
oyunekranı.listen()
oyunekranı.onkeypress(yukari,"w")
oyunekranı.onkeypress(aşağı,"s")
oyunekranı.onkeypress(sola,"a")
oyunekranı.onkeypress(sağa,"d")



def hareketet():
    if yılan.yön=="yukarı":
        y = yılan.ycor()
        yılan.sety(y+20)
    if yılan.yön=="aşağı":
        y = yılan.ycor()
        yılan.sety(y-20)
    if yılan.yön=="sola":
        x=yılan.xcor()
        yılan.setx(x-20)
    if yılan.yön=="sağa":
        x=yılan.xcor()
        yılan.setx(x+20)
        
def yanma():
    
     time.sleep(1)
     yılan.goto(-200,0)
     yılan.yön="dur"
     for i in bölümler:
         i.goto(2000,2000)
     bölümler.clear()
bölümler =[]

def yeme():
    for i in range(len(bölümler)-1,0,-1):
        x=bölümler[i-1].xcor()
        y=bölümler[i-1].ycor()
        bölümler[i].goto(x,y)
        
    if len(bölümler)>0:
        x=yılan.xcor()
        y=yılan.ycor()
        bölümler[0].goto(x,y)

while True:
    oyunekranı.update()
    time.sleep(0.1)
    if yılan.distance(yem)<20:
        x= random.randint(-290, 290)
        y= random.randint(-290,290)
        yem.goto(x,y)
        yeniBölüm=turtle.Turtle()
        yeniBölüm.speed(0)
        yeniBölüm.shape("square")
        yeniBölüm.penup()
        yeniBölüm.color("red")
        bölümler.append(yeniBölüm)
        
    hareketet()   
    
    if yılan.xcor()>290 or  yılan.xcor()<-290 or   yılan.ycor()>290 or   yılan.ycor()<-290 :
        yanma()
        
    for i in bölümler:
        if i.distance(yılan) < 20:
            yanma()
    yeme()
    
    
    
    

    
    
    
    
    
    
    
    
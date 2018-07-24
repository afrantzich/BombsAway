import random

class Bomb(object):
    
    def __init__(self, c, xpos, ypos, yspeed, dspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.yspeed = yspeed
        self.dspeed = dspeed
        self.over = False
    
    def display(self):
        stroke(0)
        ellipseMode(CENTER)
        fill(self.c)
        ellipse(self.xpos, self.ypos, 10, 15);
        fill(color(255, 0, 0))
        triangle(self.xpos - 4, self.ypos + 6, self.xpos + 4, self.ypos + 6, 
                 self.xpos, self.ypos + 14)
        triangle(self.xpos - 4, self.ypos, self.xpos - 7, self.ypos - 8, 
                 self.xpos - 4, self.ypos - 8)
        triangle(self.xpos + 4, self.ypos, self.xpos + 7, self.ypos - 8, 
                 self.xpos + 4, self.ypos - 8)
        
    def fall(self):
        self.ypos = self.ypos + self.yspeed;
        if keyPressed and key == ' ':
            self.yspeed = 1
            
    def hit(self):
        if mousePressed and abs(mouseX - self.xpos) < 20 and abs(mouseY - self.ypos) < 20:
            self.xpos = random.randrange(width)
            self.ypos = random.randrange(-100, 0)
            self.yspeed += self.dspeed
            return int(self.yspeed * 10)
            redraw()
        return 0
    
    def detonate(self):
        if self.ypos > height*9/10:
            self.ypos = -30
            self.xpos = random.randrange(width)
            return True
        
    def done(self):
        self.ypos = -20
        self.yspeed = 0
            
height = 400
width = 400
Bomb1 = Bomb(0, random.randrange(width), -20, 1, 0.11)
Bomb2 = Bomb(255, random.randrange(width), -20, 1, 0.1)
dragX = dragY = -20
score = 0
power = 3
lives = 5
fade = False

def setup():
    size(height, width)
    noCursor()
    
def draw(): 
    global dragX, dragY, score, power, lives, fade, frame
    mycolor = [0, 0, 0]
    if lives <= 0:
        Bomb1.done()
        Bomb2.done()
        background(0)
        fill(color(255, 0, 0))
        textSize(32)
        text("Game Over" , width*28/100, height*45/100)
        textSize(20)
        text("Final Score: " + str(score), width*10/100, height*70/100)
        return
    if score > 6550:
        mycolor[0] = 255 - (score - 6550)/20
    elif score > 2550:
        mycolor[0] = 255
        mycolor[1] = 200 - (score - 2550)/20
        mycolor[2] = 0
    else:
        mycolor[0] = 100 + score/10
        mycolor[1] = 200
        mycolor[2] = 255 - score/10
    background(color(mycolor[0], mycolor[1], mycolor[2]))
    Bomb1.fall()
    Bomb1.display()
    if (Bomb1.detonate()):
        lives -= 1    
    Bomb2.fall()
    Bomb2.display()
    if (Bomb2.detonate()):
        lives -= 1
    score += Bomb1.hit()
    score += Bomb2.hit()
    fill(0)
    line(0, height*11/12, width, height*11/12)
    line(width/2, height*11/12, mouseX, mouseY)
    textSize(20)
    text("Score: " + str(score), width*55/100, height*99/100)
    text("Power: " + str(power), width*5/100, height*99/100)
    text("Lives: " + str(lives), width*30/100, height*99/100)

    
def mouseDragged():   # Attack
    global dragX, dragY
    dragX = mouseX
    dragY = mouseY
    line(width/2, height*11/12, mouseX, mouseY)
    fill(255)
    ellipse(mouseX, mouseY, 20, 20)

def mouseReleased():
    global dragX, dragY
    dragX = dragY = -20
    
def keyPressed():
    global power, lives
    if key == ' ' and power > 0:
        power -= 1
        redraw()
    if lives <= 0:
        exit()

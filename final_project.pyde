x=1
def setup():
    size(1000,800)
def draw():
    global x
    background(x)
    fill(50)
    rect(100,220,180,500)
    stroke(50,0,0)
    strokeWeight(4)
    line(100,720,280,220)
    line(280,720,100,220)
    fill(50,0,0)
    triangle(100,220,280,220,190,100)
    fill(20)
    rect(280,220,400,500)
    fill(50)
    rect(680,220,180,500)
    fill(50,0,0)
    line(680,220,860,720)
    line(860,220,680,720)
    triangle(680,220,860,220,770,100)
    fill(153,204,255)
    noStroke()
    rect(320,400,100,100)
    rect(520,400,100,100)
    fill(50)
    rect(300,180,30,40)
    push()
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    translate(60,0)
    rect(300,180,30,40)
    pop()
    fill(153,102,51)
    ellipse(480,720,210,290)
    fill(0,153,51)
    rect(0,720,1000,300)
    x=x+1
    if x >= 255:
        x=x-1
    elif x <=0:
        x=x+1
    

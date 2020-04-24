import turtle

def visualize(N,dic_position_steps,errCode):
    turtle.title("Knight's Tour Problem by \"Dynamic\" WARNSDORFF Algorithm")
    Sidelength=30*15/N

    #the grid for background
    turtle.color('#7B7B7B')
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-(N/2)*Sidelength,(N/2)*Sidelength)
    turtle.pendown()
    turtle.goto(-(N/2)*Sidelength,-(N/2)*Sidelength)
    turtle.goto((N/2)*Sidelength,-(N/2)*Sidelength)
    turtle.goto((N/2)*Sidelength,(N/2)*Sidelength)
    turtle.goto(-(N/2)*Sidelength,(N/2)*Sidelength)

    tmp=(-(N/2)*Sidelength,(N/2)*Sidelength)
    for i in range(int(N/2)):
        (x,y)=tmp
        turtle.goto(x,y-Sidelength)
        turtle.goto(x+N*Sidelength,y-Sidelength)
        turtle.goto(x+N*Sidelength,y-Sidelength*2)
        turtle.goto(x,y-Sidelength*2)
        tmp=(x,y-Sidelength*2)
    turtle.goto(-(N/2)*Sidelength,-(N/2)*Sidelength)
    tmp=(-(N/2)*Sidelength,-(N/2)*Sidelength)
    for i in range(int(N/2)):
        (x,y)=tmp
        turtle.goto(x+Sidelength,y)
        turtle.goto(x+Sidelength,y+N*Sidelength)
        turtle.goto(x+Sidelength*2,y+N*Sidelength)
        turtle.goto(x+Sidelength*2,y)
        tmp=(x+Sidelength*2,y)



    #step by step~
    (x0,y0)=((-(N/2)+0.5)*Sidelength,((N/2)-0.5)*Sidelength)
    steps=dict([(value, key) for key, value in dic_position_steps.items()])#swap key and value
    turtle.color('blue')
    turtle.pensize(2)
    (xLast,yLast)=steps[0]
    for step in steps:
        (xNext,yNext)=steps[step]
        comefrom=(x0+xLast*Sidelength,y0-yLast*Sidelength)
        moveto=(x0+xNext*Sidelength,y0-yNext*Sidelength)

        #fill the block
        turtle.speed(0)
        turtle.penup()
        turtle.fillcolor('#BEBEBE')
        turtle.goto(x0+(xNext-0.33)*Sidelength,y0-(yNext-0.33)*Sidelength)
        turtle.begin_fill()
        turtle.goto(x0+(xNext+0.33)*Sidelength,y0-(yNext-0.33)*Sidelength)
        turtle.goto(x0+(xNext+0.33)*Sidelength,y0-(yNext+0.33)*Sidelength)
        turtle.goto(x0+(xNext-0.33)*Sidelength,y0-(yNext+0.33)*Sidelength)
        turtle.goto(x0+(xNext-0.33)*Sidelength,y0-(yNext-0.33)*Sidelength)
        turtle.end_fill()
        turtle.goto(moveto)

        #draw the line
        turtle.speed(10)
        turtle.penup()
        turtle.goto(comefrom)
        turtle.pendown() #if step!=0 else turtle.penup()
        if step==0:
            turtle.write('    Start')
        turtle.goto(moveto)
        turtle.dot()
        (xLast,yLast)=(xNext,yNext)

    #check errorCode
    if errCode==0:
        turtle.write('    Finish')
    else :
        turtle.write('    Fail')

    #Ending~~~
    turtle.done()

# Christopher Stephens
# Arjun Pherwani
# 14 September 2018
# UCF Programming Team Logo

from turtle import Turtle, Screen;
import math, random, time;

def main():

    # Other Vars
    random.seed();
    rot1 = random.randint(0, 180);
    rot2 = random.randint(0, 180);
    
    # Declare Screen Vars
    screen = Screen();
    screen.delay(1);
    screen.bgcolor("black");
    screen.title("Christopher and Arjun's Programming Team Flag");
    screen.setup(width = 1050, height = 910);
    screen.setworldcoordinates(-20, -20, 280, 240);

    # Declare Turtle Var
    turt = Turtle();
    turt.reset();
    turt.speed(0);
    turt.pensize(10);
    turt.shape("square");
    turt.color("white");
    turt.resizemode("auto");
    turt.hideturtle();

    # Draw TV
    turt.forward(220);
    turt.left(90);
    turt.forward(180);
    turt.left(90);
    turt.forward(220);
    turt.left(90);
    turt.forward(180);
    turt.left(90);
    turt.penup();
    turt.forward(220);
    turt.pendown();
    turt.left(45);
    turt.forward(40 * math.sqrt(2));
    turt.left(45);
    turt.forward(180);
    turt.left(135);
    turt.forward(40 * math.sqrt(2));
    turt.penup();
    turt.backward(40 * math.sqrt(2));
    turt.pendown();
    turt.right(45);
    turt.forward(220);
    turt.left(45);
    turt.forward(40 * math.sqrt(2));

    # Draw Screen
    turt.penup();
    turt.home();
    turt.setx(20);
    turt.sety(20);
    turt.pendown();
    turt.forward(140);
    turt.left(90);
    turt.forward(140);
    turt.left(90);
    turt.forward(140);
    turt.left(90);
    turt.forward(140);
    turt.left(90);

    # Draw Knob 1
    turt.penup();
    turt.home();
    turt.setx(190);
    turt.sety(150);
    turt.pendown();
    turt.dot(size = 90);
    turt.color("black");
    turt.dot(size = 75);
    turt.color("white");
    turt.left(rot1);
    turt.forward(8);
    turt.backward(16);
    
    # Draw Knob 2
    turt.penup();
    turt.home();
    turt.setx(190);
    turt.sety(120);
    turt.pendown();
    turt.dot(size = 90);
    turt.color("black");
    turt.dot(size = 75);
    turt.color("white");
    turt.left(rot2);
    turt.forward(8);
    turt.backward(16);

    # Draw Speaker
    turt.penup();
    turt.home();
    turt.setx(175);
    turt.sety(95);
    turt.pendown();
    turt.forward(30);
    turt.right(90);
    turt.forward(80);
    turt.right(90);
    turt.forward(30);
    turt.right(90);
    turt.forward(80);
    turt.right(90);
    '''
    # Draw Speaker Dots
    for x in range(178, 204, 2):
        for y in range(18, 94, 2):
            turt.penup();
            turt.setx(x);
            turt.sety(y);
            turt.pendown();
            turt.dot(3);
            '''
    # Turn Knob 1
    turt.penup();
    turt.home();
    turt.setx(190);
    turt.sety(150);
    turt.pendown();
    turt.color("black");
    turt.left(rot1);
    turt.forward(8);
    turt.backward(16);
    turt.penup();
    turt.forward(8);
    turt.pendown();
    turt.color("white");
    turt.left(60);
    turt.forward(8);
    turt.backward(16);
    
    # Tetromino 1
    turtromino1 = [turt.clone(), turt.clone(), turt.clone(), turt.clone()];
    for turtle in turtromino1:
        turtle.penup();
        turtle.home();
        turtle.pensize(6);
        turtle.setheading(270);
        turtle.color("gold");
    turtromino1[0].setx(95);
    turtromino1[0].sety(135);
    turtromino1[1].setx(95);
    turtromino1[1].sety(145);
    turtromino1[2].setx(95);
    turtromino1[2].sety(155);
    turtromino1[3].setx(105);
    turtromino1[3].sety(155);
    for turtle in turtromino1:
        turtle.showturtle();
    for y in range(135, 26, -1):
        for turtle in turtromino1:
            turtle.forward(1);

    # Tetromino 2
    turtromino2 = [turt.clone(), turt.clone(), turt.clone(), turt.clone()];
    for turtle in turtromino2:
        turtle.penup();
        turtle.home();
        turtle.pensize(6);
        turtle.setheading(270);
        turtle.color("gold");
    turtromino2[0].setx(75);
    turtromino2[0].sety(145);
    turtromino2[1].setx(75);
    turtromino2[1].sety(155);
    turtromino2[2].setx(85);
    turtromino2[2].sety(145);
    turtromino2[3].setx(95);
    turtromino2[3].sety(145);
    for turtle in turtromino2:
        turtle.showturtle();
    for y in range(145, 56, -1):
        for turtle in turtromino2:
            turtle.forward(1);
            
    # Tetromino 3
    turtromino3 = [turt.clone(), turt.clone(), turt.clone()];
    for turtle in turtromino3:
        turtle.penup();
        turtle.home();
        turtle.pensize(6);
        turtle.setheading(270);
        turtle.color("gold");
    turtromino3[0].setx(95);
    turtromino3[0].sety(155);
    turtromino3[1].setx(105);
    turtromino3[1].sety(155);
    turtromino3[2].setx(115);
    turtromino3[2].sety(155);
    #turtromino3[3].setx(125);
    #turtromino3[3].sety(155);
    for turtle in turtromino3:
        turtle.showturtle();
    for y in range(155, 66, -1):
        for turtle in turtromino3:
            turtle.forward(1);
            
    # Tetromino 4
    turtromino4 = [turt.clone(), turt.clone(), turt.clone(), turt.clone()];
    for turtle in turtromino4:
        turtle.penup();
        turtle.home();
        turtle.pensize(6);
        turtle.setheading(270);
        turtle.color("gold");
    turtromino4[0].setx(55);
    turtromino4[0].sety(155);
    turtromino4[1].setx(65);
    turtromino4[1].sety(155);
    turtromino4[2].setx(75);
    turtromino4[2].sety(155);
    turtromino4[3].setx(75);
    turtromino4[3].sety(145);
    for turtle in turtromino4:
        turtle.showturtle();
    for y in range(145, 76, -1):
        for turtle in turtromino4:
            turtle.forward(1);
            
    # Tetromino 5
    turtromino5 = [turt.clone(), turt.clone(), turt.clone(), turt.clone()];
    for turtle in turtromino5:
        turtle.penup();
        turtle.home();
        turtle.pensize(6);
        turtle.setheading(270);
        turtle.color("gold");
    turtromino5[0].setx(75);
    turtromino5[0].sety(145);
    turtromino5[1].setx(75);
    turtromino5[1].sety(155);
    turtromino5[2].setx(85);
    turtromino5[2].sety(145);
    turtromino5[3].setx(95);
    turtromino5[3].sety(145);
    for turtle in turtromino5:
        turtle.showturtle();
    for y in range(145, 96, -1):
        for turtle in turtromino5:
            turtle.forward(1);
            
    # Tetromino 6
    turtromino6 = [turt.clone(), turt.clone(), turt.clone(), turt.clone()];
    for turtle in turtromino6:
        turtle.penup();
        turtle.home();
        turtle.pensize(6);
        turtle.setheading(270);
        turtle.color("gold");
    turtromino6[0].setx(55);
    turtromino6[0].sety(155);
    turtromino6[1].setx(55);
    turtromino6[1].sety(145);
    turtromino6[2].setx(55);
    turtromino6[2].sety(135);
    turtromino6[3].setx(55);
    turtromino6[3].sety(125);
    for turtle in turtromino6:
        turtle.showturtle();
    for y in range(125, 96, -1):
        for turtle in turtromino6:
            turtle.forward(1);
            
    # Tetromino 7
    turtromino7 = [turt.clone(), turt.clone(), turt.clone(), turt.clone()];
    for turtle in turtromino7:
        turtle.penup();
        turtle.home();
        turtle.pensize(6);
        turtle.setheading(270);
        turtle.color("gold");
    turtromino7[0].setx(75);
    turtromino7[0].sety(155);
    turtromino7[1].setx(75);
    turtromino7[1].sety(145);
    turtromino7[2].setx(75);
    turtromino7[2].sety(135);
    turtromino7[3].setx(75);
    turtromino7[3].sety(125);
    for turtle in turtromino7:
        turtle.showturtle();
    for y in range(125, 116, -1):
        for turtle in turtromino7:
            turtle.forward(1);

    # Ship to blow up extra blocks
    turt.penup();
    turt.home();
    turt.left(180);
    turt.pensize(10);
    turt.shape("classic");
    turt.setx(160);
    turt.sety(145);
    turt.showturtle();
    turt.speed(1);
    turt.forward(85);
    turtromino7[0].shape("circle");
    turtromino7[0].color("red");
    turt.forward(25);
    turtromino7[0].color("black");
    turt.forward(35);
    turt.hideturtle();
    turt.setx(160);
    turt.sety(135);
    turt.showturtle();
    turt.forward(85);
    turtromino7[1].shape("circle");
    turtromino7[1].color("red");
    turt.forward(25);
    turtromino7[1].color("black");
    turt.forward(35);
    turt.hideturtle();

    # Text Fall on top
    turt.home();
    turt.color("white");
    turt.setx(90);
    turt.sety(135);
    turt.setundobuffer(1);
    string = "PROGRAMMING TEAM";
    turt.write(string[0:0]);
    for q in range(1, len(string) + 1):
        time.sleep(0.2);
        turt.undo();
        turt.write(string[:q], align = "center", font = ("Comic Sans MS", 20, "normal"));
        
main();

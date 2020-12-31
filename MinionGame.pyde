add_library('minim')
minim=Minim(this)
buttons = [0,0,0,0,0,0,0,0]
banana_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
platforms = []
high_scores = []         
page = 1 
bullets = []
user_info = []

class Bullet:
    def __init__(self, x, y, dir, img):
        self.x = x
        self.y = y
        self.dir = dir
        self.img = img

class Platform:
    def __init__(self, x1, x2, y):
        self.x1 = x1
        self.x2 = x2
        self.y = y
        
    def display(self):
        strokeWeight(3)
        stroke(0)
        line(self.x1, self.y, self.x2, self.y)
    
def setup():
    global Main
    global nameBackground, backGround,leaderboard, yellowMinion, yellowMinionFlip, purpleMinion, purpleMinionFlip, bananas, stop, pause
    global yellowIncrX, yellowIncrY, purpleIncrX, purpleIncrY, gravity, xY, yY, xP, yP
    global groundedY, groundedP
    global Instructions, page
    global timer
    global winner #0 = yellow, 1 = purple
    global name1, name2, cur_name, user_info
    global bullet, shot, directionY, directionP
    global file , high_scores
    global font, dFont
    global minionSound, sliderX, sliderY, sliderL, sliderW, sliderOn, slider, loud
    contents = loadStrings("UserInfo.txt")

    contents = list(contents)
    for i in range (len(contents)):
        contents[i] = contents[i].split()
    high_scores = []
    
    for i in range(len(contents)):
        for j in range(len(high_scores)):
            if float(contents[i][1]) < float(high_scores[j][1]) or j == (len(high_scores) - 1):
                if float(contents[i][1]) < float(high_scores[j][1]):
                    high_scores.insert(j,contents[i])   
                else:
                    high_scores.insert(j+1,contents[i])
                print(high_scores)
                break
        if high_scores == []:
            high_scores.insert(0,contents[i])
    
    print(contents)
    print(high_scores)
        
    file = open("UserInfo.txt","a")
    shot = False
    directionY = -1
    directionP = 1
    name1 = ""
    name2 = ""
    name = 0
    cur_name = 1
    winner = 0
    
    timer = 0.0
    
    size(721,450)
    Main = loadImage("Main3.png")
    leaderboard = loadImage("Leaderboard.png")
    nameBackground = loadImage("nameBackground.png")
    backGround = loadImage("Minions Background Platforms.jpg")
    Instructions = loadImage("Capture.png")
    pause = loadImage("Pause.png")
    backGround.resize(721, 450)
    
    yellowMinion = loadImage("MINIONS.PNG")
    yellowMinion.resize(50, 50)
    yellowMinionFlip = loadImage("MINIONSFLIPPED.PNG")
    yellowMinionFlip.resize(50, 50)
    
    purpleMinion = loadImage("PurpleMinion.png")
    purpleMinion.resize(50, 50)
    purpleMinionFlip = loadImage("PurpleMinionFlipped.png")
    purpleMinionFlip.resize(50, 50)
    
    bananas = loadImage("BANANAS.png")    
    stop = loadImage ("stop.png")
    bullet = loadImage("bullet.png")
    
    font= loadFont("AdobeDevanagari-Bold-15.vlw")
    dFont = loadFont("LucidaSans-48.vlw")

    minionSound = minim.loadFile("Minions Song.mp3")
    sliderX = 10
    sliderY = 10
    sliderL = 10
    sliderW = 100
    sliderOn = False
    slider = sliderX
    
    xY = 611 # x coordinate is different so that both minions start on opposite ends, 
    yY = 100   # which gives the yellow minion room and time to escape from the purple
    xP = 100 # minion
    yP = 100

    yellowIncrX = 4 # the purple minion will move slower than the yellow minion,
    yellowIncrY = 1 # to create a challenge for each minion. (ex. for the yellow minion,
    purpleIncrX = 2 # it has to collect all the bananas and for the purple minion, it has 
    purpleIncrY = 0 # to catch the yellow minion at a slower rate)
    gravity = 0.25 # acceleration of gravity
    
    # create platforms
    platforms.append(Platform(75, 326, 66))
    platforms.append(Platform(411, 662, 66))
    platforms.append(Platform(151, 571, 141))
    platforms.append(Platform(31, 451, 216))
    platforms.append(Platform(522, 662, 216))
    platforms.append(Platform(84, 638, 291))
    platforms.append(Platform(34, 212, 366))
    platforms.append(Platform(271, 452, 366))
    platforms.append(Platform(510, 688, 366))
    
def draw():
    global Main
    global nameBackground, backGround,leaderboard, yellowMinion, yellowMinionFlip, purpleMinion, purpleMinionFlip, bananas, stop, pause
    global directionY, directionP
    global yellowIncrX, yellowIncrY, purpleIncrX, purpleIncrY, gravity, xY, yY, xP, yP
    global groundedY, groundedP
    global Instructions, page
    global timer
    global winner
    global name1, name2, cur_name, user_info 
    global user_info
    global file
    global high_scores
    global sliderOn, slider, loude

    if page == 1:
        image(Main, 0, 0, 721,450)
        #we are creating the button design for PLAY into a bright, eye-catching box        
        stroke(0, 0, 0)
        fill(225, 225, 51)
        rect(225, 125, 270, 65)
        fill(0)
        textFont(dFont)
        textSize(40) 
        textAlign(CENTER)
        text("PLAY", 361, 176)
        fill(250, 250, 250)
        
        #simple text to indicate the instructions
        textSize(19)
        text("INSTRUCTIONS", 361, 225)
        text("LEADERBOARD", 361, 275)
        
        fill(180)
        rect (sliderX, sliderY, sliderW, sliderL)
        if ((mouseY >= sliderY) and (mouseY <= sliderY + sliderL ) and (mouseX >= sliderX  ) and (mouseY < sliderX + sliderW )):
            if (mouseX <= sliderX + sliderW ):
                slider = mouseX - sliderX    
                
        fill (51)
        rect (sliderX, sliderY, slider, sliderL)
        loude =  (slider * 0.3) -35.0
        
        minionSound.play() 
        minionSound.setGain(loude) 
        delay(300)
        print(minionSound.getGain())
    else:
        textAlign(LEFT)
        
    if page == 2:    
        image (backGround, 0, 0, 721, 450)
        timer = timer + 1
        #simple text which players can press if they would like to go back to the main menu
        fill(255) 
        textFont(font)
        textSize(20)
        image(stop, 682, 412, 30, 30)
        
        for b in bullets:
            b.x = b.x + 2 * b.dir
            image(b.img, b.x, b.y)
            if b.x > xY and b.x < xY + 50 and b.y > yY and b.y < yY + 50:
                winner = 1
                file.write(str(name2)+" "+ str(timer/60) +" purple" + "\n")
                if high_scores == []:
                    high_scores.insert(0,[name2,timer/60,"purple"])
                else:
                    for i in range(len(high_scores)):
                        if timer/60 < float(high_scores[i][1]) or i == (len(high_scores) - 1):
                            if timer/60 < float(high_scores[i][1]):
                                high_scores.insert(i,[name2,timer/60,"purple"])   
                            else:
                                high_scores.insert(i+1,[name2,timer/60,"purple"])
                            break
                timer = 0.0
                page = 3
                cur_name = 1
                name1 = ""
                name2 = ""
                    
                delay(400)
                break
            if b.x < 0 or b.x > 700:
                del b
    
   # # Indicates the location of the banana when the yellow minion has not yet collected the banana
        if banana_list[0] == 0:
            image (bananas, 130, 20, 30, 30)
        if banana_list[1] == 0:
            image (bananas, 240, 20, 30, 30)
        if banana_list[2] == 0:
            image (bananas, 470, 20, 30, 30)
        if banana_list[3] == 0:
            image (bananas, 590, 20, 30, 30)
        if banana_list[4] == 0:
            image (bananas, 210, 95, 30, 30)
        if banana_list[5] == 0:
            image (bananas, 350, 95, 30, 30)
        if banana_list[6] == 0:
            image (bananas, 490, 95, 30, 30)
        if banana_list[7] == 0:
            image (bananas, 100, 170, 30, 30)
        if banana_list[8] == 0:
            image (bananas, 230, 170, 30, 30)
        if banana_list[9] == 0:
            image (bananas, 370, 170, 30, 30)
        if banana_list[10] == 0:
            image (bananas, 595, 170, 30, 30)
        if banana_list[11] == 0:
            image (bananas, 150, 245, 30, 30)
        if banana_list[12] == 0:
            image (bananas, 285, 245, 30, 30)
        if banana_list[13] == 0:
            image (bananas, 420, 245, 30, 30)
        if banana_list[14] == 0:
            image (bananas, 555, 245, 30, 30)
        if banana_list[15] == 0:
            image (bananas, 110, 320, 30, 30)
        if banana_list[16] == 0:
            image (bananas, 335, 320, 30, 30)
        if banana_list[17] == 0:
            image (bananas, 560, 320, 30, 30)
            
        # Platforms which the minions run on top of
        for platform in platforms:
            platform.display()
            
        if directionY == 1:
            image (yellowMinion, xY, yY, 50, 50)
        else:
            image (yellowMinionFlip, xY, yY, 50, 50)
        
        if directionP == 1:
            image (purpleMinion, xP, yP, 50, 50)
        else:
            image (purpleMinionFlip, xP, yP, 50, 50)
        
        # Horizontal movement
        if buttons[0] ==  1:
            if xY < 685:
                xY = xY + yellowIncrX
        if buttons[1] == 1:
            if xY > 1:
                xY = xY - yellowIncrX
        if buttons[4] == 1:
            if xP < 680:
                xP = xP + purpleIncrX
        if buttons[5] == 1:
            if xP > -15:
                xP = xP - purpleIncrX
        
        # Checks if the minions are on a platform or in the air
        levelY = 1000
        levelP = 1000
        for platform in platforms:
            if xY + 38 >= platform.x1 and xY + 10 <= platform.x2 and yY + 50 <= platform.y and platform.y < levelY:
                levelY = platform.y
            if xP + 38 >= platform.x1 and xP + 23 <= platform.x2 and yP + 50 <= platform.y and platform.y < levelP:
                levelP = platform.y
        
        if levelY == 1000:
            groundedY = False
        else:
            if yY == levelY:
                groundedY = True
            else:
                if yellowIncrY <= 0 and yY + 50 - yellowIncrY > levelY:
                    yY = levelY - 50
                    yellowIncrY = 0
                    groundedY = True
                else:
                    groundedY = False
            
        if levelP == 1000:
            groundedP = False
        else:
            if yP == levelP:
                groundedP = True
            else:
                if purpleIncrY <= 0 and yP + 50 - purpleIncrY > levelP:
                    yP = levelP - 50
                    purpleIncrY = 0
                    groundedP = True
                else:
                    groundedP = False
            
        # Jumping
        if buttons[2] == 1:
            if groundedY:
                groundedY = False
                yellowIncrY = 7
                
        if buttons[6] == 1:
            if groundedP:
                groundedP = False
                purpleIncrY = 7

        # Falling through platforms
        if buttons[3] == 1:
            if groundedY:
                yellowIncrY = -2
                groundedY = False
        if buttons[7] == 1:
            if groundedP:
                purpleIncrY = -2
                groundedP = False
        
        # teleports minions back to the top if they fall off the map
        if yY > 450:
            yY = -50
        if yP > 450:
            yP = -50

        yY -= yellowIncrY
        yP -= purpleIncrY
        if yellowIncrY > -15:
            yellowIncrY -= gravity
        if purpleIncrY > -15:
            purpleIncrY -= gravity
        
        # This means that if the yellow minion has touched the banana, the banana disapears 
        if xY < 130 + 30 and xY + 50 > 130 and yY < 20 + 30 and yY + 50 > 20:
            banana_list[0] = 1
        if xY < 240 + 30 and xY + 50 > 240 and yY < 20 + 30 and yY + 50 > 20:
            banana_list[1] = 1
        if xY < 470 + 30 and xY + 50 > 470 and yY < 20 + 30 and yY + 50 > 20:
            banana_list[2] = 1
        if xY < 590 + 30 and xY + 50 > 590 and yY < 20 + 30 and yY + 50 > 20:
            banana_list[3] = 1
        if xY < 210 + 30 and xY + 50 > 210 and yY < 95 + 30 and yY + 50 > 95:
            banana_list[4] = 1
        if xY < 350 + 30 and xY + 50 > 350 and yY < 95 + 30 and yY + 50 > 95:
            banana_list[5] = 1
        if xY < 490 + 30 and xY + 50 > 490 and yY < 95 + 30 and yY + 50 > 95:
            banana_list[6] = 1
        if xY < 100 + 30 and xY + 50 > 100 and yY < 170 + 30 and yY + 50 > 170:
            banana_list[7] = 1
        if xY < 230 + 30 and xY + 50 > 230 and yY < 170 + 30 and yY + 50 > 170:
            banana_list[8] = 1
        if xY < 370 + 30 and xY + 50 > 370 and yY < 170 + 30 and yY + 50 > 170:
            banana_list[9] = 1
        if xY < 595 + 30 and xY + 50 > 595 and yY < 170 + 30 and yY + 50 > 170:
            banana_list[10] = 1
        if xY < 150 + 30 and xY + 50 > 150 and yY < 245 + 30 and yY + 50 > 245:
            banana_list[11] = 1
        if xY < 285 + 30 and xY + 50 > 285 and yY < 245 + 30 and yY + 50 > 245:
            banana_list[12] = 1
        if xY < 420 + 30 and xY + 50 > 420 and yY < 245 + 30 and yY + 50 > 245:
            banana_list[13] = 1
        if xY < 555 + 30 and xY + 50 > 555 and yY < 245 + 30 and yY + 50 > 245:
            banana_list[14] = 1
        if xY < 110 + 30 and xY + 50 > 110 and yY < 320 + 30 and yY + 50 > 320:
            banana_list[15] = 1
        if xY < 335 + 30 and xY + 50 > 335 and yY < 320 + 30 and yY + 50 > 320:
            banana_list[16] = 1
        if xY < 560 + 30 and xY + 50 > 560 and yY < 320 + 30 and yY + 50 > 320:
            banana_list[17] = 1
            
        # Once, all bananas are collected, the game will show a GAME OVER page, indicating
        # that the yellow minion has won by completing its objective
        if banana_list == [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
            winner = 0
            file.write(str(name1)+" "+ str(timer/60) +" yellow" + "\n")
            if high_scores == []:
                high_scores.insert(0,[name1,timer/60,"yellow"])
            else:
                for i in range(len(high_scores)):
                    if timer/60 < float(high_scores[i][1]) or i == (len(high_scores) - 1):
                        if timer/60 < float(high_scores[i][1]):
                            high_scores.insert(i,[name1,timer/60,"yellow"])   
                        else:
                            high_scores.insert(i+1,[name1,timer/60,"yellow"])
                        break
            timer = 0.0
            page = 3
            cur_name = 1
            name1 = ""
            name2 = ""

            delay(400) 
            
    if page == 3:
        # this is the Game Over page
        image(Main, 0, 0, 721, 450)
        fill(255)
        textFont(font)
        textSize(1)
        text("GAME OVER!", 200, 180)
        fill(255)
        textSize(25)
        if winner == 0:
            text("YELLOW MINION WINS!!", 98, 150)
        if winner == 1:
            text("PURPLE MINION WINS!!", 98, 150)
            
        stroke(0, 0, 0)
        fill(255, 255, 0)
        rect(270, 195, 182, 30)
        fill(0)
        textSize(15)
        text("PLAY AGAIN", 278, 220)
        
    if page == 4:
        # this is the instructions page
        image(Instructions, 0,0, 721,450)
        fill(255)
        textFont(dFont)
        textSize(20)
        text("BACK", 655, 435)
        
    if page == 5:
        image(nameBackground, 0, 0, 721, 450)
        fill(255)
        textFont(font)
        text("Type name of first player, then press spacebar.", 28, 75)
        text(name1,29, 215)
        text(name2, 398, 215)
        stroke(0, 0, 0)
        fill(255, 255, 0)
        rect(276, 298, 150, 28)
        fill(0)
        textSize(15)
        text("CONTINUE", 280, 320)
        
    if page == 6:
        image(leaderboard, 0, 0, 721, 450)
        fill(255)
        textFont(dFont)
        textSize(20)
        text("BACK", 655, 435)
        highScoreLen = len(high_scores)
        if highScoreLen < 10:
            for score in range(highScoreLen):
                text(high_scores[score][0], 210, 158+23*score)
                text(high_scores[score][1], 390, 158+23*score)
                text(high_scores[score][2], 580, 158+23*score)
        else:
            for score in range(10):
                text(high_scores[score][0], 210, 158+23*score)
                text(high_scores[score][1], 390, 158+23*score)
                text(high_scores[score][2], 580, 158+23*score)
    if page == 7:
        image(pause, 0, 0, 721, 450)
            

# resets all player positions and deletes all bullets
def reset():
    global xY, yY, xP, yP, yellowIncrY, purpleIncrY, banana_list, bullets
    xY = 611
    yY = 100
    xP = 100
    yP = 100
    yellowIncrY = 0
    purpleIncrY = 0
    banana_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    user_info = [] 
    del bullets[:]

def mouseClicked():
    global page, xY, yY, xP, yP, yellowIncrY, purpleIncrY, banana_list, bullets
    print(mouseX, mouseY)
    
    if page == 1:
        # this is the play button on the menu page, which will lead the player to the game
        if 225 <= mouseX <= 495:
            if 125 <= mouseY <= 190:
                page = 5
        # this is the button on the menu page, which will lead to the instructions page         
        if 298 <= mouseX <= 434:
            if 209 <= mouseY <= 227:
                page = 4
        # this is the button on the menu page, which will lead to the leaderboard page  
        if 298 <= mouseX <= 434:
            if 259 <= mouseY <= 277:
                page = 6
    if page == 2:
        # this is the button on the game page, which will go back to the pause screen
        if 682 <= mouseX <= 712:
            if 412 <= mouseY <= 442:
                page = 7
                # this resets the minions and bananas back into their original position
                #reset()
    if page == 3:
        # this is the play again button on the game over page when the yellow minion has won, it will go back to the menu 
        if 270 <= mouseX <= 452:
            if 195 <= mouseY <= 222:
                page = 1
                # this resets the minions and bananas back into their original position
                reset()
    if page == 4:
        # this is the back button on the instructions page, it will go back to the menu
        if 656 <= mouseX <= 706:
            if 419 <= mouseY <= 435:
                page = 1
    if page == 5:
        # this is the continue button on the name page, it will go back to the game over screen
        if 276 <= mouseX <= 426:
            if 299 <= mouseY <= 327:
                page = 2
                # this resets the minions and bananas back into their original position
                reset()      
    if page == 6:
        if 656 <= mouseX <= 706:
            if 419 <= mouseY <= 435:
                page = 1
                reset()
                
    if page ==7:
        if 185<= mouseX <= 531:
            if 27<= mouseY <= 133:
                page =2
        if 185 <= mouseX <= 531:
            if 155 <= mouseY <= 215:
                page = 2
                reset()
        if 185 <= mouseX <= 531:
            if 252 <= mouseY <= 311:
                page = 4
        if 185 <= mouseX <= 531:
            if 340 <= mouseY <= 414:
                page =1        
        
def keyPressed():
        global buttons
        global name1, name2, name
        global cur_name
        global xP, yP
        global bullet
        global shot, directionY, directionP
        global user_info
        # this gives certain letters and symbols (like the arrows) on the keyboard, a certain direction which it moves at
        if page == 5:
            if key == ' ' and cur_name == 1:
                cur_name = cur_name + 1
            elif cur_name == 1:
                if keyCode==8 and len(name1)<11:
                    name1 = name1[:-1]
                elif keyCode>=65 and keyCode<=90 and len(name1)<11:
                    name1+=key
            elif cur_name == 2:
                if keyCode==8 and len(name1)<11:
                    name2 = name2[:-1]
                elif keyCode>=65 and keyCode<=90 and len(name2)<11:
                    name2+=key
                    
        if key == CODED:
            if keyCode == RIGHT and xY <= 671:
                buttons[0] = 1
                directionY = 1
            elif keyCode == LEFT and xY >= 3:
                buttons[1] = 1  
                directionY = -1              
            elif keyCode == UP and yY >= 3:
                buttons[2] = 1
            elif keyCode == DOWN and yY <= 400:
                buttons[3] = 1
        if (key == 'd') and xP <= 671:
            buttons[4] = 1
            directionP = 1
        elif (key == 'a') and xP >= 3:
            buttons[5] = 1
            directionP = -1
        elif (key == 'w') and yP >= 3:
            buttons[6] = 1
        elif (key == 's')and yP <= 400: 
            buttons[7] = 1
        elif key == ' ':
            if shot == False:
                bullets.append(Bullet(xP+15, yP+25, directionP, bullet))
                shot = True
            
def keyReleased():
    global buttons, shot
    # this recognizes that when a certain key is released, the minion should stop moving 
    # or stop moving in a certain direction (ex. if the player presses the up and right 
    # button, but then the player releases the up button, the minion will only move right)  
    if key == CODED:
        if keyCode == RIGHT:
            buttons[0] = 0 
        elif keyCode == LEFT:
            buttons[1] = 0
        elif keyCode == UP:
            buttons[2] = 0
        elif keyCode == DOWN:
            buttons[3] = 0
    if key == 'd':
        buttons[4] = 0
    elif key == 'a':
        buttons[5] = 0
    elif key == 'w':
        buttons[6] = 0
    elif key == 's':
        buttons[7] = 0
    elif key == ' ':
        shot = False

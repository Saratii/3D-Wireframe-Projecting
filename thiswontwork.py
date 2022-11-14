import pygame
import numpy as np
import math

bg = pygame.image.load("spacebackground.jpeg")
bg = pygame.transform.scale(bg, (1400, 800))
vector3DCube = np.array([[0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 1], [0, 0, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1], [1, 1, 0], [1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 1, 0], [1, 1, 0]])
a=[0,0,0]
b=1,0,0
c=0.5,math.sqrt(3)/2,0
d=0.5,math.sqrt(3)/6,math.sqrt(2/3)

vector3DPyramid = np.array([a,b,c,a,d,b,d,c])
button1pressed = False
vector2D = []
Clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((1400, 800))
button1x = 1100
button2x = 1220
button3x = 1220
button4x = 1220
running = True
focalLength = 1000
buttonv = 2
button2Pressed = False
button2Direction = "none"
button3Direction = 'none'
button3Pressed = False
button4Direction = 'none'
button4Pressed = False
toggleX = False
toggleY = False
toggleZ = False
def rotate(shape, axis, theta):
    if axis == "x":
        rotationMatrix = np.array([[1, 0, 0], [0, math.cos(theta), -1*math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])
    elif axis == "y":
        rotationMatrix = np.array([[math.cos(theta), 0, math.sin(theta)], [0, 1, 0], [-1*math.sin(theta), 0, math.cos(theta)]])
    elif axis == "z":
        rotationMatrix = np.array([[math.cos(theta), -1*math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])
    return np.dot(shape, rotationMatrix)

while running:
    theta = 0.02 * (button1x - 1100) / 40
    Clock.tick(FPS)
    screen.blit(bg, (0, 0))
    if button2Pressed:
        if button2x <= 1230:
            button2Direction = "right"
            button2Pressed = False
        elif button2x > 1230:
            button2Direction = "left"
            button2Pressed = False
    if button2Direction == "left":
        if button2x > 1220:
            button2x -= buttonv
        else:
            button2Direction = "none"
            toggleX = False
    elif button2Direction == 'right':
        if button2x < 1240:
            button2x += buttonv
        else: 
            button2Direction = "none"
            toggleX = True
    if button3Pressed:
        if button3x <= 1230:
            button3Direction = "right"
            button3Pressed = False
        elif button3x > 1230:
            button3Direction = "left"
            button3Pressed = False
    if button3Direction == "left":
        if button3x > 1220:
            button3x -= buttonv
        else:
            button3Direction = "none"
            toggleY = False
    elif button3Direction == 'right':
        if button3x < 1240:
            button3x += buttonv
        else: 
            button3Direction = "none"
            toggleY = True
    if button4Pressed:
        if button4x <= 1230:
            button4Direction = "right"
        elif button4x > 1230:
            button4Direction = "left"
        button4Pressed = False
    if button4Direction == "left":
        if button4x > 1220:
            button4x -= buttonv
        else:
            button4Direction = "none"
            toggleZ = False
    elif button4Direction == 'right':
        if button4x < 1240:
            button4x += buttonv
        else: 
            button4Direction = "none"
            toggleZ = True

    if toggleX:
        vector3DCube = rotate(vector3DCube, 'y', theta)
        vector3DPyramid = rotate(vector3DPyramid, 'y', theta)
    if toggleY:
        vector3DCube = rotate(vector3DCube, 'x', theta)
        vector3DPyramid = rotate(vector3DPyramid, 'x', theta)
    if toggleZ:
        vector3DCube = rotate(vector3DCube, 'z', theta)
        vector3DPyramid = rotate(vector3DPyramid, 'z', theta)
    
    vector2DCube = []
    vector2DPyramid = []

    for i in range(len(vector3DPyramid)):
        vector2DPyramid.append((focalLength * vector3DPyramid[i][0] * 400 / (focalLength + vector3DPyramid[i][2] * 400)+100, focalLength * vector3DPyramid[i][1] * 400 / (focalLength + vector3DPyramid[i][2] * 100) + 250))
    for i in range(len(vector3DCube)):
        vector2DCube.append((focalLength * vector3DCube[i][0] * 300 / (focalLength + vector3DCube[i][2] * 300)+600, focalLength * vector3DCube[i][1] * 300 / (focalLength + vector3DCube[i][2] * 100) + 250))
    if button1pressed:
        if mx >= 1100 and mx <= 1350:
            button1x = mx
    pygame.draw.lines(screen, (255, 0, 0), False, vector2DCube, width=7)
    pygame.draw.lines(screen, (0, 0, 255), False, vector2DPyramid, width=7)
    pygame.draw.line(screen, 'cyan', (1100, 200), (1350, 200), width=5)
    pygame.draw.circle(screen, 'cyan', (button1x, 200), 10)
    pygame.draw.rect(screen, 'cyan', (1200, 250, 60, 40), 3, 600)
    pygame.draw.circle(screen, 'cyan', (button2x, 270), 17)
    pygame.draw.rect(screen, 'cyan', (1200, 300, 60, 40), 3, 600)
    pygame.draw.circle(screen, 'cyan', (button3x, 320), 17)
    pygame.draw.rect(screen, 'cyan', (1200, 350, 60, 40), 3, 600)
    pygame.draw.circle(screen, 'cyan', (button4x, 370), 17)
    pygame.display.flip()
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            running = False
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1x - 8 < mx < button1x + 8 and 186 < my < 208:
                button1pressed = True
            elif button2x - 17 < mx < button2x + 17 and 246 < my < 294:
                button2Pressed = True
            elif button3x - 17 < mx < button3x + 17 and 283 < my < 337:
                button3Pressed = True
            elif button4x - 17 < mx < button4x + 17 and 356 < my < 384:
                button4Pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if button1pressed:
                button1pressed = False
                
 

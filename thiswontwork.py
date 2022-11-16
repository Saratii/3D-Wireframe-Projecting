import pygame
import numpy as np
import math

#pygame setup
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
button1Text = font.render('Rotational Speed', False, 'cyan')
button2Text = font.render('X Axis', False, 'cyan')
button3Text = font.render('Y Axis', False, 'cyan')
button4Text = font.render('Z Axis', False, 'cyan')
button5Text = font.render('Focal Length', False, 'cyan')
button6Text = font.render('Reset', False, 'cyan')
button7Text = font.render('Shape:', False, 'cyan')
bg = pygame.image.load("spacebackground.jpeg")
bg = pygame.image.load("background3.jpeg")
bg = pygame.transform.scale(bg, (1400, 800))
Clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('3D Wireframe Projection')

running = True
focalLength = 700
buttonv = 2

#3d frame setup
vector3DCube = np.array([[-0.5, -0.5, 0.5], [0.5,-0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, -0.5, 0.5], [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5]])
a=[-0.5,0 - math.sqrt(3)/3,0 - math.sqrt(2/3)/2]
b=0.5,0 - math.sqrt(3)/3,0 - math.sqrt(2/3)/2
c=0,math.sqrt(3)/2 - math.sqrt(3)/3,0 - math.sqrt(2/3)/2
d=0,math.sqrt(3)/6 - math.sqrt(3)/3,math.sqrt(2/3) - math.sqrt(2/3)/2

#game object setup
button1x = 1100
button2x = 1220
button3x = 1220
button4x = 1220
button5x = 1100
vector3DPyramid = np.array([a, b, c, a, d, b, d, c])
vector3DX = np.array([[-1, 0, 0], [1, 0, 0]])
vector3DY = np.array([[0, -1, 0], [0, 1, 0]])
vector3DZ = np.array([[0, 0, -1], [0, 0, 1]])
button1pressed = False
button2Pressed = False
button2Direction = "none"
button3Direction = 'none'
button3Pressed = False
button4Direction = 'none'
button4Pressed = False
button5Pressed = False
toggleX = False
toggleY = False
toggleZ = False
shape = 'cube'

#rotation function
def rotate(shape, axis, theta):
    if axis == "x":
        rotationMatrix = np.array([[1, 0, 0], [0, math.cos(
            theta), -1*math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])
    elif axis == "y":
        rotationMatrix = np.array([[math.cos(theta), 0, math.sin(theta)], [
                                  0, 1, 0], [-1*math.sin(theta), 0, math.cos(theta)]])
    elif axis == "z":
        rotationMatrix = np.array([[math.cos(
            theta), -1*math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])
    return np.dot(shape, rotationMatrix)

#game loop
while running:
    focalLength = 700 - (button5x - 1100) * 5
    theta = 0.02 * (button1x - 1100) / 35
    Clock.tick(FPS)
    screen.blit(bg, (0, 0))
    #button conditions
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
    #rotation conditions
    if toggleX:
        vector3DCube = rotate(vector3DCube, 'y', theta)
        vector3DPyramid = rotate(vector3DPyramid, 'y', theta)
        vector3DX = rotate(vector3DX, 'y', theta)
        vector3DX = rotate(vector3DX, 'y', theta)
        vector3DX = rotate(vector3DX, 'y', theta)
    if toggleY:
        vector3DCube = rotate(vector3DCube, 'x', theta)
        vector3DPyramid = rotate(vector3DPyramid, 'x', theta)
        vector3DY = rotate(vector3DY, 'x', theta)
        vector3DY = rotate(vector3DY, 'x', theta)
        vector3DY = rotate(vector3DY, 'x', theta)
    if toggleZ:
        vector3DCube = rotate(vector3DCube, 'z', theta)
        vector3DPyramid = rotate(vector3DPyramid, 'z', theta)
        vector3DZ = rotate(vector3DZ, 'z', theta)
        vector3DZ = rotate(vector3DZ, 'z', theta)
        vector3DZ = rotate(vector3DZ, 'z', theta)
    #projection setup
    vector2DCube = []
    vector2DPyramid = []
    vector2DX = []
    vector2DY = []
    vector2DZ = []
    #actual projection using linear algebra dark magic
    if shape == 'cube':
        for i in range(len(vector3DCube)):
            vector2DCube.append((focalLength * vector3DCube[i][0] * 350 / (focalLength + vector3DCube[i][2] * 350) +
                                500, focalLength * vector3DCube[i][1] * 350 / (focalLength + vector3DCube[i][2] * 350) + 380))
        pygame.draw.lines(screen, (255, 0, 0), False, vector2DCube, width=10)
    elif shape == 'pyramid':
        for i in range(len(vector3DPyramid)):
            vector2DPyramid.append((focalLength * vector3DPyramid[i][0] * 400 / (focalLength + vector3DPyramid[i][2] * 400) +
                               475, focalLength * vector3DPyramid[i][1] * 400 / (focalLength + vector3DPyramid[i][2] * 400) + 450))
        pygame.draw.lines(screen, (57, 255, 20), False, vector2DPyramid, width=10)
    for i in range(len(vector3DX)):
        vector2DX.append((focalLength * vector3DX[i][0] * 90 / (focalLength + vector3DX[i][2] * 90) +
                          1240, focalLength * vector3DX[i][1] * 90 / (focalLength + vector3DX[i][2] * 90) + 640))
    for i in range(len(vector3DY)):
        vector2DY.append((focalLength * vector3DY[i][0] * 90 / (focalLength + vector3DY[i][2] * 90) +
                          1240, focalLength * vector3DY[i][1] * 90 / (focalLength + vector3DY[i][2] * 90) + 640))
    for i in range(len(vector3DZ)):
        vector2DZ.append((focalLength * vector3DZ[i][0] * 90 / (focalLength + vector3DZ[i][2] * 90) +
                          1240, focalLength * vector3DZ[i][1] * 90 / (focalLength + vector3DZ[i][2] * 90) + 640))
    if button1pressed:
        if mx >= 1100 and mx <= 1350:
            button1x = mx
    if button5Pressed:
        if mx >= 1100 and mx <= 1350:
            button5x = mx
    
    #drawing to screen
    pygame.draw.line(screen, (250, 253, 15), vector2DX[0], vector2DX[1], width=4)
    pygame.draw.line(screen, (0, 0, 255), vector2DY[0], vector2DY[1], width=4)
    pygame.draw.line(screen, (255, 0, 255), vector2DZ[0], vector2DZ[1], width=4)
    pygame.draw.line(screen, 'cyan', (1100, 200), (1350, 200), width=5)
    pygame.draw.line(screen, 'cyan', (1100, 500), (1350, 500), width=5)
    pygame.draw.circle(screen, 'cyan', (button1x, 200), 10)
    pygame.draw.circle(screen, 'cyan', (button5x, 500), 10)
    pygame.draw.rect(screen, 'cyan', (1200, 250, 60, 40), 3, 600)
    pygame.draw.circle(screen, 'cyan', (button2x, 270), 17)
    pygame.draw.rect(screen, 'cyan', (1200, 300, 60, 40), 3, 600)
    pygame.draw.circle(screen, 'cyan', (button3x, 320), 17)
    pygame.draw.rect(screen, 'cyan', (1200, 350, 60, 40), 3, 600)
    pygame.draw.circle(screen, 'cyan', (button4x, 370), 17)
    pygame.draw.rect(screen, 'cyan', (1180, 400, 100, 40), 3, 600)
    pygame.draw.rect(screen, 'cyan', (1170, 100, 50, 50), 3, 10)
    pygame.draw.rect(screen, 'cyan', (1230, 100, 50, 50), 3, 10)
    pygame.draw.rect(screen, 'red', (1185, 115, 20, 20), 2)
    pygame.draw.polygon(screen, (57, 255, 20), ((1254, 112), (1268, 135), (1240, 135), (1254, 112)), 2)

    screen.blit(button1Text, (1150, 170))
    screen.blit(button2Text, (1075, 260))
    screen.blit(button3Text, (1075, 310))
    screen.blit(button4Text, (1075, 360))
    screen.blit(button5Text, (1150, 470))
    screen.blit(button6Text, (1203, 411))
    screen.blit(button7Text, (1192, 70))
    #update display
    pygame.display.flip()
    mx, my = pygame.mouse.get_pos()
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #button checks
            if button1x - 8 < mx < button1x + 8 and 186 < my < 208:
                button1pressed = True
            elif button2x - 17 < mx < button2x + 17 and 246 < my < 294:
                button2Pressed = True
            elif button3x - 17 < mx < button3x + 17 and 283 < my < 337:
                button3Pressed = True
            elif button4x - 17 < mx < button4x + 17 and 356 < my < 384:
                button4Pressed = True
            elif button5x - 8 < mx < button5x + 8 and 492 < my < 508:
                button5Pressed = True
            elif 1175 < mx < 1215 and 110 < my < 145:
                shape = 'cube'
            elif 1235 < mx < 1275 and 105 < my < 145:
                shape = 'pyramid'
            elif 1180 < mx < 1280 and 400 < my < 440:
                button1x = 1100
                button2x = 1220
                button3x = 1220
                button4x = 1220
                button5x = 1100
                vector3DCube = np.array([[-0.5, -0.5, 0.5], [0.5,-0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, -0.5, 0.5], [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5]])
                a=[-0.5,0 - math.sqrt(3)/3,0 - math.sqrt(3)/3]
                b=0.5,0 - math.sqrt(3)/3,0 - math.sqrt(3)/3
                c=0,math.sqrt(3)/2 - math.sqrt(3)/3,0 - math.sqrt(3)/3
                d=0,math.sqrt(3)/6 - math.sqrt(3)/3,math.sqrt(2/3) - math.sqrt(3)/3
                button1pressed = False
                button2Pressed = False
                button2Direction = "none"
                button3Direction = 'none'
                button3Pressed = False
                button4Direction = 'none'
                button4Pressed = False
                toggleX = False
                toggleY = False
                toggleZ = False
                vector3DX = np.array([[-1, 0, 0], [1, 0, 0]])
                vector3DY = np.array([[0, -1, 0], [0, 1, 0]])
                vector3DZ = np.array([[0, 0, -1], [0, 0, 1]])
        elif event.type == pygame.MOUSEBUTTONUP:
            if button1pressed:
                button1pressed = False
            if button5Pressed:
                button5Pressed = False

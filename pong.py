import pygame
import random

pygame.init()

# Initials

WIDTH, HEIGHT = 1000, 600

# Creates pygame window with above dimensions
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Satta's Pong Game")
run = True
direction = [0, 1]
angle = [0, 1, 2]

# Colours
PINK = (255, 16, 240)
PURPLE = (153, 50, 204)
BLACK = (0, 0, 0)

# for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.5, 0.5

# for the paddles
#left, right paddle coordinates and dimensions
paddle_width, paddle_height = 20, 120
l_p_x, r_p_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
r_p_y = l_p_y = HEIGHT/2 - paddle_height/2
r_p_vel = l_p_vel = 0

# gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

# Main loop to run game
while run:
    window.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                r_p_vel = -0.9
            if i.key == pygame.K_DOWN:
                r_p_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
            if i.key == pygame.K_w:
                l_p_vel = -0.9
            if i.key == pygame.K_s:
                l_p_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1

        if i.type == pygame.KEYUP:
            r_p_vel = 0
            l_p_vel = 0


    # BALL'S MOVEMENT CONTROLS
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.5, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.25, 0.5
        
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.5, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.25, 0.5


        ball_vel_x *= -1
    
    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.5, 0.5
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.5, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.25, 0.5
        
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.5, 0.25
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.25, 0.25
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.25, 0.5

    # PADDLE'S MOVEMENT CONTROLS   
    if l_p_y >= HEIGHT - paddle_height:
        l_p_y = HEIGHT - paddle_height
    if l_p_y <= 0:
        l_p_y = 0
    if r_p_y >= HEIGHT - paddle_height:
        r_p_y = HEIGHT - paddle_height
    if r_p_y <= 0:
        r_p_y = 0
    
    # PADDLE COLLISIONS 
    # Left paddle
    if l_p_x <= ball_x <= l_p_x + paddle_width:
        if l_p_y <= ball_y <= l_p_y + paddle_height:
            ball_x = l_p_x + paddle_width
            ball_vel_x *= -1

    # Right paddle
    if r_p_x <= ball_x <= r_p_x:
        if r_p_y <= ball_y <= r_p_y + paddle_height:
            ball_x = r_p_x
            ball_vel_x *= -1

    # GADGETS IN ACTION
    if left_gadget == 1:
        if l_p_x <= ball_x <= l_p_x + paddle_width:
            if l_p_y <= ball_y <= l_p_y + paddle_height:
                ball_x = l_p_x + paddle_width
                ball_vel_x *= -3.5 
                left_gadget = 0
                left_gadget_remaining -= 1

    if right_gadget == 1:
        if r_p_x <= ball_x <= r_p_x:
            if r_p_y <= ball_y <= r_p_y + paddle_height:
                ball_x = r_p_x
                ball_vel_x *= 3.5
                right_gadget = 0
                right_gadget_remaining -= 1

    # MOVEMENTS
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    r_p_y += r_p_vel
    l_p_y += l_p_vel

    # OBJECTS
    pygame.draw.circle(window, PINK, (ball_x, ball_y), radius)
    pygame.draw.rect(window, PURPLE, pygame.Rect(l_p_x, l_p_y, paddle_width, paddle_height))
    pygame.draw.rect(window, PURPLE, pygame.Rect(r_p_x, r_p_y, paddle_width, paddle_height))
    pygame.display.update()
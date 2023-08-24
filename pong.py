import pygame
import random

pygame.init()

gadget_pair = 1
ch = int(input("Enter your choice for gadget pair: "))

if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2

# Initials

WIDTH, HEIGHT = 1000, 600

# Creates pygame window with above dimensions
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Satta's Pong Game")
run = True
player_1 = player_2 = 0
direction = [0, 1]
angle = [0, 1, 2]

# Colours
PINK = (255, 16, 240)
PURPLE = (153, 50, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7
dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
dummy_ball_vel_x, dummy_ball_vel_y = 0.7, 0.7

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
            if i.key == pygame.K_LEFT and right_gadget_remaining > 0:
                right_gadget = 2
            if i.key == pygame.K_w:
                l_p_vel = -0.9
            if i.key == pygame.K_s:
                l_p_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1
            if i.key == pygame.K_a and left_gadget_remaining > 0:
                left_gadget = 2

        if i.type == pygame.KEYUP:
            r_p_vel = 0
            l_p_vel = 0


    # BALL'S MOVEMENT CONTROLS
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if dummy_ball_y <= 0 + radius or dummy_ball_y >= HEIGHT - radius:
        dummy_ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        player_1 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4
        
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4

        ball_vel_x *= -1
        dummy_ball_vel_x *= -1
    
    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4
        
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_yball_vel_y, dummy_ball_vel_x = 0.7, 1.4

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
            dummy_ball_x = l_p_x + paddle_width
            ball_vel_x *= -1
            dummy_ball_vel_x *= -1

    # Right paddle
    if r_p_x <= ball_x <= r_p_x + paddle_width:
        if r_p_y <= ball_y <= r_p_y + paddle_height:
            ball_x = r_p_x
            dummy_ball_x = r_p_x
            ball_vel_x *= -1
            dummy_ball_vel_x *= -1

    # GADGETS IN ACTION
    if gadget_pair == 1:
        if left_gadget == 1:
            if l_p_x <= ball_x <= l_p_x + paddle_width:
                if l_p_y <= ball_y <= l_p_y + paddle_height:
                    ball_x = l_p_x + paddle_width
                    ball_vel_x *= -3.5 
                    dummy_ball_vel_x *= -3.5
                    left_gadget = 0
                    left_gadget_remaining -= 1

        elif left_gadget == 2:
            l_p_y = ball_y
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if r_p_x <= ball_x <= r_p_x + paddle_width:
                if r_p_y <= ball_y <= r_p_y + paddle_height:
                    ball_x = r_p_x
                    ball_vel_x *= -3.5
                    dummy_ball_vel_x *= -3.5
                    right_gadget = 0
                    right_gadget_remaining -= 1

        elif right_gadget == 2:
            r_p_y = ball_y
            right_gadget = 0
            right_gadget_remaining -= 1

    # second pair
    elif gadget_pair == 2:
        if left_gadget == 1:
            if l_p_x <= ball_x <= l_p_x + paddle_width:
                if l_p_y <= ball_y <= l_p_y + paddle_height:
                    ball_x = l_p_x + paddle_width
                    dummy_ball_x = l_p_x + paddle_width
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
                    dummy_ball_vel_y *= -1
                    left_gadget = 0
                    left_gadget_remaining -= 1

        if right_gadget == 1:
            if r_p_x <= ball_x <= r_p_x + paddle_width:
                if r_p_y <= ball_y <= r_p_y + paddle_height:
                    ball_x = r_p_x
                    dummy_ball_x = r_p_x
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1 
                    dummy_ball_vel_y *= -1
                    right_gadget = 0
                    right_gadget_remaining -= 1

    # MOVEMENTS
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    dummy_ball_x += dummy_ball_vel_x
    dummy_ball_y += dummy_ball_vel_y
    r_p_y += r_p_vel
    l_p_y += l_p_vel

    #scoreboard
    font = pygame.font.SysFont("monospace", 28)
    score_1 = font.render("Player_1: " + str(player_1), True, PINK)
    window.blit(score_1, (25, 25))
    score_2 = font.render("Player_2: " + str(player_2), True, PINK)
    window.blit(score_2, (750, 25))
    gad_left_1 = font.render("Gadget Left: " + str(left_gadget_remaining), True, PINK)
    window.blit(gad_left_1, (25, 65))
    gad_left_2 = font.render("Gadget Left: " + str(right_gadget_remaining), True, PINK)
    window.blit(gad_left_2, (750, 65))

    # OBJECTS
    pygame.draw.circle(window, PINK, (ball_x, ball_y), radius)
    pygame.draw.rect(window, PURPLE, pygame.Rect(l_p_x, l_p_y, paddle_width, paddle_height))
    pygame.draw.rect(window, PURPLE, pygame.Rect(r_p_x, r_p_y, paddle_width, paddle_height))
    
    # dummy ball section
    pygame.draw.circle(window, PINK, (dummy_ball_x, dummy_ball_y), radius)

    # gadget indication
    if left_gadget == 1:
        pygame.draw.circle(window, WHITE, (l_p_x + 10, l_p_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(window, WHITE, (r_p_x + 10, r_p_y + 10), 4)

    # end screen

    winning_font = pygame.font.SysFont('monospace', 100)
    if player_1 >= 5:
        window.fill(BLACK)
        endscreen = winning_font.render("PLAYER 1 WON!", True, WHITE)
        window.blit(endscreen, (100, 250))
    if player_2 >= 5:
        window.fill(BLACK)
        endscreen = winning_font.render("PLAYER 2 WON!", True, WHITE)
        window.blit(endscreen, (100, 250))


    pygame.display.update()


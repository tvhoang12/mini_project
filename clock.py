import time
from datetime import datetime
import pygame

HEIGHT = 400
WIDTH = 400
running = True

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()

time_font = pygame.font.SysFont('impact', 60)
capture_font = pygame.font.SysFont('impact', 30)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")
    
    # Lấy thời gian hiện tại
    now = datetime.now()
    HOUR = now.strftime("%H")
    MINUTE = now.strftime("%M")
    SECOND = now.strftime("%S")
    
    time_text = time_font.render(f"{HOUR}:{MINUTE}:{SECOND}", True, "black", "white")
    
    capture_text = capture_font.render("Current time", True, "black", "white")
    screen.blit(capture_text, (120, 10))
    
    # # Vẽ kim giờ
    # hour_angle = int(HOUR) * 30 + int(MINUTE) / 2
    # hour_angle = hour_angle % 360
    # hour_angle = hour_angle * 3.14 / 180
    # hour_x = WIDTH//2 + 70 * (3 * 3.14 / 2 - hour_angle)
    # hour_y = HEIGHT//2 + 70 * (3 * 3.14 / 2 - hour_angle)
    # pygame.draw.line(screen, "black", (WIDTH//2, HEIGHT//2), (hour_x, hour_y), 5)
    
    # #vẽ kim phút
    # minute_angle = int(MINUTE) * 6
    # minute_angle = minute_angle % 360
    # minute_angle = minute_angle * 3.14 / 180
    # minute_x = WIDTH//2 + 100 * (3 * 3.14 / 2 - minute_angle)
    # minute_y = HEIGHT//2 + 100 * (3 * 3.14 / 2 - minute_angle)
    # pygame.draw.line(screen, "black", (WIDTH//2, HEIGHT//2), (minute_x, minute_y), 3)
    
    # #ve kim giay
    # second_angle = int(SECOND) * 6
    # second_angle = second_angle % 360
    # second_angle = second_angle * 3.14 / 180
    # second_x = WIDTH//2 + 120 * (3 * 3.14 / 2 - second_angle)
    # second_y = HEIGHT//2 + 120 * (3 * 3.14 / 2 - second_angle)
    # pygame.draw.line(screen, "red", (WIDTH//2, HEIGHT//2), (second_x, second_y), 1)
    
    # Vẽ vòng tròn đồng hồ
    pygame.draw.circle(screen, "black", (WIDTH//2, HEIGHT//2), 150, 5)
    
    
    # Vẽ văn bản lên màn hình
    screen.blit(time_text, (WIDTH//2 - time_text.get_width()//2, HEIGHT//2 - time_text.get_height()//2))
    
    # Cập nhật màn hình và điều chỉnh tốc độ lặp
    pygame.display.flip()
    clock.tick(1)

pygame.quit()

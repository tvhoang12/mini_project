import time
from datetime import datetime
import pygame
import math

HEIGHT = 600
WIDTH = 600
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
    HOUR = now.hour
    MINUTE = now.minute
    SECOND = now.second

    #chuẩn hóa thời gian hiện tại với 2 chữ số mỗi đơn vị
    time_text = time_font.render(f"{HOUR:02d}:{MINUTE:02d}:{SECOND:02d}", True, "black", "white")
    #in một cái capture text lên màn hình
    # capture_text = capture_font.render("Current time", True, "black", "white")
    # screen.blit(capture_text, (120, 10))
    #xấu nên bị xóa:))))
    
    # Vẽ kim giờ
    #chuyển HOUR sang góc
    hour_angle = (HOUR % 12 + MINUTE / 60) * 30
    hour_radian = math.radians(hour_angle - 90) 
    #tính góc cho kim giò
    hour_x = WIDTH // 2 + 70 * math.cos(hour_radian)
    hour_y = HEIGHT // 2 + 70 * math.sin(hour_radian)
    #vẽ ra màn hình
    pygame.draw.line(screen, "black", (WIDTH // 2, HEIGHT // 2), (hour_x, hour_y), 5)

    # Vẽ kim phút
    # tính góc kim phút
    minute_angle = MINUTE * 6 
    minute_radian = math.radians(minute_angle - 90) 
    '''
        giả sử tâm của vòng tròn đồng hồ là O, kim giờ là bán kính của 1 đường tròn nhỏ 70 pixel
        quay quanh tâm, có góc kim giờ => tính được vị trí của điểm cuối đoạn thẳng=> vẽ
    '''
    minute_x = WIDTH // 2 + 100 * math.cos(minute_radian)
    minute_y = HEIGHT // 2 + 100 * math.sin(minute_radian)
    
    pygame.draw.line(screen, "black", (WIDTH // 2, HEIGHT // 2), (minute_x, minute_y), 3)

    # Vẽ kim giây
    second_angle = SECOND * 6  # Mỗi giây tương ứng 6 độ
    second_radian = math.radians(second_angle - 90)  # Chuyển sang radian và điều chỉnh góc -90 độ
    second_x = WIDTH // 2 + 120 * math.cos(second_radian)
    second_y = HEIGHT // 2 + 120 * math.sin(second_radian)
    pygame.draw.line(screen, "red", (WIDTH // 2, HEIGHT // 2), (second_x, second_y), 1)

    # Vẽ vòng tròn đồng hồ
    pygame.draw.circle(screen, "black", (WIDTH//2, HEIGHT//2), 150, 5)
    
    
    # Vẽ thời gian hiện tại lên màn hình
    screen.blit(time_text, (WIDTH//2 - time_text.get_width()//2, HEIGHT//2 + 2 * time_text.get_height() + 5))
    
    # Cập nhật màn hình và điều chỉnh tốc độ lặp
    pygame.display.flip()
    clock.tick(1)

pygame.quit()

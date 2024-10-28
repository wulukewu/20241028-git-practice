import pygame
import sys
import random

#初始化
pygame.init()

# 一開始的顯示大小
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

# 定義顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# 螢幕顯示
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# 小鳥的屬性
bird_width, bird_height = 30, 20
bird_x = 100
bird_y = HEIGHT // 2 - bird_height // 2

# 小鳥的速度與重力
bird_velocity = 0
gravity = 0.5

# 管子的屬性
pipe_width, pipe_height = 50, random.randint(100, 300)
pipe_x = WIDTH
pipe_gap = 100  # 两部分水管之间的间隙
pipe_top_height = HEIGHT - pipe_height - pipe_gap
pipe_bottom_height = pipe_height

# 一開始管子的速度
pipe_velocity = 5

# 初始計分
score = 0

# 已經通過的管道數量
passed_pipes = 0

# 遊戲狀態變數
game_over = False

# 重新開始按鈕
button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 100, 50)

# 主循環
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  if game_over:
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0] and button_rect.collidepoint(pygame.mouse.get_pos()):
      game_over = False
      bird_y = HEIGHT // 2 - bird_height // 2
      pipe_x = WIDTH
      pipe_height = random.randint(100, 300)
      pipe_top_height = HEIGHT - pipe_height - pipe_gap
      pipe_bottom_height = pipe_height
      score = 0
      passed_pipes = 0
      pipe_velocity = 5  

  # 更新狀態
  if not game_over:
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0]:  # 左键点击
      bird_velocity = -5

    # 更新小鳥的位置
    bird_y += bird_velocity
    bird_velocity += gravity

    # 更新管道的位置
    pipe_x -= pipe_velocity

    # 判斷管道位置
    if pipe_x < 0:
      pipe_x = WIDTH
      pipe_height = random.randint(100, 300)
      pipe_top_height = HEIGHT - pipe_height - pipe_gap
      pipe_bottom_height = pipe_height
      score += 1
      passed_pipes += 1

      # 調整速度
      if passed_pipes % 1 == 0:  
        pipe_velocity += 2

    # 碰撞檢測
    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
    pipe_top_rect = pygame.Rect(pipe_x, 0, pipe_width, pipe_top_height)
    pipe_bottom_rect = pygame.Rect(pipe_x, HEIGHT - pipe_bottom_height,
                                   pipe_width, pipe_bottom_height)

    # 死亡判定（邊界）
    if bird_y < 0 or bird_y > HEIGHT - bird_height:
      print("Game Over! Score:", score)
      game_over = True

    # 死亡判定（管道）
    if bird_rect.colliderect(pipe_top_rect) or bird_rect.colliderect(
        pipe_bottom_rect):
      print("Game Over! Score:", score)
      game_over = True

  # 背景繪製
  screen.fill(BLUE)

  if not game_over:
    # 小鳥繪製
    pygame.draw.rect(screen, YELLOW, [bird_x, bird_y, bird_width, bird_height])

    # 管道繪製
    pygame.draw.rect(screen, GREEN,
                     [pipe_x, 0, pipe_width, pipe_top_height])  # 水管繪製
    pygame.draw.rect(
        screen, GREEN,
        [pipe_x, HEIGHT - pipe_bottom_height, pipe_width, pipe_bottom_height
         ])  

  # 重新開始後
  if game_over:
    pygame.draw.rect(screen, BLACK, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Restart", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 40, HEIGHT // 2 + 10))

    # 顯示分數
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 40, HEIGHT // 2 - 40))

  # 顯示實時分數
  font = pygame.font.Font(None, 24)
  score_text = font.render("Score: " + str(score), True, WHITE)
  screen.blit(score_text, (10, 10))

  # 螢幕刷新
  pygame.display.flip()

  # 楨率控制
  pygame.time.Clock().tick(30)

import pygame
import sys

def game_over_screen(screen, score, SCREEN_WIDTH, SCREEN_HEIGHT, font):
    game_over_font = pygame.font.Font(None, 72)
    small_font = pygame.font.Font(None, 36)
    text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    score_text = small_font.render(f"Final Score: {score}", True, (255, 255, 255))
    restart_text = small_font.render("Press ENTER to restart", True, (200, 200, 200))
    quit_text = small_font.render("Press ESC to quit", True, (200, 200, 200))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2 - 60))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - score_text.get_height() // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 90))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "restart"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()               

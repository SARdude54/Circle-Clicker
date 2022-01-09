import sys

import pygame.gfxdraw

from scripts.config import *
from scripts.func import draw_activity_widget, clear_data, read_json, append_game_data
from pygame.locals import *


def run_activity_log():
    running = True
    data_cleared = False

    game_list: list = read_json(ACTIVITY_DATA_FILE)
    game_list.reverse()

    while running:

        recent_title_text.draw(screen)

        if back_btn.draw(screen):
            running = False

        if clear_btn.draw(screen):
            data_cleared = True
            clear_data(ACTIVITY_DATA_FILE)
            pygame.draw.rect(screen, BLACK, Rect(0, 90, screen.get_width(), screen.get_height() - 90))

        if not data_cleared:

            for i in range(len(game_list)):
                draw_activity_widget(i*100 + 100, screen, game_list[i]["score"], game_list[i]["level"], game_list[i]["date"])
                if i == 3:
                    break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    screen.fill(BLACK)


def run_game_events(mx, my):
    """
    Loops through pygame events
    :param mx: int
    :param my: int
    :return: None
    """
    global circle, score
    # game events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # Mouse events for circle
        if event.type == MOUSEBUTTONDOWN and circle.mouse_collide(mx, my) and timer.is_started() and not timer.is_finished():
            score += 1
            circle.delete()
            circle = Circle(screen, RED, None)
            # Main menu events---set color of text and radius of circle for each server
            if level == "EASY":
                selected_level_text.set_color(GREEN)
                circle.set_radius(50)

            elif level == "MEDIUM":
                selected_level_text.set_color(YELLOW)
                circle.set_radius(30)

            elif level == "HARD":
                selected_level_text.set_color(RED)
                circle.set_radius(10)

            circle.draw_circle()


start_game = False


def main():
    global start_game, level, score
    run = True

    # Main game loop
    while run:

        # reset score
        if timer.get_time() == f"0:10":
            score = 0

        mx, my = pygame.mouse.get_pos()

        if not start_game:
            screen.blit(title_text.get_text(), title_text.get_text_rect())

            screen.blit(level_surf, level_surf_rect)

            if medium_btn.draw(screen):
                level = "MEDIUM"
                circle.set_radius(20)
                medium_btn.update(GREEN, BLUE)
                if easy_btn.is_selected():
                    easy_btn.update(GREEN, BLUE)
                if hard_btn.is_selected():
                    hard_btn.update(GREEN, BLUE)

            if easy_btn.draw(screen):
                level = "EASY"
                circle.set_radius(20)
                easy_btn.update(GREEN, BLUE)
                if medium_btn.is_selected():
                    medium_btn.update(GREEN, BLUE)
                if hard_btn.is_selected():
                    hard_btn.update(GREEN, BLUE)

            if hard_btn.draw(screen):
                level = "HARD"
                hard_btn.update(GREEN, BLUE)
                if easy_btn.is_selected():
                    easy_btn.update(GREEN, BLUE)
                if medium_btn.is_selected():
                    medium_btn.update(GREEN, BLUE)

            hard_btn.draw(screen)

            if start_btn.draw(screen):
                timer.set_timer(0, 10)
                start_game = True

            if activity_btn.draw(screen):
                screen.fill(BLACK)
                run_activity_log()

            if exit_btn.draw(screen):
                run = False

        else:
            timer.start()
            timer_text = Text(30, 20, timer.get_time(), FONT, 32, RED, None)

            exit_btn.set_y(350)

            score_text = Text(550, 20, f"Score: {score}", FONT, 32, BLUE)

            screen.fill(BLACK)
            screen.blit(score_text.get_text(), score_text.get_text_rect())
            screen.blit(timer_text.get_text(), timer_text.get_text_rect())

            if level == "EASY":
                circle.set_radius(50)

            elif level == "MEDIUM":
                circle.set_radius(30)

            elif level == "HARD":
                circle.set_radius(10)

            circle.draw_circle()

            if timer.is_finished():
                circle.delete()
                screen.fill(BLACK)
                score_text.get_text_rect().center = 350, 150
                score_text.draw(screen)
                selected_level_text.set_text("Level: " + level.title())
                selected_level_text.center_x(screen)
                selected_level_text.set_y(200)
                selected_level_text.draw(screen)
                exit_btn.set_y(300)

                if menu_btn.draw(screen):
                    append_game_data(score, level, ACTIVITY_DATA_FILE)
                    screen.fill(BLACK)
                    exit_btn.set_y(350)
                    start_game = False

                if exit_btn.draw(screen):
                    append_game_data(score, level, ACTIVITY_DATA_FILE)
                    pygame.quit()
                    sys.exit()
        run_game_events(mx, my)
        pygame.display.update()

        clock.tick(60)


if "__main__" == __name__:
    main()

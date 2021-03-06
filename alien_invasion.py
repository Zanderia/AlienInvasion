import pygame

import game_functions
from button import Button
from game_stats import GameStats
from question import Question
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    """Game initializing and window object creation"""
    ai_settings = Settings()

    pygame.init()
    # Set screen size and caption
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_caption)

    # Create button Play
    play_button = Button(ai_settings, screen, "Play")

    # Create instance for storing game stats
    stats = GameStats(ai_settings)

    # Create scoreboard instance
    sb = Scoreboard(ai_settings, screen, stats)

    # Create a ship
    ship = Ship(ai_settings, screen)

    q = Question(screen)

    # Create a group for bullets
    bullet_group = pygame.sprite.Group()
    # Create a group for aliens
    alien_group = pygame.sprite.Group()

    # Create a fleet of aliens
    game_functions.create_fleet(ai_settings, screen, ship, alien_group)
    # Start main cycle of the game
    while True:
        # Caption keyboard and mouse events
        game_functions.check_events(ai_settings, screen, stats, sb, play_button, ship, alien_group, bullet_group, q)
        if stats.game_active:
            ship.update()
            game_functions.update_bullet_group(ai_settings, screen, stats, sb, ship, alien_group, bullet_group)
            game_functions.update_alien_group(ai_settings, stats, sb, screen, ship, alien_group, bullet_group, q)

        # Screen redraws each time through the loop
        game_functions.update_screen(ai_settings, screen, stats, sb, ship, alien_group, bullet_group, play_button, q)


run_game()

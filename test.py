import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load and play the sound
pygame.mixer.music.load('C:/Users/alexe/OneDrive/Desktop/Desktop_assistant/shotgun.mp3')
pygame.mixer.music.play()

# Keep the program running while the sound plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
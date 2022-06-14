import os
import pygame
from Hanabi import hanabi

midi_music = hanabi()
music = midi_music.generator()
freq = 44100
bit_size = -16
channels = 2
buffer = 2048
pygame.mixer.init(freq, bit_size, channels,buffer)
clock = pygame.time.Clock()
pygame.mixer.music.load("{}.MID".format(music))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    clock.tick(30)
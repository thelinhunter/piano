import pygame
from test import test

midi_music = test()
music = midi_music.generator()
freq = 44100
bit_size = -16
channels = 2
buffer = 2048
pygame.mixer.init(freq, bit_size, channels,buffer)
clock = pygame.time.Clock()
pygame.mixer.music.load(music)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    clock.tick(30)
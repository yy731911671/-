import pygame
from pygame import image, Rect, Surface

TILE_POSITIONS = [
    ('#',0,0),
    (' ',0,1),
    ('.',3,0),
    ('@',2,0)
]

SIZE = 32

imagename='tiles.xpm'

def load_tiles():
    tiles = {}
    tile_img = pygame.image.load(imagename)
    for symbol,x,y in TILE_POSITIONS:
        rect = pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE)  #(left,top,width,height)
        tiles[symbol] = rect
    return tile_img,tiles

if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    m = Surface((32*4,32))   #width, height
    m.blit(tile_img.subsurface(tiles['#']),(0,0))
    m.blit(tile_img.subsurface(tiles[' ']),(32,0))
    m.blit(tile_img.subsurface(tiles['.']),(64,0))
    m.blit(tile_img.subsurface(tiles['@']),(96,0))
    image.save(m,'tile_combo.png')

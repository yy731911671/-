from pygame import image, Surface
from load_tiles import load_tiles, get_tile_rect, SIZE
from generate_maze import create_maze

def parse_grid(data):
    """Parses the string representation into a nested list"""
    return data.strip().split('\n')


def draw_grid(data, tile_img, tiles):
    """Returns an image of a title-based gird"""
    xs = len(data[0]) * SIZE
    ys = len(data) * SIZE
    img = Surface((xs, ys))
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            rect = get_tile_rect(x, y)
            img.blit(tile_img.subsurface(tiles[char]), rect)
    return img


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    level = create_maze(12, 7)
    level = parse_grid(level)
    maze = draw_grid(level, tile_img, tiles)
    image.save(maze, 'maze.png')

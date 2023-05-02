from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flood Fill")

def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j*PIXEL_SIZE, i*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    
    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            pygame.draw.line(win, BLACK, (0, i*PIXEL_SIZE), (WIDTH, i*PIXEL_SIZE))

        for i in range(COLS+1):
            pygame.draw.line(win, BLACK, (i*PIXEL_SIZE, 0), (i*PIXEL_SIZE, HEIGHT-TOOLBAR_HEIGHT))
    
    pygame.draw.line(win, BLACK, (0, HEIGHT-TOOLBAR_HEIGHT), (WIDTH, HEIGHT-TOOLBAR_HEIGHT), 2)

def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()

def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, WHITE, "Erase"),
    Button(70, button_y, 50, 50, WHITE, "Clear"),
    Button(360, button_y, 50, 50, BLACK),
    Button(420, button_y, 50, 50, RED),
    Button(480, button_y, 50, 50, GREEN),
    Button(540, button_y, 50, 50, BLUE)
]

while(run):
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    if not button.text:
                        drawing_color = button.color
                    
                    elif button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK   
                    
                    elif button.text == "Erase":
                        drawing_color = WHITE

    draw(WIN, grid, buttons)

pygame.quit()
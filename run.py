import curses
from random import randint
import colorama
from colorama import Fore, Back, Style

colorama.init()

# constants

WINDOW_WIDTH = 60  # number of columns of window box
WINDOW_HEIGHT = 20  # number of rows of window box
"""
Number of blocks in window per line = WINDOW_WIDTH -2.
Block x index ranges from 1 to WINDOW_WIDTH -2.
Number of blocks in window per column = WINDOW_HEIGHT -2.
Block y index ranges from 1 to WINDOW_HEIGHT -2.
"""

# setup window
curses.initscr()
curses.start_color()
win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH, 0, 0)  # rows, columns
win.keypad(1)
curses.noecho()
# curses.curs_set(1)
win.border(0)
win.nodelay(1)  # -1


ESC = 27
key = curses.KEY_RIGHT


def init_values():
    init = curses.initscr()
    # snake and food
    global snake
    snake = [[4, 4], [4, 3], [4, 2]]
    global food
    food = (6, 6)

    win.addch(food[0], food[1], "#")
    # game logic
    global score
    score = 0

    global gameColor
    gameColor = "RED"

    global game_finished
    game_finished = None
    init.clear()
    curses.endwin()


init_values()

def start_game():
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)

    global score
    win.addstr(0, 2, "Score " + str(score) + " " + " \ \  USE ARROW KEYS")

    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)

    # win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    global key
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [
        curses.KEY_LEFT,
        curses.KEY_RIGHT,
        curses.KEY_UP,
        curses.KEY_DOWN,
        ESC,
    ]:
        key = prev_key

    # calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))  # append O(n)

    # check if we hit the border
    if y == 0:
        game_over()
    if y == WINDOW_HEIGHT - 1:
        game_over()
    if x == 0:
        game_over()
    if x == WINDOW_WIDTH - 1:
        game_over()

    # if snake runs over itself
    if snake[0] in snake[1:]:
        game_over()

    global food
    if snake[0] == food:
        # eat the food
        score += 1
        food = ()
        while food == ():
            food = (randint(1, WINDOW_HEIGHT - 2),
                    randint(1, WINDOW_WIDTH - 2))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], "#")
        win.bkgd(" ", curses.color_pair(1) | curses.A_BOLD)
    else:
        # move snake
        win.bkgd(" ", curses.color_pair(2) | curses.A_BOLD)
        last = snake.pop()
        win.addch(last[0], last[1], " ")

    win.addch(snake[0][0], snake[0][1], "*")


curses.endwin()


def reset_snake():
    snake.clear()


def game_over():
    curses.endwin()
    global game_finished
    game_finished = True

    # print("HELLO THIS IS THE GAME OVER")

    print()
    print(Back.RED + "################################")
    print("#                              #")
    print("#                              #")
    print("#      ******************      #")
    print("#      ******************      #")
    print("#      ****GAME OVER*****      #")
    print("#      ******************      #")
    print("#      ******************      #")
    print("#      ******************      #")
    print("#                              #")
    print("#                              #")
    print("################################")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(f"##### Final score = {score} #####")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

    i = 0
    while i < 2:
        answer = input("## DO YOU WISH TO PLAY AGAIN? YES OR NO? ## \n\n")
        print(" ")
        print(" ")
        if any(answer.lower() == f for f in ["yes", "y", "1", "ye"]):
            print("Yes :)")
            reset_snake()
            print(snake)
            # curses.endwin()
            init_values()
            break
        elif any(answer.lower() == f for f in ["no", "n", "0"]):
            print("**********GAME OVER**********!!!!!!")
            break
        else:
            i += 1
            if i < 2:
                print("Please enter yes or no")
            else:
                print("Nothing done")   


while key != ESC:
    if not game_finished:
        start_game()
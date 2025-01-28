import random

from texttable import Texttable


class Board:
    def __init__(self):
        self.__dimension = 0
        self.__number_of_apples = 0
        with open("../Controller/settings.txt", 'r') as file:
            line = file.readline()
            line = line.split(' ')
            self.__dimension = int(line[0])
            self.__number_of_apples = int(line[1])
        # making the board
        self.__board = []
        for i in range(self.__dimension):
            line = []
            for j in range(self.__dimension):
                line.append(' ')
            self.__board.append(line)
        # placing the snake and marking its positions
        snake_pos = self.__dimension // 2
        self.__board[snake_pos][snake_pos] = '*'
        self.__board[snake_pos + 1][snake_pos] = "+"
        self.__board[snake_pos + 2][snake_pos] = '+'

        for i in range(self.__number_of_apples):
            self.place_apple()

        self.__snake_pos = [[snake_pos, snake_pos], [snake_pos + 1, snake_pos], [snake_pos + 2, snake_pos]]

    def place_apple(self):
        while True:
            x = random.randint(0, self.__dimension - 1)
            y = random.randint(0, self.__dimension - 1)
            contor = True

            if self.__board[x][y] == 'a':
                contor = False

            if x > 0 and self.__board[x - 1][y] != ' ':
                contor = False

            if y > 0 and self.__board[x][y - 1] != ' ':
                contor = False

            if x < self.__dimension - 1 and self.__board[x + 1][y] != ' ':
                contor = False

            if y < self.__dimension - 1 and self.__board[x][y + 1] != ' ':
                contor = False

            if contor:
                self.__board[x][y] = 'a'
                break

    def place_snake(self, snake_pos, last):
        self.__board[last[0]][last[1]] = ' '
        self.__board[snake_pos[0][0]][snake_pos[0][1]] = '*'
        for i in range(1, len(snake_pos)):
            self.__board[snake_pos[i][0]][snake_pos[i][1]] = '+'

    def place_snake_with_apple(self, snake_pos):
        self.__board[snake_pos[0][0]][snake_pos[0][1]] = '*'
        for i in range(1, len(snake_pos)):
            self.__board[snake_pos[i][0]][snake_pos[i][1]] = '+'

    def __str__(self):
        t = Texttable()
        for i in range(self.__dimension):
            t.add_row(self.__board[i])

        return t.draw()

    @property
    def board(self):
        return self.__board

    @property
    def dimension(self):
        return self.__dimension

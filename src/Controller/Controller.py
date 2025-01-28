from src.Domain.Board import Board


class Controller:
    def __init__(self):
        self.__board = Board()
        self.__pos = [self.__board.dimension // 2, self.__board.dimension // 2]
        snake_pos = self.__board.dimension // 2
        self.__snake_pos = [[snake_pos, snake_pos], [snake_pos + 1, snake_pos], [snake_pos + 2, snake_pos]]
        self.__direction = "up"

    def check_game_over(self):
        if 0 <= self.__snake_pos[0][0] < self.__board.dimension:
            if 0 <= self.__snake_pos[0][1] < self.board.dimension:
                return True
        return False

    def update_board_apple_eatten(self, last_piece):
        self.__board.place_snake_with_apple(self.__snake_pos)
        self.__snake_pos.append(last_piece)
        self.__board.place_apple()

    def move_up(self):
        if self.__direction == "down":
            raise Exception("Cannot change direction by 180 degrees")
        else:
            self.__direction = "up"
            last_piece = self.__snake_pos[-1]
            for i in range(len(self.__snake_pos) - 1, 0, -1):
                self.__snake_pos[i] = self.__snake_pos[i - 1].copy()

            self.__snake_pos[0][0] = self.__snake_pos[0][0] - 1

            if self.__board.board[self.__snake_pos[0][0]][self.__snake_pos[0][1]] == 'a':
                self.update_board_apple_eatten(last_piece)

            else:
                self.__board.place_snake(self.__snake_pos, last_piece)

    def move_down(self):
        if self.__direction == "up":
            raise Exception("Cannot change direction by 180 degrees")
        else:
            self.__direction = "down"
            last_piece = self.__snake_pos[-1]
            for i in range(len(self.__snake_pos) - 1, 0, -1):
                self.__snake_pos[i] = self.__snake_pos[i - 1].copy()

            self.__snake_pos[0][0] = self.__snake_pos[0][0] + 1

            if self.__board.board[self.__snake_pos[0][0]][self.__snake_pos[0][1]] == 'a':
                self.update_board_apple_eatten(last_piece)

            else:
                self.__board.place_snake(self.__snake_pos, last_piece)

    def move_left(self):
        if self.__direction == "right":
            raise Exception("Cannot change direction by 180 degrees")
        else:
            self.__direction = "left"
            last_piece = self.__snake_pos[-1]
            for i in range(len(self.__snake_pos) - 1, 0, -1):
                self.__snake_pos[i] = self.__snake_pos[i - 1].copy()

            self.__snake_pos[0][1] = self.__snake_pos[0][1] - 1

            if self.__board.board[self.__snake_pos[0][0]][self.__snake_pos[0][1]] == 'a':
                self.update_board_apple_eatten(last_piece)

            else:
                self.__board.place_snake(self.__snake_pos, last_piece)

    def move_right(self):
        if self.__direction == "left":
            raise Exception("Cannot change direction by 180 degrees")
        else:
            self.__direction = "right"
            last_piece = self.__snake_pos[-1]
            for i in range(len(self.__snake_pos) - 1, 0, -1):
                self.__snake_pos[i] = self.__snake_pos[i - 1].copy()

            self.__snake_pos[0][1] = self.__snake_pos[0][1] + 1

            if self.__board.board[self.__snake_pos[0][0]][self.__snake_pos[0][1]] == 'a':
                self.update_board_apple_eatten(last_piece)

            else:
                self.__board.place_snake(self.__snake_pos, last_piece)

    @property
    def board(self):
        return self.__board

    @property
    def direction(self):
        return self.__direction

# c = Controller()
# print(c.board)
# c.move_up()
# print(c.board)
# c.move_left()
# print(c.board)
# c.move_down()
# print(c.board)

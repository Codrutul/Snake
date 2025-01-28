from src.Controller.Controller import Controller


class UI:
    def __init__(self):
        self.__controller = Controller()

    def start(self):
        while True:
            if not self.__controller.check_game_over():
                print("Game Over")
                break
            print(self.__controller.board)
            cmd = input(":")
            try:
                # functions fot the move command
                if "move" in cmd:
                    cmd = cmd.split(' ')
                    number = 0
                    if len(cmd) == 1:
                        number = 1
                    else:
                        number = int(cmd[1])
                    if self.__controller.direction == "up":
                        for i in range(number):
                            self.__controller.move_up()
                            if not self.__controller.check_game_over():
                                print("Game Over")
                                exit()
                    if self.__controller.direction == "down":
                        for i in range(number):
                            self.__controller.move_down()
                            if not self.__controller.check_game_over():
                                print("Game Over")
                                exit()
                    if self.__controller.direction == "left":
                        for i in range(number):
                            self.__controller.move_left()
                            if not self.__controller.check_game_over():
                                print("Game Over")
                                exit()
                    if self.__controller.direction == "right":
                        for i in range(number):
                            self.__controller.move_right()
                            if not self.__controller.check_game_over():
                                print("Game Over")
                                exit()

                elif cmd == 'up' and self.__controller.direction != 'up':
                    self.__controller.move_up()

                elif cmd == 'left' and self.__controller.direction != 'left':
                    self.__controller.move_left()

                elif cmd == 'right' and self.__controller.direction != 'right':
                    self.__controller.move_right()

                elif cmd == 'down' and self.__controller.direction != 'down':
                    self.__controller.move_down()
                else:
                    print("Command does not exist")
            except Exception as e:
                if not self.__controller.check_game_over():
                    print("Game Over")
                    exit()
                else:
                    print(e)


def main():
    ui = UI()
    ui.start()


main()

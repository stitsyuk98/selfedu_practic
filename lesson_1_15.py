#TODO: дописать возможность выбора соперника(компьютер\друг)
#TODO: допистаь засекать время игры
import random

FULL = '-'


class TicTakToe:
    """
    - игроку предлагается выбрать за кого он хочет сиграть (х\о)
    - перед каждым ходом неважно чьим выводиться состояние поле (изначально поле заполнено "-")
    - первый ход делает крестик
    - затем предлагается сделать ход игроку
    - после каждого ход проверяется состояние поле
    - после завершения игры выводится сообщение с объявлением победившего
    """
    def __init__(self):
        self.mas = [FULL]*(9)
        self.player = []
        self.comp = []
        self.first = True # Первым ходит игрок
        self.player_sim = 'x'
        self.computer_sim = 'o'
        self.win_combo = [(0,1,2),
                          (2,5,8),
                          (0,3,6),
                          (6,7,8),
                          (3,4,5),
                          (1,4,7),
                          (0,4,8),
                          (2,4,6)]

    def check_state(self):
        for j in self.win_combo:
            if self.mas[j[0]] == self.mas[j[1]] == self.mas[j[2]] != FULL:
                self.win = not self.first
                return False

        if self.mas.count(FULL) == 0:
            self.win = None
            return False

        return True

    # def check_state(self):
    #     ch_player = [True]*8
    #     ch_computer = [True]*8
    #
    #     for j in range(len(self.win_combo)):
    #         for i in self.win_combo[j]:
    #             if i not in self.player:
    #                 ch_player[j] = False
    #             if i not in self.comp:
    #                 ch_computer[j] = False
    #
    #     f_comp = any(ch_computer)
    #     f_player = any(ch_player)
    #
    #     if f_comp or f_player:
    #         self.win = not self.first
    #         return False
    #
    #     if self.mas.count(FULL) == 0:
    #         self.win = None
    #         return False
    #
    #     return True

    def go_player(self, sim):
        while True:
            try:
                x, y = input('Ведите пожалуйста координаты вашего хода:').split()
                x = int(x)
                y = int(y)
                if x<4 and x>0 and y<4 and y>0:
                    x -= 1
                    y -= 1
                    if self.go_(sim, x, y):
                        return
                    else:
                        print('Это поле уже занято!')
            except:
                print('Координаты введены не верно, проверьте пожалуйста: 0<х<4, 0<y<4')

    def go_copmputer(self, sim):
        while True:
            rng = random.Random()
            x = rng.randrange(3)
            y = rng.randrange(3)
            if self.go_(sim, x, y):
                return

    def go_(self, sim, x, y):
        try:
            if self.mas[x * 3 + y] == FULL:
                self.comp.append(x * 3 + y)
                self.mas[x * 3 + y] = sim
            return True
        except:
            return False

    def show(self):
        """
        выводит текущее состояние игры
        :return:
        """
        for i in range(3):
            for j in range(3):
                print(self.mas[i*3+j], end=' ')
            print('')

    def game(self):
        while self.check_state():
            self.show()

            # ход
            if self.first:
                self.go_player(self.player_sim)
            else:
                print('Ход соперника:')
                self.go_copmputer(self.computer_sim)

            self.first = not self.first

        self.show()
        if self.win is not None:
            if (self.win and self.player_sim == 'x') or (not self.win and self.player_sim == 'o'):
                print('Поздравляем! Вы выиграли!')
            else:
                print('Сожалею, вы проиграли, попробуйте еще раз!')
        else:
            print('Жаль, закончились клетки для хода!')

    def choose(self):
        answer = input('Пожалуйста выбирете за кого вы будете играть? (х\о)')
        if answer == 'o':
            self.player_sim = 'o'
            self.computer_sim = 'x'
            self.first = False

    def play(self):
        self.choose()

        print('Игра началась!')

        self.game()

        print("Игра закончилась!")



if __name__ == '__main__':
    tic = TicTakToe()
    tic.play()


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
        self.win_combo = [(0,1,2),
                          (2,5,8),
                          (0,3,6),
                          (6,7,8),
                          (3,4,5),
                          (1,4,7),
                          (0,4,8),
                          (2,4,6)]

    def check_state(self):
        ch_player = [True]*8
        ch_computer = [True]*8

        for j in range(len(self.win_combo)):
            for i in self.win_combo[j]:
                if i not in self.player:
                    ch_player[j] = False
                if i not in self.comp:
                    ch_computer[j] = False

        f_comp = any(ch_computer)
        f_player = any(ch_player)

        if f_comp or f_player:
            self.win = not self.first
            return False

        if self.mas.count(FULL) == 0:
            self.win = None
            return False

        return True

    def go_player(self, sim):
        while True:
            try:
                x, y = input('Ведите пожалуйста координаты вашего хода:').split()
                x = int(x)
                y = int(y)
                if x<4 and x>0 and y<4 and y>0:
                    x -= 1
                    y -= 1
                    self.player.append(x*3+y)
                    self.mas[x*3+y] = sim
                    return
            except:
                print('Координаты введены не верно, проверьте пожалуйста: 0<х<4, 0<y<4')

    def go_copmputer(self, sim):
        print('Ход соперника:')
        while True:
            rng = random.Random()
            x = rng.randrange(3)
            y = rng.randrange(3)
            if self.mas[x * 3 + y] == FULL:
                self.comp.append(x * 3 + y)
                self.mas[x * 3 + y] = sim
                return

    def show(self):
        """
        выводит текущее состояние игры
        :return:
        """
        for i in range(3):
            for j in range(3):
                print(self.mas[i*3+j], end=' ')
            print('')

    def game(self, player='x'):
        computer = 'o'
        if player == 'o':
            computer = 'x'
            self.first = False

        while self.check_state():
            self.show()

            # ход
            if self.first:
                self.go_player(player)
            else:
                self.go_copmputer(computer)

            self.first = not self.first

        self.show()
        if self.win is not None:
            if (self.win and player == 'x') or (not self.win and player == 'o'):
                print('Поздравляем! Вы выиграли!')
            else:
                print('Сожалею, вы проиграли, попробуйте еще раз!')
        else:
            print('Жаль, закончились клетки для хода!')


    def play(self):
        answer = input('Пожалуйста выбирете за кого вы будете играть? (х\о)')
        if answer == 'o':
            self.first = False

        print('Игра началась!')

        self.game(answer)

        print("Игра закончилась!")



if __name__ == '__main__':
    tic = TicTakToe()
    tic.play()


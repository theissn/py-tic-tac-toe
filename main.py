class Board():
    
    def __init__(self):
        self.list = {}
        self.board = []
        self.turn = 'x'

        self.win_combs = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

        self.create()
        
    def create(self):
        num = 0;
        for i in range(3):
            line = []
            for x in range(3):
                line.append(num)
                self.list[num] = False
                num += 1
            
            self.board.append(line)

    def show(self):
        for line in self.board:
            for item in line:
                if self.list[item] is False:
                    print(f"{item} ", end="")
                else:
                    print(f"{self.list[item]} ", end="")
            print("")
        print("")

    def move(self, num):
        if self.list[num] == False:
            self.list[num] = self.turn

    def who(self):
        if self.turn is 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'

        return self.turn;


    def won(self, move):
        for combs in self.win_combs:
            all = False
            num = 0
            for num in combs:
                if self.list[num] == move:
                    all = True
                    num += 1
                else:
                    all = False
            if num is 3:
                return True
        if all == True:
            return True

board = Board()

while True:
    board.show()

    move = board.who()

    user_action = input(f"Make your move ({move}):  (x to exit): ")

    if (user_action.lower() is 'x'):
        playing = False
    else:
        board.move(int(user_action))
        if board.won(move) is True:
            print(f"{move} won!!")
            break











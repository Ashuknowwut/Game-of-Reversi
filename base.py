# qingyang peng  13548257

    
def _rows() -> int:
    'get rows'
    
    while True:
        try:

            N = int(input())

            if 16 >= int(N) >= 4 and int(N)%2 == 0:
                return N

        except:

            print('INVALID')


def _columns() -> int:
    'get columns'
    
    while True:
        try:

            N = int(input())

            if 16 >= int(N) >= 4 and int(N)%2 == 0:
                return N

        except:

            print('INVALID')


def _first() -> str:
    'get who moves first'

    while True:
        try:

            I = str(input())

            if I == 'B' or I == 'W':
                return I

        except:

            print('INVALID')


def _topleft() -> str:
    'get the color of topleft'
    
    while True:
        try:

            I = str(input())

            if I == 'B' or I == 'W':
                return I

        except:

            print('INVALID')


def _win() -> str:
    'get how to count winner'

    while True:
        try:

            I = str(input())

            if I == '>' or I == '<':
                return I
            
        except:

            print('INVALID')

class othello:

    def __init__(self, board, turn, rows, columns):

        self.board = board

        self.turn = turn

        self.rows = int(rows)

        self.columns = int(columns)
        

    def _count(self) -> list:
        'count the chess num'
        
        self.count_b = 0
        self.count_w = 0
        
        for i in self.board:
            
            for s in i:
                
                if s == 'B':
                    self.count_b += 1
                    
                elif s == 'W':
                    self.count_w += 1
            
        return [self.count_b, self.count_w]
        

    def _choise(self, rows: int, columns: int) -> str:
        'check balid for input'
        b = self.board
        
        while True:
            
            try:

                M = str(input()).strip()
                r = int(M.split()[0])
                c = int(M.split()[1])
                
                if 0 < r <= rows and 0 < c <= columns:
                    
                    if b[r-1][c-1] == '':

                        if type(self._check(r,c)) == list:
                            print('VALID')
                            
                            return M

                        else:
                            print('INVALID')
                    else:
                        print('INVALID')
                else:
                    print('INVALID')

            except:

                print('INVALID')
                

    def _check(self, row: int, column: int) -> list:
        'check valid in board'
        b = self.board
        t = self._color()
        test = []
        row = row - 1
        column = column - 1
        result = []
        
        if b[row][column] == '':
        
            for i in range(-1,2):
                for c in range(-1,2):

                    if 0 <= row+i < len(b) and 0 <= column+c < len(b[0]):

                        test.append([row+i, column+c, i, c])
                                    
            for i in test:
                                    
                if b[i[0]][i[1]] == t:
                                    
                    if self.further_check(i[0],i[1],i[2],i[3]) == True:

                        result.append([i[0], i[1], i[2], i[3]])

            if result == []:

                return False
                        
            return result
            
        return False


    def further_check(self, row: int, column: int, i: int, c: int) -> bool:
        b = self.board
        t = self._color()
        T = self.turn
 
        if 0 <= row+i < len(b) and 0 <= column+c < len(b[0]):

            if b[row+i][column+c] == t:           
                if self.further_check(row+i,column+c,i,c) == True:
                    return True

            elif b[row+i][column+c] == T:
                return True
                
            elif b[row+i][column+c] == '':
                return False

                
    def _board(self, top: str, rows: int, columns: int):
        'form the initial game board'
        Board = []

        for i in range(rows):
            Board.append([])
            
            for c in range(columns):
                Board[-1].append('')
                
        if top == 'B':
            Board[int(rows/2)][int(columns/2)] = 'B'
            Board[int((rows/2)-1)][int((columns/2)-1)] = 'B'
            Board[int((rows/2)-1)][int(columns/2)] = 'W'
            Board[int(rows/2)][int((columns/2)-1)] = 'W'

        else:
            Board[int(rows/2)][int(columns/2)] = 'W'
            Board[int((rows/2)-1)][int((columns/2)-1)] = 'W'
            Board[int((rows/2)-1)][int(columns/2)] = 'B'
            Board[int(rows/2)][int((columns/2)-1)] = 'B'

        return Board

    def _color(self):
        'return the opposite color'

        if self.turn == 'B':

            return 'W'

        else:

            return 'B'
                                    

    def _turn(self):
        'switch the turn'

        if self.turn == 'black':
            
            self.turn = 'W'

        else:

            self.turn = 'B'
                                    

    def show_board(self, rows: int, columns: int):
        'display the game board'

        b = self.board
        
        display = []

        for i in range(rows):
            display.append([])

        for r in range(rows):
            for c in range(columns):
                
                if b[r][c] == '':
                    display[r].append('. ')
                elif b[r][c] == 'B':
                    display[r].append('B ')
                else:
                    display[r].append('W ')

        for r in display:

            for c in r:

                print(c, end='')

            print(end='\n')
        

    def _move(self, row: int, column: int):
        'drop chess on game board'
        b = self.board
        t = self._color()
        T = self.turn
        M = [] 
        check = self._check(row, column)

        row = row - 1
        column = column - 1

        self.board[row][column] = self.turn

        if type(check) == list:
        
            for i in check:       
                if b[row+i[2]][column+i[3]] == t:
                    self.board[row+i[2]][column+i[3]] = T

                    M.append((row+i[2],column+i[3]))
                    
                    self.further_move(row+i[2],column+i[3],i[2],i[3], M)

                    M.extend(self.further_move(row+i[2],column+i[3],i[2],i[3], M))

            return M


    def further_move(self, row: int, column: int, i: int, c: int, m: list):
        'switch the color of chesses'
        b = self.board
        t = self._color()
        T = self.turn

        if 0 <= row + i < len(b) and 0 <= column + c< len(b[0]):
            
            if b[row+i][column+c] == t:
                
                self.board[row+i][column+c] = T
                m.append((row+i, column+c))
                self.further_move(row+i,column+c,i,c, m)

            return m


    def _winner(self, rule: str, rows: int, columns: int) -> str:
        'check winner if someone wins'

        if self._find(rows, columns) == True:

            return 'Continue'

        else:
                
            if rule == '>':
                if self._count()[0] > self._count()[1]:
                    return 'B'

                if self._count()[0] < self._count()[1]:
                    return 'W'

                else:
                    return 'NONE'

            
                if self._count()[0] > self._count()[1]:
                    return 'W'

                if self._count()[0] < self._count()[1]:
                    return 'B'

                else:
                    return 'NONE'


    def _find(self, rows: int, columns: int):
        'find position if there exists on that available'

        for i in range(rows):
            for c in range(columns):

                if type(self._check(i+1, c+1)) == list:

                    return True

        return False


def user_interface():
    
    print('FULL')

    board = list()
    rows = _rows()
    columns = _columns()
    first_turn = _first()
    top = _topleft()
    rule = _win()
 
    Othello = othello(board, first_turn, rows, columns)
    
    Othello.board = Othello._board(top, rows, columns)


    print('B: {}  W: {}'.format(Othello._count()[0], Othello._count()[1]))
    

    Othello.show_board(rows, columns)

    print('Turn: ', Othello.turn)


    while True:

        choise = Othello._choise(rows, columns).split()
        
        Othello._move(int(choise[0]), int(choise[1]))

        print('B: {}  W: {}'.format(Othello._count()[0], Othello._count()[1]))

        Othello.show_board(rows, columns)
        
        Othello._turn()

        if Othello._winner(rule, rows, columns) != 'Continue':
        
            print('WINNER: ',Othello._winner(rule, rows, columns))

            break

        print('Turn: ', Othello.turn)

            


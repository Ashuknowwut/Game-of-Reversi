# Qingyang Peng  13548257

import tkinter
import base


DEFAULT_FONT = ('Calibri', 20)

info = []

class othello:

    def __init__(self):
        
        self._start_window = tkinter.Tk()

        self._start_window.configure(background='#afeeee')

        info_label = tkinter.Label(
            master = self._start_window, text = 'Creating your game!',
            font = DEFAULT_FONT, background='#afeeee')

        info_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        

        rows_info_label = tkinter.Label(
            master = self._start_window, text = 'Rows (4-16)',
            font = DEFAULT_FONT,background='#afeeee')

        rows_info_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._rows_entry = tkinter.Entry(
            master = self._start_window, width = 5, font = DEFAULT_FONT)

        self._rows_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        

        columns_info_label = tkinter.Label(
            master = self._start_window, text = 'Columns (4-16)',
            font = DEFAULT_FONT,background='#afeeee')

        columns_info_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._columns_entry = tkinter.Entry(
            master = self._start_window, width = 5, font = DEFAULT_FONT)

        self._columns_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        Var1 = tkinter.StringVar()
        
        first_info_label = tkinter.Label(
            master = self._start_window, text = 'First move',
            font = DEFAULT_FONT,background='#afeeee')

        first_info_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self.color1_button = tkinter.Radiobutton(
            master = self._start_window, text = 'Black', font = DEFAULT_FONT,
            variable = Var1, value = 'black',background='#afeeee', command = self.get_first1)

        self.color1_button.grid(row = 3, column = 1, padx = 10, pady = 10)
            
        color2_button = tkinter.Radiobutton(
            master = self._start_window, text = 'White', font = DEFAULT_FONT,
            variable = Var1, value = 'white',background='#afeeee', command = self.get_first2)
        color2_button.grid(row = 3, column = 2, padx = 10, pady = 10)

        Var2 = tkinter.StringVar()
        
        top_left_label = tkinter.Label(
            master = self._start_window, text = 'Top Left',
            font = DEFAULT_FONT,background='#afeeee')

        top_left_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        color3_button = tkinter.Radiobutton(
            master = self._start_window, text = 'Black', font = DEFAULT_FONT,
            variable = Var2, value = 'black', background='#afeeee',command = self.get_top1)

        color3_button.grid(row = 4, column = 1, padx = 10, pady = 10)
            
        color4_button = tkinter.Radiobutton(
            master = self._start_window, text = 'White', font = DEFAULT_FONT,
            variable = Var2, value = 'white',background='#afeeee', command = self.get_top2)

        color4_button.grid(row = 4, column = 2, padx = 10, pady = 10)
       

        Var3 = tkinter.StringVar()
        
        win_rule_label = tkinter.Label(
            master = self._start_window, text = 'Win Rule',
            font = DEFAULT_FONT,background='#afeeee')

        win_rule_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        rule1_button = tkinter.Radiobutton(
            master = self._start_window, text = '>', font = DEFAULT_FONT,
            variable = Var3, value = '>',background='#afeeee', command = self.get_rule1)

        rule1_button.grid(row = 5, column = 1, padx = 10, pady = 10)
            
        rule2_button = tkinter.Radiobutton(
            master = self._start_window, text = '<', font = DEFAULT_FONT,
            variable = Var3, value = '<',background='#afeeee', command = self.get_rule2)

        rule2_button.grid(row = 5, column = 2, padx = 10, pady = 10)
        
        

        button_frame = tkinter.Frame(master = self._start_window)

        button_frame.grid(
            row = 6, column = 1, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        
        button_frame.configure(background='#afeeee')

        begin_button = tkinter.Button(
            master = button_frame, text = 'Begin!', font = DEFAULT_FONT,
            command = self._begin)

        begin_button.grid(row = 6, column = 0, padx = 10, pady = 10)

        exit_button = tkinter.Button(
            master = button_frame, text = 'Exit', font = DEFAULT_FONT,
            command = self._exit)
        
        exit_button.grid(row = 6, column = 1, padx = 10, pady = 10)


        self._start_window.rowconfigure(3, weight = 1)
        self._start_window.columnconfigure(1, weight = 1)

        self._begin_clicked = False
        self._rows = ''
        self._columns = ''
        self._first = ''
        self._top = ''
        self._rule = ''
        
    'take value from radiobutton'
    def get_first1(self):
        self._first = True

    def get_top1(self):
        self._top = True

    def get_rule1(self):
        self._rule = True

    def get_first2(self):
        self._first = False

    def get_top2(self):
        self._top = False

    def get_rule2(self):
        self._rule = False

    def play(self) -> None:

        self._start_window.grab_set()
        self._start_window.wait_window()

    def _exit(self):
        'exit the window'

        self._start_window.destroy()
        
    def _begin(self):
        'when clicked the begin button'
        try:

            self._rows = int(self._rows_entry.get())
            self._columns = int(self._columns_entry.get())

            if self._rows != '' and self._columns != '' and self._first != '' and self._top != '' and self._rule != '':
                    
                if int(self._rows) % 2 == 0 and 4<= int(self._rows) <= 16:

                    if 4 <= int(self._columns) <= 16 and int(self._columns) % 2 == 0:

                        if self._first:
                            self._first = 'B'
                        else:
                            self._first = 'W'

                        if self._top:
                            self._top = 'B'
                        else:
                            self._top = 'W'

                        if self._rule:
                            self._rule = '>'
                        else:
                            self._rule = '<'

                        game_state().display()
        except:

            error()._pop()
            

    def start(self):

        self._start_window.mainloop()


class error:

    def __init__(self):
        
        self._error_window = tkinter.Toplevel()

        self._error_window.configure(background='#afeeee')
        
        message_label = tkinter.Label(
            master = self._error_window, text = 'INVALID!',
            font = DEFAULT_FONT, background='#afeeee')
        message_label.grid(
            row = 0, column = 0, columnspan = 1, padx = 15, pady = 15,
            sticky = tkinter.W)

        button_frame = tkinter.Frame(master = self._error_window)
        button_frame.grid(
            row = 2, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        
        button_frame.configure(background='#afeeee')

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._ok)

        ok_button.grid(row = 10, column = 0, padx = 10, pady = 10)



    def _ok(self):

        self._error_window.destroy()
        
        
    def _pop(self):

        self._error_window.mainloop()


class game_state:

    def __init__(self):

        self._chess_window = tkinter.Toplevel()

        self._chess_window.configure(background='#eee8aa')

        self.rows = ''
        self.columns = ''
        self.top_r = ''
        self.top_l = ''
        self.rings1 = []
        self.rings2 = []
        self.turn = ''
        self.circle = ''
        self.black = 2
        self.white = 2
        
        self.winner_label = tkinter.Label(master = self._chess_window)
        self.over_label = tkinter.Label(master = self._chess_window)
        self._size()
        self._turn()
        
        self._canvas = tkinter.Canvas(
                            master = self._chess_window,
                            width = self.rows,
                            height = self.columns,
                            background = '#EEDD82')          
        
        self._canvas.grid(
            row = 0, column = 0, padx = 30, pady = 30,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self.turn_label = tkinter.Label(
                master = self._chess_window, text = 'Turn: '+self.turn,
                font = DEFAULT_FONT, background='#eee8aa')

        self.turn_label.grid(
                row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.W)
        
        self.count_label = tkinter.Label(
                master = self._chess_window, text = 'black: {} white: {}'.format(self.black, self.white),
                font = DEFAULT_FONT, background='#eee8aa')

        self.count_label.grid(
                row = 4, column = 0, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.W)


        button_frame = tkinter.Frame(master = self._chess_window)
        
        button_frame.configure(background='#eee8aa')
        
        button_frame.grid(
            row = 5, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        new_button = tkinter.Button(
            master = button_frame, text = 'New Game', font = DEFAULT_FONT,
            command = self._new)

        new_button.grid(row = 5, column = 0, padx = 10, pady = 10)


        self._canvas.bind('<Configure>', self._resize)
        self._canvas.bind('<Button-1>', self.move)
        self._canvas.bind('<Motion>', self._entered)

        self._chess_window.rowconfigure(0, weight = 1)
        self._chess_window.columnconfigure(0, weight = 1)

        self.drop_row = ''

        self.drop_column = ''
        self.board = []

        self.Othello_in = base.othello(self.board, Othello._first, Othello._rows, Othello._columns)
        self.Othello_in.board = self.Othello_in._board(Othello._top, Othello._rows, Othello._columns)
        
    def _turn(self):
        'change turn to the whole color name'

        if Othello._first == 'B':
            self.turn = 'black'

        else:
            self.turn = 'white'

    def _size(self):
        'design the size of canvas as different rows and columns'
        
        if Othello._rows > 4 or Othello._columns > 4:

            self.rows = 50*Othello._rows
            self.columns = 50*Othello._columns
    
        else:
            
            self.rows = 300
            self.columns = 300

    def chess_board(self):
        'form the initial game board'


        self.rings1.append((self.columns/2-(self.columns/(Othello._columns*20))*19,
                                 self.rows/2-(self.rows/(Othello._rows*20))*19,
                                 self.columns/2-(self.columns/(Othello._columns*20)),
                                 self.rows/2-(self.rows/(Othello._rows*20))))
        
        self.rings2.append((self.columns/2-(self.columns/(Othello._columns*20))*19,
                                 self.rows/2+(self.rows/(Othello._rows*20)),
                                 self.columns/2-(self.columns/(Othello._columns*20)),
                                 self.rows/2+(self.rows/(Othello._rows*20))*19))

        self.rings2.append((self.columns/2+(self.columns/(Othello._columns*20)),
                                 self.rows/2-(self.rows/(Othello._rows*20))*19,
                                 self.columns/2+(self.columns/(Othello._columns*20))*19,
                                 self.rows/2-(self.rows/(Othello._rows*20))))

        self.rings1.append((self.columns/2+(self.columns/(Othello._columns*20)),
                                 self.rows/2+(self.rows/(Othello._rows*20)),
                                 self.columns/2+(self.columns/(Othello._columns*20))*19,
                                 self.rows/2+(self.rows/(Othello._rows*20))*19))

    

    def top_left(self):
        'change the str in order to use in color fill'
        
        if Othello._top == 'B':
            self.top_l = 'black'
            self.top_r = 'white'
        else:
            self.top_l = 'white'
            self.top_r = 'black'

    def change(self):
        'change the str in order to use in color fill'

        if self.Othello_in.turn == 'B':

            self.Othello_in.turn = 'black'

        else:

            self.Othello_in.turn = 'white'
        

    def display(self):

        self.chess_board()
        self._chess_window.mainloop()


    def _resize(self, event: tkinter.Event):
        'resize the canvas when the window size be changed'

        self._canvas.delete(tkinter.ALL)

        self.top_left()

        self._flash()

    def _flash(self):
        'flash the window'

        self._canvas.delete(tkinter.ALL)
        self.top_left()

        for i in self.rings1:

            self._draw(i[0],i[1],i[2],i[3], self.top_l)

        for i in self.rings2:

            self._draw(i[0],i[1],i[2],i[3], self.top_r)
        

    def _draw(self, x1: float, y1: float, x2: float, y2: float, color: str):
        'draw chesses on the game board'

        width = (self._canvas.winfo_width()-6)/self.columns
        height = (self._canvas.winfo_height()-6)/self.rows

        for i in range(Othello._rows+1):
            
            self._canvas.create_line(0, i*(self.rows/Othello._rows)*height,
                                     self.columns*width, i*(self.rows/Othello._rows)*height,
                                     fill = 'black')

        for i in range(Othello._columns+1):
            self._canvas.create_line(i*(self.columns/Othello._columns)*width, 0,
                                     i*(self.columns/Othello._columns)*width, self.rows*height,
                                     fill = 'black')           

        self._canvas.create_oval(
            width * x1, height * y1,
            width * x2, height * y2,
            fill = color)

    
    def drop(self, row: int, column: int):
        'change the turn and chess count infomation and order to draw'
        
        M = []
        m = self.Othello_in._move(row, column)
        self.change()
        
        m.append((row-1, column-1))

        for i in m:
            if i not in M:
                M.append(i)
            
        if self.Othello_in.turn == self.top_l:

            for i in M:
        
                circle = (self.columns/Othello._columns*(i[1]+1)-self.columns/Othello._columns*19/20,
                          self.rows/Othello._rows*(i[0]+1)-self.rows/Othello._rows*19/20,
                          self.columns/Othello._columns*(i[1]+1)-self.columns/Othello._columns/20,
                          self.rows/Othello._rows*(i[0]+1)-self.rows/Othello._rows/20)
                self.rings1.append(circle)
                if circle in self.rings2:
                    self.rings2.remove(circle)
        else:

            for i in M:

                circle = (self.columns/Othello._columns*(i[1]+1)-self.columns/Othello._columns*19/20,
                          self.rows/Othello._rows*(i[0]+1)-self.rows/Othello._rows*19/20,
                          self.columns/Othello._columns*(i[1]+1)-self.columns/Othello._columns/20,
                          self.rows/Othello._rows*(i[0]+1)-self.rows/Othello._rows/20)
                self.rings2.append(circle)
                if circle in self.rings1:
                    self.rings1.remove(circle)

        self._flash()
       
        self.Othello_in._turn()

        if self.Othello_in.turn == 'B':
        
            self.turn = 'black'
        else:
            self.turn = 'white'

        self.black = self.Othello_in._count()[0]
        self.white = self.Othello_in._count()[1]

        self.count_label.grid_forget()

        self.count_label = tkinter.Label(
                master = self._chess_window, text = 'black: {}  white: {}'.format(self.black, self.white),
                font = DEFAULT_FONT, background='#eee8aa')

        self.count_label.grid(
                row = 4, column = 0, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.W)
        
     
    def move(self, event: tkinter.Event):
        'check valid if cliked on the canvas'
        
        Width = self._canvas.winfo_width()
        Height = self._canvas.winfo_height()

        width_co = Width/Othello._rows
        height_co = Height/Othello._columns

        self.drop_column = int(event.x // width_co)+1
        self.drop_row = int(event.y // height_co)+1

        if 0<self.drop_column<=Othello._columns and 0<self.drop_row<=Othello._rows:

            if type(self.Othello_in._check(self.drop_row, self.drop_column)) == list:

                self.drop(self.drop_row, self.drop_column)

                self.turn_label.grid_forget()

                self.turn_label = tkinter.Label(
                    master = self._chess_window, text = 'Turn: '+self.turn,
                    font = DEFAULT_FONT, background='#eee8aa')

                self.turn_label.grid(
                    row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
                    sticky = tkinter.W)

                if self.Othello_in._winner(Othello._rule, Othello._rows, Othello._columns) != 'Continue':

                    self.game_over()
        

    def _new(self):
        'create a new game'

        self.rings1 = []
        self.rings2 = []

        self.chess_board()
        self._turn()

        self.turn_label.grid_forget()
        
        self.turn_label = tkinter.Label(
                master = self._chess_window, text = 'Turn: '+self.turn,
                font = DEFAULT_FONT, background='#eee8aa')

        self.turn_label.grid(
                row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.W)
        
        self.black = 2
        self.white = 2

        self.count_label.grid_forget()

        self.count_label = tkinter.Label(
                master = self._chess_window, text = 'black: {}  white: {}'.format(self.black, self.white),
                font = DEFAULT_FONT, background='#eee8aa')

        self.count_label.grid(
                row = 4, column = 0, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.W)
        
        self.winner_label.grid_forget()
        self.over_label.grid_forget()
        
        self._flash()

        self.board = []
        self.Othello_in = base.othello(self.board, Othello._first, Othello._rows, Othello._columns)
        self.Othello_in.board = self.Othello_in._board(Othello._top, Othello._rows, Othello._columns)
                                           

    def _entered(self, event: tkinter.Event):
        'show available or not if entered particular position'

        self._canvas.delete(self.circle)
        
        Width = self._canvas.winfo_width()
        Height = self._canvas.winfo_height()

        radio_w = (self._canvas.winfo_width()-6)/self.columns
        radio_h = (self._canvas.winfo_height()-6)/self.rows

        width_co = Width/Othello._rows
        height_co = Height/Othello._columns

        x = int(event.x // width_co)+1
        y = int(event.y // height_co)+1

        if 0<x<=Othello._columns and 0<y<=Othello._rows:

            if type(self.Othello_in._check(y, x)) == list:
                
                self.circle = self._canvas.create_oval((self.columns/Othello._columns*x-self.columns/Othello._columns*19/20)*radio_w,
                          (self.rows/Othello._rows*y-self.rows/Othello._rows*19/20)*radio_h,
                          (self.columns/Othello._columns*x-self.columns/Othello._columns/20)*radio_w,
                          (self.rows/Othello._rows*y-self.rows/Othello._rows/20)*radio_h, outline = '#696969')
                       
    def game_over(self):
        'show game result'
        
        winner = ''
        win = self.Othello_in._winner(Othello._rule, Othello._rows, Othello._columns)
        
        if win == 'W':
            winner = 'white'

        elif win == 'B':
            winner = 'black'

        else:
            winner = 'None'
            
        self.over_label = tkinter.Label(
            master = self._chess_window, text = 'Gameover!',
            font = ('Calibri', 30), background='#eee8aa')

        self.over_label.grid(
            row = 0, column = 1, columnspan = 1, padx = 20, pady = 20,
            sticky = tkinter.W)
        
        self.turn_label.grid_forget()
        
        self.winner_label = tkinter.Label(
                master = self._chess_window, text = 'Winner: '+winner,
                font = ('Calibri', 30), background='#eee8aa')

        self.winner_label.grid(
                row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
                sticky = tkinter.W)
            

if __name__ == '__main__':
    Othello = othello()
    Othello.start()






        
        

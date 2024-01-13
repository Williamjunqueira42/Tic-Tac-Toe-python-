from tkinter import *
from time import sleep


class Game:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic Tac Toe')
        self.master.geometry('600x600')

        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 0   # if you turn it to pair and the turn fo x

        #canvas
        self.canvas = Canvas(self.master, bg='#242423')
        self.canvas.pack(expand='true', fill='both')

        self.create_board()


        self.canvas.bind('<Button-1>', self.key)
        self.canvas.bind_all('<r>', self.reset)

    def create_board(self):
        self.canvas.create_line(190, 590, 190, 10, fill='white', width=15)
        self.canvas.create_line(390, 590, 390, 10, fill='white', width=15)

        self.canvas.create_line(600, 200, 10, 200, fill='white', width=15)
        self.canvas.create_line(600, 400, 10, 400, fill='white', width=15)


    def draw_figfure(self, posx, posy):
        if self.board[posx][posy] != 0:
             pass
        else:


            if self.turn % 2 == 0:
                self.turn += 1
                self.board[posx][posy] = 1
                self.create_x(posx, posy)
            else:
                self.turn += 1

                self.board[posx][posy] = 2
                self.create_O(posx, posy)



    def create_x(self, posx, posy):

        ax = 200*posx
        ay = 200*posy


        self.canvas.create_line(60+ax, 60+ay, 140+ax,  140+ay, fill='white', width=25)
        self.canvas.create_line(60+ax, 140+ay, 140+ax,  60+ay, fill='white', width=25)

        self.verify_victory()

    def create_O(self, posx, posy):

        ax = 200*posx
        ay = 200*posy

        self.canvas.create_text(100+ax, 100+ay, text='O', fill='white', font=('Helvetica 100 bold'))


        self.verify_victory()


    def verify_victory(self):
        print('-------')


        for k in range(3):
            print(self.board[k][0], self.board[k][1], self.board[k][2])
            if self.board[k][0] == self.board[k][1] == self.board[k][2] and self.board[k][0] !=0:
                    self.victory_line('v', k)

            elif self.board[0][k] == self.board[1][k] == self.board[2][k] and self.board[0][k] !=0:
                    self.victory_line('h', k)


        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
                self.victory_line('x', 1)

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
                self.victory_line('x', 2)


    def victory_line(self, d, k=None):
        if d == 'h':

            self.canvas.create_line(0, 100+200*k, 600, 100+200*k, fill='light blue', width=10)
        elif d == 'v':

            self.canvas.create_line(100+200*k, 0, 100+200*k, 600, fill='light blue', width=10)

        elif d == 'x':
            if k == 1:

                self.canvas.create_line(0, 0, 600, 600, fill='light blue', width=10)
            elif k == 2:

                self.canvas.create_line(600, 0, 0,  600, fill='light blue', width=10)



        

    def key(self, event):
        x, y = event.x, event.y
        posx, posy = 0, 0

        if x <= 200:
            posx = 0
        elif x <= 400:
            posx = 1
        elif x <= 600:
            posx=2

        if y <= 200:
            posy = 0
        elif y <= 400:
            posy = 1
        elif y <= 600:
            posy= 2

        self.draw_figfure(posx, posy)

    def reset(self, event=None):
        self.canvas.delete('all')
        self.create_board()
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



if __name__ == '__main__':
    root = Tk()
    Game(root)
    root.mainloop()

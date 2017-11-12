import Tkinter as tk
from gameoflife.data.StateReader import from_file
from gameoflife.Game import next_generation

class Player(object):

    CELL_WIDTH = 25
    CELL_COLOR_ALIVE = '#ffffff'
    CELL_COLOR_DEAD = '#000000'
    BACKGROUND = '#888888'
    TITLE = "Game Of Life"
    DELAY = 1500

    def __init__(self, initialState):
        self.state = initialState
        self.frame = None
        self.canvas = None
        self.pause = True

    def start(self):
        root = tk.Tk()
        self.frame = tk.Frame(root)
        (rows, columns) = self.state.get_dimensions()
        self.canvas = tk.Canvas(self.frame, width=columns*self.CELL_WIDTH,
                                height=rows*self.CELL_WIDTH, bg=self.BACKGROUND)
        self.frame.pack()
        self.canvas.pack()
        root.title(self.TITLE)
        self.draw_state()
        self.canvas.bind("<Button-1>", self.mouse_clicked)
        self.frame.after(self.DELAY, self.next_step)
        root.mainloop()

    def mouse_clicked(self, _):
        self.pause = not self.pause

    def draw_state(self):
        (rows, columns) = self.state.get_dimensions()
        for row in xrange(0, rows):
            for column in xrange(0, columns):
                x_coord = column * self.CELL_WIDTH
                y_coord = row * self.CELL_WIDTH
                color = self.CELL_COLOR_DEAD
                if self.state.is_alive(row, column):
                    color = self.CELL_COLOR_ALIVE
                self.canvas.create_oval(x_coord, y_coord,
                                        x_coord + self.CELL_WIDTH, y_coord + self.CELL_WIDTH,
                                        fill=color)

    def next_step(self):
        if not self.pause:
            self.state = next_generation(self.state)
            self.draw_state()
        self.frame.after(self.DELAY, self.next_step)


def main():
    state = from_file("gameoflife/examples/middle.txt")
    player = Player(state)
    player.start()

if __name__ == '__main__':
    main()

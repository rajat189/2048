import Tkinter as tkin


class look(tkin.Frame):

    def __init__(self, gd, mt=None):
        tkin.Frame.__init__(self, mt)
        self.gd = gd
        for k in "<w>", "<a>", "<s>", "<d>":
            self.master.bind(k, self.callback)

        self.tids = []
        self.ln = 100
        self.canvas = tkin.Canvas(
            mt, width=self.ln * 4, height=self.ln * 4)
        self.canvas.pack()

    def mat_look(self, mat):
        for i in self.tids:
            self.canvas.delete(i)
        self.tids = []
        
        for i in range(4):
            for j in range(4):
                crec = self.rects[i][j]
                ccell = mat[j][i]
                if ccell == 0:
                    ccell = ""
                tid = self.canvas.create_text(
                    crec[0], crec[1], text=ccell)
                self.tids.append(tid)

    def start(self, mat):
        self.mt = tkin.Tk()
        self.mt.title("2048")
        self.ln = 100
        self.canvas.pack()

        self.rects = []
        for row_index in range(4):
            row = []
            for cell_index in range(4):
                self.canvas.create_rectangle(self.ln * cell_index, 
                                            0, 
                                            self.ln * (cell_index + 1),
                                            self.ln * (row_index + 1))
                row.append([self.ln * row_index + 50, self.ln * cell_index + 50])
            self.rects.append(row)

        self.mat_look(mat)

    def callback(self, event):
        if event.char == "w":
            self.gd.slide("up")
        elif event.char == "a":
            self.gd.slide("left")
        elif event.char == "s":
            self.gd.slide("down")
        elif event.char == "d":
            self.gd.slide("right")

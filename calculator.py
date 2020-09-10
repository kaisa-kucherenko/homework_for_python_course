import tkinter as tk


class Calculator(tk.Frame):
    WIDTH = 400
    HEIGHT = 500
    BUTTONS_LIST = [
        '7', '8', '9', 'C', 'CE',
        '4', '5', '6', '+', '-',
        '1', '2', '3', '*', '/',
        '.', '0', '(', ')', '='
    ]

    def __init__(self, master):
        self.master = master.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        super().__init__(self.master)
        self.pack()
        self._create_result_frame()
        self._create_entry_frame()
        self._create_buttons_frame()

    def _create_result_frame(self):
        result_frame = tk.Frame(self.master, bd=3)
        result_frame.place(relx=0.5, rely=0, relwidth=1,
                           relheight=0.4, anchor='n')
        self.list_box = tk.Listbox(result_frame, bg='#F0F0F0',
                                   font=('roboto', 23), justify='left')
        self.list_box.place(relwidth=1, relheight=1)

    def _create_entry_frame(self):
        entry_frame = tk.Frame(self.master, bd=3)
        entry_frame.place(relx=0.5, rely=0.4, relwidth=1,
                          relheight=0.1, anchor='n')
        self.entry = tk.Entry(entry_frame, bg='#F5F5F5',
                              justify='left', validate='all',
                              validatecommand=(self.master.register(self._is_valid), '%S'),
                              font=('roboto', 15))
        self.entry.place(relwidth=1, relheight=1)

    def _create_buttons_frame(self):
        buttons_frame = tk.Frame(self.master, bd=3)
        buttons_frame.place(relx=0.5, rely=0.5, relwidth=1,
                            relheight=0.5, anchor='n')
        for column in range(5):
            buttons_frame.grid_columnconfigure(column, minsize=10,
                                               pad=5, weight=10)
        for row in range(4):
            buttons_frame.grid_rowconfigure(row, minsize=10, pad=5, weight=10)
        row = 0
        column = 0
        for button in self.BUTTONS_LIST:
            tk.Button(buttons_frame, text=button,
                      command=lambda x=button: self._calc(x)).grid(row=row,
                      column=column, sticky='nswe')
            column += 1
            if column > 4:
                column = 0
                row += 1

    def _calc(self, key):
        if self._is_valid(key):
            if key == '=':
                try:
                    result = eval(self.entry.get())
                    if self.list_box.size() <= 4:
                        self.list_box.insert('end', f'{self.entry.get()}={result}')
                    else:
                        self.list_box.delete(0)
                        self.list_box.insert('end', f'{self.entry.get()}={result}')
                    self.entry.config(validate='none')
                    self.entry.delete(0, 'end')
                    self.entry.config(validate='all')
                except SyntaxError:
                    self.list_box.delete(0, 'end')
                    self.list_box.insert('end', 'Error. Invalid operation')
                    self.entry.config(validate='none')
                    self.entry.delete(0, 'end')
                    self.entry.config(validate='all')
            elif key == 'C':
                self.entry.delete(len(self.entry.get()) - 1)
            elif key == 'CE':
                self.entry.config(validate='none')
                self.entry.delete(0, 'end')
                self.entry.config(validate='all')
                self.list_box.delete(0, 'end')
            else:
                self.entry.insert('end', key)

    def _is_valid(self, char):
        if char in self.BUTTONS_LIST:
            return True
        return False


if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(master=root)
    root.mainloop()

import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('300x450')
        self.root.configure(bg='black')
        self.tasks = []
        self.topmost = True

        self.task_list = tk.Listbox(root, bg='black', fg='#ffffb3')
        self.task_list.pack(fill='both', expand=True)
        self.task_list.bind('<Double-1>', self.edit_task)

        self.task_entry = tk.Entry(root, bg='black', fg='#ffffb3')
        self.task_entry.pack(fill='both')

        self.add_button = tk.Button(root, text='Add task', command=self.add_task, bg='black', fg='#ffffb3')
        self.add_button.pack(fill='both')

        self.del_button = tk.Button(root, text='Delete task', command=self.delete_task, bg='black', fg='#ffffb3')
        self.del_button.pack(fill='both')

        self.topmost_button = tk.Button(root, text='Toggle Topmost', command=self.toggle_topmost, bg='black', fg='#ffffb3')
        self.topmost_button.pack(fill='both')

        root.attributes('-topmost', self.topmost)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()

    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            del self.tasks[task_index[0]]
            self.update_listbox()

    def edit_task(self, event):
        global edit_entry
        index = self.task_list.curselection()[0]
        edit_entry = tk.Entry(self.root, bg='black', fg='#ffffb3')
        edit_entry.insert(0, self.tasks[index])
        edit_entry.place(x=self.task_list.winfo_rootx(), y=self.task_list.winfo_rooty() + index*20, 
                         width=self.task_list.winfo_width(), height=20)
        edit_entry.focus_set()

        def save_edit(event):
            self.tasks[index] = edit_entry.get()
            self.update_listbox()
            edit_entry.destroy()

        edit_entry.bind('<Return>', save_edit)

    def toggle_topmost(self):
        self.topmost = not self.topmost
        self.root.attributes('-topmost', self.topmost)

    def update_listbox(self):
        self.task_list.delete(0, 'end')
        for task in self.tasks:
            self.task_list.insert('end', task)


if __name__ == "__main__":
    root = tk.Tk()
    todo_app = ToDoApp(root)
    root.mainloop()

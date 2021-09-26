from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror
from shapes import Point, Line, delete_point, delete_line, points, lines, refresh_line

root = Tk()
mainframe = Frame(master=root)
menu_bar = Frame(master=mainframe)


def show_all_points():
    for point in points:
        point.show()


def hide_all_points():
    for point in points:
        point.hide()


variable_view = IntVar()
variable_view.set(1)


def variable_view_button_command():
    if variable_view.get():
        show_all_points()
    else:
        hide_all_points()


variable_view_button = Checkbutton(master=menu_bar, text='Show variable names', variable=variable_view,
                                   command=variable_view_button_command)
variable_view_button.pack(side=TOP, anchor=W, expand=False)
menu_bar.pack(side=TOP, anchor=W, fill=Y)
split_frame = PanedWindow(master=mainframe)

shape_pane = Frame(master=split_frame)


class ShapePane:
    def __init__(self, shape_name: str, switch_to_this_shape_command):
        self.mainframe = Frame(master=shape_pane)
        self.button = Button(master=self.mainframe, text=shape_name, command=switch_to_this_shape_command)
        self.button.pack(side=TOP, fill=X)
        self.listbox = Listbox(master=self.mainframe)
        self.listbox.pack(side=LEFT, fill=Y)
        self.scrollbar = Scrollbar(master=self.mainframe)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.mainframe.pack(side=TOP, expand=False, anchor=W)

    def empty(self):
        self.listbox.delete(0, END)

    def append(self, string: str):
        self.listbox.insert(END, string)

    def set_texts(self, shapes: list):
        self.empty()
        for shape in shapes:
            self.append(shape.name)

    def on_listbox_element_switch(self, command):
        def get_element(event):
            curselection = event.widget.curselection()
            if curselection:
                curselection = int(curselection[0])
            else:
                curselection = 0
            command(event.widget.get(curselection))

        def select_command(event):
            if not variable_view.get():
                variable_view.set(1)
                show_all_points()
            get_element(event)

        self.listbox.bind('<<ListboxSelect>>', select_command)


split_frame.add(shape_pane, minsize=250)

diagram_editor_frame = Frame(split_frame)
diagram_editor = Canvas(
    master=diagram_editor_frame,
    bg='white',
    width=20000,
    height=20000,
    scrollregion=(0, 0, 20000, 20000)
)
for x in range(0, 401):
    for y in range(0, 401):
        diagram_editor.create_rectangle(x * 50, y * 50, 50 + (x * 50), 50 + (y * 50), outline='lightgreen')
horizontal_scroll_bar_diagram_editor = Scrollbar(master=diagram_editor_frame, orient=HORIZONTAL)
horizontal_scroll_bar_diagram_editor.pack(side=BOTTOM, fill=X)
horizontal_scroll_bar_diagram_editor.config(command=diagram_editor.xview)

vertical_scroll_bar_diagram_viewer = Scrollbar(master=diagram_editor_frame, orient=VERTICAL)
vertical_scroll_bar_diagram_viewer.pack(side=RIGHT, fill=Y)
vertical_scroll_bar_diagram_viewer.config(command=diagram_editor.yview)

diagram_editor.config(
    xscrollcommand=horizontal_scroll_bar_diagram_editor.set, yscrollcommand=vertical_scroll_bar_diagram_viewer.set)
diagram_editor.pack(expand=True, fill=BOTH)
create_line = diagram_editor.create_line
create_text = diagram_editor.create_text
delete = diagram_editor.delete


def on_diagram_editor_enter(command):
    diagram_editor.bind('<Enter>', command)


def on_diagram_editor_leave(command):
    diagram_editor.bind('<Leave>', command)


def on_diagram_viewer_click(command):
    diagram_editor.bind('<Button-1>', command)


split_frame.add(diagram_editor_frame, minsize=1400)


def get_variable_name_from_user():
    return askstring(title='Rename variable', prompt='Please enter a variable name', parent=root)


property_panel = Frame(master=split_frame)


class PointPropertyPane:
    def __init__(self, point: Point, refresh_command, point_modify_command):
        self.mainframe = Frame(master=property_panel)
        name_label = Label(master=self.mainframe, text=f'Point: {point.name}')
        name_label.pack()

        def rename():
            user_variable = get_variable_name_from_user()
            if str(user_variable).replace(' ', '') and user_variable:
                try:
                    point.rename(str(user_variable), refresh_command)
                    name_label['text'] = f'Point: {point.name}'
                except ValueError as error_message:
                    showerror('Error while renaming', error_message)

        rename_button = Button(master=self.mainframe, text='Rename point', bg='snow', fg='black', command=rename)
        rename_button.pack()

        def delete_point_():
            delete_point(point)
            refresh_command()
            self.delete()

        change_point_location_button = Button(master=self.mainframe, text="change point location",
                                              command=point_modify_command)
        change_point_location_button.pack()
        delete_button = Button(master=self.mainframe, text='Delete point', bg='red', fg='snow', command=delete_point_)
        delete_button.pack()
        self.mainframe.pack(side=TOP, anchor=E, expand=False)

    def delete(self):
        self.mainframe.pack_forget()


class LinePropertyPane:
    def __init__(self, line: Line, refresh_command):
        self.mainframe = Frame(master=property_panel)
        name_label = Label(master=self.mainframe, text=f'Line: {line.name}')
        name_label.pack()

        def delete_line_():
            delete_line(line)
            refresh_command()
            self.delete()

        delete_button = Button(master=self.mainframe, text='Delete line', fg='snow', bg='red', command=delete_line_)
        delete_button.pack()
        self.mainframe.pack(side=TOP, anchor=E, expand=False)

    def delete(self):
        self.mainframe.pack_forget()


split_frame.add(property_panel, minsize=150)

split_frame.pack(fill=BOTH)
mainframe.pack(fill=BOTH)
mainloop = root.mainloop

from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror
from tkscrolledframe import ScrolledFrame
from shapes import Point, Line, delete_point, delete_line, points, lines

root = Tk()
root.wm_title('Geometry app')
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
current_mode_label = Label(master=menu_bar, text='Point')
current_mode_label.pack(side=TOP, anchor=W)


def set_current_mode(new_mode: str):
    current_mode_label['text'] = new_mode


split_frame = PanedWindow(master=mainframe)
shape_pane_master = ScrolledFrame(master=split_frame)
shape_pane = shape_pane_master.display_widget(Frame)


class ShapePane:
    def __init__(self, shape_name: str, switch_to_this_shape_command):
        self.mainframe = Frame(master=shape_pane)
        self.shape_name = shape_name.lower().replace('s', '')
        self.button = Button(master=self.mainframe, text=shape_name, command=switch_to_this_shape_command)
        self.button.pack(side=TOP, fill=X)
        self.listbox = Listbox(master=self.mainframe)
        self.listbox.pack(side=LEFT, fill=Y)
        self.scrollbar = Scrollbar(master=self.mainframe)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.mainframe.pack(side=TOP, expand=False, anchor=W)
        self.switch_to_this_shape_command = switch_to_this_shape_command

    def empty(self):
        self.listbox.delete(0, END)

    def append(self, string: str):
        self.listbox.insert(END, string)

    def set_texts(self, shapes: list):
        self.empty()
        for shape in shapes:
            try:
                self.append(shape.name)
            except AttributeError:
                self.append(shape)

    def on_listbox_element_switch(self, get_current_shape, command):
        def get_element(event):
            curselection = event.widget.curselection()
            if curselection:
                curselection = int(curselection[0])
            else:
                curselection = 0
            if get_current_shape() == self.shape_name:
                command(event.widget.get(curselection))

        def select_command(event):
            if not variable_view.get():
                variable_view.set(1)
                show_all_points()
            get_element(event)

        self.listbox.bind('<<ListboxSelect>>', select_command)


split_frame.add(shape_pane_master)

diagram_editor_frame = Frame(split_frame)
diagram_editor = Canvas(
    master=diagram_editor_frame,
    bg='white',
    width=1450,
    height=950,
)
def refresh_diagram_editor():
    diagram_editor.delete('all')
    for point in points:
        point.displayed = False
        point.show()
    for line in lines:
        line.displayed = FALSE
        line.show()
    for x in range(0, 29):
        for y in range(0, 19):
            diagram_editor.create_rectangle(x * 50, y * 50, 50 + (x * 50), 50 + (y * 50), outline='lightgreen')
refresh_diagram_editor()
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


split_frame.add(diagram_editor_frame)


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


split_frame.add(property_panel)
split_frame.pack(fill=Y)
on_key_press_dict = {}


def bind_key(char: str, command):
    on_key_press_dict[char] = command


def on_key_press(event):
    try:
        on_key_press_dict[event.char]()
    except KeyError:
        pass


root.bind('<Key>', on_key_press)
root.focus_set()
mainframe.pack(fill=BOTH)
mainloop = root.mainloop

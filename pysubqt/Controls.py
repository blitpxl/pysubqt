from PyQt5 import QtWidgets
from .Abstract import AbstractWidget


class Widget(QtWidgets.QWidget, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)


class MainWindow(QtWidgets.QMainWindow, AbstractWidget):
    def __init__(self, engine=None, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.menus = {}
        self.engine = engine

    def AddMenu(self, name):
        self.menus[name] = self.menuBar().addMenu(name)

    def AddAction(self, name, menu, function=None):
        if function is not None:
            obj, funcname = function.split(".")
            self.menus[menu].addAction(name).triggered.connect(getattr(getattr(self.engine, obj), funcname))
        else:
            self.menus[menu].addAction(name)


class Button(QtWidgets.QPushButton, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)


class Frame(QtWidgets.QFrame, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)


class Label(QtWidgets.QLabel, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(Label, self).__init__(*args, **kwargs)


class LineEdit(QtWidgets.QLineEdit, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(LineEdit, self).__init__(*args, **kwargs)


class Slider(QtWidgets.QSlider, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)


class TextEdit(QtWidgets.QTextEdit, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(TextEdit, self).__init__(*args, **kwargs)
        

class TextBrowser(QtWidgets.QTextBrowser, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(TextBrowser, self).__init__(*args, **kwargs)

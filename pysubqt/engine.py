import importlib
from .parse import Parser, OperationType
from typing import Union
from PyQt5 import QtWidgets
import sys


class Engine:
    def __init__(self):
        self.parser = Parser()
        self.window: Union[QtWidgets.QWidget, None] = None
        self.scope = []
        self.modules = {}

    def load_file(self, file):
        self.parser.parse(file)

    def run(self, bridge):
        setattr(self, bridge.__name__, bridge())
        app = QtWidgets.QApplication(sys.argv)
        for line in self.parser.parsed_lines:
            self.eval(line)
        win = self.window
        win.show()
        setattr(getattr(self, bridge.__name__), "ui", win)
        sys.exit(app.exec_())

    def use(self, module_name):
        self.modules[module_name] = importlib.import_module("." + module_name, "pysubqt")

    def define_component(self, name, widgetType):
        if not self.scope:
            try:
                self.window = self.get_widget(widgetType)(self)
            except TypeError:
                self.window = self.get_widget(widgetType)()
            self.scope.append(self.window)
        else:
            if isinstance(self.scope[-1], QtWidgets.QBoxLayout):
                self.add_to_layout(name, widgetType)
            else:
                self.add_to_parent(name, widgetType)

    def add_to_parent(self, name, widgetType):
        setattr(self.window, name, self.get_widget(widgetType).__call__(self.scope[-1]))
        self.scope.append(getattr(self.window, name))

    def add_to_layout(self, name, widgetType):
        # create a widget, make it a child of main window
        setattr(self.window, name, self.get_widget(widgetType).__call__(self.window))

        # if the widget that we just created is a type of a layout, then use addLayout() to make nested layout.
        # else, then add it like a regular widget, using addWidget()
        if isinstance(getattr(self.window, name), QtWidgets.QBoxLayout):
            self.scope[-1].addLayout(getattr(self.window, name))
        else:
            self.scope[-1].addWidget(getattr(self.window, name))
        self.scope.append(getattr(self.window, name))

    def get_widget(self, widgetType):
        for key in self.modules.keys():
            try:
                return getattr(self.modules[key], widgetType)
            except AttributeError:
                continue
        raise RuntimeError(f"Cannot find widget type '{widgetType}'")

    def finish_declaration(self):
        if len(self.scope) > 1:  # prevent window declaration to be removed
            self.scope.pop()

    def set_property(self, propertyName, *values):
        getattr(self.scope[-1], propertyName)(*values)

    def set_sub_property(self, value, _property, subproperty):
        value = value.split(".")
        getattr(getattr(self.scope[-1], _property), subproperty)(getattr(getattr(self, value[0]), value[1]))

    def eval(self, line):
        if line[0] == OperationType.Use:
            self.use(*line[1:])
        elif line[0] == OperationType.Define:
            self.define_component(*line[1:])
        elif line[0] == OperationType.Finish:
            self.finish_declaration()
        elif line[0] == OperationType.SetProperty:
            self.set_property(*line[1:])
        elif line[0] == OperationType.SetSubProperty:
            self.set_sub_property(*line[1:])

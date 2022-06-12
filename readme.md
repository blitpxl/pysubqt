# Description
pysubqt is a wrapper-library built on top of PyQt5.

pyqsubqt provides a simple declarative language to rapidly develop a simple graphical user interface application in python.

# Examples
### Blank Window

main.psqt
```
Use Controls

Def Window : Widget
    Title: "Hello, world!"
End
```
main.py
```python
from pysubqt import Engine


class Bridge:
    def __init__(self):
        self.ui = None


e = Engine()
e.load_file("main.psqt")
e.run(Bridge)
```
result:

![A blank window](https://i.ibb.co/WWcWLf1/blank-window.png)

### Showing a label

test.psqt
```
Use Controls
Use Layouts

Def Window : Widget
    Title: "Hello, world!"
    Size: 640 480   # set the default window size

    Def CenterLayout : VLayout
        Alignment: Center   # make the layout center aligned

        Def MyLabel : Label
            Text: "Hello, Mother!"
            Font: "JetBrains Mono" 35   # set the font and the size (in pt)
        End
    End
End
```
result:

![A window with a label saying "Hello, Mother!"](https://i.ibb.co/dQfrwPZ/a-label.png)

### Connecting a button to a python function

main.psqt
```
Use Controls
Use Layouts

Def Window : Widget
    Title: "Hello, world!"

    Def MainLayout : HLayout
        Def Btn : Button
            FixedSize: 300 100
            Text: "Click me!"
            Font: "Segoe UI" 25
            clicked.connect: Bridge.onClicked
        End
    End
End
```
main.py

```python
from pysubqt import Engine


class Bridge:
    def __init__(self):
        self.ui = None
        self.x = 0

    def onClicked(self):
        self.x += 1
        self.ui.Btn.setText(str(self.x))


e = Engine()
e.load_file("main.psqt")
e.run(Bridge)

```

result:

The number on the button will increment by one everytime you click it.

![A window with a button which when you click, the number on the button will increment by one](https://i.ibb.co/PCJ06Qy/incr.png)

# Language Reference
As you can see in the previous examples that every widgets are defined with the
`Def` keyword and then ended with the `End` keyword.

To define a widget, you have to use the `Def` keyword in the following format:

`Def WidgetName : WidgetType`

example:

`Def MyButton : Label`

Note that the widget name doesn't have to be in PascalCase.

So far, there's only 11 pre-defined widget types in pysubqt:

| Widget Name 	 | Description                                                                                                                                                                                                                                 	 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Widget      	 | Widget is the base class for all widgets below. The blank canvas for widgets if you will. You can also create a blank window out of this widget.                                                                                            	 |
| MainWindow  	 | You can create blank main window out of this widget. You can also add menus and submenus by using the property setter AddMenu and AddAction. To add a widget as central, use the property `Central: 1` in the widget defined in main window 	 |
| Button      	 | Widget that can call a function when you click it.                                                                                                                                                                                          	 |
| Frame       	 | Widget that you can use to separate or group other widgets.                                                                                                                                                                                 	 |
| Label       	 | Lets you show a text on the screen.                                                                                                                                                                                                         	 |
| LineEdit    	 | Single-line text input.                                                                                                                                                                                                                     	 |
| Slider      	 | Vertical or horizontal slider lets the user to slide the widget to control its ranged value.                                                                                                                                                	 |
| TextEdit    	 | Multi-line text input.                                                                                                                                                                                                                      	 |
| TextBrowser 	 | Multi-line text display.                                                                                                                                                                                                                    	 |
| HLayout     	 | Lets you stack widgets in horizontal direction.                                                                                                                                                                                             	 |
| VLayout     	 | Lets you stack widgets in vertical direction.                                                                                                                                                                                               	 |

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


class AbstractWidget:
    def WindowIcon(self, iconpath):
        self.setWindowIcon(QIcon(iconpath))

    def Icon(self, iconpath):
        self.setIcon(QIcon(iconpath))

    def IconSize(self, w, h):
        self.setIconSize(int(w), int(h))

    def Style(self, style):
        self.setStyleSheet(style)

    def Title(self, title):
        self.setWindowTitle(title)

    def Text(self, text):
        self.setText(text)

    def Position(self, x, y):
        self.move(int(x), int(y))

    def X(self, x):
        self.move(int(x), self.pos().y())

    def Y(self, y):
        self.move(self.pos().x(), int(y))

    def Size(self, w, h):
        self.resize(int(w), int(h))

    def Width(self, w):
        self.resize(int(w), self.size().height())

    def Height(self, h):
        self.resize(self.size().width(), int(h))

    def FixedSize(self, w, h):
        self.setFixedSize(int(w), int(h))

    def FixedWidth(self, w):
        self.setFixedWidth(int(w))

    def FixedHeight(self, h):
        self.setFixedHeight(int(h))

    def Margin(self, left, top, right, bottom):
        self.setContentsMargins(left, top, right, bottom)

    def Alignment(self, align):
        self.setAlignment(getattr(Qt, f"Align{align}"))

    def Central(self, central):
        if int(central):
            self.parent().setCentralWidget(self)

    def Orientation(self, orientation):
        self.setOrientation(getattr(Qt, orientation))

    def Font(self, font, size):
        self.setFont(QFont(font, int(size)))

    def Range(self, start, end):
        self.setRange(int(start), int(end))

    def Tag(self, tag):
        self.setObjectName(tag)

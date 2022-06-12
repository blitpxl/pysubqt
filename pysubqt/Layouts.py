from .Abstract import AbstractWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class HLayout(QHBoxLayout, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(HLayout, self).__init__(*args, **kwargs)


class VLayout(QVBoxLayout, AbstractWidget):
    def __init__(self, *args, **kwargs):
        super(VLayout, self).__init__(*args, **kwargs)

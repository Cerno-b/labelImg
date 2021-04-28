import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.uic import loadUi


from main_window_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.label_dialog = QDialog(parent=self)
        self.color_dialog = QColorDialog(parent=self)

        # todo custom edit_button
        # todo custom combo_box
        # todo custom color_dialog
        # todo custom canvas

        # self.difficult_checkbox.stateChanged.connect(self.button_state)
        # self.label_list.itemActivated.connect(self.label_selection_changed)
        # self.label_list.itemSelectionChanged.connect(self.label_selection_changed)
        # self.label_list.itemDoubleClicked.connect(self.edit_label)
        # self.label_list.itemChanged.connect(self.label_item_changed)
        # self.file_list_widget.itemDoubleClicked.connect(self.file_item_double_clicked)

        # self.canvas.zoomRequest.connect(self.zoom_request)
        # self.canvas.set_drawing_shape_to_square(settings.get(SETTING_DRAW_SQUARE, False))

        # self.canvas.scrollRequest.connect(self.scroll_request)

        # self.canvas.newShape.connect(self.new_shape)
        # self.canvas.shapeMoved.connect(self.set_dirty)
        # self.canvas.selectionChanged.connect(self.shape_selection_changed)
        # self.canvas.drawingPolygon.connect(self.toggle_drawing_sensitive)

        # todo check what action_copy_prev_bounding does
        # todo allow switching save format
        # todo check what action_edit_mode


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Model.mainDialogModel import MainDialogModel
from View.mainDialogView import MainDialogView
from Control.mainDialogControl import MainDialogControl

from Model.tokenDialogModel import TokenDialogModel
from View.tokenDialogView import TokenDialogView
from Control.tokenDialogControl import TokenDialogControl


class GUI():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.mvc = []

        _, _, _, tokenDialogControl = self.CreateDialog(
            TokenDialogModel, TokenDialogView, TokenDialogControl, None,
            '輸入Token', False, True
        )

        self.CreateDialog(
            MainDialogModel, MainDialogView, MainDialogControl, {
                'TokenDialog': tokenDialogControl
            },
            '貓之城抽卡資料匯出小工具', True, False
        )

        
        sys.exit(self.app.exec_())

    def CreateDialog(self, Model, View, Control, subControls, title = '', show = False, isModal = False):
        window = QtWidgets.QDialog()
        view = View()
        view.setupUi(window)

        if Model is not None and Control is not None:
            model = Model()
            control = Control(window, model, view, subControls)
        else:
            model = None
            control = None

        window.setWindowTitle(title)

        if isModal:
            window.setWindowModality(Qt.ApplicationModal)

        if show:
            window.show()

        self.mvc.append((window, model, view, control))
        return self.mvc[-1]

if __name__ == "__main__":
    GUI()
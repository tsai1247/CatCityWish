from View.UI.mainDialogUI import Ui_mainWindow
from Common.Chart import Chart

class MainDialogView(Ui_mainWindow):
    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.chart_SpecialSummon = Chart()
        self.chart_CommonSummon = Chart()
        self.chart_SSRSummon = Chart()

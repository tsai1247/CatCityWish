from PyQt5.QtWidgets import QDialog
from Model.tokenDialogModel import TokenDialogModel
from View.tokenDialogView import TokenDialogView

class TokenDialogControl():
    def __init__(self, mainWindow: QDialog, model: TokenDialogModel, view: TokenDialogView, subControls) -> None:
        self.mainWindow = mainWindow
        self.view = view
        self.model = model
        self.initData()
        self.setEvents()
        self.subControls = subControls

    # 資料初始化
    def initData(self):
        pass

    # 事件綁定
    def setEvents(self):
        self.view.buttonBox.accepted.connect(self.saveToken)
        self.view.buttonBox.rejected.connect(self.cancel)
        pass

    def saveToken(self):
        open('.env', 'w', encoding='utf-8').write(
f'''clientAppId = '{self.view.tf_clientAppId.text()}'
playerId = '{self.view.tf_playerId.text()}'
accessToken = '{self.view.tf_AssessToken.text()}'
''')
        self.close()
        
    def cancel(self):
        self.close()

    def close(self):
        self.mainWindow.hide()

    # 事件

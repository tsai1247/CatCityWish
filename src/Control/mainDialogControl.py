from datetime import datetime
import os
import threading
import browserhistory as bh
from urllib import parse
from PyQt5.QtWidgets import QFileDialog

from Model.mainDialogModel import MainDialogModel
from View.mainDialogView import MainDialogView

class MainDialogControl():
    def __init__(self, mainWindow, model: MainDialogModel, view: MainDialogView, subControls) -> None:
        self.mainWindow = mainWindow
        self.view = view
        self.model = model
        self.initData()
        self.setEvents()
        self.subControls = subControls

    # 資料初始化
    def initData(self):
        self.view.txt_UpdateTime.setText(f'{self.model.lastUpdatePrepend} {self.getLastUpdateTime()}')
        self.view.btn_Hint.setText(self.model.btn_Hint_Content)
        self.view.btn_UpdateData.setText(self.model.btn_UpdateData_Content)
        self.view.btn_ExportExcel.setText(self.model.btn_ExportExcel_Content)

        self.view.chart_SpecialSummon.setChart(self.model.specialSummonTitle, self.model.specialSummonData)
        self.view.space_SpecialSummon.addWidget(self.view.chart_SpecialSummon)

        self.view.chart_CommonSummon.setChart(self.model.commonSummonTitle, self.model.commonSummonData)
        self.view.space_CommonSummon.addWidget(self.view.chart_CommonSummon)

        self.view.chart_SSRSummon.setChart(self.model.SSRSummonTitle, self.model.SSRSummonData)
        self.view.space_SSRSummon.addWidget(self.view.chart_SSRSummon)


    # 事件綁定
    def setEvents(self):
        self.view.btn_ExportExcel.clicked.connect(self.exportExcel)
        self.view.btn_UpdateData.clicked.connect(self.updateData)
        self.view.btn_Hint.clicked.connect(self.showHintDialog)
        self.view.btn_GetToken.clicked.connect(self.getTokenInHistory)
        self.view.btn_EnterToken.clicked.connect(self.showTokenDialog)

    # 事件
    # 顯示說明
    def showHintDialog(self):
        os.system('start https://github.com/tsai1247/CatCityWish/blob/main/README.md')
        print('show hint')

    # 更新圖表
    def updateChart(self):
        self.view.chart_SpecialSummon.updateData(self.model.specialSummonData)
        self.view.chart_CommonSummon.updateData(self.model.commonSummonData)
        self.view.chart_SSRSummon.updateData(self.model.SSRSummonData)

    # 取得Token
    def getTokenInHistory(self):
        t = threading.Thread(target=self.getTokenInHistoryThreadTask)
        t.start()

    def getTokenInHistoryThreadTask(self):
        self.log('抓取瀏覽紀錄中')
        try:
            histories = bh.get_browserhistory()
        except:
            self.log('請先關閉瀏覽器')
            return
        
        found = False
        result = {}
        self.log('從瀏覽紀錄查詢token...')
        for browser in histories:
            if found:
                break
            for history in histories[browser]:
                url = history[0]
                if 'https://passport-user-center-pc.fundollgame.com/' in url: 
                    url = url.replace('/#/', '/')  
                    qs = parse.parse_qs(parse.urlparse(url).query)
                    if 'appId' in qs and 'uid' in qs and 'accesstoken' in qs:
                        open('.env', 'w', encoding='utf-8').write(
f'''clientAppId = '{qs['appId'][0]}'
playerId = '{qs['uid'][0]}'
accessToken = '{qs['accesstoken'][0]}'
''')
                        found = True
                        break

        if found:
            self.log('Token抓取成功')
        else:
            self.log('Token抓取失敗，請點擊貓之城登入畫面的自助中心後，完全關閉瀏覽器再試一次')

    # 更新數據
    def updateData(self):
        t = threading.Thread(target=self.updateDataThreadTask)
        t.start()

    def updateDataThreadTask(self):
        self.log('正在抓取召喚紀錄...')
        self.model.updateList()
        self.log('數據整理中...')
        self.model.getData()
        self.log('更新圖表...')
        self.updateChart()
        self.log('更新完成')

        self.setLastUpdateTime()

    def setLastUpdateTime(self):
        now = datetime.now()
        self.view.txt_UpdateTime.text = f'上次更新時間: {now}'
        open('lastUpdate.txt', 'w', encoding='utf-8').write(f'{now}')

    def getLastUpdateTime(self):
        if not os.path.isfile('lastUpdate.txt'):
            return '無'
        return open('lastUpdate.txt', 'r', encoding='utf-8').read()


    # 匯出Excel
    def exportExcel(self):
        filename, filetype = QFileDialog.getSaveFileName(
            self.mainWindow, '匯出Excel', './',"Excel檔案 (*.xlsx)"
        )

        if filename:
            self.model.exportExcel(filename)
        print('export excel')

    # 手動輸入
    def showTokenDialog(self):
        self.subControls['TokenDialog'].mainWindow.show()
        pass

    def log(self, content):
        self.view.txt_logger.setText(content)
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Chart(QChartView):
    def __init__(self, title: str = '', data: list = []) -> None:
        self.setChart(title, data)


    def updateData(self, data: list = []):
        # 清除現有資料
        self.series.clear()

        # 更新資料
        for d in data:
            self.series.append(d['name'], d['value'])
            
        self.data = data
        
        # 設定顏色與關鍵扇形
        slice = QPieSlice()
        for i in range(len(data)):
            slice = self.series.slices()[i]
            if 'exploded' in data[i] and data[i]['exploded']:
                slice.setExploded(True)
            slice.setLabelVisible(True)
            slice.setPen(QPen(data[i]['color'], 2))
            slice.setBrush(data[i]['color'])

    def setChart(self, title: str = '', data: list = []):
        # 加入資料
        self.series = QPieSeries()
        self.updateData(data)

        chart = QChart()
        chart.addSeries(self.series)
        chart.createDefaultAxes()

        # 加入動畫
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # 加入標題
        chart.setTitle(title)

        # 顯示圖例
        chart.legend().setVisible(True)

        # 圖例位置
        chart.legend().setAlignment(Qt.AlignTop)

        self.chart = chart

        # 把上方的設定加入ChartView
        super().__init__(self.chart)
        self.setRenderHint(QPainter.Antialiasing)

if __name__ == '__main__':
    data = [
        {
            'name': 'SSR',
            'value': 12,
            'color': QColor(255, 255, 0, 255),
            'exploded': True
        },
        {
            'name': 'SR',
            'value': 120,
            'color': QColor(124, 11, 255, 255) 
        },
        {
            'name': 'R',
            'value': 547,
            'color': QColor(0, 255, 241, 255) 
        }
    ]
    Chart(data)
from PyQt5.QtWidgets import QMainWindow ,QApplication, QVBoxLayout, QFileDialog
from PyQt5 import uic
from chart import Barchart,Linechart,Scatterchart, Histogramchart
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QCursor
import sys
#import matplotlib

class MAIN_menu(QMainWindow):
	def __init__(self):
		#---------------------Properties--------------------------------
		self.file_path = None#thuoc tinh file path rong

		#---------------------Set status---------------------------------
		super().__init__()#cho ham init thua ke de hon
		uic.loadUi("GUI.ui",self)
		self.normal_shown = True
		self.line_chart = Linechart()
		self.bar_chart = Barchart()
		self.scatter_chart = Scatterchart()
		self.histogram_chart = Histogramchart()

		#------------------BUTTON----------------------------------------
		self.Load.clicked.connect(lambda: self.Load_file())#button Load = Load_file
		self.Exit.clicked.connect(lambda: sys.exit())
		self.Visual.clicked.connect(lambda: self.Set_up_chart())
		
	def Load_file(self):
		self.file_path = QFileDialog.getOpenFileNames()
		#self.filename = QFileDialog.getOpenFileName(filter="CSV (*.csv)")[0]
        #self.df = pd.read_csv(self.filename, encoding='utf-8').fillna(0)

		#print(type(self.file_path),self.file_path)

	def Set_up_chart(self):
		# -------------- Compare chart method --------------- 
		#--------------- Steps ------------------------------
		#self.line_chart.chart.removeAllSeries()
		self.line_chart.file = self.file_path[0][0]			# add file path
		self.line_chart.chart.removeAllSeries()					# remove series
		self.line_chart.update_data()							# update chart series
		self.line_chart.chart.addSeries(self.line_chart.series)		# add new series
		self.Line.setLayout(self.line_chart.vbox)						# set layout
		#------------------------------------------------------


		# self.bar_chart.file = self.file_path		
		# self.Bar.setLayout(self.bar_chart.vbox)

		# self.scatter_chart.file = self.file_path
		# self.Scatter.setLayout(self.scatter_chart.vbox)
		
		#scatter chart 
		#self.line_chart.chart.removeAllSeries()
		self.scatter_chart.file = self.file_path[0][0]			# add file path
		self.scatter_chart.chart.removeAllSeries()              #remove old chart 
		self.scatter_chart.update_data()							# update chart series
		self.scatter_chart.chart.addSeries(self.scatter_chart.series)		# add new series
		self.Scatter.setLayout(self.scatter_chart.vbox)						# set layout
		#------------------------------------------------------

		#bar chart 
		#self.line_chart.chart.removeAllSeries()
		self.bar_chart.file = self.file_path[0][0]			# add file path
		self.bar_chart.chart.removeAllSeries()              #remove old chart 
		self.bar_chart.update_data()							# update chart series
		self.bar_chart.chart.addSeries(self.bar_chart.series)		# add new series
		self.Bar.setLayout(self.bar_chart.vbox)						# set layout
		#------------------------------------------------------


		#histogram chart 
		#self.line_chart.chart.removeAllSeries()
		self.histogram_chart.file = self.file_path[0][0]			# add file path
		self.histogram_chart.chart.removeAllSeries()				#remove old chart 
		self.histogram_chart.update_data()							# update chart series
		self.histogram_chart.chart.addSeries(self.histogram_chart.series)		# add new series
		self.Histogram.setLayout(self.histogram_chart.vbox)						# set layout
		#------------------------------------------------------



if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_win = MAIN_menu()
    main_win.show()
    
    sys.exit(app.exec())

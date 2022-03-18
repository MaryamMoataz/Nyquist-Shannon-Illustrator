from signal import signal
from PyQt5 import QtWidgets, uic
import sys 
from numpy import sin, pi, arange  # ceil, floor, linspace, cos
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from openpyxl import Workbook


sum_of_signals=[]

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('mainwindow.ui', self)
         # initializing frequency, magnitude, and phase shift variables
        self.frequency = 1
        self.magnitude = 1
        self.phase_shift = 0
        self.signal=0
        self.sum_of_signals= [0]

        self.time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        
        # calling the compose function using the compose button
        self.compose_button.clicked.connect(self.compose)
        # calling the summaption function using the confirm button
        self.confirm_button.clicked.connect(self.composer_summation)
        # calling the save function using the save action from the menubar
        self.action_save.triggered.connect(self.save) 

       

    def compose(self):
        # clearing the widget so that there aren't several plots on top of each other (overlapped)
        self.composer_widget.clear()
        
        # reading the inputs from the UI line edit elements
        self.frequency = float(self.freq_line_edit.text()) # frequency
        self.magnitude = float(self.magnitude_line_edit.text() ) # magnitude
        self.phase_shift = float(self.phase_line_edit.text()) # phase shift
        
        #time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        # sinusoidal changing with input frequency, magnitude, and phase shift
        
        self.signal = self.magnitude * sin(2 * pi * self.frequency * self.time + self.phase_shift) 
        
        self.composer_widget.plot(self.time, self.signal)  # plotting
        
          

    def composer_summation(self):
        self.summation_graph_widget.clear()
        #time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        
        self.sum_of_signals.append(self.signal) # appends an element to the end of the list
          
        self.summation_graph_widget.plot(self.time, sum(self.sum_of_signals))  # plotting


    def save(self):
        df = pd.DataFrame()

        list1=pd.Series(self.time)
        list2=pd.Series(sum(self.sum_of_signals))

        df = pd.concat([list1,list2], ignore_index=True, axis=1)

        df.to_excel('output.xlsx',index = False)   
       
        # df.to_csv('file.csv',index=False) for csv




app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

from pickle import GLOBAL
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QSlider
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import pathlib
import numpy as np
import pandas as pd
from numpy import sin, pi, arange

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('mainwindow.ui', self)

        # calling the compose function using the compose button
        self.compose_button.clicked.connect(self.compose)
        self.action_open.triggered.connect(self.open)
        self.horizontal_slider.valueChanged.connect( self.sampling)
        self.draw_button.clicked.connect(self.plotSeparateSamples)
        

        # initializing frequency, magnitude, and phase shift variables
        self.frequency = 1
        self.magnitude = 1
        self.phase_shift = 0
    def open(self):
        self.main_signal_widget.clear()
        files_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open only CSV ', os.getenv('HOME'), "csv(*.csv)")
        path = files_name[0]
        
        pathlib.Path(path).suffix == ".csv"
        data = pd.read_csv(path)
        self.time_col = data.values[:, 0]
        self.amp_col = data.values[:, 1]
        FtAmp = np.fft.fft(self.amp_col)
        FtAmp = FtAmp[0:int(len(self.amp_col) /2)]
        FtAmp = abs(FtAmp)
        maxpower = max(FtAmp)
        noise = (maxpower / 10)
        self.fmaxtuble = np.where(FtAmp > noise)
        self.maxFreq = max(self.fmaxtuble[0])
        print(self.maxFreq)
        self.main_signal_widget.plot(self.time_col, self.amp_col,pen='red')
        #freqs = np.fft.fftfreq(len(self.amp_col))
        #print(freqs)
    
    def changedvalue(self):
        self.min_slider = 0
        self.max_slider = 3 * self.maxFreq
        self.horizontal_slider.setMinimum(self.min_slider)
        self.horizontal_slider.setMaximum(int(self.max_slider))
        self.sampling_factor = self.horizontal_slider.value()
        print(self.sampling_factor)
        self.horizontal_slider.setTickInterval(int(1+self.maxFreq))
        return self.sampling_factor
   
    def sampling(self):
        self.main_signal_widget.clear()
        self.changedvalue()

        if self.sampling_factor == 0:

            self.main_signal_widget.plot(self.time_col, self.amp_col)

        else:
            self.size = int(len((self.time_col))) - 1
            self.step = int(self.size / self.horizontal_slider.value())
            self.data_sampled_list = [self.amp_col[0]]
            self.time_sampled_list = [self.time_col[0]]
            for index in range(int(self.step), self.size + 1, int(self.step)):
                self.data_sampled_list.append(self.amp_col[index])
                self.time_sampled_list.append(self.time_col[index])
            self.Data_sampled_nparray = np.array(self.data_sampled_list)
            self.time_sampled_nparray = np.array(self.time_sampled_list)
            
            self.main_signal_widget.plot(self.time_col, self.amp_col,pen='red')
            self.main_signal_widget.plot(self.time_sampled_nparray, self.Data_sampled_nparray, symbol="o")
    def plotSeparateSamples(self):
        self.reconstructed_graph_widget.clear()
        self.reconstructed_graph_widget.plot(self.time_sampled_nparray, self.Data_sampled_nparray, pen='blue')
        self.reconstructed_graph_widget.setBackground('black')


    
    def compose(self):
        # clearing the widget so that there aren't several plots on top of each other
        self.composer_widget.clear()
        # reading the inputs from the UI line edit elements
        self.frequency = float(self.freq_line_edit.text()) # frequency
        self.magnitude = float(self.magnitude_line_edit.text() ) # magnitude
        self.phase_shift = float(self.phase_line_edit.text()) # phase shift
        
        time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        # sinusoidal changing with input frequency, magnitude, and phase shift
        signal = self.magnitude * sin(2 * pi * self.frequency * time + self.phase_shift) 
        self.composer_widget.plot(time, signal)  # plotting
        
       
  
        
        

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

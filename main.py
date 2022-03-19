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
from mainwindow import Ui_MainWindow

import matplotlib.pyplot as plt
counter=-1

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        # uic.loadUi('mainwindow.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
         # initializing frequency, magnitude, and phase shift variables
        self.frequency = 1
        self.magnitude = 1
        self.phase_shift = 0
        self.signal=0
        self.sum_of_signals= [0]

        self.time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        
        # calling the compose function using the compose button
        self.ui.compose_button.clicked.connect(self.compose)

        self.ui.action_open.triggered.connect(self.open)
        self.ui.confirm_button.clicked.connect(self.composer_summation)
        self.ui.delete_button.clicked.connect(self.delete_signal)
        self.ui.horizontal_slider.valueChanged.connect(self.sampling)
        self.ui.draw_button.clicked.connect(self.sinc_interpolation)
        self.ui.action_save.triggered.connect(self.save)
        self.ui.move_to_main.clicked.connect(self.move_to_main)
        self.ui.show_hide_button.clicked.connect(self.hide)
    
        # self.combobox.currentIndexChanged.connect(self.change_value)
        
        # initializing frequency, magnitude, and phase shift variables
        self.frequency = 1
        self.magnitude = 1
        self.phase_shift = 0
        self.condition = 0
        self.amplitude = []
        self.showstatus=1

    def open(self):
        self.condition = 1
        self.ui.main_signal_widget.clear()
        #self.main_signal_widget.setBackground('w')
        files_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open only CSV ', os.getenv('HOME'), "csv(*.csv)")
        path = files_name[0]

        pathlib.Path(path).suffix == ".csv"
        data = pd.read_csv(path)
        self.time = data.values[:, 0]
        self.amp_col = data.values[:, 1]
        self.conditioning()
        self.plotting()
    
    def hide(self):
        if self.showstatus==1:
         self.ui.reconstructed_graph_widget.hide()
         self.showstatus=0
        elif self.showstatus==0:
         self.ui.reconstructed_graph_widget.show()
         self.showstatus=1

    def plotting(self):
        self.conditioning()
        FtAmp = np.fft.fft(self.amplitude)
        FtAmp = FtAmp[0:int(len(self.amplitude) /2)]
        FtAmp = abs(FtAmp)
        maxpower = max(FtAmp)
        noise = (maxpower / 10)
        self.fmaxtuble = np.where(FtAmp > noise)
        self.maxFreq = max(self.fmaxtuble[0])
       # print(self.maxFreq)
        #self.ui.main_signal_widget.plot(self.time, self.amplitude,pen='blue')
        #freqs = np.fft.fftfreq(len(self.amplitude))
        #print(freqs)
    
        self.ui.main_signal_widget.plot(self.time, self.amplitude)
        #freqs = np.fft.fftfreq(len(self.amplitude))
        #print(freqs)

    def changedvalue(self):
        self.conditioning()
        self.min_slider = 0
        self.max_slider = 3 * self.maxFreq
        self.ui.horizontal_slider.setMinimum(self.min_slider)
        self.ui.horizontal_slider.setMaximum(int(self.max_slider))
        self.sampling_factor = self.ui.horizontal_slider.value()
       # print(self.sampling_factor)
        self.ui.horizontal_slider.setTickInterval(int(1 + self.maxFreq))
        return self.sampling_factor

    def sampling(self):
        self.conditioning()
        self.ui.main_signal_widget.clear()
        self.changedvalue()

        if self.sampling_factor == 0:

            self.ui.main_signal_widget.plot(self.time, self.amplitude )

        else:
            self.size = int(len((self.time))) - 1
            self.step = int(self.size / self.ui.horizontal_slider.value())
            self.data_sampled_list = [self.amplitude[0]]
            self.time_sampled_list = [self.time[0]]
            for index in range(int(self.step), self.size + 1, int(self.step)):
                self.data_sampled_list.append(self.amplitude[index])
                self.time_sampled_list.append(self.time[index])
            self.Data_sampled_nparray = np.array(self.data_sampled_list)
            self.time_sampled_nparray = np.array(self.time_sampled_list)

            self.ui.main_signal_widget.plot(self.time, self.amplitude, pen='red')
            self.ui.main_signal_widget.plot(self.time_sampled_nparray, self.Data_sampled_nparray, symbol="o")

    def sinc_interpolation(self):
        self.ui.reconstructed_graph_widget.clear()
       # if len(self.Data_sampled_nparray) != len(self.time_sampled_nparray):
          #  raise ValueError('sampled Data and sampled time must be the same length')
        # Find the period
        self.Period = self.time_sampled_nparray[1] - self.time_sampled_nparray[0]
        self.sincMagnitude = np.tile(self.time, (len(self.time_sampled_nparray), 1)) - np.tile(
            self.time_sampled_nparray[:, np.newaxis], (1, len(self.time)))
        self.reconstruct = np.dot(self.Data_sampled_nparray, np.sinc(self.sincMagnitude / self.Period))
        self.ui.reconstructed_graph_widget.plot(self.time, self.reconstruct,pen='blue')


    def plotSeparateSamples(self):
        self.conditioning()
        self.ui.reconstructed_graph_widget.clear()
        self.ui.reconstructed_graph_widget.plot(self.time_sampled_nparray, self.Data_sampled_nparray, pen='blue')
        self.ui.reconstructed_graph_widget.setBackground('black')

    def compose(self):
        # clearing the widget so that there aren't several plots on top of each other (overlapped)
        self.ui.composer_widget.clear()
        
        # reading the inputs from the UI line edit elements
        self.frequency = float(self.ui.freq_line_edit.text()) # frequency
        self.magnitude = float(self.ui.magnitude_line_edit.text() ) # magnitude
        self.phase_shift = float(self.ui.phase_line_edit.text()) # phase shift
        
        #time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        # sinusoidal changing with input frequency, magnitude, and phase shift

        signal = self.magnitude * sin(2 * pi * self.frequency * self.time + self.phase_shift) 
        self.ui.composer_widget.plot(self.time, signal)  # plotting
        
        self.signal = self.magnitude * sin(2 * pi * self.frequency * self.time + self.phase_shift) 
        
        self.ui.composer_widget.plot(self.time, self.signal)  # plotting


    def composer_summation(self):
        self.condition = 2
        global counter
        self.ui.summation_graph_widget.clear()
        #time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        
        self.sum_of_signals.append(self.signal) # appends an element to the end of the list
        self.ui.combobox.addItem(str(counter + 1))
        self.ui.summation_graph_widget.plot(self.time, sum(self.sum_of_signals))  # plotting
        counter=counter+1
        self.conditioning()

    def move_to_main(self):
         self.ui.main_signal_widget.clear()
         #self.ui.main_signal_widget.plot(self.time, sum(self.sum_of_signals))
         self.conditioning()
         self.plotting()
         

    def conditioning(self):
        if self.condition == 1:
            self.amplitude = self.amp_col
        elif self.condition == 2:
            self.amplitude = sum(self.sum_of_signals)

    def delete_signal(self):
        global counter
        # if self.ui.combobox.currentIndex() == -1:
        #     self.sum_of_signals.pop(self.sum_of_signals[0])
        index = self.ui.combobox.currentIndex() #-1
        self.ui.combobox.removeItem(index)
        #print(index)
        self.sum_of_signals.pop(index)
        #print(index)

        self.ui.summation_graph_widget.clear()
        self.ui.summation_graph_widget.plot(self.time, sum(self.sum_of_signals))

            # time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
            # self.summation_graph_widget.plot(self.time, sum(self.sum_of_signals))



    def save(self):
        df = pd.DataFrame()

        list1=pd.Series(self.time)
        list2=pd.Series(sum(self.sum_of_signals))

        df = pd.concat([list1,list2], ignore_index=True, axis=1)

        df.to_csv('output.csv',index = False)   
       
        




app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

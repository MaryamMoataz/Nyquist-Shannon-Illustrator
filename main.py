from signal import signal
from PyQt5 import QtWidgets, uic
import sys 
from numpy import sin, pi, cos, arange  # ceil, floor, linspace,
import matplotlib.pyplot as plt
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
        self.sum_of_signals=0
        

        # calling the compose function using the compose button
        self.compose_button.clicked.connect(self.compose)
        self.confirm_button.clicked.connect(self.composer_summation)

       

    def compose(self):
        # clearing the widget so that there aren't several plots on top of each other
        self.composer_widget.clear()
        
        # reading the inputs from the UI line edit elements
        self.frequency = float(self.freq_line_edit.text()) # frequency
        self.magnitude = float(self.magnitude_line_edit.text() ) # magnitude
        self.phase_shift = float(self.phase_line_edit.text()) # phase shift
        
        time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        # sinusoidal changing with input frequency, magnitude, and phase shift
        
        self.signal = self.magnitude * sin(2 * pi * self.frequency * time + self.phase_shift) 
       
        #self.sum_of_signals= self.sum_of_signals + self.signal
        
        self.composer_widget.plot(time, self.signal)  # plotting
        
          

    def composer_summation(self):
        self.summation_graph_widget.clear()
        time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        
        sum_of_signals.append(self.signal) # appends an element to the end of the list
          
        self.summation_graph_widget.plot(time, sum(sum_of_signals))  # plotting





app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

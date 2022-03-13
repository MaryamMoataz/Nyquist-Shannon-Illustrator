from PyQt5 import QtWidgets, uic
import sys 
from numpy import sin, pi, arange  # ceil, floor, linspace,
import matplotlib.pyplot as plt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        #Load the UI Page
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('test.ui', self)

        # calling the compose function using the compose button
        self.compose_button .clicked.connect(self.compose)

        # initializing frequency, magnitude, and phase shift variables
        self.frequency = 1
        self.magnitude = 1
        self.phase_shift = 0

    def compose(self):
        # clearing the widget so that there aren't several plots on top of each other
        self.plot_widget.clear()
        # reading the inputs from the UI line edit elements
        self.frequency = float(self.Frequency_input.text())
        self.magnitude = float(self.Mag_input.text() )
        self.phase_shift = float(self.Phase_input.text())
        
        time = arange(0.0, 5.0, 0.02) # start:0, end:5, step:200 ms intervals
        # sinusoidal changing with input frequency, magnitude, and phase shift
        signal = self.magnitude * sin(2 * pi * self.frequency * time + self.phase_shift) 
        self.plot_widget.plot(time, signal)  # plotting
  
        
        

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
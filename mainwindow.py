# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\semester 6\DSP\tasks\Task 2\new version\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 639)
        MainWindow.setStyleSheet("background-color: rgb(220, 208, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_signal_widget = PlotWidget(self.tab_3)
        self.main_signal_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.main_signal_widget.setObjectName("main_signal_widget")
        self.verticalLayout.addWidget(self.main_signal_widget)
        self.draw_button = QtWidgets.QPushButton(self.tab_3)
        self.draw_button.setMinimumSize(QtCore.QSize(81, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(181, 126, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.draw_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.draw_button.setFont(font)
        self.draw_button.setStyleSheet("\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);\n"
"")
        self.draw_button.setObjectName("draw_button")
        self.verticalLayout.addWidget(self.draw_button)
        self.horizontal_slider = QtWidgets.QSlider(self.tab_3)
        self.horizontal_slider.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);\n"
"")
        self.horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_slider.setObjectName("horizontal_slider")
        self.verticalLayout.addWidget(self.horizontal_slider)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reconstructed_graph_widget = PlotWidget(self.tab_3)
        self.reconstructed_graph_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.reconstructed_graph_widget.setObjectName("reconstructed_graph_widget")
        self.verticalLayout_2.addWidget(self.reconstructed_graph_widget)
        self.show_hide_button = QtWidgets.QPushButton(self.tab_3)
        self.show_hide_button.setMinimumSize(QtCore.QSize(81, 23))
        self.show_hide_button.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);")
        self.show_hide_button.setObjectName("show_hide_button")
        self.verticalLayout_2.addWidget(self.show_hide_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.tab_widget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.composer_widget = PlotWidget(self.tab_4)
        self.composer_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.composer_widget.setObjectName("composer_widget")
        self.verticalLayout_3.addWidget(self.composer_widget)
        self.frequency_label = QtWidgets.QLabel(self.tab_4)
        self.frequency_label.setObjectName("frequency_label")
        self.verticalLayout_3.addWidget(self.frequency_label)
        self.freq_line_edit = QtWidgets.QLineEdit(self.tab_4)
        self.freq_line_edit.setObjectName("freq_line_edit")
        self.verticalLayout_3.addWidget(self.freq_line_edit)
        self.magnitude_label = QtWidgets.QLabel(self.tab_4)
        self.magnitude_label.setObjectName("magnitude_label")
        self.verticalLayout_3.addWidget(self.magnitude_label)
        self.magnitude_line_edit = QtWidgets.QLineEdit(self.tab_4)
        self.magnitude_line_edit.setObjectName("magnitude_line_edit")
        self.verticalLayout_3.addWidget(self.magnitude_line_edit)
        self.phase_label = QtWidgets.QLabel(self.tab_4)
        self.phase_label.setObjectName("phase_label")
        self.verticalLayout_3.addWidget(self.phase_label)
        self.phase_line_edit = QtWidgets.QLineEdit(self.tab_4)
        self.phase_line_edit.setObjectName("phase_line_edit")
        self.verticalLayout_3.addWidget(self.phase_line_edit)
        self.compose_button = QtWidgets.QPushButton(self.tab_4)
        self.compose_button.setMinimumSize(QtCore.QSize(81, 23))
        self.compose_button.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);")
        self.compose_button.setObjectName("compose_button")
        self.verticalLayout_3.addWidget(self.compose_button)
        self.confirm_button = QtWidgets.QPushButton(self.tab_4)
        self.confirm_button.setMinimumSize(QtCore.QSize(81, 23))
        self.confirm_button.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);")
        self.confirm_button.setObjectName("confirm_button")
        self.verticalLayout_3.addWidget(self.confirm_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.summation_graph_widget = PlotWidget(self.tab_4)
        self.summation_graph_widget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.summation_graph_widget.setObjectName("summation_graph_widget")
        self.verticalLayout_4.addWidget(self.summation_graph_widget)
        self.combobox = QtWidgets.QComboBox(self.tab_4)
        self.combobox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);")
        self.combobox.setCurrentText("")
        self.combobox.setObjectName("combobox")
        self.verticalLayout_4.addWidget(self.combobox)
        self.move_to_main = QtWidgets.QPushButton(self.tab_4)
        self.move_to_main.setMinimumSize(QtCore.QSize(81, 23))
        self.move_to_main.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);")
        self.move_to_main.setObjectName("move_to_main")
        self.verticalLayout_4.addWidget(self.move_to_main)
        self.delete_button = QtWidgets.QPushButton(self.tab_4)
        self.delete_button.setMinimumSize(QtCore.QSize(81, 23))
        self.delete_button.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(181, 126, 220);")
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout_4.addWidget(self.delete_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.tab_widget.addTab(self.tab_4, "")
        self.horizontalLayout.addWidget(self.tab_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 26))
        self.menubar.setObjectName("menubar")
        self.menubar_2 = QtWidgets.QMenu(self.menubar)
        self.menubar_2.setObjectName("menubar_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.menubar_2.addAction(self.action_open)
        self.menubar_2.addAction(self.action_save)
        self.menubar.addAction(self.menubar_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.draw_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.draw_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>dsds</p></body></html>"))
        self.draw_button.setText(_translate("MainWindow", "Draw"))
        self.show_hide_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.show_hide_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>dsds</p></body></html>"))
        self.show_hide_button.setText(_translate("MainWindow", "Show/Hide"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.frequency_label.setText(_translate("MainWindow", "Frequency"))
        self.magnitude_label.setText(_translate("MainWindow", "Magnitude"))
        self.phase_label.setText(_translate("MainWindow", "Phase Shift"))
        self.compose_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.compose_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>dsds</p></body></html>"))
        self.compose_button.setText(_translate("MainWindow", "Compose"))
        self.confirm_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.confirm_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>dsds</p></body></html>"))
        self.confirm_button.setText(_translate("MainWindow", "Confirm"))
        self.move_to_main.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.move_to_main.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>dsds</p></body></html>"))
        self.move_to_main.setText(_translate("MainWindow", "Move to main"))
        self.delete_button.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.delete_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>dsds</p></body></html>"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.menubar_2.setTitle(_translate("MainWindow", "File"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_save.setText(_translate("MainWindow", "Save"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
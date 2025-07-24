import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget): #Inheriting from the base class to create our own widgets
    def __init__(self):
        super().__init__() #Initializes the base class
        self.time_label=QLabel(self) #Displays the time
        self.timer=QTimer(self) #Trigger updates for each second
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700,400,500,300) #First two values is where it appears on the screen,
        #Second two values is the base width and base height

        vbox=QVBoxLayout() #Layout manager
        vbox.addWidget(self.time_label) #Adding our label to the layout manager
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:200px; color:yellowgreen")
        self.setStyleSheet("background-color:black")

        #Used to manage and query the fonts
        font_id=QFontDatabase.addApplicationFont("Oldtimer.ttf")
        #Returns a list of font names, and retrives the first element
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]

        my_font = QFont(font_family,150) #Setting the font-family and the font-size
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000) #Every 10000 miliseconds (1 second)

        self.updateTime()

    def updateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") #Get the current time
        self.time_label.setText(current_time) #Update the time

if __name__=="__main__": #Ensures that the block runs only if the script is executed
    app = QApplication(sys.argv) #Create a QApplication object to manage the GUI app
    clock=DigitalClock() #Create an instance of the DigitalClock class and show the window
    clock.show()
    sys.exit(app.exec_()) #The execute method, it starts the main event loop of the application, handles key presses, mouse clicks and etc

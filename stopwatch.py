import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime


class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label =QLabel( "00:00:00",self)
        self.startbutton= QPushButton("Start",self)
        self.stopbutton= QPushButton("Stop",self)
        self.resetbutton= QPushButton("Reset",self)
        self.timer= QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("stopwatch")
        
        vbox= QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.startbutton)
        vbox.addWidget(self.stopbutton)
        vbox.addWidget(self.resetbutton)


        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox= QHBoxLayout()

        hbox.addWidget(self.startbutton)
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)
        vbox.addLayout(hbox)


        self.setStyleSheet("""
            QPushButton, QLabel {
                    padding: 20px;
                    font-weight:bold;
                    font-family: calibri;
                           }
            QPushButton {
                font-size: 50px;
                }
            QLabel {
                font-size: 100px;
                background-color: #00d0ff;
                border-radius: 20px;
                           }
            
                





                            """)
        self.startbutton.clicked.connect(self.start)
        self.stopbutton.clicked.connect(self.stop)
        self.resetbutton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)



    def stop(self):
        self.timer.stop()


    def reset(self):
        self.timer.stop()
        self.time= QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))


    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    


    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))






if __name__ =="__main__":
    app =  QApplication(sys.argv)
    stopwatch = stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

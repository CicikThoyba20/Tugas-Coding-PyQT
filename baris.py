import sys
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    first = 1
    for i in range(10):
        textlb = QLabel(window)
        textlb.setText("Ayam" + str(first))
        textlb.move(200, first*20) 
        first += 1
    window.setGeometry(400,400,400,250)
    window.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    window()

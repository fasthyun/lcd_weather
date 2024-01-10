from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

from PyQt5.QtCore import QTimer


def timeout():
    pass


timer = QTimer()
timer.start(1000)
timer.timeout.connect(timeout)

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()

app.exec()
del app 


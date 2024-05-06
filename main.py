import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QSlider, QLabel, QMainWindow, QAction, QToolBar, QMessageBox
from PyQt5.QtCore import Qt

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ely Bot UI")
        self.setGeometry(100, 100, 300, 80)

        # Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        action = QAction('Bot Einladen', self)
        toolbar.addAction(action)

        # Hauptwidget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        left_layout = QVBoxLayout()
        center_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        layout.addLayout(left_layout)
        layout.addLayout(center_layout)
        layout.addLayout(right_layout)

        # Styles
        self.setStyleSheet(
            "background-color: #333333; color: white; border: 1px solid white; border-radius: 5px;;"
        )

        # Spalte links
        left_label = QLabel("Vorlesungslänge:")
        left_label.setStyleSheet("color: white;")
        left_layout.addWidget(left_label)

        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("border: 1px solid white;")
        self.input_field.setFixedHeight(50)
        left_layout.addWidget(self.input_field)

        left_button_layout = QHBoxLayout()
        left_layout.addLayout(left_button_layout)

        left_button1 = QPushButton("Bot starten")
        left_button1.setStyleSheet("border: 1px solid white;")
        left_button1.clicked.connect(self.button1_clicked)
        left_button2 = QPushButton("Bot beenden")
        left_button2.setStyleSheet("border: 1px solid white;")
        left_button2.clicked.connect(self.button2_clicked)
        left_button_layout.addWidget(left_button1)
        left_button_layout.addWidget(left_button2)

        # Spalte Mitte
        self.slider_label = QLabel("Slider:")
        self.slider_label.setStyleSheet("color: white;")
        center_layout.addWidget(self.slider_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 3)
        self.slider.setStyleSheet("border: 1px solid white;")
        self.slider.setFixedHeight(50)
        self.slider.valueChanged.connect(self.slider_moved)
        center_layout.addWidget(self.slider)

        center_button_layout = QHBoxLayout()
        center_layout.addLayout(center_button_layout)

        center_button1 = QPushButton("Button 3")
        center_button1.setStyleSheet("border: 1px solid white;")
        center_button1.clicked.connect(self.button3_clicked)
        center_button2 = QPushButton("Button 4")
        center_button2.setStyleSheet("border: 1px solid white;")
        center_button2.clicked.connect(self.button4_clicked)
        center_button_layout.addWidget(center_button1)
        center_button_layout.addWidget(center_button2)

        # Spalte rechts
        right_label = QLabel("Buttons:")
        right_label.setStyleSheet("color: white;")
        right_layout.addWidget(right_label)

        button1 = QPushButton("Button 5")
        button1.setStyleSheet("border: 1px solid white;")
        button1.clicked.connect(self.button5_clicked)
        button2 = QPushButton("Button 6")
        button2.setStyleSheet("border: 1px solid white;")
        button2.clicked.connect(self.button6_clicked)
        button3 = QPushButton("Button 7")
        button3.setStyleSheet("border: 1px solid white;")
        button3.clicked.connect(self.button7_clicked)
        button4 = QPushButton("Button 8")
        button4.setStyleSheet("border: 1px solid white;")
        button4.clicked.connect(self.button8_clicked)
        right_layout.addWidget(button1)
        right_layout.addWidget(button2)
        right_layout.addWidget(button3)
        right_layout.addWidget(button4)

    def button1_clicked(self):
        QMessageBox.information(self, "Button 1", "Button 1 wurde geklickt!")

    def button2_clicked(self):
        QMessageBox.information(self, "Button 2", "Button 2 wurde geklickt!")

    def button3_clicked(self):
        QMessageBox.information(self, "Button 3", "Button 3 wurde geklickt!")

    def button4_clicked(self):
        QMessageBox.information(self, "Button 4", "Button 4 wurde geklickt!")

    def button5_clicked(self):
        QMessageBox.information(self, "Button 5", "Button 5 wurde geklickt!")

    def button6_clicked(self):
        QMessageBox.information(self, "Button 6", "Button 6 wurde geklickt!")

    def button7_clicked(self):
        QMessageBox.information(self, "Button 7", "Button 7 wurde geklickt!")

    def button8_clicked(self):
        QMessageBox.information(self, "Button 8", "Button 8 wurde geklickt!")

    def slider_moved(self, value):
        if value == 0:
            self.slider_label.setText("Felipe Spam Stufe 1")
            
        elif value == 1:
            self.slider_label.setText("Felipe Spam Stufe 2")
            
        elif value == 2:
            self.slider_label.setText("Felipe Spam Stufe 3")
    
        elif value == 3:
            self.slider_label.setText("Totaler Spam für alle")
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

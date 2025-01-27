import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QComboBox, QSpinBox, QDoubleSpinBox, 
                             QPushButton, QFileDialog,QSizePolicy)
from PyQt5 .QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt 

# PyQt5.QtWidgets: Modul untuk membuat aplikasi GUI.
# QApplication: Menjalankan aplikasi PyQt.
# QMainWindow: Kelas dasar untuk membuat jendela utama (main window).
# PyQt5.QtGui: Digunakan untuk fitur GUI tambahan, seperti ikon jendela (QIcon).


class MainWindow(QMainWindow):
    #Membuat kelas bernama MainWindow yang mewarisi fungsi-fungsi dari QMainWindow.
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Surya bEjir") # nama tittle aplikasi
        self.setGeometry(700,300,500,500) #(x,y,panjang, lebar) untuk mengatur ukuran jendela
        self.setWindowIcon(QIcon("profile.jpeg")) # import gambar
        self.initUI()
        # self.button()
        
        #LABEL
        # label = QLabel("Hello World", self) # membuat label
        # label.setFont(QFont("Times New Roman", 30))
        # label.setGeometry(20,20, 500,200) # posisi label (x,y,panjang,lebar)
        # label.setStyleSheet("color: #A6AEBF;"
        #                  "background-color: #D0E8C5;"
        #                  "padding-left: 10;"
        #                  "padding-top: 10;"
        #                  )
        
        # urutan posisi
        # label.setAlignment(Qt.AlignLeft)                                                  #1
        # label.setAlignment(Qt.AlignTop)                                                   #1
        # label.setAlignment(Qt.AlignHCenter) # Horizontal                                  #2
        # label.setAlignment(Qt.AlignRight)                                                 #3
        # label.setAlignment(Qt.AlignVCenter) # Vertikal                                    #4
        # label.setAlignment(Qt.AlignCenter)                                                #5
        # label.setAlignment(Qt.AlignRight | Qt.AlignCenter)                                #6
        # label.setAlignment(Qt.AlignBottom)                                                #7
        # label.setAlignment(Qt.AlignBottom | Qt.AlignCenter) # Vertikal dan Horizontal     #8
        # label.setAlignment(Qt.AlignBottom | Qt.AlignRight) # Vertikal dan Horizontal      #9
        
        # GAMBAR
        # label2 = QLabel(self)
        # label2.setGeometry (0,0,300,200)
        # gambar = QPixmap("profile.jpeg")
        # label2.setPixmap(gambar)
        # label2.setScaledContents(True)
        # # label2.setAlignment(Qt.AlignCenter)  
        # label2.setGeometry(Qt.AlignCenter,
        #                    Qt.AlignCenter,
        #                    label2.width(),
        #                    label2.height()
        #                    )
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("1",self)
        label2 = QLabel("2",self)
        label3 = QLabel("3",self)
        label4 = QLabel("4",self)
        self.button1 = QPushButton("Click!",self)
        label6 = QLabel("6",self)
        label7 = QLabel("7",self)
        label8 = QLabel("8",self)
        label9 = QLabel("9",self)
        
        for widget in [label1, label2, label3, label4, label6, label7, label8, label9]:
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Semua elemen expandable
            widget.setAlignment(Qt.AlignCenter)  # Konten di tengah (hanya QLabel)

        # Untuk QPushButton, gunakan stylesheet untuk menyesuaikan teks di tengah
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button1.setStyleSheet("background-color: #3C3D37; color: white; font-size: 16px; padding: 10px;")
        
        
        label1.setStyleSheet("background-color: #FEF9E1;")
        label2.setStyleSheet("background-color: #E5D0AC;")
        label3.setStyleSheet("background-color: #A31D1D;")
        label4.setStyleSheet("background-color: #6D2323;")
        self.button1.setStyleSheet("background-color: #3C3D37;") 
        label6.setStyleSheet("background-color: #E17564;")
        label7.setStyleSheet("background-color: #BE3144;")
        label8.setStyleSheet("background-color: #872341;")
        label9.setStyleSheet("background-color: #09122C;")
        
        grid = QGridLayout()
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,0,2)
        grid.addWidget(label4,1,0)
        grid.addWidget(self.button1,1,1)
        grid.addWidget(label6,1,2)
        grid.addWidget(label7,2,0)
        grid.addWidget(label8,2,1)
        grid.addWidget(label9,2,2)
        
        self.button1.setText("Utama")
        self.button1.clicked.connect(self.on_click)
        
        central_widget.setLayout(grid)
        pass
    
    # def button(self):
    #     self.button = QPushButton ("Click Here!", self)
    #     self.button.setGeometry(150,200,200,100)
    #     self.button.setStyleSheet("background-color: #3C3D37;"
    #                          "font-size:30px;")
    #     self.button.clicked.connect(self.on_click)
        
    def on_click(self):
        print("Button di klik!")
        self.button1.setText("Luar")
        self.button1.clicked.connect(self.initUI)
        self.button1.setStyleSheet("background-color ;#ECDFCC;")
        
        
def main():
    app = QApplication(sys.argv)
    # Membuat objek aplikasi. sys.argv digunakan untuk membaca argumen dari command-line jika ada.
    window = MainWindow() # Membuat objek MainWindow, yaitu jendela utama.
    window.show() # Menampilkan jendela utama ke layar.
    sys.exit(app.exec_()) # Menjalankan event loop aplikasi.
    # Event loop adalah mekanisme yang terus berjalan hingga aplikasi ditutup, untuk menangani interaksi pengguna.
    
if __name__ == "__main__":
    main()






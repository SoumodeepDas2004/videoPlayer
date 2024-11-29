from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
QSlider, QFileDialog,QStackedWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon,QLinearGradient,QPalette,QBrush
from PyQt5.QtCore import Qt, QUrl
import sys
from PyQt5 import QtWidgets
class Startwindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties such as title, size, and icon
        self.setWindowTitle("DesApps -  Media Player-StartAPP")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('vo.png'))
        self.setStyleSheet(" QWidget{ background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgba(250,10,150,100), stop: 1 rgba(10,30,250,30) );}")
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, Qt.red)
        gradient.setColorAt(1.0, Qt.blue)

        # Set the gradient as the background brush
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)
        
        # Initialize the user interface
        self.show()
        #elements
        self.labelWel = QLabel("Welcome to DesApps - Media Player\n Click the Button to launch the Applicatiion", self)
        self.labelWel.move(100, 100)
        self.labelWel.setStyleSheet("QLabel {qproperty-alignment: AlignCenter;color: white; font-size: 20px; font-family: Areal; }")
        self.startbutton = QPushButton("Launch Application", self)
        buttonstyle="QPushButton {background-color: rgba(18, 191, 218, 0.83); border: 1px solid #707070; border-radius: 5px; padding: 5px; font-weight:bold;}QPushButton:hover{ background-color: rgba(18, 248, 165, 0.83); border: 1px solid }"
        self.startbutton.setStyleSheet(buttonstyle)
        #buttonfunctionality          
        def runApp():
            
            # Create the main window instance
            windows=Window()
            widget.addWidget(windows)
            # Show the main window
            widget.setCurrentIndex(widget.currentIndex()+1)
            

        
        self.startbutton.clicked.connect(runApp)
        
        mlayout=QVBoxLayout()
        r1=QHBoxLayout()
        r1.addWidget(self.labelWel)
        r2=QHBoxLayout()
        r2.addWidget(self.startbutton)
        
        mlayout.addLayout(r1)
        mlayout.addLayout(r2)
        self.setLayout(mlayout)
        





class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties such as title, size, and icon
        self.setWindowTitle("DesApps -  Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('vo.png'))
        self.setStyleSheet(" QWidget{ background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgba(250,10,150,100), stop: 1 rgba(10,30,250,30) );}")
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, Qt.red)
        gradient.setColorAt(1.0, Qt.blue)

        # Set the gradient as the background brush
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)
        
        # Initialize the user interface
        
        self.init_ui()
        self.show()

    def init_ui(self):
        # Initialize media player and video widget
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
    

        # Create buttons for controlling media playback
        openBtn = QPushButton('Open Video')
        openBtn.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color: #e0e0e0; }"
        )
        openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton('Play')
        self.playBtn.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color:orange; }"
        )
        self.playBtn.setEnabled(False)
        self.playBtn.clicked.connect(self.play_video)

        self.pauseBtn = QPushButton('Pause')
        self.pauseBtn.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color:orange; }"
        )
        self.pauseBtn.setEnabled(False)
        self.pauseBtn.clicked.connect(self.pause_video)

        self.stopBtn = QPushButton('Stop')
        self.stopBtn.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color:rgba(0, 255, 49, 0.83); }"
        )
        self.stopBtn.setEnabled(False)
        self.stopBtn.clicked.connect(self.stop_video)
        self.postext=QLabel("Video time:")
        self.postext.setStyleSheet( "QLabel { background-color: rgba(18, 191, 218, 0.83); border: 1px solid #707070; border-radius: 5px; padding: 5px;}" )

        # Create sliders for seeking within the video and adjusting volume
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setStyleSheet(
            "QSlider::groove:horizontal { height: 6px; background: #f0f0f0; border: 1px solid #707070; border-radius: 3px; }"
            "QSlider::handle:horizontal { background: red; border: 1px solid #0056b3; width: 14px; margin: -5px 0px; border-radius: 7px; }"
            "QSlider::add-page:horizontal { background: white; }"
            "QSlider::sub-page:horizontal { background: lightgreen; }"
        )
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.set_position)
        self.voltext=QLabel("Volume:")
        self.voltext.setStyleSheet( "QLabel { background-color: rgba(18, 191, 218, 0.83); border: 1px solid #707070; border-radius: 5px; padding: 5px;}" )
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setStyleSheet(
            "QSlider::groove:horizontal { height: 6px; background: #f0f0f0; border: 1px solid #707070; border-radius: 3px; }"
            "QSlider::handle:horizontal { background: red; border: 1px solid #0056b3; width: 14px; margin: -5px 0px; border-radius: 7px; }"
            "QSlider::add-page:horizontal { background: white; }"
            "QSlider::sub-page:horizontal { background:rgba(0, 255, 49, 0.83); }"
        )
        self.volumeSlider.setValue(100)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setToolTip("Volume")
        self.volumeSlider.valueChanged.connect(self.change_volume)

        # Create layout for arranging widgets horizontally
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.pauseBtn)
        hboxLayout.addWidget(self.stopBtn)
        hboxLayout.addWidget(self.postext)
        hboxLayout.addWidget(self.positionSlider)
        hboxLayout.addWidget(self.voltext)
        hboxLayout.addWidget(self.volumeSlider)

        # Create layout for arranging widgets vertically
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)

        # Set the layout of the window
        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)

        # Connect media player signals to their respective slots
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        # Open file dialog to select a video file
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            # Set the selected video file to the media player
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            # Enable playback control buttons
            self.playBtn.setEnabled(True)
            self.pauseBtn.setEnabled(True)
            self.stopBtn.setEnabled(True)

    def play_video(self):
        # Start playback
        self.mediaPlayer.play()

    def pause_video(self):
        # Pause playback
        self.mediaPlayer.pause()

    def stop_video(self):
        # Stop playback
        self.mediaPlayer.stop()

    def mediastate_changed(self, state):
        # Update button states based on media player state
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setEnabled(False)
            self.pauseBtn.setEnabled(True)
            self.stopBtn.setEnabled(True)
        else:
            self.playBtn.setEnabled(True)
            self.pauseBtn.setEnabled(False)
            self.stopBtn.setEnabled(False)

    def position_changed(self, position):
        # Update slider position based on current playback position
        self.positionSlider.setValue(position)

    def duration_changed(self, duration):
        # Set slider range based on total duration of the video
        self.positionSlider.setRange(0, duration)

    def set_position(self, position):
        # Set playback position based on slider value
        self.mediaPlayer.setPosition(position)

    def change_volume(self, volume):
        # Change media player volume based on slider value
        self.mediaPlayer.setVolume(volume)



apps = QApplication([])


widget=QtWidgets.QStackedWidget()
widget.setWindowTitle("DesApps -  Media Player")
widget.setGeometry(350, 100, 700, 500)
widget.setWindowIcon(QIcon('video.png'))
widget.setStyleSheet(" QWidget{ background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgba(250,10,150,100), stop: 1 rgba(10,30,250,30) );}")
gradient = QLinearGradient(0, 0, widget.width(), widget.height())
gradient.setColorAt(0.0, Qt.red)
gradient.setColorAt(1.0, Qt.blue)

        # Set the gradient as the background brush
widget.setAutoFillBackground(True)
palette = widget.palette()
palette.setBrush(QPalette.Window, QBrush(gradient))
widget.setPalette(palette)
        
        # Initialize the user interface
        

widget.show()
mwin=Startwindow()
widget.addWidget(mwin)

widget.show()
# Run the application event loop
sys.exit(apps.exec_())

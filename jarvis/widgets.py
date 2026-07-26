from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PySide6.QtGui import QPainter, QColor, QPen


class StatusCard(QFrame):

    def __init__(self, title):

        super().__init__()

        self.setFixedSize(220, 140)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Segoe UI", 11, QFont.Bold))

        self.value = QLabel("--")
        self.value.setAlignment(Qt.AlignCenter)
        self.value.setFont(QFont("Segoe UI", 24, QFont.Bold))

        layout.addStretch()
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        layout.addStretch()

        self.setStyleSheet("""
        QFrame{
            background-color:#161b22;
            border:2px solid #00e5ff;
            border-radius:15px;
        }

        QLabel{
            color:#00e5ff;
            background:transparent;
            border:none;
        }
        """)

    def set_value(self, value):
        self.value.setText(value)

class AICore(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(320, 320)
        self.outer_radius = 240
        self.growing = True
         # ADD THESE 4 LINES HERE
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def animate(self):

        if self.growing:
            self.outer_radius += 1

            if self.outer_radius >= 250:
                self.growing = False

        else:
            self.outer_radius -= 1

            if self.outer_radius <= 230:
                self.growing = True

        self.update()    

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

            # Outer Ring
        pen = QPen(QColor("#00e5ff"))
        pen.setWidth(4)

        painter.setPen(pen)
        radius = self.outer_radius

        offset = (320 - radius) // 2

        painter.drawEllipse(offset, offset, radius, radius)

        # Middle Ring
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawEllipse(70, 70, 180, 180)

        # Inner Ring
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawEllipse(105, 105, 110, 110)
        painter.setBrush(QColor("#00e5ff"))
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(145, 145, 30, 30) 
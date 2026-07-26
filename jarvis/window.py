from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtGui import QFont
from system_monitor import SystemMonitor
from widgets import StatusCard, AICore
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)
from constant import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    BACKGROUND_COLOR,
    TEXT_COLOR,
    TITLE_FONT,
    CLOCK_FONT,
    DEFAULT_STATUS,
    FOOTER_STATUS,
    CLOCK_UPDATE_TIME,
)


class JarvisWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        # ---------------- TOP ----------------
        top_layout = QHBoxLayout()

        # ---------------- MIDDLE ----------------
        middle_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        center_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        middle_layout.addLayout(left_layout, 1)
        middle_layout.addLayout(center_layout, 2)
        middle_layout.addLayout(right_layout, 1)

        # ---------------- BOTTOM ----------------
        bottom_layout = QHBoxLayout()

        main_layout.addLayout(top_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(bottom_layout)
        self.cpu = StatusCard("CPU")
        self.ram = StatusCard("RAM")
        self.battery = StatusCard("Battery")

        left_layout.addWidget(self.cpu)
        left_layout.addWidget(self.ram)
        left_layout.addWidget(self.battery)
        left_layout.addStretch()

        self.title = QLabel("JARVIS")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont(TITLE_FONT, 30, QFont.Bold))

        self.status = QLabel(DEFAULT_STATUS)
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setFont(QFont(TITLE_FONT, 14))

        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignCenter)
        self.clock.setFont(QFont(CLOCK_FONT, 18))

        self.ai_core = AICore()

        self.recognized_text = QLabel("You Said:\n...")
        self.recognized_text.setAlignment(Qt.AlignCenter)
        self.recognized_text.setFont(QFont(TITLE_FONT, 16))

        self.jarvis_action = QLabel("JARVIS:\nReady")
        self.jarvis_action.setAlignment(Qt.AlignCenter)
        self.jarvis_action.setFont(QFont(TITLE_FONT, 16))

        center_layout.addWidget(self.title)
        center_layout.addWidget(self.ai_core, alignment=Qt.AlignCenter)
        center_layout.addWidget(self.status)
        center_layout.addWidget(self.clock)
        center_layout.addWidget(self.recognized_text)
        center_layout.addWidget(self.jarvis_action)

        bottom_layout.addStretch()

        footer = QLabel(FOOTER_STATUS)
        footer.setFont(QFont(TITLE_FONT, 10))

        bottom_layout.addWidget(footer) 


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(CLOCK_UPDATE_TIME)

        self.update_time()

        self.setStyleSheet(f"""
            QMainWindow{{
                background-color:{BACKGROUND_COLOR};
            }}

            QLabel{{
                color:{TEXT_COLOR};
            }}
        """)

    def update_time(self):
        self.clock.setText(QTime.currentTime().toString("hh:mm:ss"))
        self.cpu.set_value(f"{SystemMonitor.cpu()}%")
        self.ram.set_value(f"{SystemMonitor.ram()}%")
        self.battery.set_value(f"{SystemMonitor.battery()}%")

    def set_status(self, text):
        self.status.setText(text) 

    def wake_word_detected(self):
        self.set_status("WAKE WORD DETECTED")     

    def set_recognized_text(self, text):
        self.recognized_text.setText(f"You Said:\n{text}")  

    def set_action(self, text):
        self.jarvis_action.setText(f"JARVIS:\n{text}")        
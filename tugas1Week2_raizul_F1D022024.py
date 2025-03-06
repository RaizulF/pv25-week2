import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from qt_material import apply_stylesheet

class Layout:
    def identitas(label):
        idLabel = QLabel(label)
        idLabel.setStyleSheet("font-size: 14px; color: #000; font-weight: bold;")
        return idLabel

    def vertical_layout():
        groupVBox = QGroupBox("Identitas (Vertical box layout)")
        v_layout = QVBoxLayout()
        v_layout.addWidget(Layout.identitas("Nama  : Raizul Furkon"))
        v_layout.addWidget(Layout.identitas("NIM   : F1D022024"))
        v_layout.addWidget(Layout.identitas("Kelas : Pemrograman Visual C"))
        groupVBox.setLayout(v_layout)
        return groupVBox    

    def horizontal_layout():
        groupHBox = QGroupBox("Navigation (Horizontal box layout)")
        h_layout = QHBoxLayout()
        h_layout.addWidget(QPushButton("Home"))
        h_layout.addWidget(QPushButton("About"))
        h_layout.addWidget(QPushButton("Contact"))
        groupHBox.setLayout(h_layout)
        return groupHBox

    def form_layout():
        groupForm = QGroupBox("User Registration (Form layout)")  
        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Full Name:"),QLineEdit())
        form_layout.addRow(QLabel("Email:"),QLineEdit())
        form_layout.addRow(QLabel("Phone:"),QLineEdit())

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(QRadioButton("Male"))
        radio_layout.addWidget(QRadioButton("Female"))
        form_layout.addRow(QLabel("Gender:"),radio_layout)

        form_layout.addRow(QLabel("Country:"),QComboBox())
        wrap_layout = QHBoxLayout()
        wrap_layout.addStretch()  
        wrap_layout.addLayout(form_layout)  
        wrap_layout.addStretch()
        groupForm.setLayout(wrap_layout)
        return groupForm

    def action():
        groupAction = QGroupBox("Action (Horizontal box layout)")
        action_Hlayout = QHBoxLayout()
        pushButton_succes = QPushButton("Succes")
        pushButton_cancel = QPushButton("Cancel")

        pushButton_succes.setProperty('class', 'success')
        pushButton_cancel.setProperty('class', 'danger')

        action_Hlayout.addWidget(pushButton_succes)
        action_Hlayout.addWidget(pushButton_cancel)

        groupAction.setLayout(action_Hlayout)
        return groupAction
    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WEEK 2 : Layout - User Registration Form")
        self.setFixedSize(500,700)
        layout = Layout
        layout_utama = QVBoxLayout()
        layout_utama.setAlignment(Qt.AlignTop)
        layout_utama.setSpacing(10)
        layout_utama.addWidget(layout.vertical_layout())
        layout_utama.addWidget(layout.horizontal_layout())
        layout_utama.addWidget(layout.form_layout())
        layout_utama.addWidget(layout.action())
        self.setLayout(layout_utama)


extra = {
    'danger': '#dc3545',
    'success': '#4CAF50',
}
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_cyan_500.xml', invert_secondary=True, extra=extra)
    window = Window()
    window.show()
    sys.exit(app.exec_())

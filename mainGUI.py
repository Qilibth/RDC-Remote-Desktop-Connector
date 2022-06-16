import PyQt5.QtWidgets as Qtw
from PyQt5.QtGui import QIcon
import os
from mainBackend import backendClass

# INITIALIZE MAIN WINDOW
class mainWindow(Qtw.QMainWindow):
	def __init__(self):
		super().__init__()

		# INITIALIZING BACKEND
		self.backend = backendClass()

		if self.backend.userState:
			pass
		else:
			os._exit(0)

		# WINDOW SETTINGS
		self.setWindowTitle('Remote Desktop Controller')
		self.setFixedSize(1000, 500)
		self.setStyleSheet('background-color: #3c3c3c')
		self.setWindowIcon(QIcon('Images/roundLogo.ico'))

		# MAIN GRID 
		self.mainGridUpLabel = Qtw.QLabel(' ', self)
		self.mainGridUpLabel.setStyleSheet('background-color : #565656; border-radius: 26px;')
		self.mainGridUpLabel.setGeometry(20, 30, 961, 260)

		self.mainGridDownLabel = Qtw.QLabel('', self)
		self.mainGridDownLabel.setStyleSheet('background-color : #565656; border-radius: 26px')
		self.mainGridDownLabel.setGeometry(20, 310, 961, 161)

		self.labelStyleSheet = """QLabel{
									background-color : none;
									font : 13pt "Questrial" ;
									color : white;
								}"""

		self.connectionStatusLabel = Qtw.QLabel(f'Connection Status : {""}', self)
		self.connectionStatusLabel.setStyleSheet(self.labelStyleSheet)
		self.connectionStatusLabel.setGeometry(50, 320, 261, 31)

		# USER CONTROLL AREA
		self.SHPwBtnStyleSheet = """QPushButton{
								background-image: url(Images/main/show2.png);
								border-radius: 15px;
								border: 1px  solid;
								border-color: white;
								background-color: #3c3c3c;
								font: 15pt "Questrial";
								color : white
								}

								QPushButton::hover
								{
									background-color : white;
									background-image: url(Images/main/show1.png);
								}
								"""

		self.userIdLabel = Qtw.QLabel('', self)
		self.userIdLabel.setGeometry(80, 80, 291, 41)
		self.userIdLabel.setStyleSheet('border-radius: 15px;')

		self.userIdNameLabel = Qtw.QLabel('', self)
		self.userIdNameLabel.setGeometry(90, 50, 261, 31)
		self.userIdNameLabel.setText('Your ID')
		self.userIdNameLabel.setStyleSheet(self.labelStyleSheet)

		self.userPwLabel = Qtw.QLabel('', self)
		self.userPwLabel.setGeometry(80, 160, 291, 41)
		self.userPwLabel.setStyleSheet('border-radius: 15px;')

		self.userPwNameLabel = Qtw.QLabel('', self)
		self.userPwNameLabel.setGeometry(90, 130, 261, 31)
		self.userPwNameLabel.setText('Your Password')
		self.userPwNameLabel.setStyleSheet(self.labelStyleSheet)

		self.userSHPwButton = Qtw.QPushButton('', self)
		self.userSHPwButton.setGeometry(390, 160, 41, 41)
		self.userSHPwButton.setStyleSheet(self.SHPwBtnStyleSheet)
		self.userSHPwButton.clicked.connect(self.btnClicked)


		# HOST CONTROLL AREA
		self.connectButtonStyleSheet = """QPushButton{
								border-radius: 15px;
								border: 1px  solid;
								border-color: white;
								background-color: #3c3c3c;
								font: 15pt "Questrial";
								color : white
								}

								QPushButton::hover
								{
								color : black;
								background-color : white;
								}"""

		self.lineEditStyleSheet = """QLineEdit{
								border-radius: 15px;
								border: 1px solid;
								border-color: white;
								color : white;
								font: 15pt "Questrial";
								}
								"""

		self.hostIdLineEdit = Qtw.QLineEdit('    ', self)
		self.hostIdLineEdit.setGeometry(520, 80, 291, 41)
		self.hostIdLineEdit.setStyleSheet(self.lineEditStyleSheet)

		self.hostPwNameLabel = Qtw.QLabel('', self)
		self.hostPwNameLabel.setGeometry(530, 50, 261, 31)
		self.hostPwNameLabel.setText('Host ID')
		self.hostPwNameLabel.setStyleSheet(self.labelStyleSheet)

		self.hostPwLineEdit = Qtw.QLineEdit('    ', self)
		self.hostPwLineEdit.setGeometry(520, 160, 291, 41)
		self.hostPwLineEdit.setStyleSheet(self.lineEditStyleSheet)

		self.userPwNameLabel = Qtw.QLabel('', self)
		self.userPwNameLabel.setGeometry(530, 130, 261, 31)
		self.userPwNameLabel.setText('Host Password')
		self.userPwNameLabel.setStyleSheet(self.labelStyleSheet)

		self.connectButton = Qtw.QPushButton('Connect', self)
		self.connectButton.setGeometry(590, 225, 161, 41)
		self.connectButton.setStyleSheet(self.connectButtonStyleSheet)

		self.hostSHPwButton = Qtw.QPushButton('', self)
		self.hostSHPwButton.setGeometry(830, 160, 41, 41)
		self.hostSHPwButton.setStyleSheet(self.SHPwBtnStyleSheet)



	def btnClicked(self):
		pass


application = Qtw.QApplication([])

# MAIN LOOP
window = mainWindow()
window.show()

os._exit(application.exec())
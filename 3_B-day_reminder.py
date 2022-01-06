
from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import datetime


class OsobaForm(QtWidgets.QWidget):

	def __init__(self, **kwargs):
		super(OsobaForm, self).__init__(**kwargs)
		pass

	def setup(self):
		pass



class PrehledForm(QtWidgets.QMainWindow):

	def __init(self, **kwargs):
		super(PrehledForm, self).__init__(**kwargs)
		
		# Title, icon and min window width
		self.setWindowTitle("Anniversery")
		self.setWindowIcon(QtGui.QIcon("3_anni_icon.png"))
		self.setMinimumWidth(650)

		formular = QtWidgets.QWidget()
		layoutFormulare = QtWidgets.QVBoxLayout()
		formular.setLayout(layoutFormulare)
		self.setCentralWidget(formular)

		# Information box with layout
		self.dnesLayout = QtWidgets.QHBoxLayout()
		layoutFormulare.addLayout(self.dnesLayout)
		self.dnesLayout.addWidget(QtWidgets.QLabel("Today is:"))
		self.dnesLayout.addStretch()
		self.dnesLabel = QtWidgets.QLabel(self.get_current_date())
		self.dnesLayout.addWidget(self.dnesLabel)

		# Information box with BoxLayout (nearest B-day)
		self.narozeninyLayout = QtWidgets.QHBoxLayout()
		layoutFormulare.addLayout(self.narozeninyLayout)
		self.narozeninyLayout.addWidget(QtWidgets.QLabel("Nearest B-day:"))
		self.narozeninyLayout.addStretch()
		self.nejblizsiLabel = QtWidgets.QLabel("")
		self.narozeninyLayout.addWidget(self.nejblizsiLabel)

		# Share layout for osobyListBox and narozenMonthCalendar
		self.prostredniLayout = QtWidgets.QHBoxLayout()
		layoutFormulare.addLayout(self.prostredniLayout)

		# Layout for osobyListBox
		self.jmenaLayout = QtWidgets.QHBoxLayout()
		self.osobyListBox = QtWidgets.QListWidget()
		self.jmenaLayout.addWidget(self.osobyListBox)
		self.prostredniLayout.addLayout(self.jmenaLayout)

		# narozenMonthCalendar layout
		self.kalendarLayout = QtWidgets.QHBoxLayout()
		self.osobyListBox = QtWidgets.QListWidget()
		self.jmenaLayout.addWidget(self.osobyListBox)
		self.prostredniLayout.addLayout(self.jmenaLayout)

		self.kalendarLayout = QtWidgets.QVBoxLayout()
		self.narozenMonthCalendar = QtWidgets.QCalendarWidget(self)
		self.narozenMonthCalendar.setEnabled(False)

		# Vytvoříme layout pro informace o osobách
		self.osobaLayout = QtWidgets.QHBoxLayout()
		self.osobaLayout.addWidget(QtWidgets.QLabel("Narozen:"))
		self.osobaLayout.addStretch()
		self.narozeninyLabel = QtWidgets.QLabel("")
		self.osobaLayout.addWidget(self.narozeninyLabel)
		self.kalendarLayout.addLayout(self.osobaLayout)
		self.osobaLayout2 = QtWidgets.QHBoxLayout()
		self.osobaLayout2.addWidget(QtWidgets.QLabel("Věk:"))
		self.osobaLayout2.addStretch()
		self.vekLabel = QtWidgets.QLabel("")
		self.osobaLayout2.addWidget(self.vekLabel)

		self.kalendarLayout.addLayout(self.osobaLayout2)
		self.kalendarLayout.addWidget(self.narozenMonthCalendar)
		self.prostredniLayout.addLayout(self.kalendarLayout)


		self.show()

	def get_current_date(self):
		return(str(datetime.datetime.now().day) + "." + str(datetime.datetime.now().month) + "." + str(datetime.datetime.now().year))

	def setup(self):
		self.osoba_form = root.osoba_form


class App(QtWidgets.QApplication):

	def __init(self):
		super(App, self).__init__(sys.argv)

	def build(self):
		self.prehled_form = PrehledForm()
		self.osoba_form = OsobaForm()

		self.prehled_form.setup()
		self.osoba_form.setup()
		sys.exit(self.exec_())



root = App()
root.build()

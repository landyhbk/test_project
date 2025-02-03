import sys, time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QTextBrowser, QComboBox, QListWidget, QProgressBar, QMessageBox, QDialogButtonBox
from PyQt5 import uic
from datetime import datetime
import json 


TIME_LIMIT = 100

def load_json(file_path="testjson.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: JSON file is invalid.")
        return {}

class My_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("firstGUIdraft.ui", self)
        self.show()

        
        self.pushButtonAUS = self.findChild(QtWidgets.QPushButton, "pushButtonAUS")
        self.pushButtonUSA = self.findChild(QtWidgets.QPushButton, "pushButtonUSA")
        self.pushButtonUK = self.findChild(QtWidgets.QPushButton, "pushButtonUK")
        self.pushButtonSA = self.findChild(QtWidgets.QPushButton, "pushButtonSA")
        self.pushButtonNZL = self.findChild(QtWidgets.QPushButton, "pushButtonNZL")
        self.pushButtonFRA = self.findChild(QtWidgets.QPushButton, "pushButtonFRA")
        self.pushButtonARG = self.findChild(QtWidgets.QPushButton, "pushButtonARG")
        self.pushButtonITA = self.findChild(QtWidgets.QPushButton, "pushButtonITA")

        self.pushButtonAUS.clicked.connect(self.open_australia_window)
        self.pushButtonUSA.clicked.connect(self.open_usa_window)
        self.pushButtonUK.clicked.connect(self.open_uk_window)
        self.pushButtonSA.clicked.connect(self.open_southafrica_window)
        self.pushButtonNZL.clicked.connect(self.open_newzealand_window)
        self.pushButtonFRA.clicked.connect(self.open_france_window)
        self.pushButtonARG.clicked.connect(self.open_argentina_window)
        self.pushButtonITA.clicked.connect(self.open_italy_window)

    def open_australia_window(self):
        self.australia_window = AustraliaWindow()
        self.australia_window.show()

    def open_usa_window(self):
        self.usa_window = USAWindow()
        self.usa_window.show()

    def open_uk_window(self):
        self.uk_window = UKWindow()
        self.uk_window.show()

    def open_southafrica_window(self):
        self.sa_window = SAWindow()
        self.sa_window.show()

    def open_newzealand_window(self):
        self.nzl_window = NZLWindow()
        self.nzl_window.show()

    def open_france_window(self):
        self.fra_window = FRAWindow()
        self.fra_window.show()

    def open_argentina_window(self):
        self.arg_window = ARGWindow()
        self.arg_window.show()

    def open_italy_window(self):
        self.ita_window = ITAWindow()
        self.ita_window.show()


class AustraliaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("australia_nodeclick.ui", self)
        self.show()

       
        self.data = load_json()

        
        self.pushButtonAUSTEAMS.clicked.connect(self.show_teams)
        self.pushButtonAUSSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonAUSFIX.clicked.connect(self.show_fixtures)
        self.pushButtonAUSTROPHIES.clicked.connect(self.show_trophies)

    

    def show_teams(self):
        teams = self.data["Australia"]["Teams"]
        team_info = "\n\n".join(teams)

        # Create a custom QMessageBox
        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  # Set the heading - this is not working try to ammend later
        msg.setText(team_info)       # Set the main content
        msg.setIcon(QMessageBox.NoIcon)  # Remove the default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

    def show_stadiums(self):
        stadiums = self.data["Australia"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        # Create a custom QMessageBox
        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()
        
       
    def show_fixtures(self):
        fixtures = self.data["Australia"]["Fixtures"]
        fixture_info = "\n\n".join(
            [f"{fixture['date']} vs {fixture['opponent']} at {fixture['venue']} - Result: {fixture['result']}" for fixture in fixtures]
        )
        
        msg = QMessageBox(self)
        msg.setWindowTitle("Fixtures")
        msg.setText(fixture_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_trophies(self):
        trophies = self.data["Australia"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Fixtures")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


class USAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("america_nodeclick.ui", self)
        self.show()



class UKWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UKpopout.ui", self)
        self.show()

        
        self.pushButtonENG = self.findChild(QtWidgets.QPushButton, "pushButtonENG")
        self.pushButtonENG.clicked.connect(self.open_england_window)
        self.pushButtonSCO = self.findChild(QtWidgets.QPushButton, "pushButtonSCO")
        self.pushButtonSCO.clicked.connect(self.open_scotland_window)
        self.pushButtonWAL = self.findChild(QtWidgets.QPushButton, "pushButtonWAL")
        self.pushButtonWAL.clicked.connect(self.open_wales_window)
        self.pushButtonIRE = self.findChild(QtWidgets.QPushButton, "pushButtonIRE")
        self.pushButtonIRE.clicked.connect(self.open_ireland_window)


    def open_england_window(self):
        self.england_window = EnglandWindow()
        self.england_window.show()

    def open_scotland_window(self):
        self.scotland_window = ScotlandWindow()
        self.scotland_window.show()

    def open_wales_window(self):
        self.wales_window = WalesWindow()
        self.wales_window.show()

    def open_ireland_window(self):
        self.wales_window = IrelandWindow()
        self.wales_window.show()


class EnglandWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("england_nodeclick.ui", self)
        self.show()

        self.data = load_json()

        
        self.pushButtonENGTEAMS.clicked.connect(self.show_teams)
        self.pushButtonENGSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonENGFIX.clicked.connect(self.show_fixtures)
        self.pushButtonENGTROPHIES.clicked.connect(self.show_trophies)

    def show_teams(self):
        teams = self.data["England"]["Teams"]
        QMessageBox.information(self, "Teams", "\n\n".join(teams))

    def show_stadiums(self):
        stadiums = self.data["England"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )
        QMessageBox.information(self, "Stadiums", stadium_info)

    def show_fixtures(self):
        fixtures = self.data["England"]["Fixtures"]
        fixture_info = "\n\n".join(
            [f"{fixture['date']} vs {fixture['opponent']} at {fixture['venue']} - Result: {fixture['result']}" for fixture in fixtures]
        )
        QMessageBox.information(self, "Fixtures", fixture_info)

    def show_trophies(self):
        trophies = self.data["England"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )
        QMessageBox.information(self, "Trophies", trophy_info)

class ScotlandWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("scotland_nodeclick.ui",self)
        self.show()

class WalesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("wales_nodeclick.ui",self)
        self.show()

class IrelandWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ireland_nodeclick.ui",self)
        self.show()

class SAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("southafrica_nodeclick.ui", self)
        self.show()

class NZLWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("newzealand_nodeclick.ui", self)
        self.show()

class FRAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("france_nodeclick.ui", self)

class ARGWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("argentina_nodeclick.ui")

class ITAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("italy_nodeclick.ui")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_UI()
    sys.exit(app.exec_())



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

        #
        self.pushButtonAUS = self.findChild(QtWidgets.QPushButton, "pushButtonAUS")
        self.pushButtonUSA = self.findChild(QtWidgets.QPushButton, "pushButtonUSA")
        self.pushButtonUK = self.findChild(QtWidgets.QPushButton, "pushButtonUK")

        self.pushButtonAUS.clicked.connect(self.open_australia_window)
        self.pushButtonUSA.clicked.connect(self.open_usa_window)
        self.pushButtonUK.clicked.connect(self.open_uk_window)

    def open_australia_window(self):
        self.australia_window = AustraliaWindow()
        self.australia_window.show()

    def open_usa_window(self):
        self.usa_window = USAWindow()
        self.usa_window.show()

    def open_uk_window(self):
        self.uk_window = UKWindow()
        self.uk_window.show()



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
        msg.setWindowTitle("Teams")  # Set the heading
        msg.setText(team_info)       # Set the main content
        msg.setIcon(QMessageBox.NoIcon)  # Remove the default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add OK button
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

    def open_england_window(self):
        self.england_window = EnglandWindow()
        self.england_window.show()

    def open_scotland_window(self):
        self.scotland_window = ScotlandWindow()
        self.scotland_window.show()



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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_UI()
    sys.exit(app.exec_())


'''
class My_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("firstGUIdraft.ui",self)
        self.show()

class AustraliaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("australia_nodeclick.ui",self)
        self.show()

class USAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("america_nodeclick.ui",self)
        self.show()

class UKWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UKpopout_nodeclick.ui",self)
        self.show()
        self.pushButtonENG = self.findChild(QtWidgets.QPushButton, "pushButtonENG")
        self.pushButtonENG.clicked.connect(self.pushButtonUKclicked)

    
    def open_england_window():
        def pushButtonENGclicked(self):
            uic.loadUi("england_nodeclick.ui")
            self.show()
        
'''


'''
class My_UI(QMainWindow):

    def __init__(self):

        super(My_UI,self).__init__() # call constrcutor of parent class
        
        uic.loadUi("firstGUIdraft.ui",self)
        
        self.pushButtonAUS = self.findChild(QPushButton, "pushButtonAUS")
        self.pushButtonAUS.clicked.connect(self.pushButtonAUSclicked)

        self.pushButtonUSA = self.findChild(QPushButton, "pushButtonUSA")
        self.pushButtonUSA.clicked.connect(self.pushButtonUSAclicked)

        self.pushButtonUK = self.findChild(QPushButton, "pushButtonUK")
        self.pushButtonUK.clicked.connect(self.pushButtonUKclicked)

       



        '''
'''
        self.heading = self.findChild(QLabel,"lbl_heading")
        self.buttonAdd = self.findChild(QPushButton,"add_btn")
        self.buttonDelete = self.findChild(QPushButton,"del_btn")
        self.buttonDelete.setEnabled(False) # disable delete button

        self.comboBox1 = self.findChild(QComboBox,"cmb_one")
        self.listWidget  = self.findChild(QListWidget,"lst_widget")
        self.txtBrowser = self.findChild(QTextBrowser,"txt_browser_one")
        self.progBar = self.findChild(QProgressBar, "progbar_one")

        self.progBar.setMaximum(100)
        self.progBar.setValue(50)

        self.labelProgressComplete = self.findChild(QLabel, "lbl_progress_complete")
        self.labelProgressComplete.setHidden(True)                                     # hide label until progress bar is full

        """ set event handlers """
        self.buttonAdd.clicked.connect(self.add_btn_clicked)
        self.buttonDelete.clicked.connect(self.del_btn_clicked)
        self.listWidget.clicked.connect(self.listwidget_clicked)
        self.lwModel = self.listWidget.model()                             # need to pick up events on the list
        self.lwModel.rowsInserted.connect(self.checkListLength)            # Any time an element is added run function
        self.lwModel.rowsRemoved.connect(self.checkListLength)             # Any time an element is removed run function

        self.show()
    
    #end def

    def pushButtonAUSclicked(self):
        uic.loadUi("australia_nodeclick.ui",self)
    def pushButtonUSAclicked(self):
        uic.loadUi("america_nodeclick.ui",self)
    def pushButtonUKclicked(self):
        uic.loadUi("Ukpopout.ui",self)
        self.pushButtonENG = self.findChild(QPushButton, "pushButtonENG")
        self.pushButtonENG.clicked.connect(self.pushButtonENGclicked)
    def pushButtonENGclicked(self):
        uic.loadUi("england_nodeclick.ui")


    
    '''
'''
    def listwidget_clicked(self):
    
        print(self.listWidget.currentRow())
        if self.listWidget.count() > 0:
            self.buttonDelete.setEnabled(True) # enable delete button
        else:
            self.buttonDelete.setEnabled(False) # disable delete button
        #end if

    #end def


    def checkListLength(self):

        if self.listWidget.count() > 0:
            self.buttonDelete.setEnabled(True) # disable delete button
        else:
            self.buttonDelete.setEnabled(False)
        # end if

    #end def


    def add_btn_clicked(self):

        """ add item from list and combo box"""

        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")

        # add item to list and combo box
        self.listWidget.addItem(d1)
        self.comboBox1.addItem(d1)

        if self.progBar.value() < self.progBar.maximum():

            self.progBar.setValue(self.progBar.value()+5)

        else:

            self.buttonAdd.setEnabled(False)
            self.labelProgressComplete.setHidden(False)                                 # show full label
            self.progBar.setEnabled(False)                                              # disable prgress bar
            self.showCompleteMessage("Progress Complete")

        #endif

    #end def


    def showCompleteMessage(self, message_text):

        msg = QMessageBox()
        msg.setStyleSheet("background-color: rgb(200, 200, 0); color rgb(255, 200, 0)")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(message_text)
        msg.setText("Have a Nice Day!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    #enddef


    def del_btn_clicked(self):

        """ remove item from list and combo box"""
        if self.listWidget.count() == 0:
            print("Nope")
        #endif

        if self.listWidget.count() > 0:
            self.listWidget.takeItem(self.listWidget.currentRow())
        else:
            print("Nope - not in list")
        #endif

    #enddef

#endclass
'''
'''
# main starts here - init App
app = QApplication(sys.argv)
window = My_UI()
app.exec_()
sys.exit(app.exec_())
'''

'''
jhvkjvjhgf
'''
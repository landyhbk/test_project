import sys, time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QTextBrowser, QComboBox, QListWidget, QProgressBar, QMessageBox, QDialogButtonBox, QLineEdit
from PyQt5 import uic
from datetime import datetime
import json
import random



TIME_LIMIT = 100

def load_json(file_path="rugbyjson.json"):
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

        # Load JSON Data
        self.data = load_json()  

        self.pushButtonAUS = self.findChild(QtWidgets.QPushButton, "pushButtonAUS")
        self.pushButtonAUS2 = self.findChild(QtWidgets.QPushButton, "pushButtonAUS2")
        self.pushButtonUSA = self.findChild(QtWidgets.QPushButton, "pushButtonUSA")
        self.pushButtonUK = self.findChild(QtWidgets.QPushButton, "pushButtonUK")
        self.pushButtonSA = self.findChild(QtWidgets.QPushButton, "pushButtonSA")
        self.pushButtonSA2 = self.findChild(QtWidgets.QPushButton, "pushButtonSA2")
        self.pushButtonNZL = self.findChild(QtWidgets.QPushButton, "pushButtonNZL")
        self.pushButtonNZL2 = self.findChild(QtWidgets.QPushButton, "pushButtonNZL2")
        self.pushButtonFRA = self.findChild(QtWidgets.QPushButton, "pushButtonFRA")
        self.pushButtonFRA2 = self.findChild(QtWidgets.QPushButton, "pushButtonFRA2")
        self.pushButtonARG = self.findChild(QtWidgets.QPushButton, "pushButtonARG")
        self.pushButtonARG2 = self.findChild(QtWidgets.QPushButton, "pushButtonARG2")
        self.pushButtonITA = self.findChild(QtWidgets.QPushButton, "pushButtonITA")
        self.pushButtonITA2 = self.findChild(QtWidgets.QPushButton, "pushButtonITA2")
        self.pushButtonFIJ = self.findChild(QtWidgets.QPushButton, "pushButtonFIJ")
        self.pushButtonFIJ2 = self.findChild(QtWidgets.QPushButton, "pushButtonFIJ2")
        self.pushButtonJAP = self.findChild(QtWidgets.QPushButton, "pushButtonJAP")
        self.pushButtonGEO = self.findChild(QtWidgets.QPushButton, "pushButtonGEO")
        self.pushButtonENG2 = self.findChild(QtWidgets.QPushButton, "pushButtonENG2")
        self.pushButtonSCO2 = self.findChild(QtWidgets.QPushButton, "pushButtonSCO2")
        self.pushButtonIRE2 = self.findChild(QtWidgets.QPushButton, "pushButtonIRE2")
        self.pushButtonRugbyRules = self.findChild(QtWidgets.QPushButton, "pushButtonRugbyRules")
        

        self.pushButtonAUS.clicked.connect(self.open_australia_window)
        self.pushButtonAUS2.clicked.connect(self.open_australia_window)
        self.pushButtonUSA.clicked.connect(self.open_usa_window)
        self.pushButtonUK.clicked.connect(self.open_uk_window)
        self.pushButtonSA.clicked.connect(self.open_southafrica_window)
        self.pushButtonSA2.clicked.connect(self.open_southafrica_window)
        self.pushButtonNZL.clicked.connect(self.open_newzealand_window)
        self.pushButtonNZL2.clicked.connect(self.open_newzealand_window)
        self.pushButtonFRA.clicked.connect(self.open_france_window)
        self.pushButtonFRA2.clicked.connect(self.open_france_window)
        self.pushButtonARG.clicked.connect(self.open_argentina_window)
        self.pushButtonARG2.clicked.connect(self.open_argentina_window)
        self.pushButtonITA.clicked.connect(self.open_italy_window)
        self.pushButtonITA2.clicked.connect(self.open_italy_window)
        self.pushButtonFIJ.clicked.connect(self.open_fiji_window)
        self.pushButtonFIJ2.clicked.connect(self.open_fiji_window)
        self.pushButtonJAP.clicked.connect(self.open_japan_window)
        self.pushButtonGEO.clicked.connect(self.open_georgia_window)
        self.pushButtonENG2.clicked.connect(self.open_england_window)
        self.pushButtonSCO2.clicked.connect(self.open_scotland_window)
        self.pushButtonIRE2.clicked.connect(self.open_ireland_window)
        self.pushButtonRugbyRules.clicked.connect(self.open_rugbyrules_window)

        self.listWidgetSearchResults.itemClicked.connect(self.handle_search_selection)

        self.last_selected_country = None

        # Ensure Fact Box Works on Startup
        self.textFactContent = self.findChild(QTextBrowser, "textBrowserFACTBOX")
        self.pushButtonFactRefresh = self.findChild(QPushButton, "pushButtonREFRESHFACT")

        if self.pushButtonFactRefresh:
            self.pushButtonFactRefresh.clicked.connect(self.refresh_fact_box)

        # Show a random fact immediately on startup
        self.show_random_fact()

                        # Initialize Search Bar Widgets
        self.lineEditSearch = self.findChild(QLineEdit, "lineEditSearch")
        self.listWidgetSearchResults = self.findChild(QListWidget, "listWidgetSearchResults")

        # Connect Search Bar to Search Function
        if self.lineEditSearch:
            self.lineEditSearch.textChanged.connect(self.update_search_results)

    def open_australia_window(self):
        self.australia_window = AUSWindow()
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

    def open_fiji_window(self):
        self.fij_window = FIJWindow()
        self.fij_window.show()

    def open_japan_window(self):
        self.jap_window = JAPWindow()
        self.jap_window.show()

    def open_georgia_window(self):
        self.geo_window = GEOWindow()
        self.geo_window.show()

    def open_england_window(self):
        self.england_window = ENGWindow()
        self.england_window.show()

    def open_scotland_window(self):
        self.scotland_window = SCOWindow()
        self.scotland_window.show()

    def open_wales_window(self):
        self.wales_window = WALWindow()
        self.wales_window.show()

    def open_ireland_window(self):
        self.wales_window = IREWindow()
        self.wales_window.show()

    def refresh_fact_box(self):
        self.show_random_fact()

            # Show a random fact at startup
        self.show_random_fact()
    
    def open_rugbyrules_window(self):
        self.rugbyrules_window = RRWindow()
        self.rugbyrules_window.show()


###########


    def show_random_fact(self):
        all_facts = []

        if "Countries" in self.data:
            for country, details in self.data["Countries"].items():
                if "FactBox" in details and "Facts" in details["FactBox"]:
                    all_facts.extend(details["FactBox"]["Facts"])

        if all_facts:
            random_fact = random.choice(all_facts)
            self.textFactContent.setText(random_fact)
        else:
            self.textFactContent.setText("No facts available.")


##################



    def update_search_results(self):
        search_text = self.lineEditSearch.text().strip().lower()
        self.listWidgetSearchResults.clear()

        if not search_text:
            return 

        results = []
        search_terms = search_text.split()  
        search_length = len(search_terms)

        for country, details in self.data["Countries"].items():
            country_name = country.lower()

            if search_text == country_name:
                results.append(f"🌍 Country: {country}")
                if "Teams" in details:
                    results.append(f"🏉 Teams (Click to View)")
                if "Stadiums" in details:
                    results.append("🏟️ Stadiums (Click to View)")
                if "Players" in details:
                    results.append("👕 Players (Click to View)")
                if "Trophies" in details:
                    results.append("🏆 Trophies (Click to View)")
                if "Fixtures" in details:
                    results.append("📅 Fixtures & Results (Click to View)")

        for country, details in self.data["Countries"].items():
            if "Stadiums" in details:
                for stadium in details["Stadiums"]:
                    if search_text in stadium["name"].lower():
                        results.append(f"🏟️ {stadium['name']} ({country}) - Capacity: {stadium['capacity']}")

            if "Teams" in details:
                for team in details["Teams"]:
                    if search_text in team.lower():
                        results.append(f"🏉 Team: {team} ({country})")

            if "Players" in details:
                for pos, player in details["Players"]["Starting XV"].items():
                    if search_text in player.lower():
                        results.append(f"👕 Player: {player} ({country})")
                for pos, player in details["Players"]["Substitutes"].items():
                    if search_text in player.lower():
                        results.append(f"👕 Player: {player} ({country})")

            if "Fixtures" in details:
                if "fixture" in search_text or any(char.isdigit() for char in search_text):  
                    for fixture in details["Fixtures"]:
                        fixture_text = f"{fixture['date']} vs {fixture['opponent']} at {fixture['venue']} - Result: {fixture['result']}"
                        if search_text in fixture_text.lower():
                            results.append(f"📅 Fixture: {fixture_text} ({country})")

            if "Trophies" in details:
                for trophy in details["Trophies"]:
                    if search_text in trophy["name"].lower():
                        results.append(f"🏆 Trophy: {trophy['name']} ({country}) - Won in: {', '.join(map(str, trophy['year_won']))}")


        if results:
            self.listWidgetSearchResults.addItems(results)
        else:
            self.listWidgetSearchResults.addItem("No results found.")

###########
    def show_stadiums(self, country):
        if not country:
            QMessageBox.warning(self, "Error", "No country selected.")
            return

        stadiums = self.data["Countries"][country]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle(f"🏟️ Stadiums in {country}")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()

    def show_teams(self, country):
        if not country:
            QMessageBox.warning(self, "Error", "No country selected.")
            return

        teams = self.data["Countries"][country]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle(f"🏉 Teams in {country}")
        msg.setText(team_info)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()

    def show_players(self, country):
        if not country:
            QMessageBox.warning(self, "Error", "No country selected.")
            return

        players = self.data["Countries"][country]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle(f"👕 Players in {country}")
        msg.setText(player_info)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()

    def show_trophies(self, country):
        if not country:
            QMessageBox.warning(self, "Error", "No country selected.")
            return

        trophies = self.data["Countries"][country]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} (Won in: {', '.join(map(str, trophy['year_won']))})" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle(f"🏆 Trophies in {country}")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()

    def show_fixtures(self, country):
        if not country:
            QMessageBox.warning(self, "Error", "No country selected.")
            return

        fixtures = self.data["Countries"][country]["Fixtures"]
        fixture_info = "\n\n".join(
            [f"{fixture['date']} vs {fixture['opponent']} at {fixture['venue']} - Result: {fixture['result']}" for fixture in fixtures]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle(f"📅 Fixtures in {country}")
        msg.setText(fixture_info)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()





##################


    def handle_search_selection(self, item):
        result_text = item.text()

        for country in self.data["Countries"]:
            if country in result_text:
                self.last_selected_country = country
                return

        if self.last_selected_country:
            if "🏟️ Stadiums" in result_text:  
                self.show_stadiums(self.last_selected_country)
            elif "🏉 Teams" in result_text:  
                self.show_teams(self.last_selected_country)
            elif "👕 Players" in result_text:  
                self.show_players(self.last_selected_country)
            elif "🏆 Trophies" in result_text:  
                self.show_trophies(self.last_selected_country)
            elif "📅 Fixtures" in result_text:  
                self.show_fixtures(self.last_selected_country)
        else:
            QMessageBox.warning(self, "Error", "No country selected. Please search for and click a country first.")






#################
class RRWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("rugbyruleswindow.ui", self)
        self.show()

    

class AUSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("australia_nodeclick.ui", self)
        self.show()

       
        self.data = load_json()

        
        self.pushButtonAUSTEAMS.clicked.connect(self.show_teams)
        self.pushButtonAUSSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonAUSFIX.clicked.connect(self.show_fixtures)
        self.pushButtonAUSTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonAUSPLAYERS.clicked.connect(self.show_players)


    def show_teams(self):
        teams = self.data["Countries"]["Australia"]["Teams"]
        team_info = "\n\n".join(teams)

        # Create a custom QMessageBox
        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  # Set the heading - this is not working try to ammend later
        msg.setText(team_info)       # Set the main content
        msg.setIcon(QMessageBox.NoIcon)  # Remove the default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

    def show_stadiums(self):
        stadiums = self.data["Countries"]["Australia"]["Stadiums"]
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
        fixtures = self.data["Countries"]["Australia"]["Fixtures"]
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
        trophies = self.data["Countries"]["Australia"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Fixtures")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()

    def show_players(self):
        players = self.data["Countries"]["Australia"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

 ##############       

class USAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("america_nodeclick.ui", self)
        self.show()
       
        self.data = load_json()

        
        self.pushButtonUSATEAMS.clicked.connect(self.show_teams)
        self.pushButtonUSASTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonUSAFIX.clicked.connect(self.show_fixtures)
        self.pushButtonUSATROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonUSAPLAYERS.clicked.connect(self.show_players)


    def show_teams(self):
        teams = self.data["Countries"]["America"]["Teams"]
        team_info = "\n\n".join(teams)

        # Create a custom QMessageBox
        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  # Set the heading - this is not working try to ammend later
        msg.setText(team_info)       # Set the main content
        msg.setIcon(QMessageBox.NoIcon)  # Remove the default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

    def show_stadiums(self):
        stadiums = self.data["Countries"]["America"]["Stadiums"]
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
        fixtures = self.data["Countries"]["America"]["Fixtures"]
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
        trophies = self.data["Countries"]["America"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Fixtures")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()

    def show_players(self):
        players = self.data["Countries"]["America"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

 ##########       


class UKWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UKpopoutMAP.ui", self)
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
        self.england_window = ENGWindow()
        self.england_window.show()

    def open_scotland_window(self):
        self.scotland_window = SCOWindow()
        self.scotland_window.show()

    def open_wales_window(self):
        self.wales_window = WALWindow()
        self.wales_window.show()

    def open_ireland_window(self):
        self.wales_window = IREWindow()
        self.wales_window.show()

#########

class ENGWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("england_nodeclick.ui", self)
        self.show()

        self.data = load_json()

        
        self.pushButtonENGTEAMS.clicked.connect(self.show_teams)
        self.pushButtonENGSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonENGFIX.clicked.connect(self.show_fixtures)
        self.pushButtonENGTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonENGPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["England"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["England"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["England"]["Fixtures"]
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
        trophies = self.data["Countries"]["England"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["England"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

##########

class SCOWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("scotland_nodeclick.ui",self)
        self.show()

        self.data = load_json()

        
        self.pushButtonSCOTEAMS.clicked.connect(self.show_teams)
        self.pushButtonSCOSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonSCOFIX.clicked.connect(self.show_fixtures)
        self.pushButtonSCOTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonSCOPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Scotland"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Scotland"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Scotland"]["Fixtures"]
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
        trophies = self.data["Countries"]["Scotland"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Scotland"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

class WALWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("wales_nodeclick.ui",self)
        self.show()

        self.data = load_json()

        
        self.pushButtonWALTEAMS.clicked.connect(self.show_teams)
        self.pushButtonWALSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonWALFIX.clicked.connect(self.show_fixtures)
        self.pushButtonWALTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonWALPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Wales"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Wales"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Wales"]["Fixtures"]
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
        trophies = self.data["Countries"]["Wales"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Wales"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

class IREWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ireland_nodeclick.ui",self)
        self.show()

        self.data = load_json()

        
        self.pushButtonIRETEAMS.clicked.connect(self.show_teams)
        self.pushButtonIRESTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonIREFIX.clicked.connect(self.show_fixtures)
        self.pushButtonIRETROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonIREPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Ireland"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Ireland"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Ireland"]["Fixtures"]
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
        trophies = self.data["Countries"]["Ireland"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Ireland"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

class SAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("southafrica_nodeclick.ui", self)
        self.show()

        self.data = load_json()

        
        self.pushButtonSATEAMS.clicked.connect(self.show_teams)
        self.pushButtonSASTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonSAFIX.clicked.connect(self.show_fixtures)
        self.pushButtonSATROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonSAPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["South Africa"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["South Africa"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["South Africa"]["Fixtures"]
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
        trophies = self.data["Countries"]["South Africa"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["South Africa"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

class NZLWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("newzealand_nodeclick.ui", self)
        self.show()

        self.data = load_json()

        
        self.pushButtonNZLTEAMS.clicked.connect(self.show_teams)
        self.pushButtonNZLSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonNZLFIX.clicked.connect(self.show_fixtures)
        self.pushButtonNZLTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonNZLPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["New Zealand"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["New Zealand"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["New Zealand"]["Fixtures"]
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
        trophies = self.data["Countries"]["New Zealand"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["New Zealand"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

class FRAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("france_nodeclick.ui", self)

        self.data = load_json()

        
        self.pushButtonFRATEAMS.clicked.connect(self.show_teams)
        self.pushButtonFRASTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonFRAFIX.clicked.connect(self.show_fixtures)
        self.pushButtonFRATROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonFRAPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["France"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["France"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["France"]["Fixtures"]
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
        trophies = self.data["Countries"]["France"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["France"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

###########

class ARGWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("argentina_nodeclick.ui", self)

        self.data = load_json()

        
        self.pushButtonARGTEAMS.clicked.connect(self.show_teams)
        self.pushButtonARGSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonARGFIX.clicked.connect(self.show_fixtures)
        self.pushButtonARGTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonARGPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Argentina"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Argentina"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Argentina"]["Fixtures"]
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
        trophies = self.data["Countries"]["Argentina"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Argentina"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

########

class ITAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("italy_nodeclick.ui", self)

        self.data = load_json()

        
        self.pushButtonITATEAMS.clicked.connect(self.show_teams)
        self.pushButtonITASTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonITAFIX.clicked.connect(self.show_fixtures)
        self.pushButtonITATROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonITAPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Italy"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Italy"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Italy"]["Fixtures"]
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
        trophies = self.data["Countries"]["Italy"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Italy"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

class FIJWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("fiji_nodeclick.ui", self)

        self.data = load_json()

        
        self.pushButtonFIJTEAMS.clicked.connect(self.show_teams)
        self.pushButtonFIJSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonFIJFIX.clicked.connect(self.show_fixtures)
        self.pushButtonFIJTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonFIJPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Fiji"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Fiji"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Fiji"]["Fixtures"]
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
        trophies = self.data["Countries"]["Fiji"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Fiji"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

class JAPWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("japan_nodeclick.ui", self)

        self.data = load_json()

        
        self.pushButtonJAPTEAMS.clicked.connect(self.show_teams)
        self.pushButtonJAPSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonJAPFIX.clicked.connect(self.show_fixtures)
        self.pushButtonJAPTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonJAPPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Japan"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Japan"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Japan"]["Fixtures"]
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
        trophies = self.data["Countries"]["Japan"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Japan"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#######

class GEOWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("georgia_nodeclick.ui", self)

        self.data = load_json()

        
        self.pushButtonGEOTEAMS.clicked.connect(self.show_teams)
        self.pushButtonGEOSTADIUMS.clicked.connect(self.show_stadiums)
        self.pushButtonGEOFIX.clicked.connect(self.show_fixtures)
        self.pushButtonGEOTROPHIES.clicked.connect(self.show_trophies)
        self.pushButtonGEOPLAYERS.clicked.connect(self.show_players)

    def show_teams(self):
        teams = self.data["Countries"]["Georgia"]["Teams"]
        team_info = "\n\n".join(teams)

        msg = QMessageBox(self)
        msg.setWindowTitle("Teams")  
        msg.setText(team_info)       
        msg.setIcon(QMessageBox.NoIcon)  
        msg.setStandardButtons(QMessageBox.Close)  
        msg.exec_()


    def show_stadiums(self):
        stadiums = self.data["Countries"]["Georgia"]["Stadiums"]
        stadium_info = "\n\n".join(
            [f"{stadium['name']} ({stadium['city']}) - Capacity: {stadium['capacity']}" for stadium in stadiums]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Stadiums")
        msg.setText(stadium_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_fixtures(self):
        fixtures = self.data["Countries"]["Georgia"]["Fixtures"]
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
        trophies = self.data["Countries"]["Georgia"]["Trophies"]
        trophy_info = "\n\n".join(
            [f"{trophy['name']} - Won in: {', '.join(map(str, trophy['year_won']))}" for trophy in trophies]
        )

        msg = QMessageBox(self)
        msg.setWindowTitle("Trophies")
        msg.setText(trophy_info)
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Close)
        msg.exec_()


    def show_players(self):
        players = self.data["Countries"]["Georgia"]["Players"]
        starting_players = "\n".join([f"{pos}. {name}" for pos, name in players["Starting XV"].items()])
        substitutes = "\n".join([f"{pos}. {name}" for pos, name in players["Substitutes"].items()])
        player_info = f"**Starting XV**:\n{starting_players}\n\n**Substitutes**:\n{substitutes}"

        msg = QMessageBox(self)
        msg.setWindowTitle("Players")  # Title of the message box
        msg.setText(player_info)  # Set the content
        msg.setIcon(QMessageBox.NoIcon)  # No default icon
        msg.setStandardButtons(QMessageBox.Close)  # Add close button
        msg.exec_()

#########

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_UI()
    sys.exit(app.exec_())



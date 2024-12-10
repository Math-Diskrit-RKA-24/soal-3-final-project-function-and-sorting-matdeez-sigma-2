import sys
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QComboBox
from PyQt5.QtCore import Qt
import game
import csv

class GameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Player Management Game')
        self.setGeometry(100, 100, 600, 500)

        layout = QVBoxLayout()

        add_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Player Name")
        self.damage_input = QLineEdit()
        self.damage_input.setPlaceholderText("Damage")
        self.defense_input = QLineEdit()
        self.defense_input.setPlaceholderText("Defense Power")
        add_button = QPushButton("Add Player")
        add_button.clicked.connect(self.add_player)
        add_layout.addWidget(self.name_input)
        add_layout.addWidget(self.damage_input)
        add_layout.addWidget(self.defense_input)
        add_layout.addWidget(add_button)
        layout.addLayout(add_layout)

        modify_layout = QHBoxLayout()
        self.modify_combo = QComboBox()
        self.attribute_combo = QComboBox()
        self.attribute_combo.addItems(["score", "damage", "health", "defensePower", "defense"])
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("New Value")
        modify_button = QPushButton("Modify Player")
        modify_button.clicked.connect(self.modify_player)
        modify_layout.addWidget(QLabel("Player:"))
        modify_layout.addWidget(self.modify_combo)
        modify_layout.addWidget(QLabel("Attribute:"))
        modify_layout.addWidget(self.attribute_combo)
        modify_layout.addWidget(self.value_input)
        modify_layout.addWidget(modify_button)
        layout.addLayout(modify_layout)

        import_export_layout = QHBoxLayout()
        import_button = QPushButton("Import CSV")
        import_button.clicked.connect(self.import_csv)
        export_button = QPushButton("Export CSV")
        export_button.clicked.connect(self.export_csv)
        import_export_layout.addWidget(import_button)
        import_export_layout.addWidget(export_button)
        layout.addLayout(import_export_layout)

        attack_layout = QHBoxLayout()
        self.attacker_combo = QComboBox()
        self.target_combo = QComboBox()
        attack_button = QPushButton("Attack")
        attack_button.clicked.connect(self.attack_player)
        attack_layout.addWidget(QLabel("Attacker:"))
        attack_layout.addWidget(self.attacker_combo)
        attack_layout.addWidget(QLabel("Target:"))
        attack_layout.addWidget(self.target_combo)
        attack_layout.addWidget(attack_button)
        layout.addLayout(attack_layout)

        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        layout.addWidget(self.results_text)

        display_button = QPushButton("Display Match Results")
        display_button.clicked.connect(self.display_results)
        layout.addWidget(display_button)

        self.setLayout(layout)

        game.initPlayers()

    def import_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        if file_name:
            with open(file_name, 'r') as file:
                reader = csv.DictReader(file)
                game.initPlayers()  # Clear existing players
                for row in reader:
                    player = game.createNewPlayer(
                        row['name'],
                        int(row['damage']),
                        int(row['defensePower'])
                    )
                    player['score'] = int(row['score'])
                    player['health'] = int(row['health'])
                    player['defense'] = row['defense'].lower() == 'true'
                    game.addPlayer(player)
            self.update_player_combos()
            self.display_results()

    def export_csv(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Export CSV", "", "CSV Files (*.csv)")
        if file_name:
            with open(file_name, 'w', newline='') as file:
                fieldnames = ['name', 'score', 'damage', 'health', 'defensePower', 'defense']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for player in game.PlayerList:
                    writer.writerow(player)

    def add_player(self):
        name = self.name_input.text()
        damage = int(self.damage_input.text() or 0)
        defense = int(self.defense_input.text() or 0)
        player = game.createNewPlayer(name, damage, defense)
        game.addPlayer(player)
        self.update_player_combos()
        self.name_input.clear()
        self.damage_input.clear()
        self.defense_input.clear()

    def modify_player(self):
        player = game.PlayerList[self.modify_combo.currentIndex()]
        attribute = self.attribute_combo.currentText()
        value = self.value_input.text()

        if attribute == "defense":
            value = value.lower() == "true"
        elif attribute != "name":
            value = float(value) if '.' in value else int(value)

        game.setPlayer(player, attribute, value)
        self.value_input.clear()
        self.display_results()
    def attack_player(self):
        attacker = game.PlayerList[self.attacker_combo.currentIndex()]
        target = game.PlayerList[self.target_combo.currentIndex()]
        game.attackPlayer(attacker, target)
        self.display_results()

    def display_results(self):
        self.results_text.clear()
        game.displayMatchResult()
        sorted_data = sorted(game.PlayerList, key=lambda x: (-x["score"], -x["health"]))
        for i, player in enumerate(sorted_data):
            self.results_text.append(f"Rank {i+1}: {player['name']} | Score: {player['score']} | Health: {player['health']} | Damage: {player['damage']} | Defense Power: {player['defensePower']} | Defense: {player['defense']}")

    def update_player_combos(self):
        self.attacker_combo.clear()
        self.target_combo.clear()
        self.modify_combo.clear()
        for player in game.PlayerList:
            self.attacker_combo.addItem(player['name'])
            self.target_combo.addItem(player['name'])
            self.modify_combo.addItem(player['name'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameGUI()
    ex.show()
    sys.exit(app.exec_())


class Player:
    def __init__(self, name, positions, height, team):
        self.name = name
        self.positions = positions
        self.height = height
        self.team = team

    def __str__(self):
        return f"{self.name} ({', '.join(self.positions)}) - {self.height} - {self.team}"


class PlayerSelectionApp:
    def __init__(self, players):
        self.players = players
        self.selected_players = {
            'G': [],
            'F': [],
            'C': []
        }

    def select_players(self):
        while True:
            print("\nWelcome to the Player Selection App!")
            print("1. Select Guards (POS G) - 4 players")
            print("2. Select Forwards (POS F) - 4 players")
            print("3. Select Centers (POS C) - 4 players")
            print("4. Go Back")
            print("5. List Full Team")
            print("6. Quit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.select_position('G', 4)
            elif choice == '2':
                self.select_position('F', 4)
            elif choice == '3':
                self.select_position('C', 4)
            elif choice == '4':
                return
            elif choice == '5':
                self.display_full_team()
            elif choice == '6':
                print("\nThank you for using the Player Selection App. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")

    def select_position(self, position, max_players):
        print(f"\nSelect {max_players} {position} players (Enter numbers separated by spaces):")
        
        # Filter players based on the selected position
        eligible_players = [player for player in self.players if position in player.positions]
        
        for i, player in enumerate(eligible_players, start=1):
            print(f"{i}. {player}")

        user_input = input(f"Example: 1 3 5 ... (Select {max_players} players)\n")

        try:
            selected_indices = [int(index) - 1 for index in user_input.split()]
            if len(selected_indices) != max_players:
                print(f"\nPlease select exactly {max_players} {position} players.")
                return

            selected_players = [eligible_players[i] for i in selected_indices]
            self.selected_players[position].extend(selected_players)
            print(f"\nSelected {position} Players:")
            for player in selected_players:
                print(player)
        except ValueError:
            print("\nInvalid input. Please enter valid numbers separated by spaces.")

    def display_full_team(self):
        full_team = []

        for position, players in self.selected_players.items():
            full_team.extend(players)

        # Sort the full team by height (from shortest to tallest)
        sorted_team = sorted(full_team, key=lambda player: player.height)

        print("\nFull Team (Shortest to Tallest):")
        for player in sorted_team:
            print(player)

def main():
    players = [
        Player("Bam Adebayo", "C", "6-9", "Miami Heat"),
        Player("Jarrett Allen", "C", "6-9", "Cleveland Cavaliers"),
        Player("Paolo Banchero", "F", "6-10", "Duke Blue Devils"),
        Player("Desmond Bane", "G", "6-5", "Memphis Grizzlies"),
        Player("Scottie Barnes", "F/G", "6-7", "Toronto Raptors"),
        Player("Devin Booker", "G", "6-5", "Phoenix Suns"),
        Player("Mikal Bridges", "F", "6-6", "Phoenix Suns"),
        Player("Jaylen Brown", "G/F", "6-6", "Boston Celtics"),
        Player("Jalen Brunson", "G", "6-2", "Dallas Mavericks"),
        Player("Jimmy Butler", "F", "6-7", "Miami Heat"),
        Player("Alex Caruso", "G", "6-5", "Chicago Bulls"),
        Player("Stephen Curry", "G", "6-2", "Golden State Warriors"),
        Player("Anthony Davis", "F/C", "6-10", "Los Angeles Lakers"),
        Player("Kevin Durant", "F", "6-10", "Brooklyn Nets"),
        Player("Anthony Edwards", "G", "6-4", "Minnesota Timberwolves"),
        Player("Joel Embiid", "C", "7-0", "Philadelphia 76ers"),
        Player("De’Aaron Fox", "G", "6-3", "Sacramento Kings"),
        Player("Paul George", "F", "6-8", "LA Clippers"),
        Player("Aaron Gordon", "F", "6-8", "Denver Nuggets"),
        Player("Tyrese Haliburton", "G", "6-5", "Sacramento Kings"),
        Player("James Harden", "G", "6-5", "Brooklyn Nets"),
        Player("Josh Hart", "G", "6-5", "New Orleans Pelicans"),
        Player("Tyler Herro", "G", "6-5", "Miami Heat"),
        Player("Jrue Holiday", "G", "6-3", "Milwaukee Bucks"),
        Player("Chet Holmgren", "C/F", "7-1", "Gonzaga Bulldogs"),
        Player("Brandon Ingram", "F", "6-8", "New Orleans Pelicans"),
        Player("Kyrie Irving", "G", "6-2", "Brooklyn Nets"),
        Player("Jaren Jackson Jr.", "C", "6-11", "Memphis Grizzlies"),
        Player("LeBron James", "F", "6-9", "Los Angeles Lakers"),
        Player("Cam Johnson", "F", "6-8", "Phoenix Suns"),
        Player("Walker Kessler", "C", "7-0", "Auburn Tigers"),
        Player("Kawhi Leonard", "F", "6-7", "LA Clippers"),
        Player("Damian Lillard", "G", "6-2", "Portland Trail Blazers"),
        Player("Donovan Mitchell", "G", "6-3", "Utah Jazz"),
        Player("Chris Paul", "G", "6-0", "Phoenix Suns"),
        Player("Bobby Portis", "F", "6-11", "Milwaukee Bucks"),
        Player("Austin Reaves", "G", "6-5", "Los Angeles Lakers"),
        Player("Duncan Robinson", "F", "6-7", "Miami Heat"),
        Player("Jayson Tatum", "F", "6-8", "Boston Celtics"),
        Player("Derrick White", "G", "6-4", "San Antonio Spurs"),
        Player("Trae Young", "G", "6-1", "Atlanta Hawks"),
    ]

    app = PlayerSelectionApp(players)
    app.select_players()

if __name__ == "__main__":
    main()



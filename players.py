import json

def load_players():
    try:
        with open("players.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_players(players):
    with open("players.json", "w") as file:
        json.dump(players, file)

def login():
    players = load_players()
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if name in players:
        if players[name]["password"] == password:
            print(f"Welcome back, {name}!")
            return name
        else:
            print("Incorrect password. Try again.")
            return None
    else:

        print("New player! Registering your information.")
        players[name] = {"password": password, "score": 0}
        save_players(players)
        return name

def update_score(name, score):
    players = load_players()
    if name in players:
        players[name]["score"] += score
        save_players(players)
        print(f"{name}'s total score is now: {players[name]['score']}")
    else:
        print("Player not found.")

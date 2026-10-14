import random


players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    new_list = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {new_list}")

    only_capitalize_list = [
        player for player in players if player == player.capitalize()
    ]
    print(f"New list of capitalized names only: {only_capitalize_list}") 
    scores = {player: random.randrange(1000) for player in new_list}  
    print(f"Score dict: {scores}")
    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")    
    high_scores = {
        player : scores[player]
        for player in scores
        if scores[player] > avg
    }
    print(f"High scores: {high_scores}")
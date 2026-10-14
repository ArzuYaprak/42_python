import random

achievements = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 10)
    #random.sample birbirinden farklı seçer
    selected_achievements = random.sample(achievements, amount)
    return set(selected_achievements)

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")
    print()
    common_achievements = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_achievements}")
    print()
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print()
    all_achievements = set(achievements)
    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")
 # not: Dictionary, bir oyuncuyu anahtar üzerinden hızlıca bulmak için kullanılıyor.

from ex3 import *
from ex4 import *

def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    #bu döngünün amacı her rakip birbiriyle bir kez denk gelecek
    for i in range(len(opponents)):
        for j in range(i+1, len(opponents)):
            first_factory, first_strategy = opponents[i]
            second_factory, second_strategy = opponents[j]
            first = first_factory.create_base()
            second = second_factory.create_base()
            print("\n* Battle *")
            print(first.describe())
            print("vs.")
            print(second.describe())
            print("now fight!")
            try:
                first_strategy.act(first)
                second_strategy.act(second)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return
            
def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")

    opponents: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]

    battle(opponents)

    print("\nTournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")

    invalid_opponents: list[tuple[CreatureFactory, BattleStrategy]] = [
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy()),
    ]

    battle(invalid_opponents)


if __name__ == "__main__":
    main()

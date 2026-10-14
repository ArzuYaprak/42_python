import typing
import random



players = [
    "alice",
    "bob",
    "charlie",
    "dylan",
]


actions = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


""" Generator[üretilen_değer, dışarıdan_alınan_değer, dönüş_değeri]
 Generator’a .send(...) ile dışarıdan değer göndermiyorsun. Yalnızca next() kullanıyorsun.
İkinci None
Generator sonunda özel bir değer return etmiyor. """
def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)
        
        
def consume_event(
    events_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events_list) > 0:
        index = random.randrange(len(events_list))
        selected = events_list[index]
        del events_list[index]
        yield selected     
          
if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    generator_event = gen_event()
    for i in range(1000):
        event = next(generator_event)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        
    events_list = []
    generator_event1 = gen_event()

    for i in range(10):
        event = next(generator_event1)
        events_list += [event]
    print(f"Built list of 10 events: {events_list}")
    for selected in consume_event(events_list):
        print(f"Got event from list: {selected}")
        print(f"Remains in list: {events_list}")
    
        
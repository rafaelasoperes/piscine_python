import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = ['alice', 'bob', 'charlie', 'dylan']
    actions: list[str] = ['run', 'eat', 'sleep',
                          'grab', 'move', 'climb', 'swim']

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    remaining = len(event_list)

    while remaining > 0:
        idx = random.randrange(remaining)
        event = event_list[idx]

        event_list[idx] = event_list[remaining - 1]
        event_list[remaining - 1] = event

        remaining -= 1
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    meu_gerador = gen_event()
    for i in range(1000):
        player, action = next(meu_gerador)
        print(f"Event {i}: Player {player} did action {action}")

    eventos_estaticos: list[tuple[str, str]] = [('', '')] * 10
    for i in range(10):
        eventos_estaticos[i] = next(meu_gerador)

    print(f"Built list of 10 events: {eventos_estaticos}")

    consumidor = consume_event(eventos_estaticos)
    for _ in range(10):
        event = next(consumidor)
        print(f"Got event from list: {event}")


if __name__ == "__main__":
    main()

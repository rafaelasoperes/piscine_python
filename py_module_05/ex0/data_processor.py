from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._data_store: list[tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data_store:
            raise IndexError("No data to output")
        return self._data_store.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._data_store.append((self._counter, str(item)))
            self._counter += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._data_store.append((self._counter, item))
            self._counter += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        def is_log(d: Any) -> bool:
            return (isinstance(d, dict) and
                    all(isinstance(k, str) and isinstance(v, str)
                        for k, v in d.items()))

        if is_log(data):
            return True
        if isinstance(data, list) and data:
            return all(is_log(x) for x in data)
        return False

    def ingest(self, data: Union[dict[str, str],
                                 list[dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            log_str = ": ".join(item.values())
            self._data_store.append((self._counter, log_str))
            self._counter += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")

    np.ingest([1, 2, 3, 4, 5])
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = np.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")

    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    tp.ingest(['Hello', 'Nexus', 'World'])
    print("Processing data: ['Hello', 'Nexus', 'World']")
    rank, val = tp.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    logs = [
        {'level': 'NOTICE', 'msg': 'Connection to server'},
        {'level': 'ERROR', 'msg': 'Unauthorized access!!'}
    ]
    lp.ingest(logs)
    print(f"Processing data: {logs}")
    for _ in range(2):
        rank, val = lp.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()

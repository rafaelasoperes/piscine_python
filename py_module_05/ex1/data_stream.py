import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._processed_count: int = 0
        self._outputs: list[typing.Any] = []

    @abc.abstractmethod
    def can_process(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def process(self, data: typing.Any) -> None:
        pass

    def get_output(self) -> typing.Any:
        if len(self._outputs) == 0:
            return None
        return self._outputs.pop(0)

    def get_processed_count(self) -> int:
        return self._processed_count

    def get_remaining_count(self) -> int:
        return len(self._outputs)

    @abc.abstractmethod
    def get_name(self) -> str:
        pass


class NumericProcessor(DataProcessor):
    def can_process(self, data: typing.Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True
        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                if (not isinstance(data[i], int)
                        and not isinstance(data[i], float)):
                    return False
                i += 1
            return True
        return False

    def process(self, data: typing.Any) -> None:
        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                self._outputs.append(data[i])
                self._processed_count += 1
                i += 1
        else:
            self._outputs.append(data)
            self._processed_count += 1

    def get_name(self) -> str:
        return "Numeric Processor"


class TextProcessor(DataProcessor):
    def can_process(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                if not isinstance(data[i], str):
                    return False
                i += 1
            return True
        return False

    def process(self, data: typing.Any) -> None:
        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                self._outputs.append(data[i])
                self._processed_count += 1
                i += 1
        else:
            self._outputs.append(data)
            self._processed_count += 1

    def get_name(self) -> str:
        return "Text Processor"


class LogProcessor(DataProcessor):
    def _is_valid_log(self, data: typing.Any) -> bool:
        return (
            isinstance(data, dict)
            and "log_level" in data
            and "log_message" in data
        )

    def can_process(self, data: typing.Any) -> bool:
        if self._is_valid_log(data):
            return True
        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                if not self._is_valid_log(data[i]):
                    return False
                i += 1
            return True
        return False

    def process(self, data: typing.Any) -> None:
        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                self._outputs.append(data[i])
                self._processed_count += 1
                i += 1
        else:
            self._outputs.append(data)
            self._processed_count += 1

    def get_name(self) -> str:
        return "Log Processor"


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        i: int = 0
        while i < len(stream):
            element: typing.Any = stream[i]
            processed: bool = False

            j: int = 0
            while j < len(self._processors):
                if self._processors[j].can_process(element):
                    self._processors[j].process(element)
                    processed = True
                    break
                j += 1

            if not processed:
                print("DataStream error - can't process element in stream:"
                      f" {element}")
            i += 1

    def print_processor_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        i: int = 0
        while i < len(self._processors):
            proc: DataProcessor = self._processors[i]
            print(f"{proc.get_name()}: total {proc.get_processed_count()} "
                  f"items processed, remaining {proc.get_remaining_count()} "
                  f"on processor")
            i += 1


def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processor_stats()

    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User vil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processor_stats()

    print("\nRegistering other data processors\n")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processor_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    numeric.get_output()
    numeric.get_output()
    numeric.get_output()
    text.get_output()
    text.get_output()
    log.get_output()

    stream.print_processor_stats()


if __name__ == "__main__":
    main()

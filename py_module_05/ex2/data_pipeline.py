import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._storage: list[str] = []
        self._total_processed: int = 0
        self._next_rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._storage) == 0:
            raise Exception("No data available")

        value: str = self._storage[0]
        rank: int = self._next_rank
        self._next_rank += 1

        i: int = 1
        while i < len(self._storage):
            self._storage[i - 1] = self._storage[i]
            i += 1
        self._storage = self._storage[:-1]

        return (rank, value)

    def print_stats(self) -> None:
        print(
            f"{self.name}: total {self._total_processed} items processed, "
            f"remaining {len(self._storage)} on processor"
        )


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True

        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                if (
                    not isinstance(data[i], int)
                    and not isinstance(data[i], float)
                ):
                    return False
                i += 1
            return True

        return False

    def ingest(
        self,
        data: int | float | list[int] | list[float] | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, int) or isinstance(data, float):
            self._storage.append(str(data))
            self._total_processed += 1
        else:
            i: int = 0
            while i < len(data):
                self._storage.append(str(data[i]))
                self._total_processed += 1
                i += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: typing.Any) -> bool:
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

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, str):
            self._storage.append(data)
            self._total_processed += 1
        else:
            i: int = 0
            while i < len(data):
                self._storage.append(data[i])
                self._total_processed += 1
                i += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_log_dict(data)

        if isinstance(data, list):
            i: int = 0
            while i < len(data):
                if not isinstance(data[i], dict):
                    return False
                if not self._is_valid_log_dict(data[i]):
                    return False
                i += 1
            return True

        return False

    def _is_valid_log_dict(self, data: dict[typing.Any, typing.Any]) -> bool:
        for key in data:
            if not isinstance(key, str):
                return False
            if not isinstance(data[key], str):
                return False
        return True

    def _dict_to_string(self, data: dict[str, str]) -> str:
        if "log_level" in data and "log_message" in data:
            return data["log_level"] + ": " + data["log_message"]

        result: str = ""
        first: bool = True
        for key in data:
            if not first:
                result += ", "
            result += key + ": " + data[key]
            first = False
        return result

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, dict):
            self._storage.append(self._dict_to_string(data))
            self._total_processed += 1
        else:
            i: int = 0
            while i < len(data):
                self._storage.append(self._dict_to_string(data[i]))
                self._total_processed += 1
                i += 1


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        result: str = ""
        i: int = 0
        while i < len(data):
            if i > 0:
                result += ","
            result += data[i][1]
            i += 1
        print("CSV Output:")
        print(result)


class JSONExportPlugin:
    def _escape_json(self, text: str) -> str:
        result: str = ""
        i: int = 0
        while i < len(text):
            char: str = text[i]
            if char == "\\":
                result += "\\\\"
            elif char == '"':
                result += '\\"'
            else:
                result += char
            i += 1
        return result

    def process_output(self, data: list[tuple[int, str]]) -> None:
        result: str = "{"
        i: int = 0
        while i < len(data):
            if i > 0:
                result += ", "
            key: str = "item_" + str(data[i][0])
            value: str = self._escape_json(data[i][1])
            result += '"' + key + '": "' + value + '"'
            i += 1
        result += "}"

        print("JSON Output:")
        print(result)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        i: int = 0
        while i < len(stream):
            item: typing.Any = stream[i]
            handled: bool = False

            j: int = 0
            while j < len(self._processors):
                if self._processors[j].validate(item):
                    self._processors[j].ingest(item)
                    handled = True
                    break
                j += 1

            if not handled:
                print("DataStream error - can't process element "
                      f"in stream: {item}")
            i += 1

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        i: int = 0
        while i < len(self._processors):
            self._processors[i].print_stats()
            i += 1

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if len(self._processors) == 0:
            print("No processor found, no data")
            return

        i: int = 0
        while i < len(self._processors):
            extracted: list[tuple[int, str]] = []
            count: int = 0

            while count < nb:
                try:
                    extracted.append(self._processors[i].output())
                    count += 1
                except Exception:
                    break

            plugin.process_output(extracted)
            i += 1


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    stream: DataStream = DataStream()

    print("Initialize Data Stream...\n")
    stream.print_processors_stats()
    print()

    print("Registering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User vil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print("Send first batch of data on stream:", batch1)
    stream.process_stream(batch1)
    print()
    stream.print_processors_stats()
    print()

    csv_plugin: CSVExportPlugin = CSVExportPlugin()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)
    print()
    stream.print_processors_stats()
    print()

    batch2: list[typing.Any] = [
        [21, ["I love AI", "LLMs are wonderful", "Stay healthy"]],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"}
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("Send another batch of data:")
    print(batch2)

    fixed_batch2: list[typing.Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"}
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    stream.process_stream(fixed_batch2)
    print()
    stream.print_processors_stats()
    print()

    json_plugin: JSONExportPlugin = JSONExportPlugin()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()

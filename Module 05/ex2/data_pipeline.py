#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise IndexError("No data available")
        return self._queue.pop(0)

    def _save(self, value: str) -> None:
        self._queue.append((self._rank, value))
        self._rank += 1

    def remaining(self) -> int:
        return len(self._queue)

    def total_processed(self) -> int:
        return self._rank

    def display_name(self) -> str:
        return self.__class__.__name__.replace("Processor", " Processor")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._save(str(item))
            return
        self._save(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._save(item)
            return
        self._save(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        if isinstance(data, list):
            return all(self.validate(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self._save(self._format_log(item))
            return
        self._save(self._format_log(data))

    @staticmethod
    def _format_log(entry: dict[str, str]) -> str:
        if "log_level" in entry and "log_message" in entry:
            return f"{entry['log_level']}: {entry['log_message']}"
        return ", ".join(f"{key}: {value}" for key, value in entry.items())


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.display_name()}: total {proc.total_processed()} "
                f"items processed, remaining {proc.remaining()} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()

    print("Initialize Data Stream...")
    stream_engine = DataStream()
    stream_engine.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()
    print()

    print("Registering Numeric Processor")
    print()

    stream_engine.register_processor(numeric)
    sample_stream: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {sample_stream}")
    stream_engine.process_stream(sample_stream)
    stream_engine.print_processors_stats()
    print()

    print("Registering other data processors")
    stream_engine.register_processor(text)
    stream_engine.register_processor(logs)
    print("Send the same batch again")
    stream_engine.process_stream(sample_stream)
    stream_engine.print_processors_stats()
    print()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    logs.output()
    stream_engine.print_processors_stats()


if __name__ == "__main__":
    main()

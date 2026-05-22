#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
        print("which will check whether the input data are appropriate for the current data processor")
        print(" This method returns a bool that indicates if the provided data can be ingested by this data processor.")

    @abstractmethod
    def ingest(self, data: Any) -> None:
        print("which will process the input data")
        print(
            " The overriding methods in the specialized classes will have"
            "their own specific signatures to match the types they expect. In case the user"
            "does not validate the data before calling ingest, and provides invalid data, an"
            "exception must be raised."
        )

    def output(self) -> tuple[int, str]:
        print("which will output ingested data")
        print(" There is no need to override it in the specialized classes")


class NumericProcessor(DataProcessor):
    print(
        " The NumericProcessor ingests int, float, and lists of both types (including"
        "mixed-type lists). It then converts the data into strings and stores it internally,"
        "waiting to be extracted using the output method. The overriding ingest method"
        "signature must reflect the accepted types."
    )


class TextProcessor(DataProcessor):
    print(
        " The TextProcessor ingests str and lists of strings. It stores the data internally,"
        "waiting to be extracted using the output method. The overriding ingest method"
        "signature must reflect the accepted types."
    )


class LogProcessor(DataProcessor):
    print(
        " The LogProcessor ingests a dict of string key-value pairs, and lists of that type. It"
        "then converts the data into strings and stores it internally, waiting to be extracted"
        "using the output method. The overriding ingest method signature must reflect"
        "the accepted types."
    )


def main() -> None:
    print(
        "The output method will extract the oldest piece of data stored internally in the"
"data processor, along with the associated processing rank within the data processor."
"The piece of data is then removed from the data processor."
    )
    print(
        "• Create instances for each specialized class."
        "• Test valid and invalid data for each class through the validate method."
        "• Test at least one invalid data item with the ingest method without prior validation,"
        "and check that it raises an exception. This will leave you with a mypy warning, on"
        "purpose."
        "• Ingest various data for each data processor and then extract it using output"
    )
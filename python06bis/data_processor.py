from abc import ABC, abstractmethod
from typing import Any#metodun herhangi bir türde veri olabileceğini belirtir


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []#işlenmiş verileri burda saklayacağız
        self._next_rank: int = 0#çıkarılan her veriye sıra numarası verilir
        """_def __init__ içersinde tanımlanmsının sebebi: 
        Eğer _data class seviyesinde tanımlansaydı, bütün 
        processor nesneleri aynı listeyi paylaşabilirdi.
        __init__() içinde tanımlayınca her nesne oluşturulduğunda 
        yeni ve bağımsız liste oluşur.
        """
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    
    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available")
        
        value: str = self._data.pop(0)
        rank: int = self._next_rank
        self._next_rank += 1
        return (rank, value)
    
NumericValue = int | float
NumericData = NumericValue | list[NumericValue]
TextData = str | list[str]
LogEntry = dict[str, str]
LogData = LogEntry | list[LogEntry]


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
    
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                for item in data
            )
        return False
    def ingest(self, data: NumericData) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        
        if isinstance(data, list):#sadece validationa güvenmiyoruz kendimz de tip kontrolü yapıyoruz
            for item in data:
                self._data.append(str(item))
        else:
            self._data.append(str(data))
            

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(
                isinstance(item, str)
                for item in data
            )

        return False

    def ingest(self, data: TextData) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data.append(item)
        else:
            self._data.append(data)
            
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_log_entry(data)

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and self._is_valid_log_entry(item)
                for item in data
            )

        return False

    def _is_valid_log_entry(self, data: dict[Any, Any]) -> bool:
        required_keys: set[str] = {"log_level", "log_message"}

        return (
            set(data.keys()) >= required_keys
            and all(isinstance(key, str) for key in data)
            and all(isinstance(value, str) for value in data.values())
        )

    def ingest(self, data: LogData) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._add_log_entry(item)
        else:
            self._add_log_entry(data)

    def _add_log_entry(self, data: LogEntry) -> None:
        log_level: str = data["log_level"]
        log_message: str = data["log_message"]
        self._data.append(f"{log_level}: {log_message}")
        
def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(
        f"Trying to validate input 'Hello': "
        f"{numeric.validate('Hello')}"
    )

    print(
        "Test invalid ingestion of string 'foo' "
        "without prior validation:"
    )
    try:
        numeric.ingest("foo")  # type: ignore[arg-type]
    except ValueError as error:
        print(f"Got exception: {error}")

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for index in range(3):
        _, value = numeric.output()
        print(f"Numeric value {index}: {value}")

    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    _, value = text.output()
    print(f"Text value 0: {value}")

    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    print(
        "Processing data: "
        "[{'log_level': 'NOTICE', "
        "'log_message': 'Connection to server'}, "
        "{'log_level': 'ERROR', "
        "'log_message': 'Unauthorized access!!'}]"
    )

    log.ingest(
        [
            {
                "log_level": "NOTICE",
                "log_message": "Connection to server",
            },
            {
                "log_level": "ERROR",
                "log_message": "Unauthorized access!!",
            },
        ]
    )

    print("Extracting 2 values...")
    for index in range(2):
        _, value = log.output()
        print(f"Log entry {index}: {value}")


if __name__ == "__main__":
    main()
    
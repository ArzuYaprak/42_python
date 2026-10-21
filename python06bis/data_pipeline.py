from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []#işlenmiş verileri burda saklayacağız işlendikçe popla çıkaracağımız için bize aslında remaining kıdmını veriyor
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
    
    def number_remaining_data(self) -> int:
            return len(self._data)
            
    def number_total_data(self) -> int:
        return self._next_rank + len(self._data)
    
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
        
class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        
    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        
    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            handled = False

            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    handled = True
                    break

            if not handled:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{data}"
                )
                
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")#processor un öncesine boşlk bıralmak için NumericProcessor -> Numeric Processor olur
            #type(proc) nesnenin sınıfını bulur, .__name__. o sınıfın adını metin olrak verir
            total = proc.number_total_data()
            remaining = proc.number_remaining_data()

            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )
            
    def output_pipeline(self, nb: int, plugin: "ExportPlugin") -> None:
        for proc in self._processors:
            data: list[tuple[int, str]] = []
            count = min(nb, proc.number_remaining_data())#işlemcide 2 varsa 3 çıkarmayaım diye, outputu çağırıp hata almayalım diye
            for _ in range(count):
                data.append(proc.output())
                
            plugin.process_output(data)#listeyi eklentiye gönderiyoruz
            
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...#metodun uygulamasını protokol içeisinde vermiyoruz
class CSVExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        fields: list[str] = []
        
        for _, value in data:#subjecte rank yani sıra numaraları kullanılmadığı için _ dedik
            if any(char in value for char in ',\"\r\n'):#bu metinde bu karakterlerden en az biri var mı (bu karakterler karakterin içerisinde)diye kontrol ediyor.any kontrollerden en az biri varsa true döndürür
                value = value.replace('"', '""')
                value = f'"{value}"'
                
            fields.append(value)
            
        print("CSV Output:")
        print(",".join(fields))
        
class JSONExporter:
    def _escape(self, value: str) -> str:
        result = ""

        for char in value:
            if char == '"':
                result += '\\"'
            elif char == "\\":
                result += "\\\\"
            elif ord(char) < 32:
                result += f"\\u{ord(char):04x}"
            else:
                result += char

        return result
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items: list[str] = []
        
        for rank, value in data:
            escape_value = self._escape(value)
            item = f'"item_{rank}": "{escape_value}"'
            items.append(item)
        result = "{" + ", ".join(items) + "}"#Çiftleri virgülle birleştir ve süslü parantezlerin içine koy
        print("JSON Output:")
        print(result)
            
def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors\n")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

    first_batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    print()
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExporter()
    data_stream.output_pipeline(3, csv_plugin)
    print()
    data_stream.print_processors_stats()

    second_batch: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {second_batch}")
    data_stream.process_stream(second_batch)
    print()
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExporter()
    data_stream.output_pipeline(5, json_plugin)
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
    


from abc import ABC, abstractmethod
from typing import Any#metodun herhangi bir türde veri olabileceğini belirtir


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
            
def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(numeric)

    batch: list[Any] = [
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

    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    log.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
        
    """Nesneyi oluşturmak, kaydetmek değildir. text ve log başta oluşturuluyor ama ilk gönderimde kayıtlı değiller. Bu yüzden metinler ve loglar için hata mesajı bekliyoruz.
Aynı batch tekrar gönderiliyor. Sayısal işlemci iki gönderimi de aldığı için toplamı 4 → 8 olur. Metin ve log işlemcileri yalnızca ikinci gönderimi alır.
output() veriyi işlemciden çıkarır. Burada dönen değeri kullanmıyoruz; kalan sayısının azaldığını istatistiklerde göreceğiz.
for _ in range(3), bir işlemi üç kez yapmak demektir. Döngü değişkenine ihtiyacımız olmadığı için _ yazıyoruz.
    """

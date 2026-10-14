import typing
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file_name = sys.argv[1]
        try:
            file: typing.IO[str] = open(file_name, "r")
            content: str = file.read()
            file.close()
        except OSError as error:
            print(f"[STDERR] Error opening file '{file_name}': {error}", file=sys.stderr)
        else:
            print("---")
            print()
            print(content)
            print()
            print("---")
            print(f"File '{file_name}' closed.")
            print()
            transformed_content = ""

            for line in content.splitlines():
                transformed_content += line + "#\n"
            print("Transform data:")
            print("---")
            print()
            print(transformed_content)
            print("---")
            print("Enter new file name (or empty): ", end="")
            sys.stdout.flush()
            """sys.stdout.flush() Neden Gerekli?
            İşletim sistemleri ekrana yazı yazdırırken performans için 
            "tampon bellek" (buffer) kullanır. Genellikle bu bellek, satır sonu karakteri (\n) 
            gelene kadar yazıları bekletir ve ekrana basmaz. Biz az önce print içinde alt satıra
            geçmeyi (\n) iptal ettiğimiz için, "Enter new file name..." yazısı ekranda hemen 
            görünmeyip bellekte takılı kalabilir. flush() (sifonu çekmek gibi düşünebilirsin)
            bellekte ne varsa beklemeden zorla ekrana basılmasını sağlar. Böylece yazının 
            anında kullanıcıya görünmesini garanti altına alırız.
            sys.stdin.readline().strip() Nasıl Çalışır?
            Kullanıcı klavyeden dosya ismini yazıp Enter tuşuna bastığında, 
            sys.stdin.readline() bu akışı okur. Ancak önemli bir detay var: Kullanıcının
            bastığı Enter tuşu da bir karakterdir (\n).
            Yani sen dosyaya "ornek.txt" yazıp Enter'a basarsan, readline() 
            bunu "ornek.txt\n" olarak alır. Eğer bunu bu haliyle kaydedersen
            dosya adı hatalı olur.
            İşte sondaki o .strip() metodu devreye girer;
            kelimenin başındaki ve sonundaki boşlukları ve \n gibi 
            görünmez karakterleri kırpar. Geriye sadece "ornek.txt" kalır.
            Bu adımlarla, yasaklanmış olan input() fonksiyonunun arka 
            planda ne yaptığını manuel olarak kendimiz inşa etmiş olduk!
            """
            new_file_name = sys.stdin.readline().strip()
            if new_file_name == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file_name}'")
                try:
                    new_file: typing.IO[str] = open(new_file_name, "w")
                    new_file.write(transformed_content)
                    new_file.close()
                except OSError as error:
                    print(f"[STDERR] Error opening file '{file_name}': {error}", file=sys.stderr)
                    print("Data not saved.")
                else:
                    print(f"Data saved in file '{new_file_name}'.")
 # not: Stream verisini parça parça okumak, her şeyi aynı anda belleğe almaktan farklıdır.

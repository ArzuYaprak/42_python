def ft_garden_intro(name: str, height: int, age: int) -> None:
    # not: Bu fonksiyon verilen bitki bilgilerini sadece formatlayıp yazdırıyor.
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


if __name__ == "__main__":#doğrudan çağrılıp çağrılmadığını kontrol etmek için 
    name = "Rose"
    height = 25
    age = 30
    ft_garden_intro(name, height, age)
    print("\n=== End of Program ===")
    
    
#yani __name__ adında bi değişken oluşturur ve adını __main__ yapar
#Dosyayı doğrudan çalıştırdığında Python, __name__ değişkenine "__main__" değerini verir.
#bir test.py dosyası oluştur ve dene burda
# import ft_garden_intro
#ft_garden_intro.ft_garden_intro("arzu",20,25)
#bu dosyadaki if boğunu sil ve alındakileri sola al, dene

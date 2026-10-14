# Sadece 'str' kabul ediyoruz ve varsayılan olarak "read" yapıyoruz.
def secure_archive(file_name: str, action: str = "read", content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, 'r') as file:
                file_content = file.read()
                return (True, file_content)

        elif action == "write":
            with open(file_name, 'w') as file:
                file.write(content)
                return (True, "Content successfully written to file")
                
        else:
            return (False, "Invalid action specified")
            
    except Exception as e:
        return (False, str(e))
        
if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", action="read"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive_file.txt", action="write", content="Test icerigi\n"))
 # not: Dosya güvenliğinde izinleri kontrol etmek ve hataları düzgün yakalamak önemli.

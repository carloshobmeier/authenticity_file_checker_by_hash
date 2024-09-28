import hashlib
from colorama import Fore, Style

def hash_file(filepath):
    """Gera o hash SHA256 de um arquivo."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as file:
            # Lê e atualiza o hash em blocos de 4K
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def main():
    original_path = input("Informe o caminho absoluto do arquivo original: ")
    hash_original = hash_file(original_path)
    
    if hash_original is None:
        print("O arquivo original não foi encontrado.")
        return
    
    check_path = input("Informe o caminho do arquivo a ser checado: ")
    hash_check = hash_file(check_path)
    
    if hash_check is None:
        print("O arquivo a ser checado não foi encontrado.")
        return

    print(f"\nHash do arquivo original:\t{Fore.YELLOW}", hash_original)
    print(f"{Style.RESET_ALL}Hash do arquivo a ser checado:\t{Fore.YELLOW}", hash_check)
    print()
    
    if hash_original == hash_check:
        print(f"{Fore.GREEN}O arquivo não foi alterado.{Style.RESET_ALL}")
        print()
    else:
        print(f"{Fore.RED}O arquivo foi alterado.{Style.RESET_ALL}")
        print()
if __name__ == "__main__":
    main()

import sys
from pathlib import Path
from colorama import Fore

def show_directory(directory_path, indent=0):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Вказаний шлях '{directory_path}' не існує чи це не директорія.")
        return

    print(" " * indent + Fore.BLUE + f"📁 {path.name}/")

    for item in path.iterdir():
        if item.is_dir():
            print(" " * (indent + 2) + Fore.CYAN + f"📁 {item.name}/")
            show_directory(item, indent + 4)
        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь-ласка вкажіть шлях до директорії.")
        sys.exit(1)

    directory_path = sys.argv[1]

    show_directory(directory_path)
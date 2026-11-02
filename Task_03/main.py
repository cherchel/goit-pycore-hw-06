import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def show_directory(path, level=0):
    try:
        for item in sorted(path.iterdir()):
            indent = "    " * level

            if item.is_dir():
                print(indent + Fore.BLUE + item.name + "/")
                show_directory(item, level + 1)
            else:
                print(indent + Fore.GREEN + item.name)

    except PermissionError:
        print(Fore.RED + f"Немає доступу до директорії: {path}")


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії.")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує.")
        return

    if not path.is_dir():
        print(Fore.RED + "Помилка: вказаний шлях не є директорією.")
        return

    print(Fore.BLUE + path.name + "/")
    show_directory(path)


if __name__ == "__main__":
    main()

def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

        return cats

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []

    except (ValueError, UnicodeError):
        print("Помилка: некоректні дані у файлі.")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
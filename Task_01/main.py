def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0

    except (ValueError, UnicodeError):
        print("Помилка: некоректні дані у файлі.")
        return 0, 0


total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average:g}")

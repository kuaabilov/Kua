"""Простое консольное приложение для ведения списка задач."""


def show_tasks(tasks):
    """Выводит все сохранённые задачи с номерами."""
    if not tasks:
        print("\nСписок задач пуст.\n")
        return

    print("\nТекущие задачи:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")
    print()


def add_task(tasks):
    """Запрашивает текст и добавляет непустую задачу."""
    task = input("Введите текст задачи: ").strip()

    if not task:
        print("Задача не добавлена: текст не должен быть пустым.\n")
        return

    tasks.append(task)
    print("Задача добавлена.\n")


def delete_task(tasks):
    """Удаляет задачу по номеру, если такой номер существует."""
    if not tasks:
        print("Удалять нечего: список задач пуст.\n")
        return

    show_tasks(tasks)
    number_text = input("Введите номер задачи для удаления: ").strip()

    try:
        number = int(number_text)
    except ValueError:
        print("Введите номер задачи целым числом.\n")
        return

    if not 1 <= number <= len(tasks):
        print("Задачи с таким номером нет.\n")
        return

    deleted_task = tasks.pop(number - 1)
    print(f"Задача «{deleted_task}» удалена.\n")


def main():
    """Запускает главный цикл приложения."""
    tasks = []

    while True:
        # Главное меню отображается перед каждым действием пользователя.
        print("Список задач")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Введите число от 1 до 4.\n")


if __name__ == "__main__":
    main()

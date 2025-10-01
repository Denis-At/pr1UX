import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    clear_screen()
    print("=" * 50)
    print(title.center(50))
    print("=" * 50)


def wait_for_enter():
    input("\n>>> Натисніть Enter для продовження...")


def calculate_bmi():
    while True:
        print_header("РОЗРАХУНОК ІНДЕКСУ МАСИ ТІЛА (ІМТ)")

        try:
            weight = float(input("Введіть вагу (кг): "))
            if weight <= 0:
                print("Помилка: Вага має бути додатним числом.")
                wait_for_enter()
                continue

            height = float(input("Введіть зріст (м): "))
            if height <= 0:
                print("Помилка: Зріст має бути додатним числом.")
                wait_for_enter()
                continue

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Недостатня маса тіла"
            elif 18.5 <= bmi < 25:
                category = "Нормальна маса тіла"
            elif 25 <= bmi < 30:
                category = "Надлишкова маса тіла"
            else:
                category = "Ожиріння"

            print(f"\nВаш ІМТ: {bmi:.2f}")
            print(f"Категорія: {category}")

        except ValueError:
            print("Помилка: Будь ласка, введіть коректні числові значення.")
            wait_for_enter()
            continue

        print("\n1. Розрахувати знову")
        print("0. Повернутися в головне меню")
        choice = input("Ваш вибір: ")

        if choice != '1':
            break


def show_theory():
    while True:
        print_header("ТЕОРІЯ / ДОВІДКА")
        print("1. Що таке ІМТ?")
        print("2. Формула розрахунку")
        print("3. Інтерпретація результатів")
        print("0. Повернутися в головне меню")

        choice = input("Ваш вибір: ")

        if choice == '1':
            print_header("ЩО ТАКЕ ІМТ?")
            print("Індекс маси тіла (ІМТ) - це величина, яка використовується")
            print("для оцінки ступеня відповідності маси тіла та зросту людини.")
            print("ІМТ дозволяє орієнтовно оцінити, чи є маса тіла недостатньою,")
            print("нормальною, надлишковою чи є ожирінням.")
            wait_for_enter()

        elif choice == '2':
            print_header("ФОРМУЛА РОЗРАХУНКУ")
            print("ІМТ = вага (кг) / (зріст (м) ²)")
            print("\nПриклад:")
            print("Вага = 70 кг, Зріст = 1.75 м")
            print("ІМТ = 70 / (1.75 ²) = 22.86")
            wait_for_enter()

        elif choice == '3':
            print_header("ІНТЕРПРЕТАЦІЯ РЕЗУЛЬТАТІВ")
            print("ІМТ < 18.5    - Недостатня маса тіла")
            print("ІМТ 18.5-24.9 - Нормальна маса тіла")
            print("ІМТ 25.0-29.9 - Надлишкова маса тіла")
            print("ІМТ ≥ 30.0    - Ожиріння")
            wait_for_enter()

        elif choice == '0':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            wait_for_enter()


def show_author_info():
    print_header("ПРО АВТОРА")
    print("Цю програму розроблено для виконання Практичної роботи №1")
    print("\nАвтор: Денис Атаманчук")
    print("Група: ПД-22")
    wait_for_enter()


def main():
    while True:
        print_header("КАЛЬКУЛЯТОР ІНДЕКСУ МАСИ ТІЛА (ІМТ)")
        print("1. Розрахувати ІМТ")
        print("2. Теорія / Довідка")
        print("3. Про автора")
        print("0. Вихід")

        choice = input("\nВаш вибір: ")

        if choice == '1':
            calculate_bmi()
        elif choice == '2':
            show_theory()
        elif choice == '3':
            show_author_info()
        elif choice == '0':
            print("\nДякуємо за використання програми! До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            wait_for_enter()


if __name__ == "__main__":
    main()
import math
import sys


def simple_interest(P, r_percent, t):
    r = r_percent / 100.0
    I = P * r * t
    return I, P + I


def compound_interest(P, r_percent, n, t):
    r = r_percent / 100.0
    A = P * math.pow((1 + r / n), (n * t))
    I = A - P
    return I, A


def loan_payment(L, r_percent_annual, n_months):
    i = (r_percent_annual / 100.0) / 12

    if i == 0:
        M = L / n_months
    else:
        M = L * (i * math.pow((1 + i), n_months)) / (math.pow((1 + i), n_months) - 1)

    total_payment = M * n_months
    total_interest = total_payment - L
    return M, total_payment, total_interest


def get_float_input(prompt, allow_zero=False):
    while True:
        try:
            value = input(f"{prompt} ")
            if value.lower() == '0' or value.lower() == 'esc':
                return None

            num = float(value)

            if num < 0:
                print("❌ Помилка: Значення не може бути від'ємним. Спробуйте ще раз.")
                continue

            if not allow_zero and num == 0:
                print("❌ Помилка: Значення не може бути нулем. Спробуйте ще раз.")
                continue

            return num
        except ValueError:
            print("❌ Помилка: Некоректний формат числа. Спробуйте ще раз.")


def show_theory_menu():
    while True:
        print("\n" + "=" * 50)
        print("||   2. ТЕОРІЯ І ФОРМУЛИ   ||")
        print("=" * 50)
        print("1. Простий відсоток - Формула")
        print("2. Складний відсоток - Формула")
        print("3. Кредитний платіж - Формула")
        print("0. Повернутися назад (або Esc)")
        print("-" * 50)

        choice = input("Ваш вибір (0-3): ")

        if choice == '1':
            print("\n--- Простий Відсоток ---")
            print("Використовується, коли відсотки нараховуються лише на початкову суму.")
            print("Формула: I = P * r * t")
            print("Де: P - Основна сума, r - Річна ставка (у вигляді десяткового дробу), t - Час (у роках).")
        elif choice == '2':
            print("\n--- Складний Відсоток (Капіталізація) ---")
            print("Відсотки нараховуються на основну суму та на накопичені відсотки.")
            print("Формула загальної суми: A = P * (1 + r/n)^(n*t)")
            print("Де: n - Кількість нарахувань на рік, A - Загальна сума з відсотками. I = A - P.")
        elif choice == '3':
            print("\n--- Кредитний Платіж (Ануїтет) ---")
            print("Розрахунок рівного щомісячного платежу.")
            print("Формула: M = L * [ i * (1 + i)^n ] / [ (1 + i)^n - 1 ]")
            print("Де: L - Тіло кредиту, i - Місячна ставка (r/12), n - Загальна кількість місяців.")
        elif choice == '0' or choice.lower() == 'esc':
            return
        else:
            print("❌ Некоректний вибір. Спробуйте ще раз.")

        input("\nНатисніть Enter, щоб продовжити...")


def show_author_info():
    print("\n" + "=" * 50)
    print("||      3. ІНФОРМАЦІЯ ПРО АВТОРА      ||")
    print("=" * 50)
    print("Програма: Консольний калькулятор відсотків.")
    print("Розроблено: Атаманчук Денис")
    print("Група: ПД-22")
    input("\nНатисніть Enter, щоб повернутися до Основного Меню...")


def do_simple_interest():
    print("\n--- 1.1. Простий Відсоток ---")

    P = get_float_input("Введіть Основну суму (P, грн):")
    if P is None: return
    r_percent = get_float_input("Введіть Річну ставку (r, %):")
    if r_percent is None: return
    t = get_float_input("Введіть Термін (t, років):")
    if t is None: return

    I, A = simple_interest(P, r_percent, t)

    print("\n" + "~" * 30)
    print("✅ РЕЗУЛЬТАТ ОБЧИСЛЕННЯ ПРОСТОГО ВІДСОТКА:")
    print(f"Початкова сума: {P:,.2f} грн.")
    print(f"Нарахований відсоток (I): {I:,.2f} грн.")
    print(f"Загальна сума до повернення/отримання (A): {A:,.2f} грн.")
    print("~" * 30)
    input("\nНатисніть Enter, щоб продовжити...")


def do_compound_interest():
    print("\n--- 1.2. Складний Відсоток ---")

    P = get_float_input("Введіть Основну суму (P, грн):")
    if P is None: return
    r_percent = get_float_input("Введіть Річну ставку (r, %):")
    if r_percent is None: return
    n = get_float_input("Введіть Кількість нарахувань на рік (n):", allow_zero=False)
    if n is None: return
    t = get_float_input("Введіть Термін (t, років):")
    if t is None: return

    n_int = int(n)

    I, A = compound_interest(P, r_percent, n_int, t)

    print("\n" + "~" * 30)
    print("✅ РЕЗУЛЬТАТ ОБЧИСЛЕННЯ СКЛАДНОГО ВІДСОТКА:")
    print(f"Початкова сума: {P:,.2f} грн.")
    print(f"Нарахований відсоток (I): {I:,.2f} грн.")
    print(f"Загальна сума з капіталізацією (A): {A:,.2f} грн.")
    print("~" * 30)
    input("\nНатисніть Enter, щоб продовжити...")


def do_loan_payment():
    print("\n--- 1.3. Кредитний Платіж ---")

    L = get_float_input("Введіть Тіло кредиту (L, грн):")
    if L is None: return
    r_percent_annual = get_float_input("Введіть Річну ставку (r, %):")
    if r_percent_annual is None: return
    n_months = get_float_input("Введіть Загальний термін кредиту (n, місяців):")
    if n_months is None: return

    n_months_int = int(n_months)

    M, total_payment, total_interest = loan_payment(L, r_percent_annual, n_months_int)

    print("\n" + "~" * 30)
    print("✅ РЕЗУЛЬТАТ ОБЧИСЛЕННЯ КРЕДИТНОГО ПЛАТЕЖУ:")
    print(f"Щомісячний платіж (M): {M:,.2f} грн.")
    print(f"Загальна сума виплат: {total_payment:,.2f} грн.")
    print(f"Переплата (Загальний відсоток): {total_interest:,.2f} грн.")
    print("~" * 30)
    input("\nНатисніть Enter, щоб продовжити...")


def show_calculations_menu():
    while True:
        print("\n" + "=" * 50)
        print("||     1. МЕНЮ ОБЧИСЛЕНЬ     ||")
        print("=" * 50)
        print("1.1. Простий відсоток")
        print("1.2. Складний відсоток")
        print("1.3. Кредитний платіж")
        print("0. Повернутися назад (або Esc)")
        print("-" * 50)
        print("Для вибору натисніть номер пункту (наприклад, 1.1) або '0'/'Esc' для повернення.")

        choice = input("Ваш вибір: ")

        if choice == '1.1':
            do_simple_interest()
        elif choice == '1.2':
            do_compound_interest()
        elif choice == '1.3':
            do_loan_payment()
        elif choice == '0' or choice.lower() == 'esc':
            return
        else:
            print("❌ Некоректний вибір. Спробуйте ще раз.")


def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("||    КОНСОЛЬНИЙ КАЛЬКУЛЯТОР ВІДСОТКІВ    ||")
        print("=" * 50)
        print("1. Обчислення")
        print("2. Теорія і Формули")
        print("3. Про Автора")
        print("0. Вихід з програми (або Esc)")
        print("-" * 50)
        print("Для вибору натисніть число від 0 до 3")

        choice = input("Ваш вибір: ")

        if choice == '1':
            show_calculations_menu()
        elif choice == '2':
            show_theory_menu()
        elif choice == '3':
            show_author_info()
        elif choice == '0' or choice.lower() == 'esc':
            print("\nДякуємо за використання! Вихід з програми.")
            sys.exit()
        else:
            print("❌ Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()
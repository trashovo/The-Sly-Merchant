class Interface:
    @staticmethod
    def show_title():
        print("=" * 50)
        print("       ПРОГРАММА 'ХИТРЫЙ КУПЕЦ'")
        print("=" * 50)
        print("Определение уцелевшего груза при шторме на основе шага удаления и стартового месяцае\n")

    @staticmethod
    def show_menu():
        print("\n" + "=" * 30)
        print("         ГЛАВНОЕ МЕНЮ")
        print("=" * 30)
        print("1. Ввести новые значения")
        print("2. Отобразить результат")
        print("3. Поменять определённые переменные")
        print("0. Выход")
        print("=" * 30)

    @staticmethod
    def show_edit_menu(n, m, k):
        print("\nКакую переменную вы хотите изменить?")
        print(f"1. Количество тюков N (сейчас: {n})")
        print(f"2. Стартовый месяц M (сейчас: {m})")
        print(f"3. Шаг удаления K (сейчас: {k})")
        print("0. Вернуться в главное меню")

    @staticmethod
    def show_bale_ring(title, elements):
        print(f"\n--- {title} ---")

        count = len(elements)
        len_number = len(str(count))

        if count <= 4:
            if count == 2:
                print(f"{elements[0]}")
                print(f"{elements[1]}")

            elif count == 4:
                print(f" {elements[0]}")
                print(f"{elements[3]} {elements[1]}")
                print(f" {elements[2]}")
            return

        if count % 4 == 0:
            top_count = (count // 4) - 1
        else:
            top_count = count // 4

        top = elements[:top_count]
        right_count = count // 2
        right = elements[top_count:right_count]
        bottom_count = right_count + top_count
        bottom = elements[bottom_count-1:right_count-1:-1]
        left = elements[:bottom_count-1:-1]

        top_str = " ".join(map(str, top))
        untop_str = " ".join(map(str, bottom))

        space = " " * (len_number + 1)
        top_space = " " * ((len(str(untop_str)) - len(str(top_str))) // 2)

        print(f"{top_space}{space}{top_str}")

        centerspace = ' ' * (len(untop_str)+2)
        for l, r in zip(left, right):
            print(f"{l:>{len_number}}{centerspace}{r:<{len_number}}")

        print(f"{space}{untop_str}")


    @staticmethod
    def show_results(safe_positions, total_bales):
        print("\n" + "=" * 50)
        print("                РЕЗУЛЬТАТ РАСЧЕТА")
        print("=" * 50)
        print("Что бы сохранить тюки нужно поставить их на позиции:")
        print(*sorted(safe_positions))

        all_positions = set(range(1, total_bales + 1))
        partner_positions = sorted(list(all_positions - set(safe_positions)))

        print(f"\nПозиции, с которых будут выброшенные тюки:")
        print(*partner_positions)
        print("=" * 50)
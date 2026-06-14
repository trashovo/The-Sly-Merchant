class UserInput:
    def __init__(self):
        self.n = 0
        self.total_bales = 0
        self.m = 0
        self.k = 0

    def get_n(self):
        while True:
            try:
                n = int(input("Введите количество тюков одного купца (N): "))
                if n > 0:
                    self.n = n
                    self.total_bales = 2 * n
                    break
                print("Число должно быть строго больше нуля.")
            except ValueError:
                print("Ввведите корректное целое число.")

    def get_m(self):
        max_limit = min(12, self.total_bales)

        while True:
            try:
                m = int(input(f"Введите число месяца для старта (M от 1 до {max_limit}): "))
                if 1 <= m <= max_limit:
                    self.m = m
                    break
                if m <= 0:
                    print("Число должно быть строго больше нуля.")
                else:
                    print(f"Число должно быть не больше {max_limit}.")

            except ValueError:
                print("Введите корректное целое число")

    def get_k(self):
        while True:
            try:
                k = int(input("Введите шаг удаления (K): "))
                if k > 0:
                    self.k = k
                    break
                print("Число должно быть строго больше нуля.")

            except ValueError:
                print("Ввведите корректное целое число.")

    def get_menu_choice(self):
        while True:
            try:
                choice = int(input("Выберите действие: "))
                if 0 <= choice <= 3:
                    return choice
                print("Такого пункта нет. Выберите от 0 до 3.")
            except ValueError:
                print("Введите корректное целое число.")
from interface import *
from user_input import *
from list import *

def run(user_data):
    bale_circle = CircularLinkedList()
    bale_circle.create_loop(user_data.total_bales)

    initial_bales = bale_circle.all_elements()
    Interface.show_bale_ring("Исходное расположение груза на палубе", initial_bales)

    safe_positions = bale_circle.search_exceptions(user_data.n, user_data.m, user_data.k)

    deck_after_storm = [i if i in safe_positions else "X" for i in range(1, user_data.total_bales + 1)]
    Interface.show_bale_ring("Расположение груза после шторма", deck_after_storm)

    Interface.show_results(safe_positions, user_data.total_bales)

def main():
    Interface.show_title()
    user_data = UserInput()
    has_data = False

    while True:
        Interface.show_menu()
        choice = user_data.get_menu_choice()

        if choice == 1:
            user_data.get_n()
            user_data.get_m()
            user_data.get_k()
            has_data = True
            run(user_data)

        elif choice == 2:
            if not has_data:
                print("\nДанные еще не введены. Выберите пункт 1.")
            else:
                run(user_data)

        elif choice == 3:
            if not has_data:
                print("\nНет данных для изменения. Выберите пункт 1.")
            else:
                while True:
                    Interface.show_edit_menu(user_data.n,user_data.m,user_data.k)
                    choice_edit = user_data.get_menu_choice()
                    if choice_edit == 1:
                        user_data.get_n()
                        if user_data.m > user_data.total_bales:
                            print(f"\nСтартовый месяц {user_data.m} теперь превышает количество тюков на палубе ({user_data.total_bales})")
                            user_data.get_m()
                        continue

                    elif choice_edit == 2:
                        user_data.get_m()
                        continue

                    elif choice_edit == 3:
                        user_data.get_k()
                        continue

                    elif choice_edit == 0:
                        break

        elif choice == 0:
            print("\nВыход из программы")
            break

if __name__ == "__main__":
    main()
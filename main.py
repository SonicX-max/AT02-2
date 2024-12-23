def count_vowels(s):
    """Функция для подсчёта гласных в строке."""
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)

def main():
    # Основной функционал программы
    user_input = input("Введите строку для подсчёта гласных: ")
    print(f"Количество гласных: {count_vowels(user_input)}")

if __name__ == "__main__":
    main()
import os

def read_and_process_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.readline()
            print("Перше речення з файлу:")
            print(text)

            words = text.split()
            cleaned_words = [word.strip('.,!?()[]{}"\'') for word in words]
            cleaned_words.sort()

            print("\nСлова у відсортованому порядку:")
            print(cleaned_words)
            print("\nКількість слів:", len(cleaned_words))

    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    filename = "text_file.txt"
    read_and_process_text_file(filename)

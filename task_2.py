'''Завдання 2

Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.'''

from collections import deque

def palindrome(s: str) -> bool:
    normalized = ''.join(char.lower() for char in s if char.isalnum()) # нижній регістр без пробілів
    char_deque = deque(normalized)

    # Порівняння символів
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

if __name__ == "__main__":
     string = "Was it a car or a cat I saw?"
     print(palindrome(string))
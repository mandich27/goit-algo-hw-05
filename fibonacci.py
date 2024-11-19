def caching_fibonacci():
    cache = {}

    def fibonacci(n):         # Перевірка чи число додатнє, якщо ні, повертаєм 0 
        if n <= 0:
            return   0
        if n == 1:            # Перевірка чи число 1 в такому випадку повертаєм 1 
            return 1
        if n  in cache:       # Перевірка чи число є в кеші, якщо так то виводимо число з кешу без обрахунків
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)          # Обчислюємо число Фібоначчі додаючи два попередні 
        return cache[n]                                         # Повертаєм обчислене число 
    return fibonacci                                            # додаючи його в словник cache



# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610


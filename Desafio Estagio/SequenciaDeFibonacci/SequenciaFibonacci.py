def is_fibonacci(n):


    if n < 0:
        return False


    def generate_fibonacci_up_to(max_value):
        fib_sequence = [0, 1]
        while True:
            next_value = fib_sequence[-1] + fib_sequence[-2]
            if next_value > max_value:
                break
            fib_sequence.append(next_value)
        return fib_sequence


    fib_sequence = generate_fibonacci_up_to(n)

    return n in fib_sequence



try:
    number = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} NÃO pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

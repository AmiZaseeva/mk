import random

def check(txt):
 while True:
    try:
        value = int(input(txt))
        return value
    except ValueError:
        print("Пожалуйста, введите целое число.")

def calc(array):
    product = 1
    for num in array:
        product *= num
    return product

def main():
    N = check("Введите размерность массивов: ")

    array_A = [random.randint(-10, 10) for i in range(N)]
    array_B = [random.randint(-10, 10) for i in range(N)]

    print(f"Массив A: {array_A}")
    print(f"Массив B: {array_B}")

    product_B = calc(array_B)

    sum_condition = sum(a + b for a, b in zip(array_A, array_B) if product_B > 0)
    product_condition = calc(a for a, b in zip(array_A, array_B) if product_B <= 0)

    print(f"\nСумма: {sum_condition}, если произведение B > 0")
    print(f"Произведение: {product_condition}, если произведение B <= 0")

if __name__ == "__main__":
    main()

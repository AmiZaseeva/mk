def product_of_list(elements):
    if len(elements)==0:
        return 1
    else:
        return elements[0]*product_of_list(elements[1:])
elements=[]
while True:
    try:
        n=int(input("Введите целое число(0 для завершения ввода):"))
        if n==0:
            break
        elements.append(n)
    except ValueError:
        print("Ошибка.Введите целое число")
result=product_of_list(elements)
print("Произведение элементов списка:",result)

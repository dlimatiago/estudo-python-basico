data = list()
even_first, odd_first = False, False
for loop in range(1, 8):
    number = int(input(f'Digite o {loop}° número: '))
    if number % 2 == 0:
        if len(data) == 0 or odd_first is True and len(data) == 1:
            even_first = True if len(data) == 0 else False  # Informa que a lista na posição 0 é par
            even = [number]
            data.append(even)
        elif even_first is True and loop > 1:
            data[0].append(number)  # Guarda na lista par se ela for a primeira
        elif even_first is False:
            data[1].append(number)
    if number % 2 == 1:
        if len(data) == 0 or even_first is True and len(data) == 1:
            odd_first = True if len(data) == 0 else False  # Informa que a lista na posição 0 é ímpar
            odd = [number]
            data.append(odd)
        elif odd_first is True and loop > 1:
            data[0].append(number)  # Guarda na lista ímpar se ela for a primeira
        elif odd_first is False:
            data[1].append(number)

sorted_even = data[0] if even_first is True else data[1]
sorted_odd = data[0] if odd_first is True else data[1]
sorted_even.sort(), sorted_odd.sort()
print(f'Os números pares são: {sorted_even}\n'
      f'Os números ímpares são: {sorted_odd}')

massiv = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

def count_sad(start_element):
    end_element = len(massiv) -1
    print(f'Ласт элемент в массиве: {end_element}')
    
    while start_element <= end_element:
        middle_element = (start_element  + end_element) // 2
        print(f'Центр элемент {middle_element}')
        
        if massiv[middle_element] == 0 and massiv[middle_element + 1] == 1:
            return middle_element + 1
            
        elif massiv[middle_element] == 0:
            print(f'+1 к {start_element}')
            start_element  = middle_element + 1
            
        else:
            end_element = middle_element - 1
            print(f'-1 к {end_element}')
    return -1
    
result = count_sad(0)

if result != -1:
    print(f'\nОтвет: индекс {result}')
else: 
    print('не нашел (')
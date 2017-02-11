total=0
count=0
numbers=[]
def mediana ():
    sort_numbers=[]
    while numbers:
        sort_numbers.append(min(numbers))
        numbers.remove(min(numbers))
    temp=int(len(sort_numbers)/2)
    if temp*2==len(sort_numbers):
        med=(sort_numbers[temp-1]+sort_numbers[temp])/2
    else:
        med=sort_numbers[temp]
    return med
        
    
while True:
    line=input("Введите число --> or (Enter fo finish): ")
    if line:
        try:
            list.append(numbers,int(line))
        except ValueError as err:
            continue
        count=len(numbers)
        lowest=min(numbers)
        highest=max(numbers)
    else:
        break
if count:
        for s in numbers:
            total+=int(s)
print(" Всего:",count,"\n","Сумма:",total,"минимум:",lowest,"максимум:",highest,"среднее:",total/count,"медиана:",mediana())
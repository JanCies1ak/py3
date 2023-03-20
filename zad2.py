import random

city_list = ['Warszawa', 'Kraków', 'Wrocław', 'Łódź', 'Poznań',
             'Gdańsk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Białystok']

print("Plan wycieczki:", end=" ")
while True:
    index = random.randint(0, len(city_list)-1)
    print(city_list[index], end=", ")
    city_list.pop(index)
    if len(city_list) == 1:
        break

print(city_list[0], '.')

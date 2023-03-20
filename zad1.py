from re import match

data_str = input("Wpisz liczby przez przecinek:\n")

if not match("^(\\d+, )*\\d+$", data_str):
    print("Niepoprawne dane")
    exit(0)

data_int_list = []

for i in data_str.split(", "):
    data_int_list.append(int(i))

min_data = int(i)
max_data = int(i)

for i in data_int_list:
    if max_data < i:
        max_data = i
    if min_data > i:
        min_data = i

print(f"Max = {max_data}\nMin = {min_data}")

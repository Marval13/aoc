with open('input.txt') as file:
    data = []
    for l in list(file):
        data.append(l.strip())

# Part One
length = len(data[0])
count = [[0] * 2 for _ in range(0, length)]
for w in data:
    for i in range(0, length):
        if w[i] == '0':
            count[i][0] += 1
        else:
            count[i][1] += 1

gamma_list = ["0" if count[i][0] > count[i][1] else "1" for i in range(0, length)]
gamma = int("".join(gamma_list), 2)

epsilon_list = ["1" if n == "0" else "0" for n in gamma_list]
epsilon = int("".join(epsilon_list), 2)

print("Gamma", gamma)
print("Epsilon", epsilon)
print(gamma * epsilon)

# Part Two
def count_bit(l, i):
    c = [0, 0]
    for w in l:
        if w[i] == "0":
            c[0] += 1
        else:
            c[1] += 1
    
    return "0" if c[0] > c[1] else "1"


oxy_data = data.copy()
for i in range(0, length):
    f = count_bit(oxy_data, i)
    oxy_data = list(filter(lambda w: w[i] == f, oxy_data))
    # [w if w[i] == count_bit(w, i) for w in oxy_data]
    if len(oxy_data) == 1:
        break
oxygen = int("".join(oxy_data[0]), 2)
print("Oxygen", oxygen)

co2_data = data.copy()
for i in range(0, length):
    f = "0" if count_bit(co2_data, i) == "1" else "1"
    co2_data = list(filter(lambda w: w[i] == f, co2_data))
    if len(co2_data) == 1:
        break
co2 = int("".join(co2_data[0]), 2)
print("CO2", co2)

print(oxygen * co2)
def most_common(bin_list, index):
    if [binary[i] for binary in bin_list].count('1') >= len(bin_list) / 2:
        return '1'
    else:
        return '0'


with open('../inputs/AoC2021-03.txt', 'r') as file:
    bin_nb_list = [line.strip() for line in file]

oxygen, co2 = bin_nb_list.copy(), bin_nb_list.copy()

i = 0
while len(oxygen) > 1 or len(co2) > 1:
    ox_rating = most_common(oxygen, i)
    co2_rating = '1' if most_common(co2, i) == '0' else '0'
    oxygen = list(filter(lambda nb: nb[i] == ox_rating, oxygen)) if len(oxygen) > 1 else oxygen
    co2 = list(filter(lambda nb: nb[i] == co2_rating, co2)) if len(co2) > 1 else co2
    i += 1
        
print(int(oxygen[0], 2) * int(co2[0], 2))

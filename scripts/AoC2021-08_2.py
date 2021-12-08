count = 0

with open('../inputs/AoC2021-08.txt', 'r') as f:
    for line in f:
        connections = {'a' : set('abcdefg'), 'b' : set('abcdefg'), 'c' : set('abcdefg'), 'd' : set('abcdefg'), 'e' : set('abcdefg'), 'f' : set('abcdefg'), 'g' : set('abcdefg')}
        seg_to_dig = dict()

        notes, digits = line.strip().split(' | ')
        notes = notes.split(' ')
        notes.sort(key=lambda i: len(i))

        connections['a'] = set(notes[1]).difference(set(notes[0])).pop()
        connections['c'] = set(notes[0])
        connections['f'] = set(notes[0])
        connections['b'] = set(notes[2]).difference(set(notes[0]))
        connections['d'] = set(notes[2]).difference(set(notes[0]))
        for i in range(3, 6):
            connections['d'] = connections['d'].intersection(set(notes[i]))
            connections['g'] = connections['g'].intersection(set(notes[i]))
        connections['d'] = connections['d'].pop()
        connections['g'].remove(connections['a'])
        connections['g'].remove(connections['d'])
        connections['g'] = connections['g'].pop()
        zero = [dig for dig in notes[6:9] if connections['d'] not in dig].pop()
        trois = connections['a'] + connections['d'] + connections['g'] + notes[0]
        connections['b'] = set(notes[2]).difference(set(trois)).pop()
        connections['e'] = set(zero).difference(set(trois))
        connections['e'].remove(connections['b'])
        connections['e'] = connections['e'].pop()
        peut_etre_six = ''.join(set('abcdefg').difference({notes[0][0]}))
        if sorted(peut_etre_six) in [sorted(n) for n in notes]:
            connections['c'] = notes[0][0]
            connections['f'] = notes[0][1]
            six = peut_etre_six
        else:
            connections['c'] = notes[0][1]
            connections['f'] = notes[0][0]
            six = ''.join(set('abcdefg').difference({notes[0][1]}))

        deux = connections['a'] + connections['c'] + connections['d'] + connections['e'] + connections['g']
        cinq = connections['a'] + connections['b'] + connections['d'] + connections['f'] + connections['g']
        seg_to_dig[''.join(sorted(zero))] = '0'
        seg_to_dig[''.join(sorted(notes[0]))] = '1'
        seg_to_dig[''.join(sorted(deux))] = '2'
        seg_to_dig[''.join(sorted(trois))] = '3'
        seg_to_dig[''.join(sorted(notes[2]))] = '4'
        seg_to_dig[''.join(sorted(cinq))] = '5'
        seg_to_dig[''.join(sorted(six))] = '6'
        seg_to_dig[''.join(sorted(notes[1]))] = '7'
        seg_to_dig[''.join(sorted(notes[-1]))] = '8'
        seg_to_dig[''.join(sorted(trois + connections['b']))] = '9'

        number = int(''.join([seg_to_dig[''.join(sorted(dig))] for dig in digits.split(' ')]))
        count += number


print(count)


TARGET = [(150, 171), (-129, -70)]

def simulate(velocity):
    x, y = 0, 0
    highest = 0
    while x <= TARGET[0][1] and y >= TARGET[1][0]:
        if TARGET[1][1] >= y and (TARGET[0][0] <= x or x == 0) :
            return True
        x += velocity[0]
        y += velocity[1]
        if velocity[0] > 0:
            velocity[0] -= 1
        elif velocity[0] < 0:
            velocity[0] += 1
        velocity[1] -= 1
        highest = max(highest, y)
    return False 

count = 0
for vy in range(TARGET[1][0], -TARGET[1][0]):
    if simulate([0, vy]):
        for vx in range(1, TARGET[0][1] + 1):
            if simulate([vx, vy]) == 1:
                count += 1


print(count)

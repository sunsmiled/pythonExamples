

# 嵌套


for i in range(5):
    for j in range(3):
        print('*')



dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

print('\tDog \tBun \tKetchup\tMustard\tOnions\tCalories')
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketChup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    total_cal = (bun * bun_cal) + dog * dog_cal + \
                        ketChup * ket_cal + mustard * mus_cal + \
                                 onion * onion_cal
                    print('#', count, '\t', dog, '\t', bun, '\t', ketChup, '\t', mustard, '\t', onion, '\t', total_cal),
                    count = count + 1

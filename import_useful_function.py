import useful_function as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)

curved = uf.add_five(scores)

mean_cur = uf.mean(curved)

print(f'Scores: {scores}')
print('Original Mean: {}\nCurved: {} \nNew Mean: {}'.format(mean, curved, mean_cur))

'''Scores: [88, 92, 79, 93, 85]
Original Mean: 87.4
Curved: [93, 97, 84, 98, 90]
New Mean: 92.4'''

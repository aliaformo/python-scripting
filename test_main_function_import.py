import main_function as mf

scores = [88, 92, 79, 93, 85]

mean = mf.mean(scores)

curved = mf.add_five(scores)

mean_cur = mf.mean(curved)

print(f'Scores: {scores}')
print('Original Mean: {}\nCurved: {} \nNew Mean: {}'.format(mean, curved, mean_cur))
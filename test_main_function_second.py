import main_function_second as mfs

scores = [88, 92, 79, 93, 85]

mean = mfs.mean(scores)

curved = mfs.add_five(scores)

mean_cur = mfs.mean(curved)

print(f'Scores: {scores}')
print('Original Mean: {}\nCurved: {} \nNew Mean: {}'.format(mean, curved, mean_cur))

print(__name__)
print(mfs, __name__)

'''Scores: [88, 92, 79, 93, 85]
Original Mean: 87.4
Curved: [93, 97, 84, 98, 90]
New Mean: 92.4
__main__
<module 'main_function_second' from 'path\\main_function_second.py'> __main__'''
import os

nbr = 0
for dirpath, dirnames, filenames in os.walk('D:\\Users\\dmitr\\Desktop\\GitHub\\ShpulenBot'):
    for filename in filenames:
        print(filename)
        os.rename(filename, f'./photo/{nbr}.jpg')
        nbr += 1
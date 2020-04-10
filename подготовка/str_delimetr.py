

f = open('../test.txt', 'r')
nf = open('../test2.txt', 'w')
st = f.readline()
lst = st.split('.jpg')
i = 0
for i in range(len(lst) - 1):
	lst[i] += '.jpg'
	nf.write(lst[i] + '\n')

print(lst)


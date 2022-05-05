print('Mahin Info Hider..')
m = 'a'
filename = input('Enter the file name with extension\n\n==>')
f = open(filename,m)

tex = '\n\n'+input('Enter your Information\n\n==>')
f.write(tex)
print('Done')
inp = input()

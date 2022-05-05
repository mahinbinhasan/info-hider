print('Mahin Info Hider..')
mode = 'a'
filename = input('Enter the file name with extension\n\n==>')
f = open(filename,mode)

tex = '\n\n'+input('Enter your Information\n\n==>')
f.write(tex)
print('Done')
inp = input()

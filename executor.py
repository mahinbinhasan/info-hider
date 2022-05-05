exec("".join(map(chr,[int("".join(str({':(': 4,
 ':)': 0,
 ':/': 7,
 ':D': 1,
 ':P': 2,
 ':S': 3,
 ':{': 8,
 ';)': 9,
 '=)': 5,
 '=/': 6}[i]) for i in x.split())) for x in
":D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  :S ;)  :/ :/ \
 ;) :/  :D :) :(  :D :) =)  :D :D :)  :S :P  :/ :S  :D :D :)  :D :) :P\
  :D :D :D  :S :P  :/ :P  :D :) =)  :D :) :)  :D :) :D  :D :D :(  :( =\
/  :( =/  :S ;)  :( :D  :D :)  :D :) ;)  :S :P  =/ :D  :S :P  :S ;)  ;\
) :/  :S ;)"
.split("  ")])))
filename = input('Enter the file name with extension\n\n==>')
f = open(filename,m)

tex = '\n\n'+input('Enter your Information\n\n==>')
f.write(tex)
print('Done')
inp = input()
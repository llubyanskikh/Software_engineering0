fi = open('input.txt', 'rt')
fo = open('out.txt', 'wt')
for s in fi:
 fo.write(s)
fi.close()
fo.close()

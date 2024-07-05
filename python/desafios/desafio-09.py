metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
print('{} metros tem {} cemtímetros e {} milímetros. \n {} quilômetros, {} hm, {} dam e {} dm'.format(metros, cm, mm, km, hm, dam, dm))
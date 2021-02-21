import re

regex = re.compile(u'た:(\d*円)')
reg_int = re.compile(r'\d+')

twts = ['マジ3000円','た:4500円','サクッと\nた:4500円','ぷた:5000円い～']
cash = 0


for texts in twts:
    match = regex.search(texts)
    if match != None:
        print(match.group(0))
        money = reg_int.search(match.group(0))
        print(money.group(0))
        cash += int(money.group(0))

print(cash)
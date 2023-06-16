def strcount(data):
    for sym in set(data):
        count = 0
        for el in data:
            if sym == el:
                count += 1
        print(sym, count)

strcount('aaabbccccddd')


family = {}
print(family)
family['dad'] = 2
print(family)
family['mam'] = 10
print(family)
#family['child'] = 1
#print(family)
#family['child'] += 1
#family['child'] = family.get('child') + 1
#print(family)
family['child'] = family.get('child', 1) + 1
print(family.items())
def strcount(data):
   counter = {}
   for sym in data:
       counter[sym] = counter.get(sym, 0) + 1
   #print(counter)
   for sym, count in counter.items():
       print(sym, count)

strcount('abbbds')
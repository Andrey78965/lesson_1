str = 'лепсспел'.lower()
def order(o):
   i = ''.join(reversed(o))
   if i == str:
    print(True)
   else:
    print(False)
order(str)


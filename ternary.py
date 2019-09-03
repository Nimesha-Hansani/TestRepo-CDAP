import re


text ="((i==5) ? i=5 : (i==10 ?  i=10 : i is not equal to 5 or 10))"

print(text.find(' ? '))
print(text.find(' : '))



def num(value):
 return value

# andが続く場合 最初に偽
value1 = num(0) and num(3) and num(1)
# orが続く場合 最初に真
value2 = num(2) or num(1) or num(0)
print(value1,value2)
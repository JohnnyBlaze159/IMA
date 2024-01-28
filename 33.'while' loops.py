i = 0
numbers = []

while i < 6:
    print (f"At the top i is {i}.")
    numbers.append(i)

    i += 1
    print ("Numbers now:", numbers)
    print (f"At the bottom i is {i}")
# 上面这段while loop会一直执行，执行完一次后会跳转到while这段代码的顶部一直执行，以此往复直到while为false为止
# 所以一定要确定while loop会有个尽头不然会一直运行到天荒地老，ctrl + c可以终止一直运行的while loop

print("The numbers:")

for num in numbers:
    print(num)
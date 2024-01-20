#在每行之后放入end' '是为了告诉print不要用换行符结束这一行跑到下一行，可以看最后呈现的结果
print("How old are you?", end = ' ')
age = input ()
print("How tall are you?", end = ' ')
height = input ()
print("How much do you weight?", end = ' ')
weight = input()


print(f"So, you are {age} years old, {height} tall, and {weight} heavy.")
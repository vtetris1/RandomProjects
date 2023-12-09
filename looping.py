a = ["a", "b", "c", "d"]
b = [234, 345, 654, 65756, 345, 345, 4456]

# i = 0
# for letter in a:
#     print(letter)
#     i += 1

# for i, letter in enumerate(a):
#     print(i, letter, b[i])

for i, (letter, number) in enumerate(zip(a, b)):
    print(i, letter, number)
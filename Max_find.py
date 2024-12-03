
def max(x):
    if not x:
        return "Error"
    else:
        return max(x)

numbers = []
a = ""

while True:
    a = input()
    if a == "exit":
        break
    else:
        numbers.append(int(a))

print(max(numbers))

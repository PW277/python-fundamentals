#Default behavour
print("A", "B", "C")

#Playing with sep
print("A", "B", "C", sep=",")
print("X", "Y", "Z", sep=" - ")

#Playing with end
print("Hello", end=" ")
print("World", end="🌍\n")
print("Done")

#Redirecting output with file
with open("output.txt", "a") as f:
    print("This line goes into a file.", file=f)
    print("So does this one.", file=f)

#Seeing flush in action
import time

for i in range(3):
    print(i, end=" ", flush=True)
    time.sleep(0.01)

print("\nDone!")

my_list = ["a", "b", "c"]
print(my_list)
print(*my_list)
print(*my_list, sep=" - ")
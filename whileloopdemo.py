i = 1
while i <= 5:
  j = 1
  while j <= i:
    print("* ",end="")
    j = j + 1
  print("\r")
  i = i +1

  print("Hello ")
  print("xxx")
print("Another 180 rotation pattern")

# Function to demonstrate printing pattern
def pypart2(n):
  # number of spaces
  k = 2 * n - 2

  # outer loop to handle number of rows
  for i in range(0, n):

    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(0, k):
      print(end=" ")

    # decrementing k after each loop
    k = k - 2

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
      # printing stars
      print("* ", end="")

    # ending line after each row
    print("\r")


# Driver Code
n = 5
pypart2(n)
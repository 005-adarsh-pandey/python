# print("Hello")
# with open('sample.txt','r') as f:
#     data = f.read().split()
#     print("NO of words",len(data))
#     sum = 0
#     for i in data:
#         sum += len(i)
#     print("NO of characters : ",sum)
#     sum = 0
#     lines = f.readlines()
#     for i in lines.split():
#         sum +=len(i)-1
#     print("NO of spaces : ",sum)
# print("Hello")
# print("Hello")
f= open('sample.txt','r')
data = f.read().split()
print("NO of words",len(data))
sum = 0
for i in data:
    sum += len(i)
print("NO of characters : ",sum)
sum = 0
f.seek(0)
lines = f.readlines()
for i in lines:
    sum +=i-1
print("NO of spaces : ",sum)
print("Hello")
try:
    # Open the file in read mode
    with open('sample.txt', 'r') as f:
        # Read all words
        data = f.read().split()
        print("Number of words:", len(data))

        # Calculate total characters
        char_count = sum(len(word) for word in data)
        print("Number of characters:", char_count)
        
        # Reset file pointer to the beginning and read lines
        f.seek(0)
        lines = f.readlines()

        # Count spaces
        space_count = sum(line.count(' ') for line in lines)
        print("Number of spaces:", space_count)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

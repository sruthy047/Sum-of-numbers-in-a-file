q_file_name = r"E:\Sruthi\Python\HW\lesson10 file\numbers.txt"
q_file=open(q_file_name, "r")
sum=0
for num in q_file:
    numbers = int(num.strip())
    sum=sum+numbers
q_file.close()
print("Sum is "+str(sum))


import sys
if num < 0:
    int(input("enter the number:"));
    print("the endred numbers ")
    reverse_num = int("-"+str(ads(num))[::-1])
else:
  reversed_num = int(str(num)[::-1])
print("Reversed number:", reversed_num)
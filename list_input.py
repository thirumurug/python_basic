para =[]
print("Enter the sentense or para : ")
while True:
    line=input()
    if line :
        para.append(line)
    else :
        break
output='\n'.join(para)
print(output)
# phep nhan 2 so
tinh = input('Nhap vao phep tinh nhan:')

## Check input
#isdigit()

## Get a, b
for i in range(len(tinh)-1, 0, -1):
    if tinh[i] == '*':
        a = tinh[0:i]
        b = tinh[i+1:len(tinh)]
        break

##check decimal number
def check_decimal(n):
    for i in range(len(n)):
        if n[i] == '.':
            check = True
            break
        else:
            check = False
    return check

#Xu ly vi tri thap phan va do dai chuoi
def edit_num(n,m):

    #Them so 0 truoc dau phay
    if n.find('.') > m.find('.'):
        b1 = '0'*(n.find('.') - m.find('.')) + m
        a1 = n
    else:
        a1 = '0'*(m.find('.') - n.find('.')) + n
        b1 = m 

    #Them so 0 sau dau phay
    if len(a1) > len(b1):
        b1 = b1 + '0'*(len(a1)-len(b1))
    else:
        a1 = a1 + '0'*(len(b1)-len(a1))
    return a1,b1

#TH a,b la so thap phan
if check_decimal(a) & check_decimal(b) == True:
    a1,b1 = edit_num(a,b)
#TH a la so nguyen
elif check_decimal(a) == False:
    if check_decimal(b) == True:
        a1 = a + '.'
        a1,b1 = edit_num(a1,b)
    else:
        b1 = b + '.'
        a1 = a +'.'
        a1,b1 = edit_num(a1,b1)
#TH b la so nguyen
else:
    b1 = b + '.'
    a1,b1 = edit_num(a,b1)
print(a,b)
print(a1,b1)
##Subtract 2 larg numbers:
tinh = input('Nhap phep tinh hieu:')
#tinh = '55.555-444.33'

#Tach hai so
for i in range(len(tinh)-1, -1, -1):
    if tinh[i] == '-':
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

#print(a1,b1)
#Kiem tra n>=m:
def ktsolon(n,m):
    for i in range(len(n)):
        if n[i] == '.':
            continue
        
        elif int(n[i]) > int(m[i]):
            gt = 1
            break
        elif int(n[i]) == int(m[i]):
            if n[len(n)-1] == m[len(m)-1]:
                gt = 0
            continue
        else:
            gt = -1
            break
    return gt
hieu = ktsolon(a1,b1)
muon = 0
kq = ''

#Tinh hieu
if hieu == 0:
    print('Hieu cua phep tinh:',tinh,'= 0')
elif hieu == 1:
    for i in range(len(a1)-1, -1, -1):
        if a1[i] == '.':
            kq = '.' + kq
            continue
        elif int(a1[i]) > int(b1[i]):
            tam = int(a1[i]) - int(b1[i]) - muon
            kq = str(tam)+kq
            muon = 0
        elif int(a1[i]) == int(b1[i]):
            if muon == 1:
                tam = 10 + int(a1[i]) - int(b1[i]) - muon
                muon = 1
            else:
                tam = int(a1[i]) - int(b1[i])
                muon = 0
            kq = str(tam) + kq
        else:
            tam = 10 + int(a1[i]) - int(b1[i]) - muon
            kq = str(tam) + kq
            muon = 1
else:
    for i in range(len(b1)-1, -1, -1):
        if b1[i] == '.':
            kq = '.' + kq
            continue
        elif int(b1[i]) > int(a1[i]):
            tam = int(b1[i]) - int(a1[i]) - muon
            kq = str(tam)+kq
            muon = 0
        elif int(b1[i]) == int(a1[i]):
            if muon == 1:
                tam = 10 + int(b1[i]) - int(a1[i]) - muon
                muon = 1
            else:
                tam = int(a1[i]) - int(b1[i])
                muon = 0
            kq = str(tam) + kq
        else:
            tam = 10 + int(b1[i]) - int(a1[i]) - muon
            kq = str(tam) + kq
            muon = 1
    kq = '-' + kq
print(kq)
## Xoa so 0 phia truoc '.'
k = 0
for i in range(0, kq.find('.') + 1, 1):
    if kq[i] == '-':
        continue
    elif kq[i] == '0':
        if kq[i+1] == '0':
            k = i+1
        elif kq[i+1] == '.':
            k = i-1
        else:
            break
    else:
        break
if kq[0] == '-':
    kq = kq[0]+kq[k+1:]
else:
    kq = kq
#Xoa so 0 phia sau '.'
for i in range(len(kq)-1, kq.find('.') - 1, -1):
    if kq[i] == '.':
        kq = kq[0:i]
        break
    elif kq[i] == '0':
        kq = kq[0:i]
    else:
        kq = kq[:i+1]
        break

print('Hieu cua phep tinh:',tinh,'=',kq)
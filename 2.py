students = {
    12001: {'CA1': 'S', 'CA2': 'S', 'CA3': 'A', 'CA4': 'E', 'CA5': 'C'},
    12002: {'CA1': 'B', 'CA2': 'F', 'CA3': 'C', 'CA4': 'D', 'CA5': 'E'}
}

for l,i in students.items():
    flag=0
    for k,j in i.items():
        if j=='S':
            flag = 1
            print(l," ",k)
    if flag==0:
        print(l,"None")
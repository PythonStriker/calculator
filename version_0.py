while(True):
    flag = 0
    print("请输入计算公式：")
    clc = input()
    clc = clc.replace(' ','')
    clc = clc.replace('^','**')
    #print(len(clc),clc)
    numberInclc = 0
    for char in clc:
        if char not in '()1234567890+-*/.':
            print('INPUT ERROR')
            flag = 1
            break
        else:
            if char in '()/*-+':
                if char == '/':
                    if clc[numberInclc+1] == '0':
                        print('VALUE ERROR')
                        flag = 1
                        break
                elif char == '*':
                    if clc[numberInclc+1] in '/-+' and clc[numberInclc+2] != '*' :
                        print('FORMAT ERROR')
                        flag = 1
                        break
        numberInclc += 1
    #print(clc)
    if flag :
        pass
    else:
        print('计算结果为：',round(eval(clc),10))
from tkinter import *
from tkinter.messagebox import showinfo

#计算器主窗体
root = Tk()
root.geometry('250x380')
root.title('一个普通计算器       version_2.0')
frame_show = Frame(width=300,height=150,bg='#dddddd')

#顶部区域
v = StringVar()
v.set('0')
show_label = Label(frame_show,textvariable =v, bg = 'white',width=13,height=1,font=("黑体", 20, "bold"),justify=LEFT,anchor='e')
show_label.pack(padx = 10,pady = 10)
frame_show.pack()

#是否按下了运算符
isopear = False

#操作数中小数点个数
pointnumber = 0

#统计输入运算符个数
opearnumber = 0

#操作序列
calc = []

#区分计算与按键计算flag
equal_flag = False

def change(num):
    global equal_flag
    global isopear
    global pointnumber
    if isopear == False:
        if v.get() == '0' and num !='.':
            v.set('')
            v.set(num)
        elif v.get() == '0' and num == '.':
            v.set('0.')
            pointnumber = 1
        else:
            if num == '.' and pointnumber == 1:
                pass
            elif num == '.' and pointnumber == 0:
                v.set(v.get() + num)
                pointnumber = 1
            else:
                if equal_flag :
                    v.set(num)
                    equal_flag = False
                else :
                    v.set(v.get() + num)
    else:
        if num == '.':
            v.set('0.')
            pointnumber = 1
        elif v.get() == '-':
            v.set(v.get() + num)
        else:
            v.set(num)
        isopear = False

#运算
def operation(sign):
    global isopear
    global calc
    global pointnumber
    global opearnumber
    if isopear == False and opearnumber == 0:
        calc.append(v.get())
        if sign == '+':
            calc.append('+')
        elif sign == '-':
            calc.append('-')
        elif sign == '*':
            calc.append('*')
        elif sign == '/':
            calc.append('/')
        elif sign == '%':
            calc.append('%')
    else:
        #加上符号的情况
        if sign == '+':
            equal('+')
        elif sign == '-':
            equal('-')
        elif sign == '*':
            equal('*')
        elif sign == '/':
            equal('/')
        elif sign == '%':
            equal('%')
    opearnumber = opearnumber + 1
    isopear = True
    pointnumber = 0

def equal(sign):
    global calc
    #获取当前界面的数值准备运算
    calc.append(v.get())
    #组成运算字符串
    calcstr = ''.join('%s' %id for id in calc)
    #检测最后一位是否是运算符，是就删除
    if calcstr[-1] in '+*/%':
        calcstr = calcstr[0:-1]
    if lastNoteZero(calcstr):
        # 运算操作
        if sign == '/':
            new_calcstr = calcstr.replace('/','%')
            result = eval(new_calcstr)
            if result == 0:
                result = int(eval(calcstr))
            else:
                result = eval(calcstr)
        else:
            result = eval(calcstr)
    else:
        result='输入有误！'
    #显示结果
    if result != '输入有误！' and  result//10000000 == 0 :
        if type(result) == float:
            v.set('%7.3f'%result)
        elif type(result) == int:
            v.set(result)
    elif result == '输入有误！':
        v.set(result)
    else:
        v.set('%e'%result)
    calc.clear()
    if result != '输入有误！':
        calc.append(result)
    calc.append(sign)

def button_equal():
    global equal_flag
    global calc
    global opearnumber
    global isopear
    #获取当前界面的数值准备运算
    calc.append(v.get())
    #组成运算字符串
    calcstr = ''.join('%s' %id for id in calc)
    #检测最后一位是否是运算符，是就删除
    if calcstr[-1] in '+*/%':
        calcstr = calcstr[0:-1]
    if lastNoteZero(calcstr):
        # 运算操作
        if '/' in calcstr:
            new_calcstr = calcstr.replace('/', '%')
            result = eval(new_calcstr.strip())
            if result == 0:
                result = int(eval(calcstr.strip()))
            else:
                result = eval(calcstr.strip())
        else:
            result = eval(calcstr.strip())
    else:
        result='输入有误！'
    #显示结果
    if result != '输入有误！' and  result//10000000 == 0 :
        if type(result) == float:
            v.set('%7.3f'%result)
        elif type(result) == int:
            v.set(result)
    elif result == '输入有误！':
        v.set(result)
    else:
        v.set('%e'%result)
    calc.clear()
    opearnumber = 0
    isopear = False
    equal_flag = True

#删除操作
def delete():
    global pointnumber
    if v.get().strip() == '' or v.get().strip() == '0':
        v.set('0')
        return
    else:
        num = len(v.get().strip())
        if num > 1:
            strnum = v.get()
            if strnum[num-1] == '.':
                pointnumber = 0
            strnum = strnum[0:num-1]
            v.set(strnum)
        else:
            v.set('0')

#清空操作
def clear():
    global calc
    global isopear
    global pointnumber
    global opearnumber
    global equal_flag
    calc = []
    opearnumber = 0
    v.set('0')
    isopear = False
    pointnumber = 0
    equal_flag = False


#正负操作
def fan():
    global calc
    global isopear
    strnum = v.get()
    if isopear == False:
        if strnum[0] == '-':
            v.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0' :
            v.set('-'+strnum)
    else:
        if v.get() == '-':
            v.set('0')
        else:
            v.set('-')

#判断除数是否为0
def lastNoteZero(String):
    LenOfString=len(String)
    for CharNumber in range(0,LenOfString):
        if String[CharNumber] =='/' and CharNumber != LenOfString:
            if String[CharNumber+1]=='0':
                return False
            else:
                pass
    return True

def creatNewWindows():
    #计算器高级窗体
    higher = Toplevel(root)
    higher.geometry('200x200')
    root.title('一个高级计算器       version_2.0')
    
#按键区域
frame_bord = Frame(width=400,height=350,bg='#cccccc')
button_del = Button(frame_bord,text = '←',width = 5,height =1,command = delete).grid(row = 0,column = 0)
button_yv = Button(frame_bord,text = '%',width = 5,height =1,command =lambda: operation('%')).grid(row = 0,column = 1)
button_fan = Button(frame_bord,text = '±',width = 5,height =1,command = fan).grid(row = 0,column = 2)
button_ce = Button(frame_bord,text = 'CE',width = 5,height =1,command = clear).grid(row = 0,column = 3)
button_1 = Button(frame_bord,text = '1',width = 5,height =2,command = lambda:change('1')).grid(row = 1,column = 0)
button_2 = Button(frame_bord,text = '2',width = 5,height =2,command = lambda:change('2')).grid(row = 1,column = 1)
button_3 = Button(frame_bord,text = '3',width = 5,height =2,command = lambda:change('3')).grid(row = 1,column = 2)
button_jia = Button(frame_bord,text = '+',width = 5,height =2,command = lambda:operation('+')).grid(row = 1,column = 3)
button_4 = Button(frame_bord,text = '4',width = 5,height =2,command = lambda:change('4')).grid(row = 2,column = 0)
button_5 = Button(frame_bord,text = '5',width = 5,height =2,command = lambda:change('5')).grid(row = 2,column = 1)
button_6 = Button(frame_bord,text = '6',width = 5,height =2,command = lambda:change('6')).grid(row = 2,column = 2)
button_jian = Button(frame_bord,text = '-',width = 5,height =2,command = lambda:operation('-')).grid(row = 2,column = 3)
button_7 = Button(frame_bord,text = '7',width = 5,height =2,command = lambda:change('7')).grid(row = 3,column = 0)
button_8 = Button(frame_bord,text = '8',width = 5,height =2,command = lambda:change('8')).grid(row = 3,column = 1)
button_9 = Button(frame_bord,text = '9',width = 5,height =2,command = lambda:change('9')).grid(row = 3,column = 2)
button_cheng = Button(frame_bord,text = 'x',width = 5,height =2,command = lambda:operation('*')).grid(row = 3,column = 3)
button_0 = Button(frame_bord,text = '0',width = 5,height =2,command = lambda:change('0')).grid(row = 4,column = 0)
button_dian = Button(frame_bord,text = '.',width = 5,height =2,command = lambda:change('.')).grid(row = 4,column = 1)
button_deng = Button(frame_bord,text = '=',width = 5,height =2,command = button_equal).grid(row = 4,column = 2)
button_chu = Button(frame_bord,text = '/',width = 5,height =2,command = lambda:operation('/')).grid(row = 4,column = 3)
button_auther = Button(frame_bord,text = '查看出版团队',width = 25,height =2,command = lambda: print('It is a very nice team!This project made by Mr ma,nie,shao,song!')).grid(row = 5,column = 0,columnspan=4)
button_hight = Button(frame_bord,text = '高级',width = 5,height =1,command = creatNewWindows).grid(row = 6,column = 3)
frame_bord.pack(padx = 10,pady = 10)
root.mainloop()
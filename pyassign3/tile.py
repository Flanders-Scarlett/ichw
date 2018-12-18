"""tile.py: 解决铺砖方法.
__author__ = "Fu Yixuan"
__pkuid__  = "1800011720"
__email__  = "Fu Yixuan@pku.edu.cn"
"""



def transk(k,a,b,m,n):
    #坐标与方块标号之间的转化#
    i = k % m
    j = k // m
    return(i,j)

def transij(i,j,a,b,m,n):
    #坐标与方块标号之间的转化#
    k = i + j * m
    return(k)

def finds(wall,a,b,m,n):
    #寻找没铺过砖的位置坐标，如果没有输出None#
    for i in range(m):
        for j in range(n):
            if wall[i][j] == 0:
                return i,j

def assert_brick(x,y,aa,bb,wall,m,n):
    #判断在(x，y)处是否可以铺砖#
    t = 0
    if x + aa < m + 1 and y + bb < n + 1:   #判断是否会铺出墙外#
        for i in range(aa):           #判断是否所铺位置均未未铺#
            for j in range(bb):
                if wall[x+i][y+j] == 1:  
                    t += 1
        if t == 0:
            return True
    else:
        return False

def puzhuan(ans,wall,a,b,m,n,all_ans):
    #开始铺砖，思路与教学网上思路一致#
    z = 0
    Q = finds(wall,a,b,m,n)
    if Q == None: #判断如果墙均被铺满，即无没铺的砖时，输出一个结果#
        all_ans.append(ans.copy())
    else : #迭代铺砖#
        brick = []
        x = Q[0]
        y = Q[1]
        if assert_brick(x,y,a,b,wall,m,n)==True: #横着铺#
            for i in range(a):
                for j in range(b):
                    wall[x+i][y+j] = 1     #铺过的位置设为1#
                    brick.append(transij(x+i,y+j,a,b,m,n))
            tbrick = tuple(brick)
            ans.append(tbrick)
            puzhuan(ans,wall,a,b,m,n,all_ans)
            for i in range(a):   #铺完这块砖之后，再拆掉这块砖#
                for j in range(b):
                    wall[x+i][y+j] = 0
            brick = []
            ans.pop()          
            
        if assert_brick(x,y,b,a,wall,m,n)==True: #竖着铺#
            for i in range(b):
                for j in range(a):
                    wall[x+i][y+j] = 1    #铺过的位置设为1#
                    brick.append(transij(x+i,y+j,a,b,m,n))
            tbrick = tuple(brick)
            ans.append(tbrick)
            puzhuan(ans,wall,a,b,m,n,all_ans)
            for i in range(b):  #铺完这块砖之后，再拆掉这块砖#
                for j in range(a):
                    wall[x+i][y+j] = 0
            brick = []
            ans.pop()
            
        return all_ans
    
def square_brick(a,b,w):
    #判断如果为砖为正方形，实际上只有一种方法#
    all_w = []
    if a == b:
        all_w.append(w[0])
    else:
        all_w = w
    return all_w

def assert_puzhuan(w):
    #判断如果无法密铺时，结果w应为空列表，输出无法被铺满#
    if w == []:
        w = '在这种方案下墙无法被铺满'
    return w

def main_puzhuan():
    m = int(input("请输入墙的长度："))
    n = int(input("请输入墙的宽度："))
    a = int(input("请输入砖的长度："))
    b = int(input("请输入砖的宽度："))
    all_ans = []
    wall = []     #定义墙，所有位置为0#
    for i in range(m):
        wlist = []
        for j in range(n):
            wlist.append(0)
        wall.append(wlist)
    w = puzhuan([],wall,a,b,m,n,all_ans)
    w = square_brick(a,b,w)
    w = assert_puzhuan(w)
    if type(w) == list:
        print("共有"+str(len(w))+"种方案，分别如下")
        print(w)
    else:
        print(w)
    return w,a,b,m,n

def draw_wall(tur,a,b,m,n):
    #画墙#
    tur.pensize(2)
    tur.color('blue')
    tur.pu()
    
    for j in range(n+1):
        tur.goto(-30*m , 30*n-60*j)
        tur.pd()
        tur.fd(60*m)
        tur.pu()   
    tur.rt(90)
        
    for i in range(m+1):
        tur.goto(-30*m+60*i , 30*n)
        tur.pd()
        tur.fd(60*n)
        tur.pu()
    tur.lt(90)

def draw_number(tur,a,b,m,n):
    #填数字#
    tur.pensize(2)
    tur.color('blue')
    
    for j in range(n):
        tur.goto(-30*m+30 , 30*n-30-60*j)
        for i in range(m):
            tur.write(j*m+i,True,align='center')
            tur.fd(60)

def draw_brick(i1,i2,j1,j2,tur,a,b,m,n):
    #画砖#
    tur.pensize(4)
    tur.color('black')
    tur.pu()
    tur.goto(-30*m+60*i1,30*n-60*j1)
    tur.pd()
    tur.goto(-30*m+60*i1,30*n-60*j2)
    tur.goto(-30*m+60*i2,30*n-60*j2)
    tur.goto(-30*m+60*i2,30*n-60*j1)
    tur.goto(-30*m+60*i1,30*n-60*j1)
    tur.pu()

def exchange_brick(plan,tur,a,b,m,n):
    #将砖转化为砖四个角的坐标#
    for i in range(len(plan)):
        tbrick1 = transk(plan[i][0],a,b,m,n)
        tbrick2 = transk(plan[i][-1],a,b,m,n)
        i1 = tbrick1[0]
        i2 = tbrick2[0]+1
        j1 = tbrick1[1]
        j2 = tbrick2[1]+1
        draw_brick(i1,i2,j1,j2,tur,a,b,m,n)
    
def main_turtle(all_plan,a,b,m,n):
    import turtle
    t = len(all_plan)
    s = int(turtle.numinput('Select plan','Input number of 1 - '+str(t),1,1,t))
    plan = all_plan[s-1]
    tur = turtle.Turtle()
    tur.ht()
    tur.speed(4)
    draw_wall(tur,a,b,m,n)
    draw_number(tur,a,b,m,n)
    exchange_brick(plan,tur,a,b,m,n)

def main():
    alw = main_puzhuan()
    if type(alw[0]) == list:
       main_turtle(alw[0],alw[1],alw[2],alw[3],alw[4]) 

if __name__ == '__main__':
    main()

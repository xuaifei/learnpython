'''寻找水仙花数，
水仙花数 是一个三位数，他每位上面的数字的三次方是数本身

打印出所有的水仙花数
author：xuaifei
'''
from math import pow
def print_flower_num_3():
    for n in range(100,1000,1):
        hundard = n//100
        ten = (n-hundard*100)//10
        one = n-hundard*100-ten*10
        if n == hundard**3+ten**3+one**3:
            print(n)

def print_flower_num(n):
    '''
    n is power
    '''
    """for n in range(100,1000,1):
        hundard = n//100
        ten = (n-hundard*100)//10
        one = n-hundard*100-ten*10
        if n == hundard**3+ten**3+one**3:
            print(n)"""
    print("start check"+str(10**(n-1))+"~"+str(10**n))
    for check in range(10**(n-1), 10**n, 1):
    #check = 10**(n-1)
    #while check<10**n:
        #if check==1111:
        check_sum = 0
        check_data = check
        for j in range(n, 0, -1):
            check_bit = check_data//(10**(j-1))
            check_sum+=check_bit**n
            check_data = check_data-check_bit*(10**(j-1))
        
        if check_sum == check:
            print(check)

        check+=1

def find_perfect_number(max_num):
    '''
    完全数 是 除自身之外的所有因子的和 等于这个数本身
    '''
    for is_perfect in range(1,max_num+1,1):
        sum_num = 0
        for div_num in range(1,is_perfect//2,1):
            if is_perfect%div_num==0 and div_num != is_perfect:
                sum_num+=div_num
        if sum_num == is_perfect:
            print(str(is_perfect) + " is perfect number")

def hundred_chicken_hundred_money():
    '''
    百钱白鸡问题，公鸡1=5钱，母鸡1=3钱，小鸡*3=1钱，问一百钱买一百鸡该如何分配？
    x=公鸡，y=母鸡，小鸡=(100-x-y)
    5*x+3*y+(100-x-y)/3=100 注意要整数
    '''
    for x in range(0, 100//5, 1):
        for y in range(0, 100//3, 1):
            z = 100 - x - y
            if z%3==0 and z>=0 and z<=100 and 5*x+3*y+z/3==100:
                print(str(x)+"\t"+str(y)+"\t"+str(z))

def fib(n):
    '''
    斐波那契数列（Fibonacci sequence）:
    后一个数等于前两个数相加，第一二个数是1,1 
    '''
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_print(max_n):
    '''
    打印出max_n个fib数
    '''
    for n in range(1, max_n+1, 1):
        print(fib(n))
from random import randint
def gamble_game():
    '''
    Craps赌博游戏 - 两个色子
第一次摇色子
如果摇出了7点或11点 - 玩家胜
如果摇出了2点、3点或12点 - 庄家胜
如果摇出其他点数 - 游戏继续
继续
如果摇出了7点 - 庄家胜
如果摇出了第一次摇的点数 - 玩家胜
如果摇出了其他点数 - 游戏继续'''
    role_tuple=('banker', 'player')
    score_list=[0,0]
    input("enter to start roll")
    score_list[0] = randint(1,6)
    score_list[1] = randint(1,6)
    score_sum = score_list[0]+score_list[1]
    #score_sum = 4
    print("roll socre first "+str(score_sum))
    if score_sum == 7 or score_sum == 11:
        print(role_tuple[1]+" win!")
        return
    elif score_sum == 2 or score_sum == 3 or score_sum == 12:
        print(role_tuple[0]+" win!")
        return
    else:
        while(True):
            input("not end enter to start roll")
            score_list[0] = randint(1,6)
            score_list[1] = randint(1,6)
            score_sum_next = score_list[0]+score_list[1]
            #score_sum_next = 4
            print("roll socre again "+str(score_sum_next))
            if score_sum_next == 7:
                print(role_tuple[0]+" win!")
                return
            elif score_sum_next == score_sum:
                print(role_tuple[1]+" win!")
                return
            else:
                print("please roll again")


    


if __name__=='__main__':
    #print_flower_num_3()
    #print_flower_num(4)
    #find_perfect_number(10**5)
    #hundred_chicken_hundred_money()
    #fib_print(1000)
    gamble_game()
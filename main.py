import time
import os
import msvcrt
import random
import winsound
from threading import Thread
hight = 20    #游戏地图大小
wide = 20

class python(Thread):
    def __init__(self):
        super().__init__()
        self.x = 5   #初始位置
        self.y = 5   
        self.snake_list = []
        self.str1 = u'■'
        self.str2 = u'□'
        self.speed = 0.5
        self.w = 0  #贪吃蛇状态
        self.s = 0
        self.d = 1
        self.a = 0
        self.food_y = 9
        self.food_x = 9
        self.branch = 0

    def run(self):
        while True:
            for y in range(hight):     #y轴循环
                string = ""
                for x in range(wide):  #x轴循环
                    if x == self.x and y == self.y:   #蛇位置 
                        string += self.str1
                        continue
                    if x == 0 or x == wide-1 or y == 0 or y == hight-1 or (y == self.food_y and x == self.food_x) or self.check(y,x):   #判断是否绘制白点
                        string += self.str1
                    else:
                        string += self.str2   #绘制方框
                print(string)
            self.snake_list.append((self.y,self.x))   #添加一个蛇身位置
            time.sleep(self.speed)
            self.x += self.d
            self.x -= self.a
            self.y -= self.w
            self.y += self.s
            if self.x >= hight-1 or self.y >= hight-1 or self.x < 1 or self.y < 1 or (self.y,self.x) in self.snake_list:   #判断贪吃蛇是否撞线或者撞到蛇身
                print("游戏结束\n你的分数是:{:d}".format(self.branch))
                break
            else:
                if (self.x == self.food_x and self.y == self.food_y):    #判断贪吃蛇是否吃到食物
                    self.snake_list.append((y,x))   #吃到食物，贪吃蛇变长
                    self.branch +=1
                    self.food()
                    print(self.branch)
            os.system("cls")
            self.snake_list.pop(0)  #移除上一个位置

    def food(self):
        while True:
            self.food_x = random.randint(1,wide-2)
            self.food_y = random.randint(1,hight-2)
            if not (self.food_x == self.x and self.food_y == self.y):  #确保食物不会出现在蛇身上
                break

    def check(self,y,x):
        if (y,x) in self.snake_list:
            return True
        else:
            return False



if __name__ == "__main__":
    ss = python()
    ss.start()
    winsound.PlaySound("bgm.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
    while True:
        key = msvcrt.getch()
        if key == b'w':
            if ss.s == 1:
                pass
            else:
                ss.w = 1
                ss.s = 0
                ss.a = 0
                ss.d = 0
        elif key == b's':
            if ss.w == 1:
                pass
            else:
                ss.w = 0
                ss.s = 1
                ss.a = 0
                ss.d = 0
        elif key == b'a':
            if ss.d == 1:
                pass
            else:
                ss.w = 0
                ss.s = 0
                ss.a = 1
                ss.d = 0
        elif key == b'd':
            if ss.a == 1:
                pass
            else:
                ss.w = 0
                ss.s = 0
                ss.a = 0
                ss.d = 1
        else:
            pass
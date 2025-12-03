from tkinter import *
import random
import time
import os
#実行場所を変更したいパスを指定する
os.chdir("C:/Users/81809/python/VSCodeGitHub/RepositoryForVSCode3/stickman")
print("現在の実行場所:", os.getcwd())
print("ファイル存在:", os.path.isfile('background.gif'))

class Coords:
  def __init__(self, x1=0, y1=0, x2=0, y2=0):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
#スプライトの衝突
  # def within_x(co1, co2):
  #   if co1.x1 >co2.x1 and co1.x1 < co2.x2:
  #     return True
  #   elif co1.x2 >co2.x1 and co1.x2 < co2.x2:
  #     return True
  #   elif co2.x1 > co1.x1 and co2.x1 < co1.x2:
  #     return True
  #   elif co2.x2 > co1.x1 and co2.x2 <co1.x2:
  #     return True
  #   else:
  #     return False ↓と同義

#縦軸の衝突を判断するメソッド
def within_x(co1, co2):
  if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
     or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
     or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
     or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
     return True
  else:
      return False

#横軸の衝突を判断するメソッド
def within_y(co1, co2):
  if(co1.y1 > co2.y1 and co1.y1 < co2.y2)\
     or (co1.y2 > co2.y1 and co1.y2 < co2.y2)\
     or (co2.y1 > co1.y1 and co2.y1 < co1.y2)\
     or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
    return True
  else:
    return False

#左側の衝突を調べるメソッド
def collided_left(co1, co2):
  if within_y(co1, co2):
    if co1.x1 >= co2.x1 and co1.x1 <= co2.x2:
      return True
  return False

#右側の衝突を調べるメソッド
def collided_right(co1, co2):
  if within_y(co1, co2):
      if co1.y1 >= co2.y1 and co1.y1 <= co2.y2:
        return True
  return False

#上側の衝突を調べるメソッド
def collided_top(co1, co2):
  if within_x(co1, co2):
      if co1.y1 >= co2.y1 and co1.y1 <= co2.y2:
        return True
  return False

#下側の衝突を調べるメソッド
def collided_bottom(y, co1, co2):
  if within_x(co1, co2):
    y_calc =  co1, co2 + y
    if y_calc >=co2.y1 and y_calc <= co2.y2:
      return True
  return False

#ゲームループ
class Game:
 def __init__(self):
    self.tk =Tk()
    self.tk.title('Mr. Stick Man Races for the Exit')
    self.tk.resizable(0, 0)
    self.tk.wm_attributes('-topmost', 1)
    self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
    self.canvas.pack()
    self.tk.update()
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
    self.bg = PhotoImage(file='background.gif')
    w = self.bg.width()
    h = self.bg.height()
    for x in range(0, 5):
      for y in range(0, 5):
        self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True

    for x in range(0, 5):
     for y in range(0, 5):
       self.canvas.create_image(x * w, y * h,
                              image=self.bg, anchor='nw')
    self.sprites = []
    self.running = True

def mainloop(self):
  while True:
    if self.running == True:
        for sprite in self.sprites:
            sprite.move()
    self.tk.update_idletasks()
    self.tk.update()
    time.sleep(0.01)

g = Game()
g.tk.mainloop()

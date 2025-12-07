from tkinter import *
import tkinter as tk
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

#スプライトのクラス
class Sprite:
  def __init__(self, game):
    self.game = game
    self.endgame = False
    self.coordinates = None

  def move(self):
    pass

  def coords(self):
    return self.coordinates

#床クラス
class PlatformSprite(Sprite):
  def __init__(self, game, photo_image, x, y, width, height):
    Sprite.__init__(self, game)
    self.photo_image = photo_image
    self.image = game.canvas.create_image(x, y,\
                                          image=self.photo_image, anchor='nw')
    self.coordinates = Coords(x, y, x + width, y + height)

#スティックマン
class StickFigureSprite(Sprite):
  def __init__(self, game):
      Sprite.__init__(self, game)
      self.images_left = [
          tk.PhotoImage(file='figure-EL1.gif'),
          tk.PhotoImage(file='figure-El2.gif'),
          tk.PhotoImage(file='figure-EL3.gif')
        ]
      self.images_right = [
          tk.PhotoImage(file='figure-ER1.gif'),
          tk.PhotoImage(file='figure-ER2.gif'),
          tk.PhotoImage(file='figure-ER3.gif')
        ]
      self.image = game.canvas.create_image(200, 470,image=self.images_left[0], anchor='nw')
      self.x = -2
      self.y = 0
      self.current_image = 0
      self.current_image_add = 1
      self.jump_count = 0
      self.last_time = time.time()
      self.coordinates = Coords()

      game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
      game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
      game.canvas.bind_all('<space>', self.jump)

  def turn_left(self, evt):
    if self.y == 0:
        self.x = -2
        self.game.canvas.itemconfig(self.image, image=self.images_left[0])

  def turn_right(self, evt):
    if self.y == 0:
        self.x = 2
        self.game.canvas.itemconfig(self.image, image=self.images_right[0])

  def jump(self, evt):
    if self.y == 0:
        self.y = -4
        self.jump_count = 0

  def animate(self):
     if self.x != 0 and self.y == 0:
        if time.time() - self.last_time > 0.1:
           self.last_time = time.time()
           self.current_image += self.current_image_add
           if self.current_image >=2:
              self.current_image_add = -1
           if self.current_image_add <= 0:
              self.current_image_add = 1

     if self.x < 0:
         if self.y != 0:
          self.game.canvas.itemconfig(self.image,image=self.images_left[2])
         else:
          self.game.canvas.itemconfig(self.image,image=self.images_left[self.current_image])
     elif self.x > 0:
        if self.y != 0:
           self.game.canvas.itemconfig(self.image,image=self.images_right[2])
        else:
           self.game.canvas.itemconfig(self.image,image=self.images_right[self.current_image])

def coords(self):
   xy = self.game.canvas.coods(self.image)
   self.coodinates.x1 = xy[0]
   self.coodinates.y1 = xy[1]
   self.coodinates.x2 = xy[0] + 27
   self.coodinates.y2 = xy[1] + 30
   return self.coordinates

def move(self):
   self.animate()
   if self.y < 0:
      self.jump_count += 1
      if self.jump_count > 20:
         self.y = 4
   if self.y > 0:
      self.jump_count -=1

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

platform1 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 230, 200, 32, 10)

g.sprites.append(platform1)

stickman = StickFigureSprite(g)
g.sprites.append(stickman)

g.tk.mainloop()
#0,480,100,10は位置キャンバスの横0縦480ピクセルと画像の幅100、高さ10ピクセルを表している

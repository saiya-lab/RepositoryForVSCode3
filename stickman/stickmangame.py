from tkinter import *
import random
import time
import os
#実行場所を変更したいパスを指定する
os.chdir("C:/Users/81809/python/VSCodeGitHub/RepositoryForVSCode3/stickman")
print("現在の実行場所:", os.getcwd())
print("ファイル存在:", os.path.isfile('background.gif'))
print("ファイル存在:", os.path.isfile('figure-enemy-sword-l1.gif'))
print("door1.gif存在:", os.path.isfile('door1.gif'))


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
      if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
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
    y_calc =  co1.y2 + y
    if y_calc >= co2.y1 and y_calc <= co2.y2:
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
      self.game = game
      self.images_left = [
          PhotoImage(file='figure-EL1.gif'),
          PhotoImage(file='figure-EL2.gif'),
          PhotoImage(file='figure-EL3.gif')
        ]
      self.images_right = [
          PhotoImage(file='figure-ER1.gif'),
          PhotoImage(file='figure-ER2.gif'),
          PhotoImage(file='figure-ER3.gif')
        ]
      self.image = game.canvas.create_image(200, 470,image=self.images_left[0], anchor='nw')
      self.x = -2
      self.vx = 0 #横方向の加速度
      self.y = 0
      self.current_image = 0
      self.current_image_add = 1
      self.jump_count = 0
      self.last_time = time.time()
      self.coordinates = Coords()
      game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
      game.canvas.bind_all('<KeyRelease-Left>', self.stop)
      game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
      game.canvas.bind_all('<KeyRelease-Right>', self.stop)
      game.canvas.bind_all('<space>', self.jump)

  def turn_left(self, evt):
    if self.y == 0:
        self.x = -2
        self.game.canvas.itemconfig(self.image, image=self.images_left[0])
        self.vx = -3

  def turn_right(self, evt):
    if self.y == 0:
        self.x = 2
        self.game.canvas.itemconfig(self.image, image=self.images_right[0])
        self.vx = -3

  def jump(self, evt):
    if self.y == 0:
        self.y = -4
        self.jump_count = 0

  def stop(self, evt):
     self.x = 0
     self.vx = 0
  #keyRleaseで横移動をstop

  def animate(self):
     if self.x != 0 and self.y == 0:
        if time.time() - self.last_time > 0.1:
           self.last_time = time.time()
           self.current_image += self.current_image_add
           if self.current_image >=2:
              self.current_image_add = -1
           elif self.current_image_add <= 0:
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
      xy = self.game.canvas.coords(self.image)
      self.coordinates.x1 = xy[0]
      self.coordinates.y1 = xy[1]
      self.coordinates.x2 = xy[0] + 27
      self.coordinates.y2 = xy[1] + 30
      return self.coordinates

  def move(self):
      self.animate()
      if self.y < 0:
          self.jump_count += 1
          if self.jump_count > 20:
              self.y = 4
      if self.y > 0:
          self.jump_count -=1
      co = self.coords()
      left = True
      right = True
      top = True
      bottom = True
      falling = True

      if self.y > 0 and co.y2 >= self.game.canvas_height:
          self.y = 0
          bottom = False
      elif self.y < 0 and co.y1 <= 0:
          self.y = 0
          top = False
      if self.x > 0 and co.x2 >= self.game.canvas_width:
          self.x = 0
          right = False
      elif self.x <0 and co.x1 <= 0:
          self.x = 0
          left = False
      for sprite in self.game.sprites:
           if sprite == self:
               continue
           sprite_co = sprite.coords()
           if top and self.y < 0 and collided_top(co, sprite_co):
               self.y = -self.y
               top = False

           if bottom and self.y > 0 and collided_bottom(self.y,co, sprite_co):
               self.y = sprite_co.y1 - co.y2
               if self.y < 0:
                   self.y = 0
               bottom = False
               top = False
           if bottom and falling and self.y == 0 \
                    and co.y2 < self.game.canvas_height\
                    and collided_bottom(1, co, sprite_co):
               falling = False
           if left and self.x < 0 and collided_left(co, sprite_co):
               self.x = 0
               left = False
               if sprite.endgame:
                   self.game.running = False
                   show_game_clear(self.game)
           if right and self.x > 0 and collided_right(co, sprite_co):
               self.x = 0
               right = False
               if sprite.endgame:
                  self.game.running = False
                  show_game_clear(self.game)

           if collided_left(co, sprite_co) or collided_right(co, sprite_co)\
           or collided_top(co, sprite_co) or collided_bottom(self.y, co, sprite_co):
              if  isinstance(sprite, EnemySprite):
                 self.game.running = False
                 show_game_over(self.game)

      if falling and bottom and self.y == 0\
      and co.y2 < self.game.canvas_height:
         self.y = 4
         self.x = self.vx
      self.game.canvas.move(self.image, self.x, self.y)

#gameclear
def show_game_clear(game):
    game.is_game_clear = True
    x = game.canvas.winfo_width() // 2
    y = game.canvas.winfo_height() // 2
    #font_size = 60

    for dx, dy in [(-3,0),(3,0),(0,-3),(0,3),(-3,-3),(3,-3),(-3,3),(3,3)]:
        game.canvas.create_text(
            x+dx, y+dy,
            text="GAME CLEAR",
            font=("Helvetica", 32, "bold"),
            fill="black"
       )
    #本体の文字
    game.canvas.create_text(
       x, y,
       text="GAME CLEAR",
       font=("Helvetica", 32, "bold"),
       fill="orange"
    )
    game.canvas.create_text(
      x, y + 30,
      text='Press r to Restart',
      font=('Helvetica', 20, 'bold'),
      fill='white'
    )
    game.canvas.bind_all('<r>', lambda e: restart_game(game))

    game.canvas.create_text(
      x, y + 50,
      text='Press n for Next Stage',
      font=('Helvetica', 20, 'bold'),
      fill='black'
    )
    game.canvas.bind_all('<n>', lambda e: restart_game(game))

def next_stage(game):
   game.stage += 1
   setup_stage(game, game.stage)
   game.is_game_clear = False

#gameover
def show_game_over(game):
   if game.is_game_clear:
      return

   game.is_game_over = True

   x = game.canvas_width // 2
   y = game.canvas_height // 2

   game.canvas.create_text(
      x, y,
      text='GAME OVER',
      font=('Helvetica', 32, 'bold'),
      fill='red'
   )

   game.canvas.create_text(
      x, y + 30 ,
      text='Press r to Restart',
      font=('Helvetica', 20, 'bold'),
      fill='white'
   )
   game.canvas.bind_all('<r>', lambda e: restart_game(game))


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

      self.bg = PhotoImage(file='background.gif')
      self.draw_background()
      self.sprites = []
      self.running = True
      self.is_game_over = False
      self.is_game_clear = False

      self.canvas_height = self.canvas.winfo_height()
      self.canvas_width = self.canvas.winfo_width()
      self.stage = 1

  def draw_background(self):
      w = self.bg.width()
      h = self.bg.height()

      for x in range(0, 5):
         for y in range(0, 5):
             self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')

  def create_platforms(self):
     platform_img1 = PhotoImage(file='platform1.gif')
     platform_img2 = PhotoImage(file='platform2.gif')
     platform_img3 = PhotoImage(file='platform3.gif')

     p1 = PlatformSprite(self, platform_img1, 0, 480, 100, 10)
     p2 = PlatformSprite(self, platform_img1, 150, 440, 100, 10)
     p3 = PlatformSprite(self, platform_img1, 300, 400, 100, 10)
     p4 = PlatformSprite(self, platform_img1, 300, 160, 100, 10)
     p5 = PlatformSprite(self, platform_img2, 175, 350, 66, 10)
     p6 = PlatformSprite(self, platform_img2, 50, 300, 66, 10)
     p7 = PlatformSprite(self, platform_img2, 170, 120, 66, 10)
     p8 = PlatformSprite(self, platform_img2, 45, 60, 66, 10)
     p9 = PlatformSprite(self, platform_img3, 170, 250, 32, 10)
     p10 = PlatformSprite(self, platform_img3, 230, 200, 32, 10)

     self.sprites.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])

  def mainloop(self):
       while True:
          if self.running == True:
              for sprite in self.sprites:
                  sprite.move()
          self.tk.update_idletasks()
          self.tk.update()
          time.sleep(0.01)

class DoorSprite(Sprite):
   def __init__(self, game, photo_image, x, y, width, height):
      Sprite.__init__(self, game)
      self.photo_image = photo_image
      self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
      self.coordinates = Coords(x, y, x + (width / 2), y + height)
      self.endgame = True

#動く敵
class EnemySprite(Sprite):
   def __init__(self, game, photo_image, x, y, width, height):
      Sprite.__init__(self, game)
      self.photo_image = photo_image
      self.image = game.canvas.create_image(x, y, image=self.photo_image , anchor='nw')
      self.coordinates = Coords(x, y, x + width, y + height)

      self.vx = 1
    #移動範囲
      self.min_x = x
      self.max_x = x + 150

   def move(self):
      self.game.canvas.move(self.image, self.vx, 0)
      co = self.coords()

      if co.x1 <= self.min_x or co.x2 >= self.max_x:
          self.vx = -self.vx

   def coords(self):
       xy = self.game.canvas.coords(self.image)
       if not xy :
          return self.coordinates
       self.coordinates.x1 = xy[0]
       self.coordinates.y1 = xy[1]
       self.coordinates.x2 = xy[0] +32
       self.coordinates.y2 = xy[1] +32

       return self.coordinates


#リセットボタン
def restart_game(game):
  game.canvas.delete('all')
  game.is_game_clear = False
  game.is_game_over = False
  w = game.bg.width()
  h = game.bg.height()

  for x in range(0, 5):
    for y in range(0, 5):
        game.canvas.create_image(x * w, y * h, image=game.bg, anchor='nw')

  game.sprites = []
  game.create_platforms()

  stickman = StickFigureSprite(game)
  game.sprites.append(stickman)

  enemy = EnemySprite(game, PhotoImage(file='figure-enemy-sword-l1.gif'),170, 30, 32, 32)
  game.sprites.append(enemy)

  door = DoorSprite(game, PhotoImage(file='door1.gif'), 45, 30, 40, 35)
  game.sprites.append(door)

  game.running = True

def setup_stage(game, stage_number):
  game.canvas.delete('all')
  game.draw_background()
  game.sprites = []
  game.create_platforms()
  stickman = StickFigureSprite(game)
  game.sprites.append(stickman)

  if stage_number == 1:
    enemy = EnemySprite(game, PhotoImage(file='figure-enemy-sword-l1.gif'),170, 30, 32, 32)
    door = DoorSprite(game, PhotoImage(file='door1.gif'), 45, 30, 40, 35)
  elif stage_number == 2:
    enemy = EnemySprite(game, PhotoImage(file='figure-enemy-sword-l1.gif'),170, 30, 32, 32)
    door = DoorSprite(game, PhotoImage(file='door1.gif'), 45, 30, 40, 35)


    game.sprites.append(door)
    game.sprites.append(enemy)
    game.running = True
#append一つ追加 extend複数ついか



g = Game()




platform1 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file='platform1.gif'), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file='platform2.gif'), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file='platform3.gif'), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file='platform3.gif'), 230, 200, 32, 10)

g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)
door = DoorSprite(g, PhotoImage(file='door1.gif'), 45, 30, 40, 35)
g.sprites.append(door)
sf = StickFigureSprite(g)
g.sprites.append(sf)

try:
   enemy = EnemySprite(g, PhotoImage(file='figure-enemy-sword-l1.gif'), 170, 30, 32, 32)
   g.sprites.append(enemy)
except Exception as e:
   print("EnemySprite 初期化エラー", e)


g.mainloop()
#0,480,100,10は位置キャンバスの横0縦480ピクセルと画像の幅100、高さ10ピクセルを表している

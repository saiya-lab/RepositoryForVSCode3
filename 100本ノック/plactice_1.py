x = 100
result_1 = x + 100
print(result_1)

#x = x + 1 → x += 1
#x = x - 1 → x -= 1
#x = x * 1 → x *= 1
#x = x / 1 → x /=1

name = "saiya"
age = 27

name_age = f"私は{name}です。{age}です。"
print(name_age)

tell_number = "03-1111-2222"
new_tell = tell_number.replace("-","")
print(new_tell)

print("あ\nい\nう\nえ\nお")#\n改行

#12
name_1 = " 鈴木　太郎\n"
name_2 = name_1.replace(" ","").replace("\n","")
print(name_2)
#name = " 鈴木　太郎\n"
#name_stripped = name.strip()
#print(name_stripped)

#13
apple_x = "Apple"
uppercase_text = apple_x.upper()
print(uppercase_text)
lowercase_text = apple_x.lower()
print(lowercase_text)

#14 []list
fruits = ["りんご","バナナ","オレンジ"]
print(fruits)

#15
flength = len(fruits)
print(flength)

#16
print(f"先頭は{fruits[0]}です。末尾は{fruits[2]}です。")

#17 抽出
telly = tell_number[:2]
tel_len =len (tell_number)
print(telly,tel_len)

#18 
tel_47 = tell_number[3:7]
print(tel_47)

#19 sprit 区切る
tel_split1 = tell_number.split("-")
print(tel_split1)

#20 join 区切り結合
phone_list = ["03","1111","2222"]
phone_1 = "-".join(phone_list)
print(phone_1)

#21 sortedは順番にする
numbers = [3, 1, 4, 2, 5]
num_sort = sorted(numbers)
new_num = num_sort[:3]
print(new_num)

#22 reverseは逆順にする
num_sort.reverse()
print(num_sort)

#23
sum_num = sum(numbers)
max_num = max(numbers)
min_num = min(numbers)
print(sum_num,max_num,min_num)

#24
second_number=numbers.pop(1)
print(numbers)
print(second_number)

#25 listの結合　
odd_numbers = [1, 3, 5, 7]
even_numbers = [2, 4, 6, 8]
combined_list = odd_numbers + even_numbers
print(combined_list)

#26 listの要素の追加・削除
odd_numbers.append(9)
print(odd_numbers)
even_numbers.remove(8)
print(even_numbers)

#27 辞書作り方
months = {1: "睦月", 2: "如月", 3: "弥生"}
print(months)

#28 辞書に追加　辞書[key] = value
months[4] = "卯月"
print(months)

#29 辞書から取り出し　x=辞書[key]
kisaragi_value = months[2]
print(kisaragi_value)

#30 辞書変更　辞書[key]=新しい文字
months[1] = "January"
print(months)

#31 
months_x = months.pop(3)
print(months_x)
print(months)

#32
keys = list(months.keys())
values = list(months.values())
print(keys)
print(values)

#33
my_set = { 1, 2, 3, 4, 5,5}
print(my_set)

#34 addメソッド
my_set.add(6)
my_set.remove(1)
print(my_set)

#35
numbers_1 = [1, 1, 5, 2, 5, 3, 3]
numbers_2 = list(set(numbers_1))
print(numbers_2)

#36
group_a = { 1, 2, 3, 4, 5}
group_b = { 4, 5, 6, 7, 8}
group_c =group_a & group_b
print(group_c)

#37
unique_numbers = group_a - group_b 
print(unique_numbers)

#38 パティカルバー
group_ab = group_a | group_b
print(group_ab)

#39 
numbers_3 = { 1, 12, 5, 10, 13, 7, 90}
sorted_numbers = sorted(numbers_3)
second_largest_number = sorted_numbers[-2]
print(second_largest_number)

#40
tuple_1 = (1920 , 1080)
print(tuple_1)

#41
width = tuple_1[0]
print(width)

#42
empty_list = []
empty_set = set()
empty_dict = {}

print(empty_dict)
print(empty_list)
print(empty_set)

#43
x = 12
y = 14
if x == y :
   print("同じです")
         
#44 ! ←　not =
if x != y :
   print("異なります")

#45　elif はじょうけんがつけれる　else それ以外
if x >= y :
   print("ｘはｙ以上です。")
elif x < y :
   print("ｘはｙ未満です。")
 
#46
x1 = 84
if x1 >= 90 :
   print("A")
elif 80 <= x1 < 90 :
   print("B")
else :
   print("c")

#47 
favorite_fruits = ["りんご", "ばなな", "みかん", "梨", "桃"]
x2 = ("ばなな")
if x2 in favorite_fruits:
   print("好きな果物です")

#48
allergy_foods = ["卵", "乳", "小麦", "そば", "落花生"]   
x3 = ("チョコレート")
if x3 not in allergy_foods:
   print("アレルギーの食べ物ではありません")

#49
document = "私はpythonをまなんでいます"

if "python" in document:
   print("pythonが含まれています")

#50 startswith 
phone_number = "0120333906"

if phone_number.startswith("0120"):
   print("フリーダイヤルです。")

#51 endswith
mail_address = "sapu@gmail.com"
if mail_address.endswith("gmail.com"):
   print("Gmailアドレスです。")

#52
math_score = 78
eng_score = 89
jpn_score = 90

if math_score >= 80 and eng_score >= 80 and jpn_score >= 80:
   print("合格")
else:
   print("不合格")

#53
age1 = 27
if age <= 12 and age >= 65:#if age <=12 or 65 <= age:
   print("割引料金")
else:
   print("通常料金")

#54 yokuwakaran
age2 = 20
is_student = False

if age < 18:
   print(500)
else:
   if is_student:
      print(1000)
   else:
      print(2000)

#55
names = ["鈴木", "田中", "山田", "佐藤", "伊藤"]

for name in names:
   print(f"{name}さん")

#56
months2 = {1:"睦月", 2:"如月", 3:"弥生"}

for k, v in months2.items():
   print(f"{k}月は和風月名で{v}です。")

#57 多重リスト
bottom_and_height = [
   [13,40],
   [15,30],
   [20,25]
]

for b_and_h in bottom_and_height:
   bottom = b_and_h[0]
   height = b_and_h[1]
   area = bottom * height / 2
   print(f"底辺{bottom}、高さ{height}の三角形の面積は{area}です")

#58
items = [
   {"name": "りんご", "unit_price": 100, "quantity": 3},
   {"name": "みかん", "unit_price": 50, "quantity": 5},
   {"name": "バナナ", "unit_price": 80, "quantity": 2}
]

total_price = 0
for item in items:
   price = item["unit_price"] * item["quantity"]
   total_price += price

   print(total_price)

#59 0から100までの数値を出力してください。
for zero_to_100 in range(101):
   print(zero_to_100)

#60 for ～ in 1から100までのリスト作成　for文の場所注意
zero_100list = []
for i in range(1,101):
   zero_100list.append(i)

print(zero_100list)

#61 break →if ^^^^ in :
text = "あかさたな-はまやらわ"
for jp_text in text:
   if jp_text == "-":
      break
   print(jp_text)


#62
# ng_numbers = [4, 9, 13]
# for i2 in range(1,21):
#    if i2 == ng_numbers: # int 4 == list [4, 9, 13]
#       continue
#    print(i2)

ng_numbers = [4, 9, 13]

for i2 in range(1,21):
   if i2 in ng_numbers:
      continue
   print(i2)

#63
for i3 in range(1,21):
   if i3 % 3 == 0:
      print(f"{i3}は3の倍数")
   else:
      print(i3)

#64 endswith 文字列が指定した文字列で終わっているか確認する
addresses = { "鈴木": "suzuki@example.com",
             "田中": "tanaka@example.com",
             "山田": "yamadaa@example.com",
             "サプー": "python.supu.vtuber@gmail.com"
}
gmail_addresse = {}
for name, address in addresses.items():
   if address.endswith("@gmail.com"):
      gmail_addresse[name] = address

print(gmail_addresse)

#65 九九の出力
for ku in range(1,10):                      #
   for kuku in range(1,10):
      print(f"{ku} x {kuku} = {ku * kuku}")

#66 def 引数に文字列の値を一つ受け取る
def print_string(text):
   print(text)


print_string("hello,python!")

#67 def add2つの数値を足し合わせる関数
a = 10
b = 20

def add(xa, xb):
   z = xa + xb
   return z

result = add(a, b)
print(result)

#68
numbers_68 = [14, 32, 80, 1, 9]

def sum_and_avg(nums):
   total = sum(nums)
   ave = total / len(nums)
   return total, ave

total, ave = sum_and_avg(numbers_68)
print(total)
print(ave)

#69
numbers_69 = [14, 32, 80, 1, 9]

def is_even(n):
    return n % 2 == 0

for num in numbers_69:
   if is_even(num):
      print(f"{num}は偶数")
   else:
      print(f"{num}は奇数")

#70
def drink_price(drink_size, has_whip=False): 
   price = 0
   if drink_size == "S":
      price += 100
   elif drink_size == "M":
      price += 200
   elif drink_size == "L":
      price += 300

   if has_whip:
      price += 100
   return price

drink_price_M_whip = drink_price("M",True)
drink_price_L = drink_price("L")
print(drink_price_M_whip)
print(drink_price_L)

#71
JP_MONTHS = {1:"睦月", 2:"如月", 3:"弥生", 4:"卯月", 
             5:"皐月", 6:"水無月", 7:"文月", 8:"葉月",
             9:"長月", 10:"神無月", 11:"霜月", 12:"師走"}

def print_jp_month(month):
   print(f"{month}月は和風月名で{JP_MONTHS[month]}です")

print_jp_month(3)
print_jp_month(12)

#72 リストの先頭の文字が大文字だったらすべて大文字にして返す
words = ["Apple", "banana", "Cherry", "lemon"]
def modify_words(word):
   first_char = word[0]
   if first_char.isupper():
      return word.upper()
   else:
      return word
   
modified_words = []
for word in words:
   m_word = modify_words(word)
   modified_words.append(m_word)

print(modified_words)

#73　studesというクラス定義をかいてください　インスタンス変数???
#　インスタンス変数　nameは名前　（文字列）→空文字で初期化　gradeは学年１で初期化。。。
#class Student:
   #def __init__(self):#オブジェクトが生成されたとき自動で呼び出されるめそっど？
      # self.name = ""
       #self.grade = 1
       #self.section = "A"
       #self.scores = {}

#74 イニシャライザーの引数で初期化するように変更？？
#class Student:
   #def __init__(self, name, grade, section):
       #self.name = name
       #self.grade = grade
       #self.section = section
       #self.scores = {}

#student = Student("鈴木", 2, "B")
#print(student.grade)

#75
#class Student:
   #def __init__(self, name, grade, section):
       #self.name = name
       #self.grade = grade
       #self.section = section
       #self.scores = {}

   #def add_score(self, subject, score):
      #self.scores[subject] = score#keyをsubjectvalueをscoreとしてついか


#student = Student("鈴木", 2, "B")
#student.add_score("数学", 80)
#student.add_score("英語", 70)
#student.add_score("国語", 90)
#print(student.scores)

#76
#class Student:
   #def __init__(self, name, grade, section):
       #self.name = name
       #self.grade = grade
       #self.section = section
       #self.scores = {}

   #def add_score(self, subject, score):
      #self.scores[subject] = score

   #def total_score(self):
       #return  sum(self.scores.values())
   
#student = Student("鈴木", 2, "B")
#student.add_score("数学", 80)
#student.add_score("英語", 70)
#student.add_score("国語", 90)
#print(student.total_score())

#77 インスタンス変数変更
#class Student:
   #def __init__(self, name, grade, section):
       #self.name = name
       #self.grade = grade
       #self.section = section
       #self.scores = {}

   #def add_score(self, subject, score):
      #self.scores[subject] = score

   #def total_score(self):
       #return  sum(self.scores.values())
   
#student = Student("鈴木", 2, "B")
#student.grade = 3
#student.section = "C"
#print(student.grade)
#print(student.section)

#78 三人の合計
class Student:
   def __init__(self, name, grade, section, scores):
       self.name = name
       self.grade = grade
       self.section = section
       self.scores = scores

   def add_score(self, subject, score):
      self.scores[subject] = score

   def total_score(self):
       return  sum(self.scores.values())

student_1 = Student("鈴木", 2, "B", {"数学": 80, "英語": 70, "国語":90})
student_2 = Student("田中", 2, "B", {"数学": 70, "英語": 80, "国語":75})
student_3 = Student("斎藤", 2, "B", {"数学": 90, "英語": 85, "国語":80})

for student in [student_1, student_2, student_3]:
   print(f"{student.name}さんの合計点数は{student.total_score()}点です")

#79
class Card:
   def __init__(self, suit, number):
      self.suit = suit
      self.number = number

import random #pythonのrandomという標準装備を呼び出し

class Deck:
   def __init__(self):
      self.cards = []
      for suit in ["ハート", "ダイヤ", "スペード", "クラブ"]:
          for number in range(1,14):
              card = Card(suit, number)
              self.cards.append(card)

   def shuffle(self):
       random.shuffle(self.cards)

   def draw_card(self):
       return self.cards.pop(0)

#80    カード全部だす
#deck = Deck()
#deck.shuffle()
#for card in deck.cards:
   #print(f"{card.suit}{card.number}")

#81
deck = Deck()
deck.shuffle()
for _ in range(5):#処理を5回する_はrangeから生成される数字を使わないという意
   card = deck.draw_card()
   print(f"{card.suit}{card.number}")

#82
from module import add

result = add(1, 2)
print(result)

#83
from module import Card, URL

card = Card("ハート", 1)
print(f"{card.suit}{card.number}")
print(URL)

#84
import module
result = module.add(1, 2)
print(result)
print(module.URL)

#85
from __pycache__.module2 import add, URL

result = add(1,2)
print(result)

#86 新しいファイルをつくる
text = "こんにちわ！"

with open("doc.txt", "w") as f:
   f.write(text)
#87　新しいファイルに書き込み
with open("doc.txt", "a") as f:
   f.write("\nさようなら！")
#88　ファイルの読み込み
with open("doc.txt", "r") as f:
   text = f.read()

   print(text)
#89 外部ファイルリスト化
with open("doc.txt", "r") as f:
   lines = f.readlines()

print(lines)

#90
#x = 230
#result = x / 0
#print(result)
#91 try例外が発生する可能性があるコードexcept例外の種類
x = 10
try:
   result = x / 0
   print(result)
except ZeroDivisionError:
   print("ゼロで割ることはできません。")

#92
#x = 10
#y = 12
#numbers = [1, 4, 0, 12, 6]

#try:
   #result = y / numbers[x]
   #print(result)
#except IndexError:
   #print("リストの範囲を超えるインデックスです")
#except ZeroDivisionError:
   #print("ゼロで割ることはできません")

#93 exceptの後ろには,で複数指定できる。 
x = 10
y = 12
numbers = [1, 4, 0, 12, 6]

try:
   result = y / numbers[x]
   print(result)
except (IndexError, ZeroDivisionError):
   print("エラーが発生しました。")

#94 python module math
import math

r = 3
circle_area = r ** 2 * math.pi
print(circle_area)

#95 os getenv
import os
home= os.getenv("HOMEPATH")
print(home)

#96 date time today
from datetime import date

today = date.today()
print(today)

#97 time sleep
import time 

for i in range(1, 4):
   print(i)
   time.sleep(1)

#98 pathlib
from pathlib import Path

current_dir = Path.cwd()
print(current_dir)

#99 art
from art import text2art

result = text2art("Python VTuber")
print(result)

#100 qrcode 引数にURL　makeの戻り値は画像オブジェクト
import qrcode

url = "https://www.youtube.com/watch?v=v5lpFzSwKbc&list=LL&index=11&t=6489s"
img = qrcode.make(url)
img.save("supu.png")
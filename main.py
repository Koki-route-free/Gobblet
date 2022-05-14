# 2人のプレイヤーをそれぞれBLACK,WHITEとする
BLACK = +1
WHITE = -1
EMPTY = 0

# 小から特大を1から4で表示
# 黒
B1 = 1
B2 = 2
B3 = 3
B4 = 4
# 白
W1 = -1
W2 = -2
W3 = -3
W4 = -4

# 初期配置（3次元で考える4*4*4）
board_3d = [
  [[EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY]],
  [[EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY]],
  [[EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY]],
  [[EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY]],
]


# コマとプレイヤーの表示方法
disk_character = {EMPTY:"  -", B1:" B1", B2:" B2", B3:" B3", B4:" B4", W1:" W1", W2:" W2", W3:" W3", W4:" W4"}
player_name = {BLACK: "BLACK : ", WHITE: "WHITE : "}

# 最初の手持ちのコマ
black_hand = [B1, B1, B2, B2, B3, B3, B4, B4]
white_hand = [W1, W1, W2, W2, W3, W3, W4, W4]
hand = {BLACK: black_hand, WHITE: white_hand}

# 2次元の表示配置 (一番上に見えているものを表示)
def d_board_2d():
  board_2d = []
  for row in board_3d:
      board_line = []
      for disk in row:
          if EMPTY!=disk[3]:
              board_line.append(disk[3])
          elif EMPTY!=disk[2]:
              board_line.append(disk[2])
          elif EMPTY!=disk[1]:
              board_line.append(disk[1])
          elif EMPTY!=disk[0]:
              board_line.append(disk[0])
          else:
              board_line.append(disk[0])
      board_2d.append(board_line)
  return board_2d
    
# ゲームボードの表示
def print_board():
  print()
  print("   a  b  c  d")
  board_2d = d_board_2d()
  for y, row in enumerate(board_2d):
      board_line = str(y + 1)
      for disk in row:
          board_line += disk_character[disk]
      print(board_line)
  print()

# 手持ちの表示
def print_hand(player: int):
  str_hand = player_name[player]
  for i in hand[player]:
      str_hand += disk_character[i]
  print(str_hand)
    
# プレイヤーの取得
def opponent(player: int):
  return player * -1

# 置く位置を入力し取得
def input_coordinate(player: int):
  while True:
      try:
          coordinate = input(player_name[player] + "Input. 動かすコマの場所（手駒からならz9）、置く盤面、置くコマex) a2a1B1 : ")
          assert len(coordinate) == 6  # 6 文字で無ければ、再入力
          input_1 = ord(coordinate[0]) - ord("a")
          input_2 = int(coordinate[1]) - 1
          input_3 = ord(coordinate[2]) - ord("a")
          input_4 = int(coordinate[3]) - 1
          input_56= int(coordinate[5])
          return input_1, input_2, input_3, input_4, input_56
      except (ValueError, AssertionError):
          pass

# ゲームが終わる条件
def finish_game():
  board_2d = d_board_2d()
  winner = 0
  #横が揃う
  for i in board_2d:
      if all([j > 0 for j in i]):
          winner = +1
          return winner
      elif all([j < 0 for j in i]):
          winner = -1
          return winner
  #縦が揃う
  for i in range(4):
      if board_2d[0][i]>0 and board_2d[1][i]>0 and board_2d[2][i]>0 and board_2d[3][i]>0:
          winner = +1
          return winner
      elif board_2d[0][i]<0 and board_2d[1][i]<0 and board_2d[2][i]<0 and board_2d[3][i]<0:
          winner = -1
          return winner
  #斜めが揃う
  if board_2d[0][0]>0 and board_2d[1][1]>0 and board_2d[2][2]>0 and board_2d[3][3]>0:
      winner = +1
      return winner
  elif board_2d[0][0]<0 and board_2d[1][1]<0 and board_2d[2][2]<0 and board_2d[3][3]<0:
      winner = -1
      return winner
  if board_2d[0][3]>0 and board_2d[1][2]>0 and board_2d[2][1]>0 and board_2d[3][0]>0:
      winner = +1
      return winner
  elif board_2d[0][3]<0 and board_2d[1][2]<0 and board_2d[2][1]<0 and board_2d[3][0]<0:
      winner = -1
      return winner
  return winner

# ゲームが続くかの判定
def exist_input():
  winner = finish_game()
  if winner==0:
      return True
  else:
      return False

# ゲーム結果の表示
def print_judgment():
  winner = finish_game()
  if winner == +1:
      print("Black Winner!!")
  elif winner == -1:
      print("White Winner!!")

# 手持ちとボードの確認と実行
def conduct_game(player:int, v:int, w:int, x:int, y:int, z:int):
  if board_3d[y][x][z-1]==EMPTY:
      wz = z * -1
      if player==BLACK:
          if w==8 and z in black_hand:
              black_hand.remove(z)
              board_3d[y][x][z-1] = z
              return True
          elif board_3d[w][v][z-1]==z:
              board_3d[w][v][z-1] = EMPTY
              board_3d[y][x][z-1] = z
              return True
      elif player==WHITE: 
          if w == 8 and wz in white_hand:
              white_hand.remove(wz)
              board_3d[y][x][z-1] = wz
              return True
          elif board_3d[w][v][z-1]==wz:
              board_3d[w][v][z-1] = EMPTY
              board_3d[y][x][z-1] = wz
              return True
  return False

# 座標入力を正しくできるまで繰り返す
def input_disk(player: int):
  while True:
      v, w, x, y, z = input_coordinate(player)
      if conduct_game(player, v, w, x, y, z):
          break

# 実際の実行関数
def main():
  player = BLACK
  print_board()
  print_hand(player)
  while True:
      input_disk(player)
      opponent_player = opponent(player)
      print()
      print("-----------------")
      print_board()
      if exist_input():
          player = opponent_player
          print_hand(player)
      else:
          break
  print_judgment()
  print()

if __name__ == "__main__":
  main()
  
bars_distance = 0
outposts_distance = 0
inns_distance = 0
bar, outpost, inn = input().split(' ')
location = int(input())
position = 1
flag = True
while flag:
  print(position)
  bars = int(bars)
  closest = bars*position
  nearest = bars_distance
  bars_distance = location - closest
  if bars_distance > nearest:
    bars_distance = closest
    flag = False
  position += 1
print(bars_distance)
  
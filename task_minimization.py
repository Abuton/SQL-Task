import sys
def ArrayChallenge(arr):

  # code goes here
  give = True
  difference = 0
  if arr[0] > 20:
    print('error')
    sys.exit

  else:
    total_sandwiches = arr[0]
    hunger_levels = sorted(arr[1:], reverse=True)
    give = False

  while give:
    for i in range(len(hunger_levels)):
      temp = hunger_levels[i] - hunger_levels[i+1]
      if temp != 0 and total_sandwiches > 0:
        if temp < 0:
          hunger_levels[i] -= total_sandwiches
          give= True
        else:
          hunger_levels[i] -= temp
          total_sandwiches -= temp
          give = True
        break

  difference = 0
  for i in range(len(hunger_levels)-1):
    temp = hunger_levels[i] - hunger_levels[i+1]
    if temp < 0:
      temp *= -1
    difference += temp
  return difference

# keep this function call here 
print(ArrayChallenge(input()))

import random
import time
import requests
print("***The Ultimate POKEMON card stats game!***")
print()
time.sleep(2)
print("Click run and you will be assigned a random POKEMON character.")
print()
time.sleep(2)
print("When prompted, type which stat you want to compare agaisnt your opponent's character.")
print()
time.sleep(2)
print("There will be 3 chances to play and the first player to have 2/3 wins, wins the entire game!")
print()
time.sleep(2)
print("Good luck! Now go play!...")
print()
time.sleep(2)

def random_pokemon():
  pokemon_number = random.randint(1, 151)
  url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
  response = requests.get(url)
  pokemon = response.json()
    
  return {
  'name': pokemon['name'],
  'id': pokemon['id'],
  'height': pokemon['height'],
  'weight': pokemon['weight'],
    }


def run():
  mywin = 0
  oppwin = 0
  while mywin<2 and oppwin<2:
    
    my_pokemon = random_pokemon()
    print()
    print('You were given {}'.format(my_pokemon['name']))
    print()
    stat_choice = input('Which stat do you want to use? (id, height, weight) >> ')
    print()
    opponent_pokemon = random_pokemon()
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    print()
    time.sleep(2)
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    
    if my_stat > opponent_stat:
      mywin +=1
      print('Your stat is ', my_stat)
      print('Your opponents stat is ', opponent_stat)
      print('You Win! You have', mywin, "point!")
      print()
      time.sleep(2)
      
    elif my_stat < opponent_stat:
      oppwin+=1
      print('Your stat is ', my_stat)
      print('Your opponents stat is ', opponent_stat)
      print('You Lose! Your oppenent has', oppwin, "point!")
      print()
      time.sleep(2)

    else:
        print("The game is over.")
   
    if mywin==2 or oppwin==2:
      print("Game is over.")
      print()
  while True:
    start_again = input("Do you want to play again? y/n > ")
    if start_again == "y":
      run()
    else:
      break
run()


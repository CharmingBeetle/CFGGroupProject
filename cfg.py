import random
import requests
import time


#THIS FUNCTION IS GETTING A RANDOM POKEMON FROM THE API
def random_pokemon():
  pokemon_number = random.randint(1, 151)
  url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
  response = requests.get(url)
  pokemon = response.json()
  return dict(name=pokemon['name'],
              id=pokemon['id'],
              height=pokemon['height'],
              weight=pokemon['weight'],
              experience=pokemon['base_experience'])


#THIS FUNCTION IS GETTING A POKEMON BY ITS NAME OR ID NUMBER FROM THE API
def fetch_certain_pokemon(poke_name):
  url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_name)
  response = requests.get(url)
  pokemon = response.json()
  return dict(name=pokemon['name'],
              id=pokemon['id'],
              height=pokemon['height'],
              weight=pokemon['weight'],
              experience=pokemon['base_experience'])


def game():
  #SET GAME SCORE COUNTER TO ZERO
  user_score = 0
  computer_score = 0

  #GAME INSTRUCTIONS
  print("***The Ultimate POKEMON card stats game!***")
  time.sleep(2)
  winning_score = int(
    input(
      "You will play rounds with your opponent until one of you wins.  How many points is your goal? "
    ))
  print("Good luck! Now go play!...")
  time.sleep(2)

  #LOOP THE GAME UNTIL THE WINNING SCORE
  while user_score < winning_score and computer_score < winning_score:

    #RETREIVE TWO RANDOM POKEMONS AND IF THEY ARE THE SAME CHANGE IT TO ANOTHER ONE
    pokemon_one = random_pokemon()
    pokemon_two = random_pokemon()
    while pokemon_one == pokemon_two:
      pokemon_two = random_pokemon()
    print('You were given 1-{} and 2-{}'.format(pokemon_one['name'],
                                                pokemon_two['name']))
    pokemon_choice = input('Which pokemon do you want to choose? ').lower()

    #USER CANNOT ENTER ANOTHER POKEMON NAME AND GET ITS DATA
    if pokemon_choice != pokemon_one['name'] and pokemon_choice != pokemon_two[
        'name']:
      print('Invalid answer')

    #USER PICKS ONE OF THE OPTIONS AND GET A RANDOM POKEMON FOR THE COMPUTER
    elif pokemon_choice == pokemon_one['name'] or pokemon_two['name']:
      print('You have chosen {}'.format(pokemon_choice))
      opponent_pokemon = random_pokemon()
      time.sleep(2)
      print('Your opponent chose {}'.format(opponent_pokemon['name']))
      time.sleep(2)
      my_pokemon = fetch_certain_pokemon(pokemon_choice)

      #USER PICKS THE HIGHEST SCORE WITHIN THE STATS
      print('Your stats are id:{}, weight:{}, height:{},experience:{}'.format(
        my_pokemon['id'], my_pokemon['weight'], my_pokemon['height'],
        my_pokemon['experience']))
      time.sleep(3)
      stat_choice = input('Which stat do you want to use? ').lower()
      print('You have chosen {}'.format(stat_choice))
      my_stat = my_pokemon[stat_choice]
      time.sleep(2)

      #COMPUTER PICKS THE HIGHEST STAT
      choice_list = [
        opponent_pokemon['id'], opponent_pokemon['height'],
        opponent_pokemon['weight'], opponent_pokemon['experience']
      ]

      if opponent_pokemon['id'] == max(choice_list):
        computer_stat_choice = 'id'
      elif opponent_pokemon['height'] == max(choice_list):
        computer_stat_choice = 'height'
      elif opponent_pokemon['weight'] == max(choice_list):
        computer_stat_choice = 'weight'
      elif opponent_pokemon['experience'] == max(choice_list):
        computer_stat_choice = 'experience'
      opponent_stat = opponent_pokemon[computer_stat_choice]
      print('Your opponent has chosen {}, and its value is {}'.format(
        computer_stat_choice, opponent_pokemon[computer_stat_choice]))
      time.sleep(3)

      #WHEN USER STAT IS HIGHER THAN COMPUTER, USER WINS
      if my_stat > opponent_stat:
        user_score += 1
        print('You Win! Your Score: ', user_score, 'Computer Score: ',
              computer_score)
        print(
          '---'
        )  #THIS PRINT AND SLEEP IS ONLY FOR FORMATTING AND MORE READABILITY
        time.sleep(2)

      #USER STAT IS LESS THAN COMPUTER, COMPUTER WINS
      elif my_stat < opponent_stat:
        computer_score += 1
        print('You Lose! Your Score: ', user_score, 'Opponents Score: ',
              computer_score)
        print('---')
        time.sleep(2)

      #DRAW
      else:
        print('Draw!')
        print('---')
        time.sleep(2)

  #GAME IS OVER WHENEVER THE WINNING SCORE IS ACHIEVED
  if user_score or computer_score == winning_score:
    print('Game Over!')
    play_again_answer = input('Would you like to play again? (Yes/No) ')
    if play_again_answer == 'Yes':
      game()
    elif play_again_answer == 'No':
      print('Thank you for playing! Goodbye for now')
      exit()


game()
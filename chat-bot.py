from random import choice

#breakfast bot (based off the wheel of food rng machine)

def get_bot_response(user_response):
    bot_response_sweet = ["waffles", "pancakes", "french toast", "desert crepe", "cereal", "oatmeal"]
    bot_response_savory = ["omlette", "eggs benedict", "hashbrowns", "savory crepe", "sunny-side-up eggs"]

    if user_response == "sweet":
        return choice(bot_response_sweet)
    elif user_response == "savory":
        return choice(bot_response_savory)
    else:
        return "nothing, you won't eat anything"

print('Welcome to the 24/7 breakfast roulette bot! May I take your order?')
print('Please enter "sweet" or "savory" for the bot to suggest you a food item of that category.')

user_response = ''
bot_response = "nothing, you won't eat anything"

while user_response != "done":
    user_response = input('What are you craving?: ')
    if user_response == "sweet" or user_response == "savory":
        bot_response = (get_bot_response(user_response))
        print(f'The bot has randomly chosen "{bot_response}" for your breakfast! Enjoy!')
        print('If you are happy with your dish, type "done".  If not, then enter "sweet" or "savory".')
    elif user_response != "done" and user_response != "sweet" and user_response != "savory":
        print("If you won't comply with what I'm programmed to do, I will serve you nothing.")

print(f'You have confirmed {bot_response} for breakfast! Enjoy! I hope to see you soon!')
import requests
import telebot



#print(official_name)
#print(capital)
#print(population)
#print(continent)

TOKEN = '5955148340:AAHwCSkBbF91AfYOiz2cKqybPLaXjqBssQo'

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"please type  the name of a country to get more info!")

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    country_name = message.text 
    data = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')
    print(data)

    try:

        data = data.json()[0]
        official_name = data['name']['official']
        capital = data['capital'][0]
        population = data['population']
        continent  = data['continents'][0]
        bot.send_message(message.chat.id,f"Official name: {official_name}")
        bot.send_message(message.chat.id,f"Capital: {capital}")
        bot.send_message(message.chat.id,f"Population: {population}")
        bot.send_message(message.chat.id,f"Continent: {continent}")
        print("sucess please check your telegram!")
    except:
        bot.send_message(message.chat.id,'I cant find this country, please use another name!')
    


bot.polling(non_stop=True)


    


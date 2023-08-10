import random
import openai
import aiohttp


def handle_response(message, channel) -> str:
    p_message = message.lower()
    c_message = channel

    if p_message == 'f!roll':
        return str(random.randint(1, 6))

    if p_message == 'f!help':
        return "`These are the commands that you can use: \nf!roll - to roll a dice \nf!play - to play music`"

    if p_message == 'sa':
        return 'as hg'

    if p_message.startswith('f!play'):
        if p_message.split(" ", 1)[1].startswith("https://"):
            url = p_message.split()[1]
            pass
        else:
            song = p_message.split(" ", 1)[1]
            url = create_youtube_url(song)
            pass

    if p_message.startswith('f!stats'):
        if p_message.split(" ", 2)[1] == 'valorant':
            game = p_message.split(" ", 2)[1]
            nickname = p_message.split(" ", 2)[2]
            url = create_trackergg_url(game, nickname)
            return "Displaying stats for"
        else:
            return "Invalid game, please try one of these --> valorant"

    if c_message == 'ask_ai':
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=p_message,
            max_tokens=3000,
            temperature=0.7
        )
        output = response["choices"][0]["text"]
        return output


def create_youtube_url(search) -> str:
    youtube_url = "https://www.youtube.com/results?search_query="
    for i in search:
        if i.index == 0:
            youtube_url += i
        else:
            youtube_url += "+"
            youtube_url += i
    return youtube_url


def create_trackergg_url(game, nickname) -> str:
    stats_url = "https://tracker.gg/"
    stats_url += game
    stats_url += "/profile/riot/"
    stats_url += nickname.replace("#", "%23")
    stats_url += "/overview"
    return stats_url

import datetime
import json
import random
from pathlib import Path

#This script provides a daily news header for the Discord webhook message, consisting of a formatted date and randomly selected awesome headline.

#Headlines to cycle through, resets once all are used. DON'T READ UNLESS YOU WANT TO SPOIL YOURSELF!!
HEADLINES = [
    "Of course the bloody incredible MudSk1p squad once again has done something truly remarkable.",
    "We have some :bangbang:BREAKING NEWS:bangbang: over at the MudSkip clan:",
    "<:dogwater:839613193092857916> ***Woof Woof!*** <:Dog:1022526553827070062> ... wait, is that a dog? Is that Mayh? Wait, no! it is the Mudsk1pperz barking up a storm once again!",
    "Ouughhehhhn",
    "Wagwan fam, news innit?",
    "Reporters say this is something never seen before. Something no one has ever done before. This might genuinely be a world first.",
    "Hey guys could we not schedule officials for 20? I have to eat dinner with my family. :fork_knife_plate: :yum: ",
    ":bangbang:A NUCLEAR STRIKE HEADING STRAIGHT FOR HULL HAS BEEN DETECTED:bangbang: \"Good riddance.\" - Andy Burnham",
    "The announcement today might not be a new logjam update, but it is the next best thing. Mud Skip News.",
    "I'm never letting Figaro write a news headline again the burtons on my keybaort is all fuicking chewed on.",
    "GZZZZ",
    "You know they actually keep me locked in a dark and damp room in Darkmeyer and have me write these, right? By contributing to these news, you are contributing to my suffering.",
    "A Saradoming brew and a Super restore, just 10,000 GP today at Tesco's meal deal.",
    "Tragically, with today's game update you will be able to buy XP lamps through the new Squeal of Fortune. LOL u got pranked here is actually the crazy news of the day.",
    "<:bgs:1515022043475738724>\nbobbyBojack: i hit a big one"
    "<a:muttadozer:731552600243306516>"
]

#File to keep track of used headlines.
USED_HEADLINES_PATH = "used_headlines.json"

#Returns a formatted header string with today's date and a rotating headline. Ensures no headline is replaced until all others have been used once.
def get_daily_header():
    #Load list of previously used headlines (or start fresh if none exist)
    try:
        with open(USED_HEADLINES_PATH, "r") as f:
            used = json.load(f)
    except FileNotFoundError:
        used = []
    
    #Filter out used headlines.
    available = [h for h in HEADLINES if h not in used]

    #Reset the cycle once all headlines have been used.
    if not available:
        used = []
        available = HEADLINES[:]

    #Pick a headline at random from the remaining pool.
    chosen = random.choice(available)
    used.append(chosen)

    #Save the updated used list back to file.
    with open(USED_HEADLINES_PATH, "w") as f:
        json.dump(used, f)

    #Format today's date in bold with the correct ordinal suffix. Assumes Discord's markdown text
    today = datetime.date.today()
    day = today.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    date_str = f"**{day}{suffix} of {today.strftime('%B')}**"

    #Return a combined string of the date and headline.
    return f"{date_str}\n{chosen}"

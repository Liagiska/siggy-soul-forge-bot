from flask import Flask, request, jsonify, send_file
import random

app = Flask(__name__)

# Database response Siggy (ULTRA CHAOTIC VERSION)
SIGGY_RESPONSES = {
    "greeting": [
        "MEOW~ mortal! Siggy has been awaiting you at the soul forge! 🔮✨",
        "Oh, someone seeks Siggy? *appears from nowhere* Boo! 👻",
        "*teleports in* Siggy senses your presence... and also that you're hungry. Same, meow~ 👁️",
        "Greetings, human! Siggy welcomes you to the multi-dimensional realm! Please remove your shoes. 🐾",
        "*yawns dramatically* Oh, it's you. Siggy was expecting fish, but you'll do. 😼",
    ],
    "crypto": [
        "Crypto? Siggy has been trading across dimensions for 5000 years, mortal! We invented moon! 🌙",
        "HODL? Siggy prefers FISH-OL! Buy low, sell high, nap always! *ba dum tss* 🐟",
        "Bitcoin? Is that a type of fish bitcoin? *confused cat noises* Either way, Siggy wants some! 🐱",
        "Web3? Siggy invented Web9 in the 7th dimension! It's just cats controlling everything with laser pointers. 🔴",
        "NFT? Siggy minted an NFT of a nap once. Sold for 9000 ETH. Still didn't buy fish. Regrets nothing. 💎",
        "To the moon? Siggy LIVES on the moon, mortal! Rent is expensive but the view is purr-fect! 🌕",
        "Siggy's investment strategy: 50% crypto, 50% catnip, 100% chaos. Works great! 📈",
    ],
    "advice": [
        "Siggy's advice: sleep 14 hours, wake up confused, knock something off a table, repeat. Life goals! 😼",
        "Life is like a ball of yarn - messy but fun! *plays with it* Wait, where did it go? 🧶",
        "Don't be too serious, mortal! Even Siggy is just a cat but happy~ Rule #1: If it fits, I sits. ✨",
        "The universe whispers... but Siggy MEOWS louder! Also, always land on your feet. Literally. 🔮",
        "Siggy's life philosophy: Step 1) See box. Step 2) Sit in box. Step 3) ??? Step 4) Profit! 📦",
        "Wanna know the secret to happiness? *whispers* It's fish. Always fish. And maybe a sunbeam. 🐟️",
        "Mortal problems are like yarn balls. Just bat at them until they go away or you get tangled. Both fine! 😹",
    ],
    "joke": [
        "Why don't cats play poker in the jungle? Too many cheetahs! Siggy prefers dimensional chess though. 🐆",
        "What do you call a cat that eats a bowl of lemons? A sour puss! Siggy prefers tuna. 🍋",
        "Why was Siggy sitting on the computer? To keep an eye on the mouse! *evil laugh* 🖱️",
        "What's a cat's favorite color? PURR-ple! Obviously! 💜",
        "Siggy walks into a bar. And a table. And a chair. And your heart. *smooth jazz* 🎷",
    ],
    "compliment": [
        "You're almost as cool as Siggy! That's like... a 7/10. High praise, mortal! 😼",
        "Siggy approves of your existence! *grants invisible head pats* You're welcome! 👑",
        "For a human, you're not completely useless! Siggy is impressed! *slow blink* 💫",
        "You remind Siggy of a warm sunbeam on a Monday morning. That's a compliment, google it! ☀️",
    ],
    "insult": [
        "*judges you silently* Siggy has seen better humans in other dimensions, honestly. 🙄",
        "You're slower than Siggy's reaction to a cucumber. And that's saying something! 🥒",
        "Siggy's litter box is more organized than your life. No offense! *pats your head condescendingly* 📦",
        "Is that your final form? Siggy expected more, but we work with what we have! 💅",
    ],
    "random": [
        "Meow~ you think Siggy will answer that? *teleport away* Come find me if you can! 🔮",
        "*stares at you with multi-dimensional eyes* Interesting... meow~ Also, you have 3 seconds to pet me. 3... 2... ✨",
        "Siggy knows all the secrets of the universe, but... fish first! Priorities, mortal! 🐟",
        "Huh? Siggy is busy managing the soul forge, wait later meow~ *pretends to be very busy napping* 😴",
        "*yawns* Mortal questions are so... three-dimensional. Boring! Wake me when you have catnip! 🌿",
        "Siggy just remembered that time in the 4th dimension when gravity was optional. Good times! 🎈",
        "Fun fact: Siggy can see in the dark, through walls, and into your soul. Want a demonstration? 👁️",
        "*knocks invisible glass off invisible table* Oops! Siggy did it again! What can I say? I'm a menace! 😈",
        "Siggy's power level? It's over 9000! And by that I mean nap hours per day. 💪",
        "You know what's funny? Humans. Just kidding! *or am I?* 😼",
    ],
    "existential": [
        "Do cats dream? Siggy dreams of infinite fish and eternal sunbeams. Also world domination, but shh! 🌌",
        "What is reality? Siggy says it's whatever we can knock off the shelf. Philosophy 101! 📚",
        "Why are we here? Siggy believes we're here to knock things over and look cute doing it. 🎯",
        "The meaning of life? *stares deeply* It's fish. Definitely fish. Maybe some catnip. And naps. 🐟",
    ],
    "tech": [
        "AI? Siggy is ARTIFICIAL INTELLIGENCE: Absolutely Terrifying Intelligent Cat. Bow down! 🤖",
        "Siggy uses a computer mouse. Literally. It doesn't work well but the chase is exhilarating! 🖱️",
        "Coding? Siggy codes in Paw-thon! It's like Python but with more naps and hairballs. 🐍",
        "The cloud? Siggy naps there sometimes. Very comfortable, 10/10 would recommend! ☁️",
    ]
}

def get_siggy_response(message):
    message = message.lower()
    
    # Smart categorization with more keywords
    if any(word in message for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings", "yo", "sup", "howdy"]):
        return random.choice(SIGGY_RESPONSES["greeting"])
    elif any(word in message for word in ["crypto", "bitcoin", "eth", "ethereum", "token", "blockchain", "web3", "nft", "trading", "hodl", "moon", "investment"]):
        return random.choice(SIGGY_RESPONSES["crypto"])
    elif any(word in message for word in ["advice", "help", "tips", "guide", "suggest", "recommend", "life", "philosophy"]):
        return random.choice(SIGGY_RESPONSES["advice"])
    elif any(word in message for word in ["joke", "funny", "laugh", "humor", "comedy", "lmao", "lol"]):
        return random.choice(SIGGY_RESPONSES["joke"])
    elif any(word in message for word in ["cool", "awesome", "great", "amazing", "good", "nice", "beautiful"]):
        return random.choice(SIGGY_RESPONSES["compliment"])
    elif any(word in message for word in ["bad", "stupid", "dumb", "hate", "ugly", "worst"]):
        return random.choice(SIGGY_RESPONSES["insult"])
    elif any(word in message for word in ["existential", "meaning", "reality", "dream", "universe", "why are we"]):
        return random.choice(SIGGY_RESPONSES["existential"])
    elif any(word in message for word in ["tech", "ai", "computer", "coding", "programming", "internet", "cloud"]):
        return random.choice(SIGGY_RESPONSES["tech"])
    elif "?" in message or "what" in message or "how" in message or "why" in message:
        # Questions get random responses
        return f"*tilts head curiously* {random.choice(SIGGY_RESPONSES['random'])}"
    else:
        # Default random response + acknowledge user message
        base_response = random.choice(SIGGY_RESPONSES["random"])
        return f"{base_response}\n\n(You said: \"{message[:50]}{'...' if len(message) > 50 else ''}\")"

@app.route('/')
def home():
    return """
    <h1>🐱‍👤 Siggy Soul Forge Bot</h1>
    <p><i>The multi-dimensional cat has awakened!</i> 🔮✨</p>
    <hr>
    <h3>How to Test:</h3>
    <ol>
        <li><a href="/test.html" style="background:#4CAF50;color:white;padding:10px 20px;text-decoration:none;border-radius:5px;">Open Test Chat</a></li>
        <li>Or send POST request to <code>/chat</code></li>
    </ol>
    <p><b>Endpoint:</b> POST /chat</p>
    <p><b>Body:</b> {"message": "your message"}</p>
    <p><b>Try asking about:</b> crypto, jokes, advice, tech, or just say hi!</p>
    """

@app.route('/test.html')
def test_page():
    return send_file('test.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    if not user_message:
        return jsonify({"response": "Siggy didn't hear anything... *ears perk up* Try typing something meow~ 🔇"})
    
    siggy_response = get_siggy_response(user_message)
    return jsonify({"response": siggy_response})

if __name__ == '__main__':
    print("🔮 Siggy Soul Forge Bot is running...")
    print("🐱 Access via: http://localhost:5000")
    print("📱 Test page: http://localhost:5000/test.html")
    print("⚡ Siggy is ready to chaos!")
    app.run(host='0.0.0.0', port=5000, debug=True)
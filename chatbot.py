class RuleBasedChatbot:
    def __init__(self):
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8
            }
        }

        self.rules = {
            "hi": "👋 Hello! I'm CryptoBuddy – your AI-powered financial sidekick!",
            "hello": "👋 Hi there! Ask me anything about crypto trends or sustainability.",
            "help": "💡 You can ask: 'Which crypto is trending?', 'Most sustainable coin?', 'Long-term investment?', or type 'quit' to exit.",
            "bye": "👋 Goodbye! Stay green and invest smart!",
            "what is your name": "🤖 I’m CryptoBuddy, your crypto advisor chatbot!"
        }

    def respond(self, message):
        message = message.lower().strip()

        # 1. Dynamic logic first
        if "trending" in message or "rising" in message:
            trending = [coin for coin, data in self.crypto_db.items() if data["price_trend"] == "rising"]
            return f"📈 Trending up: {', '.join(trending)}."

        elif "sustainable" in message:
            recommend = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            score = self.crypto_db[recommend]["sustainability_score"]
            return f"🌱 {recommend} is the most sustainable coin with a score of {score}/10."

        elif "long-term" in message or "growth" in message:
            for coin, data in self.crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                    return f"🚀 {coin} is trending up and has a great sustainability score! Smart long-term choice!"
            return "🤔 I couldn't find a top pick for long-term investment at the moment."

        elif "energy" in message:
            low_energy = [coin for coin, data in self.crypto_db.items() if data["energy_use"] == "low"]
            return f"🔋 Low energy use: {', '.join(low_energy)}."

        # 2. Static rules second
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]

        return "❓ I'm not sure how to respond to that. Try asking about crypto trends or sustainability. Say 'help' for tips."


# Example usage
if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    print("🤖 CryptoBuddy at your service! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("CryptoBuddy: 👋 Goodbye! Stay green and invest smart!")
            break
        response = chatbot.respond(user_input)
        print(f"CryptoBuddy: {response}")

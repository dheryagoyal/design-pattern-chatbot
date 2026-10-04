from chatbot import Chatbot
from strategy import FormalStrategy, InformalStrategy

print("Welcome to the Design Pattern Chatbot!")
print("Choose a personality:")
print("1. Formal")
print("2. Informal")

choice = input("Enter 1 or 2: ")

if choice == "1":
    strategy = FormalStrategy()
    print("Formal personality selected.")
else:
    strategy = InformalStrategy()
    print("Informal personality selected.")

bot = Chatbot(strategy)

print("Type 'switch to formal' or 'switch to informal' to change personality.")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    command = user_input.lower().strip()

    if command == "bye":
        print("Bot:", bot.strategy.respond("bye"))
        break

    if command == "switch to formal":
        bot.set_strategy(FormalStrategy())
        print("Bot: Switched to formal personality.")
        continue

    if command == "switch to informal":
        bot.set_strategy(InformalStrategy())
        print("Bot: Switched to informal personality.")
        continue

    response = bot.get_response(user_input)
    print("Bot:", response)

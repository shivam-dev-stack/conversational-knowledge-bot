from agent import KnowledgeBot

bot = KnowledgeBot()

while True:
    q = input("\nYou: ")

    if q == "exit":
        break

    ans = bot.ask(q)
    print("\nBot:", ans)

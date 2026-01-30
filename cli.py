from agent import create_agent

agent = create_agent()

print("Conversational Knowledge Bot (type 'exit')")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = agent.run(user_input)
    print("\nBot:", response)

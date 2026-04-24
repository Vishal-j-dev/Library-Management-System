import time
from datetime import datetime


class User:
    def __init__(self, name):
        self.name = name
        self.__history = []

    def add_history(self, message):
        self.__history.append((datetime.now(), message))

    def get_history(self):
        return self.__history


class HealthAdvisor:
    def __init__(self):
        # symptom : advice
        self.__advice_db = {
            "fever": "Stay hydrated, take rest, and monitor temperature.",
            "cold": "Drink warm fluids and rest well.",
            "headache": "Try resting in a quiet room and stay hydrated.",
            "cough": "Drink warm water or honey tea.",
            "stomach pain": "Avoid heavy food and drink plenty of water.",
            "tired": "Ensure proper sleep and balanced diet."
        }

    def get_advice(self, symptom):
        symptom = symptom.lower()

        for key in self.__advice_db:
            if key in symptom:
                return self.__advice_db[key]

        return "I'm not sure about that. Please consult a healthcare professional."


class ChatBot:
    def __init__(self):
        self.advisor = HealthAdvisor()
        self.user = None

    def slow_print(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()

    def greet(self):
        self.slow_print("🤖 Hello! I am your Health Assistant.")
        name = input("Enter your name: ")
        self.user = User(name)
        self.slow_print(f"Nice to meet you, {name}!")

    def chat(self):
        self.slow_print("You can describe your symptoms or type 'exit' to quit.")

        while True:
            user_input = input("\nYou: ")

            if user_input.lower() == "exit":
                self.slow_print("Take care! Stay healthy 👋")
                break

            self.user.add_history(user_input)

            self.slow_print("Analyzing your symptoms...")
            time.sleep(1)

            advice = self.advisor.get_advice(user_input)

            self.slow_print(f"💡 Advice: {advice}")
            self.slow_print("⚠️ This is general advice, not a medical diagnosis.")

    def run(self):
        self.greet()
        self.chat()


# Run the chatbot
if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
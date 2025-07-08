import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import scrolledtext
import random
import time
import threading

nltk.download('punkt')

# 🎯 Knowledge Base
knowledge_base = {
    "how can i return a product?": "You can return a product within 30 days of purchase.",
    "how to track my order?": "You can track your order using the tracking link sent to your email.",
    "do you ship internationally?": "Yes, we offer international shipping to selected countries.",
    "what payment methods are available?": "We accept debit cards, credit cards, UPI, and digital wallets."
}

# 🎯 Preprocess Text
def clean_text(text):
    return text.lower().strip()

# 🎯 Chatbot Engine
class SupportBot:
    def __init__(self, knowledge):
        self.questions = list(knowledge.keys())
        self.answers = list(knowledge.values())
        self.cleaned_questions = [clean_text(q) for q in self.questions]
        self.vectorizer = TfidfVectorizer()
        self.vector_matrix = self.vectorizer.fit_transform(self.cleaned_questions)

    def get_answer(self, user_query):
        user_query_clean = clean_text(user_query)
        query_vector = self.vectorizer.transform([user_query_clean])
        similarity = cosine_similarity(query_vector, self.vector_matrix)
        best_match_index = similarity.argmax()

        # Optional delay to simulate thinking
        time.sleep(random.uniform(0.5, 1.0))

        return self.answers[best_match_index]

# 🎯 GUI App
class ChatBotApp:
    def __init__(self, master):
        self.bot = SupportBot(knowledge_base)
        self.master = master
        self.master.title("Smart ChatBot")
        self.master.geometry("500x500")
        self.master.resizable(False, False)

        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled', font=("Arial", 12))
        self.chat_area.place(x=20, y=20, width=460, height=400)

        self.user_input = tk.Entry(master, font=("Arial", 14))
        self.user_input.place(x=20, y=440, width=360, height=30)
        self.user_input.bind("<Return>", self.handle_enter)

        self.send_button = tk.Button(master, text="Send", font=("Arial", 12), command=self.send_message)
        self.send_button.place(x=400, y=440, width=80, height=30)

        self.add_bot_message("Hello! I can help you. Type 'exit' to leave.")

    def add_bot_message(self, message):
        self.chat_area['state'] = 'normal'
        self.chat_area.insert(tk.END, f"Bot: {message}\n")
        self.chat_area['state'] = 'disabled'
        self.chat_area.see(tk.END)

    def add_user_message(self, message):
        self.chat_area['state'] = 'normal'
        self.chat_area.insert(tk.END, f"You: {message}\n")
        self.chat_area['state'] = 'disabled'
        self.chat_area.see(tk.END)

    def send_message(self):
        user_text = self.user_input.get().strip()
        if user_text == "":
            return

        self.add_user_message(user_text)
        self.user_input.delete(0, tk.END)

        if user_text.lower() == 'exit':
            self.add_bot_message("Goodbye! Have a nice day.")
            self.master.after(1000, self.master.quit)
            return

        threading.Thread(target=self.respond, args=(user_text,)).start()

    def handle_enter(self, event):
        self.send_message()

    def respond(self, user_text):
        reply = self.bot.get_answer(user_text)
        self.add_bot_message(reply)

# 🎯 Run the GUI
if __name__ == "__main__":
    window = tk.Tk()
    app = ChatBotApp(window)
    window.mainloop()

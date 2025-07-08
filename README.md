# codealpha_tasks
# Task 1
<h1>🌐 Language Translator Tool</h1>

A desktop language translation application built with Python.  
It translates text between over 100 languages using Google Translate,  
supports speech input via microphone, and reads the translated output aloud.  
It also features a Light/Dark mode toggle for better user experience.

---

## 🧠 Features

- Translate text between 100+ languages using Google Translate
- Voice input via microphone using Speech Recognition
- Text-to-Speech output for translated text
- Light and Dark mode themes
- Clean and responsive GUI with Tkinter

---

## 🚀 Usage

bash
1. Run the application:
    python translator_app.py

2. Select Source Language and Target Language from the dropdown menus.

3. Enter text manually OR click the 🎤 Speak button to input by voice.

4. Click the Translate button to translate the entered text.

5. Click the 🔊 Read Aloud button to hear the translated output.

6. Use the "Dark Mode" button to toggle between Light and Dark themes.


## 📦 Requirements

- Python 3.7+
- tkinter (usually included with Python)
- googletrans==4.0.0-rc1
- pyttsx3
- SpeechRecognition
- pyaudio (for microphone input)

---




# Task 2
# 🤖 FAQ Chatbot using Python and NLP

This is a simple command-line FAQ Chatbot built using Python. It uses *NLTK* for natural language processing and *TF-IDF with cosine similarity* to match user questions with the most relevant frequently asked question.

---

## 🚀 Features

- Preprocesses questions using tokenization, lowercasing, punctuation removal, and stopword filtering
- Matches user queries with closest FAQ using cosine similarity
- Returns the most appropriate answer
- Works on command line — simple and lightweight
- Easy to customize or extend with more questions

---

## 📚 Technologies Used

- Python 3.x
- NLTK
- Scikit-learn


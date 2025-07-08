# codealpha_tasks
# Task 1
<h1>🌐 Language Translator Tool</h1>

<p>
  This project is a simple Language Translator application built in Python using Tkinter for the GUI and <code>googletrans</code> for translation.
</p>

<h2>✅ Features</h2>
<ul>
  <li>Translate text between multiple languages</li>
  <li>Easy-to-use graphical interface</li>
  <li>Copy translated text to clipboard</li>
  <li>Clear text fields easily</li>
  <li>Status messages to indicate success or errors</li>
</ul>

<h2>⚙ Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>googletrans library</li>
  <li>tkinter (usually included with Python)</li>
</ul>

<h2>🚀 Installation</h2>
<ol>
  <li>Clone this repository or download the code.</li>
  <li>Open your terminal or command prompt.</li>
  <li>Navigate to the project directory.</li>
  <li>Install the googletrans library by running:<br>
    <code>pip install googletrans==4.0.0rc1</code>
  </li>
</ol>

<h2>▶ How to Run</h2>
<ol>
  <li>Open your terminal or VS Code terminal.</li>
  <li>Navigate to the folder containing <code>language_translator.py</code>.</li>
  <li>Run the script using:<br>
    <code>python language_translator.py</code>
  </li>
  <li>The application window will open.</li>
</ol>

<h2>📝 Usage</h2>
<ol>
  <li>Type or paste the text you want to translate in the input box.</li>
  <li>Select the source language and target language from the dropdowns.</li>
  <li>Click the <strong>Translate</strong> button.</li>
  <li>View the translated text in the output box.</li>
  <li>Use the <strong>Copy Result</strong> button to copy the text to your clipboard.</li>
  <li>Use the <strong>Clear</strong> button to reset all fields.</li>
</ol>

<h2>🌍 Supported Languages</h2>
<ul>
  <li>English</li>
  <li>Hindi</li>
  <li>French</li>
  <li>Spanish</li>
  <li>German</li>
  <li>Chinese</li>
</ul>

<h2>💡 Customization</h2>
<p>
  You can add more languages by extending the <code>supported_languages</code> dictionary in the code.
</p>

<h2>📂 Project Structure</h2>
<pre>
language_translator.py
README.md
</pre>

<h2>🙌 Acknowledgments</h2>
<ul>
  <li>Google Translate API (via googletrans library)</li>
  <li>Tkinter for the GUI</li>
</ul>

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


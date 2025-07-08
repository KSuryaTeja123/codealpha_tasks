import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Custom Translator Function
def perform_translation():
    try:
        translation_engine = Translator()
        source = source_language.get()
        destination = target_language.get()
        user_input = input_text.get("1.0", tk.END).strip()

        if user_input == "":
            messagebox.showwarning("Empty Input", "Please type something to translate.")
            return

        translated = translation_engine.translate(user_input, src=source, dest=destination)
        result_box.config(state=tk.NORMAL)
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, translated.text)
        result_box.config(state=tk.DISABLED)

        status_label.config(text="Translation successful!", fg="green")

    except Exception as error:
        messagebox.showerror("Translation Error", f"Oops! Something went wrong: {error}")
        status_label.config(text="Translation failed!", fg="red")

def copy_result():
    translated_output = result_box.get("1.0", tk.END).strip()
    if translated_output:
        root.clipboard_clear()
        root.clipboard_append(translated_output)
        messagebox.showinfo("Copied", "The translated text has been copied.")

def clear_all():
    input_text.delete("1.0", tk.END)
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.config(state=tk.DISABLED)
    status_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Smart Language Translator")
root.geometry("650x520")
root.resizable(False, False)

supported_languages = {
    'English': 'en',
    'Telugu': 'te',
    'Hindi': 'hi',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Chinese': 'zh-cn',
}

tk.Label(root, text="Type Text to Translate:", font=("Arial", 14)).pack(pady=10)
input_text = tk.Text(root, height=7, width=75)
input_text.pack(pady=5)

selection_frame = tk.Frame(root)
selection_frame.pack(pady=10)

tk.Label(selection_frame, text="From:").grid(row=0, column=0, padx=10)
source_language = ttk.Combobox(selection_frame, values=list(supported_languages.keys()), state='readonly')
source_language.current(0)
source_language.grid(row=0, column=1, padx=10)

tk.Label(selection_frame, text="To:").grid(row=0, column=2, padx=10)
target_language = ttk.Combobox(selection_frame, values=list(supported_languages.keys()), state='readonly')
target_language.current(1)
target_language.grid(row=0, column=3, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Translate", command=perform_translation, bg="#008080", fg="white", width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Copy Result", command=copy_result, bg="#6A5ACD", fg="white", width=15).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Clear", command=clear_all, bg="#B22222", fg="white", width=15).grid(row=0, column=2, padx=10)

tk.Label(root, text="Translated Text:", font=("Arial", 14)).pack(pady=10)
result_box = tk.Text(root, height=7, width=75, state=tk.DISABLED)
result_box.pack(pady=5)

status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=5)

root.mainloop()

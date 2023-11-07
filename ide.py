import tkinter as tk
from tkinter import ttk
from simplestplus import Lexer

def analyze_lexical():
    code = text_editor.get("1.0", "end-1c")
    lexer = Lexer(code)
    tokens, errors = lexer.tokenize()
    clear()
    for token in tokens:
        token_table.insert("", "end", values=(repr(token.val), token.type.value))
    for error in errors:
        print_to_console(error.as_string())
        print_to_console(" ")
    else:
        print_to_console("Lexical analysis completed successfully")

def analyze_syntax():
    pass

def analyze_semantic():
    pass

def clear_token_table():
    token_table.delete(*token_table.get_children())  # Clear the token table

def clear():
    clear_console()
    clear_token_table()
    pass

def run_analysis():
    clear()
    analyze_lexical()
    analyze_syntax()
    analyze_semantic()

def print_to_console(message):
    console.config(state="normal")  # Temporarily make the console editable
    console.insert("end", message + "\n")  # Insert the message at the end
    console.config(state="disabled")  # Make the console read-only again

def clear_console():
    console.config(state="normal")  # Temporarily make the console editable
    console.delete("1.0", "end")  # Delete all the text in the console
    console.config(state="disabled")  # Make the console read-only again

# Create a dark mode color scheme
dark_bg = "#1E1E1E"  # Background color
dark_fg = "#FFFFFF"  # Text color
dark_button_bg = "#1E1E1E"  # Button background color
dark_console_bg = "#1E1E1E"  # Change the background color for the error console
dark_token_table_bg = "#0000000"  # Token table background color
dark_token_table_fg = "#FFFFFF"  # Token table text color

# Create the main window
root = tk.Tk()
root.title("Simplest+ IDE")
root.configure(bg=dark_bg)  # Set the main window background color

# Create frame for buttons
button_frame = tk.Frame(root, bg=dark_bg)
button_frame.grid(row=0, column=0, columnspan=3, sticky="w")

# Buttons for analysis
lexical_button = tk.Button(button_frame, text="Lexical Analyzer", command=analyze_lexical, bg="white", fg="black", relief="raised", borderwidth=4)
lexical_button.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=5)
syntax_button = tk.Button(button_frame, text="Syntax Analyzer", command=analyze_syntax, bg="white", fg="black", relief="raised", borderwidth=4)
syntax_button.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5)
semantic_button = tk.Button(button_frame, text="Semantic Analyzer", command=analyze_semantic, bg="white", fg="black", relief="raised", borderwidth=4)
semantic_button.grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=5)

# Create a LabelFrame for the "Text Editor" heading
text_editor_frame = tk.LabelFrame(root, text="Text Editor", bg=dark_bg, fg=dark_fg, font=("Helvetica", 14), labelanchor="n", borderwidth=4)
text_editor_frame.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")

# Create text editor inside the LabelFrame
text_editor = tk.Text(text_editor_frame, wrap=tk.NONE, bg=dark_bg, fg=dark_fg)
text_editor.pack(fill="both", expand=True)

# Create a LabelFrame for the "Error" label
error_frame = tk.LabelFrame(root, text="Console", bg=dark_bg, fg=dark_fg, font=("Helvetica", 14), labelanchor="n", borderwidth=4)
error_frame.grid(row=2, column=0, padx=10, pady=(10, 0), columnspan=3, sticky="nsew")

# Create console for errors inside the LabelFrame with a different background color
console = tk.Text(error_frame, wrap=tk.WORD, height=10, bg=dark_console_bg, fg=dark_fg)
console.pack(fill="both", expand=True)
console.config(state="disabled")  # Make the console read-only

# Create a LabelFrame for the "Token Table" heading
token_table_frame = tk.LabelFrame(root, text="Token Table", bg=dark_bg, fg=dark_fg, font=("Helvetica", 14), labelanchor="n", borderwidth=4)
token_table_frame.grid(row=1, column=3, padx=10, pady=10, rowspan=2, sticky="nsew")

# Create token table inside the LabelFrame
token_table = ttk.Treeview(token_table_frame, columns=("Lexeme", "Token"), show="headings", style="Treeview")
token_table.heading("Lexeme", text="Lexeme")
token_table.heading("Token", text="Token")
token_table.pack(fill="both", expand=True)

# Create a frame for the "Clear" and "Run" buttons
button_frame2 = tk.Frame(root, bg=dark_bg)
button_frame2.grid(row=4, column=3, padx=10, pady=10)

# Add "Clear" and "Run" buttons inside the new frame with white text color
clear_button = tk.Button(button_frame2, text="Clear", command=clear, bg="white", fg="black", relief="raised", borderwidth=4)
clear_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

run_button = tk.Button(button_frame2, text="Run", command=run_analysis, bg="white", fg="black", relief="raised", borderwidth=4)
run_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=10)

# Configure row and column weights to make the text editor area larger compared to the error console
root.grid_rowconfigure(1, weight=3)  # Allocate more weight to the text editor
root.grid_rowconfigure(3, weight=3)  # Allocate the same weight to the error console
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=3)  # Allocate more weight to the token table

# Create a custom style for the token table with dark mode colors
style = ttk.Style()
style.configure("Treeview", background=dark_token_table_bg, foreground=dark_token_table_fg)

# Start the main event loop
root.mainloop()
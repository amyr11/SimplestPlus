import tkinter.font as tkfont
import customtkinter as ctk
from tkinter import ttk, filedialog, messagebox

import pysimplestplus.compiler as sp

file_is_modified = False
saved_as_file = False


def analyze_lexical():
    code = text_editor.get("1.0", "end-1c")

    global current_file_name
    tokens, errors = sp.run_lexical(current_file_name, code)
    clear()
    for token in tokens:
        token_table.insert("", "end", values=(token.lexeme_str(), token.token_type_str()))
    for error in errors:
        print_to_console(error.as_string(), message_type="error")
        print_to_console(" ")
    if len(errors) == 0:
        print_to_console("Lexical analysis completed successfully")


def analyze_syntax():
    code = text_editor.get("1.0", "end-1c")

    global current_file_name
    tokens, ast, errors = sp.run_syntax(current_file_name, code)
    clear()
    for token in tokens:
        token_table.insert(
            "", "end", values=(token.lexeme_str(), token.token_type_str())
        )
    if errors:
        for error in errors:
            print_to_console(error.as_string(), message_type="error")
            print_to_console(" ")
    elif ast:
        print_to_console("Syntax analysis completed successfully")


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
    # analyze_lexical()
    analyze_syntax()
    # analyze_semantic()


def print_to_console(message, message_type="normal"):
    console.configure(state="normal")  # Temporarily make the console editable
    if message_type == "error":
        console.tag_config("error", foreground="red")
        console.insert(
            "end", message + "\n", "error"
        )  # Insert the message at the end with 'error' tag
    else:
        console.insert("end", message + "\n")  # Insert the message at the end
    console.configure(state="disabled")  # Make the console read-only again


def clear_console():
    console.configure(state="normal")  # Temporarily make the console editable
    console.delete("1.0", "end")  # Delete all the text in the console
    console.configure(state="disabled")  # Make the console read-only again


def update_line_numbers():
    pass

current_file_name = None

def open_file_dialog():
    global file_is_modified, saved_as_file
    # add prompt to save file if it is modified
    if file_is_modified:
        choice = messagebox.askyesno(
            "Save File", "The current file is modified. Do you want to save it?"
        )
        print(choice)
        if choice:
            return save_file_dialog()

    file = filedialog.askopenfile(
        title="Open File",
        filetypes=[("SimplestPlus files", "*.simp"), ("All files", "*.*")],
    )

    # open the file and load the content to the text editor
    if not file:
        return
    
    global current_file_name
    current_file_name = file.name
    
    with open(file.name, "r") as file:
        text_editor.delete("1.0", "end")
        text_editor.insert("1.0", file.read())
        root.title(f"Simplest+ IDE | {file.name}")
    file_is_modified = False
    saved_as_file = True

    if text_editor_label.winfo_exists():
        text_editor_label.destroy()
    print(f"The selected file is {file.name}")


def save_file_dialog():
    global file_is_modified, saved_as_file

    # if file already exists, save it
    if file_is_modified and saved_as_file:
        file_path = root.title().split("|")[1].strip()[:-1]
        with open(file_path, "w") as file:
            file.write(text_editor.get("1.0", "end-1c"))
            root.title(f"Simplest+ IDE | {file_path}")
        file_is_modified = False
        return

    # if file is not saved, save it as file
    if not saved_as_file:
        file = filedialog.asksaveasfile(
            title="Save File",
            filetypes=[("SimplestPlus files", "*.simp"), ("All files", "*.*")],
            defaultextension=".simp",
        )
        if not file:
            return
        with open(file.name, "w") as file:
            file.write(text_editor.get("1.0", "end-1c"))
            root.title(f"Simplest+ IDE | {file.name}")
        file_is_modified = False
        saved_as_file = True
        return
    
    global current_file_name
    current_file_name = file.name

    print(f"The selected file is {file.name}")


def new_file_dialog():
    global file_is_modified, saved_as_file
    # add prompt to save file if it is modified
    if file_is_modified:
        choice = messagebox.askyesnocancel(
            "Save File", "The current file is modified. Do you want to save it?"
        )
        print(choice)
        if choice:
            file_is_modified = False
            return save_file_dialog()
        elif choice is None:
            return

    file_is_modified = False
    saved_as_file = False
    text_editor.delete("1.0", "end")
    clear()
    if text_editor_label.winfo_exists():
        text_editor_label.destroy()
    global current_file_name
    current_file_name = "Untitled.simp"
    root.title("Simplest+ IDE | New File")


# Create a dark mode color scheme
dark_bg = "#1E2429"  # Background color
dark_fg = "#1E2429"  # Text color
dark_button_bg = "#353D46"  # CTkButton background color
dark_button_hover_color = "#3E4752"  # CTkButton hover color
dark_console_bg = "#1E1E1E"  # Change the background color for the error console
dark_token_table_bg = "#0000000"  # Token table background color
dark_token_table_fg = "#FFFFFF"  # Token table text color

analysis_button_fg = "#2e433d"  # Analysis button text color
analysis_button_hover_color = "#295246"  # Analysis button hover color
analysis_button_text_color = "#3c874a"  # Analysis button text color

dark_button_text_color = "#6E787D"  # Button text color

# Create the main window
root = ctk.CTk(fg_color=dark_bg)
root.title("Simplest+ IDE | New File")
root.minsize(1000, 600)

root.bind("<Control-n>", lambda e: new_file_dialog())
root.bind("<Control-o>", lambda e: open_file_dialog())
root.bind("<Control-s>", lambda e: save_file_dialog())

# Create frame for buttons
button_frame = ctk.CTkFrame(root, fg_color="transparent")
button_frame.grid(row=0, column=0, columnspan=3, sticky="w")

# Buttons for analysis
lexical_button = ctk.CTkButton(
    button_frame,
    text="Lexical Analyzer",
    command=analyze_lexical,
    fg_color=analysis_button_fg,
    corner_radius=10,
    text_color=analysis_button_text_color,
    hover_color=analysis_button_hover_color,
    font=("Helvetica", 14, "bold"),
)
lexical_button.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=5)
syntax_button = ctk.CTkButton(
    button_frame,
    text="Syntax Analyzer",
    command=analyze_syntax,
    fg_color=analysis_button_fg,
    corner_radius=10,
    text_color=analysis_button_text_color,
    hover_color=analysis_button_hover_color,
    font=("Helvetica", 14, "bold"),
)
syntax_button.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5)
semantic_button = ctk.CTkButton(
    button_frame,
    text="Semantic Analyzer",
    command=analyze_semantic,
    fg_color=analysis_button_fg,
    corner_radius=10,
    text_color=analysis_button_text_color,
    hover_color=analysis_button_hover_color,
    font=("Helvetica", 14, "bold"),
)
semantic_button.grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=5)

# add frame for Open and Save buttons
file_button_frame = ctk.CTkFrame(root, fg_color="transparent")
file_button_frame.grid(row=0, column=3, sticky="e")

# Buttons for file operations
open_button = ctk.CTkButton(
    file_button_frame,
    text="Open File",
    command=open_file_dialog,
    fg_color=dark_button_bg,
    corner_radius=10,
    text_color=dark_button_text_color,
    hover_color=dark_button_hover_color,
    font=("Helvetica", 14, "bold"),
    width=0,
)
open_button.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=5)

save_button = ctk.CTkButton(
    file_button_frame,
    text="Save File",
    command=save_file_dialog,
    fg_color=dark_button_bg,
    corner_radius=10,
    text_color=dark_button_text_color,
    hover_color=dark_button_hover_color,
    font=("Helvetica", 14, "bold"),
    width=0,
)
save_button.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=5)

new_button = ctk.CTkButton(
    file_button_frame,
    text="New File",
    command=new_file_dialog,
    fg_color=dark_button_bg,
    corner_radius=10,
    text_color=dark_button_text_color,
    hover_color=dark_button_hover_color,
    font=("Helvetica", 14, "bold"),
    width=0,
)
new_button.grid(row=0, column=2, padx=10, pady=10, ipadx=0, ipady=5)

# Create text editor and maximize it to fill the entire row
text_editor = ctk.CTkTextbox(
    root,
    wrap="none",
    bg_color="#23292F",
    fg_color="transparent",
    font=("FiraCode Nerd Font", 14),
)
text_editor.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")

text_editor_label = ctk.CTkLabel(
    root,
    text="Open or create a new file to get started.",
    bg_color=dark_bg,
    fg_color=dark_fg,
    text_color=dark_button_text_color,
    font=("Helvetica", 14, "bold"),
)
text_editor_label.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")


def toggle_file_is_modified():
    global file_is_modified
    if file_is_modified:
        return
    file_is_modified = True
    root.title(root.title() + "*")


# check if the current file is modified
text_editor.bind("<Key>", lambda e: toggle_file_is_modified())


def toggle_file_is_modified():
    global file_is_modified
    if file_is_modified:
        return
    file_is_modified = True
    root.title(root.title() + "*")


# check if the current file is modified
text_editor.bind("<Key>", lambda e: toggle_file_is_modified())

# Set tab width to 4 spaces
tab_width = ctk.CTkFont().measure(
    " " * 4
)  # Measure the width of 4 spaces
text_editor.configure(tabs=(tab_width,))

# Create a LabelFrame for the "Error" label
error_frame = ctk.CTkLabel(
    root,
    text="Console",
    bg_color=dark_bg,
    fg_color=dark_fg,
    text_color=dark_button_text_color,
    font=("Helvetica", 14, "bold"),
    anchor="n",
)
error_frame.grid(row=2, column=0, padx=10, pady=(5, 0), columnspan=3, sticky="nsew")

# Create console for errors inside the LabelFrame with a different background color
console = ctk.CTkTextbox(
    master=error_frame,
    wrap="none",
    bg_color=dark_console_bg,
    fg_color="transparent",
    font=("FiraCode Nerd Font", 14),
)
console.grid(row=0, column=0, padx=0, pady=(20, 10), sticky="nsew")
console.configure(state="disabled")  # Make the console read-only

# Create a LabelFrame for the "Token Table" heading
token_table_frame = ctk.CTkLabel(
    root,
    text="Token Table",
    bg_color=dark_bg,
    fg_color=dark_fg,
    text_color=dark_button_text_color,
    font=("Helvetica", 14, "bold"),
    anchor="n",
)
token_table_frame.grid(
    row=1, column=3, padx=10, pady=(10, 70), rowspan=2, sticky="nsew"
)

# Create token table inside the LabelFrame
token_table = ttk.Treeview(
    token_table_frame,
    columns=("Lexeme", "Token"),
    show="headings",
    style="Treeview",
)
token_table.heading("Lexeme", text="Lexeme")
token_table.heading("Token", text="Token")
token_table.grid(
    row=0, column=0, padx=10, pady=(20, 0), ipadx=10, ipady=5, sticky="nsew"
)
# token_table.pack(fill="both", expand=True)

# Create a frame for the "Clear" and "Run" buttons
button_frame2 = ctk.CTkFrame(root, fg_color="transparent")
button_frame2.grid(row=2, column=3, padx=10, pady=(200, 0))

# Add "Clear" and "Run" buttons inside the new frame with white text color
clear_button = ctk.CTkButton(
    button_frame2,
    text="Clear",
    command=clear,
    fg_color=dark_button_bg,
    corner_radius=10,
    text_color=dark_button_text_color,
    hover_color=dark_button_hover_color,
    font=("Helvetica", 14, "bold"),
)
clear_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=10)

run_button = ctk.CTkButton(
    button_frame2,
    text="Run",
    command=run_analysis,
    fg_color=dark_button_bg,
    corner_radius=10,
    text_color=dark_button_text_color,
    hover_color=dark_button_hover_color,
    font=("Helvetica", 14, "bold"),
)
run_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=10)

# Configure row and column weights to make the text editor area larger compared to the error console
root.grid_rowconfigure(1, weight=1)  # Allocate more weight to the text editor
# # Allocate the same weight to the error console
root.grid_rowconfigure(3, weight=0)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=0)

# Create a custom style for the token table with dark mode colors
style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview",
    background=dark_bg,
    foreground="white",
    fieldbackground=dark_bg,
    borderwidth=0,
)
style.configure(
    "Treeview.Heading",
    background=dark_bg,
    fieldbackground=dark_bg,
    foreground=dark_button_text_color,
    font=("Helvetica", 11, "bold"),
    borderwidth=0,
)
# remove background on treeview heading on hover
style.map(
    "Treeview.Heading",
    relief=[("active", "flat")],
    background=[("active", dark_bg)],
    fieldbackground=[("active", dark_bg)],
)

# Start the main event loop
root.mainloop()

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Tk, Label, PhotoImage


def is_valid_move(board, x, y):
    """
    Check if a move is valid
    """
    if x >= 0 and x < 5 and y >= 0 and y < 5 and board[x][y] == -1:
        return True
    return False


def solve_knight_tour(board, x, y, move_count):
    """
    Solve the knight's tour problem
    """
    if move_count == 25:
        return True

    # Possible moves for the knight
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    # Try all possible moves
    for i in range(8):
        next_x = x + x_moves[i]
        next_y = y + y_moves[i]
        if is_valid_move(board, next_x, next_y):
            board[next_x][next_y] = move_count
            if solve_knight_tour(board, next_x, next_y, move_count + 1):
                return True
            # Backtrack
            board[next_x][next_y] = -1

    return False


def draw_board(canvas, board):
    """
    Draw the board with black and white alternative squares
    """
    canvas.delete("all")
    for i in range(5):
        for j in range(5):
            x1 = j * 100
            y1 = i * 100
            x2 = (j + 1) * 100
            y2 = (i + 1) * 100
            if (i + j) % 2 == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            canvas.create_text(x1 + 50, y1 + 50, text=str(board[i][j]), fill="blue", font="Arial 18")


def draw_knight(canvas, x, y):
    """
    Draw the knight
    """
    canvas.create_oval(y * 100 + 10, x * 100 + 10, y * 100 + 40, x * 100 + 40, fill="red")


# Start from a given location
def knights_tour(start_x, start_y):
    """
    Generate a knight's tour from a given location
    """
    board = [[-1 for _ in range(5)] for _ in range(5)]
    board[start_x][start_y] = 0

    # Create the window and canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()

    # Draw the initial board
    draw_board(canvas, board)
    draw_knight(canvas, start_x, start_y)

    # Solve the problem and update the canvas
    if solve_knight_tour(board, start_x, start_y, 1):
        draw_board(canvas, board)
        draw_knight(canvas, start_x, start_y)
        if board[start_x][start_y] == 24:
            root.title('Knight\'s Tour - Closed Path')
        else:
            root.title('Knight\'s Tour - Open Path')
    else:
        root.title('Knight\'s Tour - No Solution')


root = Tk()
root.attributes('-fullscreen', True)
root.title('project')

# Load the background image
img = Image.open(r"C:\Users\prasanna.k\Desktop\knight1.png")

# Resize the image to fit the screen
img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))

# Convert the image to a PhotoImage object
background_image = ImageTk.PhotoImage(img)

# Create a label with the background image
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add your other widgets to the root window here
l2 = Label(root, text='5X5 chessboard - A knight tour', relief='solid', bg="orange", font="times 50 bold").pack(pady=2,
                                                                                                                fill='x')

# mroot.geometry("1366x764")
start_image = tk.PhotoImage(file=r"C:\Users\prasanna.k\Pictures\Camera Roll\start.png")


def start_function():
    # Create the new window
    input_window = tk.Toplevel(root)
    input_window.attributes('-fullscreen', True)  # set fullscreen
    input_window.title('Enter Values')

    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\prasanna.k\Desktop\chessknight.png")

    # Create the canvas and add the background image
    canvas = tk.Canvas(input_window, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    # Create the x label and entry
    x_label = tk.Label(canvas, text="Enter x value(0 to 4) :", bg='beige', font=("Arial", 16))
    x_label.pack()
    x_entry = tk.Entry(canvas, font=("Arial", 16))
    x_entry.pack()

    # Create the y label and entry
    y_label = tk.Label(canvas, text="Enter y value(0 to 4) :", bg='beige', font=("Arial", 16))
    y_label.pack()
    y_entry = tk.Entry(canvas, font=("Arial", 16))
    y_entry.pack()

    # Create the submit button
    def submit():
        x = int(x_entry.get())
        y = int(y_entry.get())
        input_window.destroy()
        knights_tour(x, y)

    submit_button = tk.Button(canvas, text="Submit", command=submit, bg='beige', font=("Arial", 16))
    submit_button.pack()

    input_window.mainloop()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to place the button in the middle of the screen
button_width = 200
button_height = 50

x = (screen_width - button_width) // 2
y = (screen_height - button_height) // 2

# Create the start button and place it in the middle of the screen
start_button = tk.Button(root, image=start_image, command=start_function)
start_button.place(x=x, y=y)
# Start the GUI event loop
root.mainloop()
knights_tour(x, y)
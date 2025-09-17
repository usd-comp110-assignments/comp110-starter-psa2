"""
COMP 110, PSA 2 (Sampler Quilt)

This module contains functions to draw a sampler quilt using tkinter.

Author: INSERT YOUR NAME AND EMAIL HERE
"""
import tkinter as tk

# Global constants. Do not modify these or add new constants.
NUM_ROWS = 5
NUM_COLUMNS = 7
NUM_LOG_CABIN_FRAMES = 4

def draw_log_cabin(canvas):
    pass


def draw_flower_petals(canvas):
    pass


def draw_celtic_cross(canvas):
    pass


def draw_hybrid(canvas):
    pass


def draw_custom(canvas):
    pass


def draw_quilt(canvas, block_size):
    """
    Draw the entire quilt by iterating through a pattern and drawing each block.

    Parameters:
        canvas (tkinter.Canvas): The tkinter Canvas to draw on.
        block_size (int): The width and height of each block in pixels.
    """
    for current_row in range(NUM_ROWS):
        for current_col in range(NUM_COLUMNS):
            # To Do: complete this function
            pass





# DO NOT MODIFY ANY CODE BELOW THIS LINE!!!!

def get_block_size():
    """
    Prompt the user for a positive integer block size.

    Returns:
        int: The block size entered by the user.
    """
    while True:
        try:
            block_size = int(input("Enter block size (positive integer): "))
            if block_size > 0:
                return block_size
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def test_draw_quilt():
    """
    Test function to draw a quilt with a user-defined block size for verification.
    """
    block_size = get_block_size()

    root = tk.Tk()
    root.title("USD COMP110 Sampler Quilt (PSA2)")

    canvas_width = NUM_COLUMNS * block_size
    canvas_height = NUM_ROWS * block_size

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    draw_quilt(canvas, block_size)

    root.mainloop()

def test_draw_quilt_block():
    """
    Test function to draw each type of quilt block individually for verification.
    """
    print("Note: Canvas size will be 300 by 300 pixels.")
    canvas_width = 300
    canvas_height = 300

    print("Note: The canvas object is named test_canvas.")

    # ask user to enter the code to call the individual block function
    user_code = input("Enter the code to call the individual quilt block function: ")

    root = tk.Tk()
    root.title("USD COMP110 Sampler Quilt Block Test (PSA2)")
    test_canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    test_canvas.pack()

    # run the code that the user entered
    eval(user_code)

    root.mainloop()

def main():
    """
    Main function to prompt user for testing options.
    """

    print("Welcome to the USD COMP110 Sampler Quilt (PSA2) Tester Program!")

    # prompt the user to enter 1 to test individual blocks, or 2 to test the full quilt
    while True:
        choice = input("Enter 1 to test individual blocks, or 2 to test the full quilt: ")
        if choice.strip() == '1':
            test_draw_quilt_block()
            return
        elif choice.strip() == '2':
            test_draw_quilt()
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
import streamlit as st
import os
import subprocess

def main():
    st.title("Interactive Games Hub 🎮")
    st.subheader("Choose a game to play!")

    game = st.selectbox(
        "Select a game:",
        ["Chess" , "Wordle" , "Tic Tac Toe", "Tetris"]
    )

    st.write("---")  
    ttt_path = r"C:\Users\ADMIN\OneDrive\Documents\GAMES\TICTACTOE\ttt.py"
    wordle_path = r"C:\Users\ADMIN\OneDrive\Documents\GAMES\WORDLE\main.py"
    tetris_path = r"C:\Users\ADMIN\OneDrive\Documents\GAMES\TETRIS\main.py"
    chess_path = r"C:\Users\ADMIN\OneDrive\Documents\GAMES\CHESS\src\main.py"
    
    if st.button("Play Game"):
        if game == "Tic Tac Toe":
            launch_game(ttt_path)
        elif game == "Chess":
             launch_game(chess_path)
        elif game == "Wordle":
             launch_game(wordle_path)
        elif game == "Tetris":
             launch_game(tetris_path)
        # elif game == "Number Guessing":
        #     launch_game("games/number_guessing/game.py")

def launch_game(game_script_path):
    try:
        subprocess.run(["python", game_script_path])
    except Exception as e:
        st.error(f"Failed to launch the game: {e}")

if __name__ == "__main__":
    main()

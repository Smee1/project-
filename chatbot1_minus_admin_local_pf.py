# Here is the python code for an example of chatbot creation. This code is for a chatbot with a local profanity filter.
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext


def profanity_filter(message):
    profane_words = ["wordone", "wordtwo", "wordthree"]  # Add the words you want to filter
    flagged = False
    clean_message = message
    for word in profane_words:
        if word in message:
            flagged = True
            clean_message = clean_message.replace(word, '*' * len(word))
    return clean_message, flagged


def handle_client(client_socket, addr, other_client_socket, admin_window):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{addr}] {message}")
                filtered_message, flagged = profanity_filter(message)
                if flagged:
                    admin_window.log_profanity(addr, message)
                other_client_socket.sendall(filtered_message.encode('utf-8'))
            else:
                break
        except:
            break
    print(f"[DISCONNECT] {addr} disconnected.")
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 12345))
    server.listen(2)
    print("[SERVER STARTED] Waiting for connections...")


if __name__ == "__main__":
    main()

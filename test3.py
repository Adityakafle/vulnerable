# vulnerable.py
import os
import pickle

def load_data(filename):
    # Unsafe: directly loading a pickle file from user input
    with open(filename, "rb") as f:
        data = pickle.load(f)
    return data

def delete_file(filename):
    # Unsafe: directly using user input in os.system
    os.system(f"rm {filename}")

if __name__ == "__main__":
    file_to_load = input("Enter filename to load: ")
    data = load_data(file_to_load)
    print("Data loaded:", data)

    file_to_delete = input("Enter filename to delete: ")
    delete_file(file_to_delete)

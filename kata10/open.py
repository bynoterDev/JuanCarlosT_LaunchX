""" 
try:
    open('config.py')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")
 """
def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")

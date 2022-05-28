# If location of this file is not /home/booruledie/Programming/python/score2rgb.py, please adjust score2rgb alias in .bashrc file

import argparse
import webbrowser

parser = argparse.ArgumentParser("python3 score2rgb")
parser.add_argument("score", help="Score of severity of vulnerability that is a float number between 0 and 10.", type=float)
args = parser.parse_args()

score = args.score

r = int(score * 255 / 10)
g = 255 - r
b = 0

url = f"https://www.google.com/search?q=rgb({r},{g},{b})"
#print(f"r: {r}, g:{g}, b:{b}")

webbrowser.open(url)


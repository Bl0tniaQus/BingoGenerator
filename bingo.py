from flask import Flask,render_template
from random import shuffle
def find_square(x):
	for i in range(x):
		if i*i >= x:
			return i
app = Flask(__name__)


@app.route("/")
def index():
	phrases_file = open("phrases.txt", "r")
	phrases = [x.rstrip()for x in phrases_file.readlines()]
	phrases_file.close()
	shuffle(phrases)
	lines = len(phrases)
	table = "<table>"
	dimension = find_square(lines)
	counter = 0
	for x in range(dimension):
		table = table + "<tr>"
		for y in range(dimension):
			if counter<lines:
				table = table + f"<td>{phrases[counter]}</td>"
				counter=counter+1
			else:
				table = table + "<td></td>"
		table = table + "</tr>"
	table = table + "</table>"
	return render_template("bingo.html",table=table)
	
	
if __name__ =="__main__":
	app.run(debug=True)
	
	

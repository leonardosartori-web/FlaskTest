from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
	connection = sqlite3.connect('database.db')
	connection.row_factory = sqlite3.Row
	posts = connection.execute('SELECT * FROM posts').fetchall()
	connection.close()
	return render_template('index.html', posts=posts)

@app.route('/<int:idx>/delete', method=('POST',))
def delete(idx):
	connection = sqlite3.connect('database.db')
	connection.row_factory = sqlite3.Row
	posts = connection.execute('DELETE FROM posts WHERE id=?', (idx,))
	connection.commit()
	connection.close()
	return redirect('/')

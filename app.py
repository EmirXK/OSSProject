from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        tasks.append({"title": title})
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:task_index>', methods=['GET', 'POST'])
def update(task_index):
    if request.method == 'POST':
        title = request.form['title']
        tasks[task_index]["title"] = title
        return redirect(url_for('index'))
    return render_template('update.html', task_index=task_index, task=tasks[task_index])

@app.route('/delete/<int:task_index>')
def delete(task_index):
    del tasks[task_index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


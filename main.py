from flask import Flask, render_template, redirect
from flask import send_file


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/link2yDisk')
def returnLink():
    return send_file('static/downloadebles /filesProjectFomin.zip', as_attachment=True)

@app.route('/link2github')
def returnLink2():
    return redirect("https://github.com/GennaFomin/MyProgrammingProject", 301)


@app.route('/datasetredir')
def redirDataset():
    return redirect('https://www.kaggle.com/tmdb/tmdb-movie-metadata', 301)


@app.route('/plot1')
def returnPlot1():
    return render_template('plt1.html')


@app.route('/plot2')
def returnPlot2():
    return render_template('plt2.html')


@app.route('/plot3')
def returnPlot3():
    return render_template('plt3.html')


@app.route('/plot4')
def returnPlot4():
    return render_template('plt4.html')


@app.route('/plot5')
def returnPlot5():
    return render_template('plt5.html')


@app.route('/plot6')
def returnPlot6():
    return render_template('plt6.html')


@app.route('/plot7')
def returnPlot7():
    return render_template('pltBud.html')


@app.route('/plot8')
def returnPlot8():
    return render_template('pltScr.html')


@app.route('/plot9')
def returnPlot9():
    return render_template('pltRev.html')


@app.route('/pipeline')
def returnIndex2():
    return render_template('main.html')


app.run(debug=True, host='0.0.0.0')

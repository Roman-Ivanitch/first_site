from flask import * 
# Flask, render_template, url_for, send_file

app = Flask(__name__)
 
@app.route('/')
def index():
    print( url_for('index') )
    return render_template('index.html')


@app.route('/abram')
def abran():
    return render_template('abram.html')   
 

@app.route('/ivanitch')
def ivan():
    return render_template('ivanitch.html')  


@app.route('/alekseevsk')
def alek():
    return render_template('alekseevsk.html') 


if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0',debug = True)

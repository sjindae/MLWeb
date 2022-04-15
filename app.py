from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mnist',methods=['GET', 'POST'])
def mnist():
    if request.method == 'GET':
        return render_template('mnistform.html')
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
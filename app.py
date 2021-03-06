from flask import Flask,render_template,request
import os,pickle
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mnist',methods=['GET', 'POST'])
def mnist():
    if request.method == 'GET':
        return render_template('mnistform.html')
    else:    # upload 폴더에 파일 가져옴
        f = request.files['mnistfile']
        path = os.path.dirname(__file__)+'/upload/'+f.filename    # os.path에서 path는 어디서 온걸까..
        f.save(path)
        img = Image.open(path).convert("L")    # 그레이스케일로 바뀐다는디? 그게 모야>? 수업보셈
        img = np.resize(img,(1,784))
        # img = 255 - (img)
        mpath = os.path.dirname(__file__)+'/model1.pickle'
        with open(mpath,'rb') as f:
            model = pickle.load(f)
        pred = model.predict(img)    # 여기서 predict가 어떻게 되는 걸까
        return render_template('mnistresult.html',data=pred) # "성공!!"+str(pred)


if __name__ == '__main__':
    app.run(debug=True)
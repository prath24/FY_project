from flask import Flask,request,jsonify
import pickle

model = pickle.load(open('model.pkl','rb'))



app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/predict', methods = ['POST'])
def predict():
    review = request.form.get('review')

    result = model.predict([review])
    if result == 'neg':
        ret = 1
    else:
        ret = 0    

    return jsonify({'result':str(ret)})


if __name__ == "__main__":
    app.run()    
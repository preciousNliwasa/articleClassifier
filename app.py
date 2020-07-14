from flask import Flask,request,render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict",methods = ['GET','POST'])
def predict_spam():
    
    mm = pickle.load(open('textm3.pkl','rb'))
    message = request.form['message']
    
    message = [message]
    
    prediction = mm.predict(message)
    
    return render_template('index.html',prediction = 'The article belongs to {}'.format(prediction))


if __name__ == '__main__':
    app.run(debug=True)
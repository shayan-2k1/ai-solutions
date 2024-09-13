from flask import Flask,render_template, request
import pickle

app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def linear_model():
    global m,b
    if request.method == 'POST':
        plot_size = float(request.form['plot_size'])
        prediction = b+plot_size*m
        return render_template('prediction.html', prediction=prediction)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    m=0
    b=0
    with open('path of model.pkl file', 'rb') as f:
        m, b = pickle.load(f)
    
    app.run(debug=True)
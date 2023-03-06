from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
#from imblearn.ensemble import BalancedBaggingClassifier

modeloIA=pickle.load(open("ModeloRLSS10000.pkl","rb"))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Eliminar estos campos que en el analisis resultaron con una menor correlación al error ingresao 
    # ['dimensión fractal MD':9, 'texturaSE':11, 'simetríaSE':18]
    xTestNames="radioMD,texturaMD,perímetroMD,áreaMD,suavidadMD,compacidadMD,concavidadMD,puntos cóncavosMD,simetríaMD,radioSE,perímetroSE,áreaSE,suavidadSE,compacidadSE,concavidadSE,puntos cóncavosSE,dimensión fractal SE,radioPeor,texturaPeor,perímetroPeor,áreaPeor,suavidadPeor,compacidadPeor,concavidadPeor,puntos cóncavosPeor,simetríaPeor,dimensión fractal Peor".split(',')
    xTestA=request.form['cancermama'].split(',')
    del xTestA[18]
    del xTestA[11]
    del xTestA[9]
    xTest=pd.DataFrame(xTestA).transpose()
    xTest.columns = xTestNames
    res=modeloIA.predict(xTest)
    if res==0:
        resultado="Benigno"
    else:
        resultado="Maligno"
    return render_template('submit.html', resIA=resultado, valTest=xTestA)

if __name__ == '__main__':
    app.run(debug=True)
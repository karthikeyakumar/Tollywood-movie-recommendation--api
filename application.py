from flask import Flask, render_template, request
import requests
import json

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def search():
    global search_query
    global result
    search_query=request.form['query']
   
    try:
        response = requests.get('https://movierecommender-telugu.herokuapp.com/recommend?movie='+search_query)
        result = json.loads(response.content)
        return render_template('catalog1.html', result = result, results_len = len(result))
    
    except:
        return render_template('404.html') 
                          
if __name__=="__main__":
    app.run(debug=True)

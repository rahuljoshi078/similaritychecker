from flask import Flask, request, jsonify, render_template
import spacy

app = Flask(__name__)


nlp = spacy.load('en_core_web_sm')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/similarityscore_api', methods = ['POST'])
def similarityscore_api():
    posted_data = request.json['data']
    
    text1 = posted_data['text1']
    text2 = posted_data['text2']

    # 
    text1_nlp = nlp(text1)
    text2_nlp = nlp(text2)


    ratio = text1_nlp.similarity(text2_nlp)
    
    return jsonify(ratio)



if __name__ == '__main__':
    app.run(debug=True)
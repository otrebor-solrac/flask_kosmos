# import the Flask library
from flask import Flask, render_template, request
import spacy

import pudb
 
 
# Create the Flask instance
app = Flask(__name__)
  

@app.route('/', methods=['POST'])
def get_entities():
    if request.method == 'POST':
        # get json
        values = request.json

        sentences =  values["oraciones"]
        nlp = spacy.load("es_core_news_sm")
        results={"resultado":[]}

        for s in sentences:  
            doc = nlp(s)
            entities={}
            for token in doc:
                entities[token.text] = token.pos_
            
            results["resultado"].append({"oracion":s,
                                  "entidades":entities})

        return results
 
# Start with flask web app with debug as
if(__name__ == "__main__"):
    app.run(debug=True)
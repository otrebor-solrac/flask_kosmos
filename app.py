# import the Flask library
from flask import Flask, render_template, request
import spacy

#To debug code
import pudb
 
 
# Create the Flask instance
app = Flask(__name__)
  

@app.route('/', methods=['POST'])
def get_entities():
    if request.method == 'POST':
        # get json
        values = request.json

        # Parse sentences and initialization
        sentences =  values["oraciones"]
        results={"resultado":[]}

        # Create model
        nlp = spacy.load("es_core_news_sm")
        
        # Uncomment to debug
        # pu.db
        for s in sentences:  
            doc = nlp(s)
            entities={}

            for token in doc:
                if token.ent_type_!= "":
                    entities[token.text] = token.ent_type_
                    # entities[token.text] = token.pos_
            
            # Save results
            results["resultado"].append({"oracion":s,
                                  "entidades":entities})

        return results
 
# Start with flask web app with debug
if(__name__ == "__main__"):
    app.run(debug=True)
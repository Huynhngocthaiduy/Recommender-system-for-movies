from flask import Flask, request, jsonify
from annoy import AnnoyIndex

app = Flask(__name__)

# Load the Annoy database
annoy_db = AnnoyIndex(960, metric='angular')
annoy_db.load('rec_imdb_960_full.ann')

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/reco', methods=['POST'])
def reco():    
    vector = request.json['vector']
    #print("Feature vector received from Gradio interface:", vector[:20])
    
    closest_indices = annoy_db.get_nns_by_vector(vector, 5)
    reco = closest_indices
    #print(reco)
    return jsonify(reco)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

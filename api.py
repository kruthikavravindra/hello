import flask
from flask import request, jsonify
import face_recognition
import numpy as np
import glob
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/faces/all', methods=['GET'])
def test_images():
    
    image_rgb = face_recognition.load_image_file("C:/Users/kruthikar/Desktop/test/sharukhspecs.jfif")
    return 'ok'
    locations, encodings = get_face_embeddings_from_image(image_rgb)
    return 'okk'
    # distances = face_recognition.face_distance(all_face_encodings, encodings[0])
    
    # print(distances)
    
    # # use the name in the filename as the identity key
    # identity = os.path.splitext(os.path.basename(image_location))[0]
        
    # if np.any(distances <= MAX_DISTANCE):
            # best_match_idx = np.argmin(distances)
            # print("Face of ", identity, " is matching with ", all_names[best_match_idx])
            

app.run()
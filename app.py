from flask import Flask, request
app = Flask(__name__)

from detector.mutant_detector import is_mutant

@app.route('/')
def welcome():
    return 'Welcome mutants of the world'

@app.route('/mutant/', methods = ['POST'])
def detect_dna():
    data = request.get_json()
    print(data['dna'])
    if is_mutant(data['dna']):
        return dict(
            statusCode = 200,
            body = "Ok"
        )
    else:   
        return dict(
            statusCode = 403,
            body = "Foribiden"
        )
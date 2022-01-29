from flask import Flask, render_template, request, jsonify, make_response, url_for, redirect
from flask_cors import CORS
import requests
import json
from nlp.utils import get_named_entities, tokenize_with_pos

app = Flask(__name__)


CORS(app, resources={r'/*': {'origins': '*'}})

OUTPUT = {}

@app.route('/about', methods=['GET', 'POST'])
def about(post=None):

    """This function should serve the about.html file on POST and GET requests
    Fill out the route decorator and function body
    """

    return render_template('about.html', content=post)



# @app.route('/manual_json_pos', methods=['POST'])
# def manual_json_pos():
#     content_type = request.headers.get('Content-Type')
#     if (content_type == 'application/json'):
#         tokens_output = request.json
#         return render_template('about.html', content=tokens_output)

@app.route('/pos', methods=['GET', 'POST'])
def pos():
    global OUTPUT
    response_object = {}

    if request.method == 'POST':

        tokens_output = request.json['input']
        print('DATA ' + str(tokens_output))

        if tokens_output and (tokens_output != "") and (tokens_output != " "):
            tokens_output = tokenize_with_pos(tokens_output)
            print(tokens_output)
            #Using json.dumps instead of jsonify as is easier with list
            OUTPUT=json.dumps(tokens_output)
        else:
            return render_template('illegal.html', error='Status code 451 - Empty/invalid text')
    else:
        response_object = OUTPUT
    return json.dumps(response_object)



    """This function should accept only POST requests
    If the request body contains a "text" key it should process the associated value using
    your tokenize_with_pos() function and return the output in json format
    (Use request.form to get the POST requests body, you can use Flask's jsonify() function to return json)
    Since it makes no sense to tokenize empty text, also add a custom response with status code 451
    if the "text" value is a blank or empty string and serve the illegal.html file
    Fill out the route decorator and function body
    """
    pass


@app.route('/ner', methods=['GET', 'POST'])
def ner():
        # testOutput = get_named_entities(input)
        # if testOutput == []:
        #     tokens_output = requests.get('http://localhost:5000/sampling').text
        # else:
        #     tokens_output = input
    global OUTPUT
    response_object = {}

    if request.method == 'POST':

        tokens_output = request.json['input']
        print('DATA ' + str(tokens_output))

        if tokens_output and (tokens_output != "") and (tokens_output != " "):
            tokens_output = get_named_entities(tokens_output)
            print(tokens_output)
            #Using json.dumps instead of jsonify as is easier with list
            OUTPUT=json.dumps(tokens_output)
        else:
            return render_template('illegal.html', error='Status code 451 - Empty/invalid text')
    else:
        response_object = OUTPUT
    return json.dumps(response_object)
    """This function should accept POST and GET requests
    It should work like the pos() function but use your get_named_entities() function
    to process text instead (Use request.method to handle POST vs GET requests)
    Fill out the route decorator and function body
    """
    pass

@app.route('/sampling', methods=['GET'])
def sampling():
    # Sample text used for get requests
    # return '<html><head>custom head stuff here</head><body><h1>Test</h1></body></html>'
    return 'There is nothing more exciting in life than a get request, Tom discoered this fact when he visited London, he asked where he could get a good time, someone said to go to Soho, which he did; he met a new friend there named Angel, what followed was a rash and some awkward telephone calls on his Nokia'


if __name__ == '__main__':
    app.run(use_reloader=True)
    payload = 'This is a test'
    requests.post("http://localhost:5000/pos", data=payload)
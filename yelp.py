from flask import Flask
from flask_cors import CORS
from flask import request

import requests

app = Flask(__name__)
CORS(app)

@app.route('/getyelp', methods=['POST'])
def fetchFromYelp():
    req=request.get_json()
    print ('request:', req)
    
    url = 'https://api.yelp.com/v3/businesses/search?location=' + req['zip'] + '&categories=restaurants&sort_by=best_match&limit=20'

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer TVioWvYyqlIMLJ6QnNNXDMQBM3A_0Ka1ZuM3NUrT8R9CMs2y8yogw8lGUh7gGGPmpgeH4MQbYEeWHuA9dJRDDEJEoJlS-ycSD7uuLTpiIU6bF-8fJZYD7SMBEt7LZXYx"
    }

    response = requests.get(url, headers=headers)

    # print (type(response.json()))
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
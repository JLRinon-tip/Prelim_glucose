from flask import Flask, jsonify, request
app = Flask(__name__)

getglucose=[
    {
        "glucose_id":"01",
        "date":"October 01, 2022",
        "glucose":"10"
    },
    {
        "glucose_id":"02",
        "date":"October 02, 2022",
        "glucose":"20"
    },
    {
        "glucose_id":"03",
        "date":"October 03, 2022",
        "glucose":"30"
    }
]
postglucose=[
        {
        "glucose_id":"01",
        "date":"October 30, 2021",
        "glucose":"50"
    },
    {
        "glucose_id":"02",
        "date":"October 02, 2022",
        "glucose":"20"
    }
]
putglucose=[
        {
        "glucose_id":"01",
        "date":"October 01, 2022",
        "glucose":"10"
    }
]
deleteglucose=[
        {
        "glucose_id":"01",
        "date":"October 01, 2022",
        "glucose":"10"
    },
        {
        "glucose_id":"02",
        "date":"October 02, 2022",
        "glucose":"20"
    }  
]

@app.route('/getglucose', methods= ['GET'])
def getGlucose():

    return jsonify(getglucose)

@app.route('/postglucose', methods= ['POST'])
def postGlucose():

    return jsonify(postglucose)

@app.route('/putglucose', methods= ['PUT'])
def putGlucose():

    return jsonify(putglucose)

@app.route('/deleteglucose', methods= ['DELETE'])
def deleteGlucose():

    return jsonify(deleteglucose)
if __name__=='__main__':
    app.run()
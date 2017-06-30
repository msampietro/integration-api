from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/newClient", methods=['POST'])    #For POST method add - methods=['POST'] -
def hello():
    req = request.get_json()
    print(req['name'])
    return '.'.join(req['cars'])

@app.route("/postForm", methods=['POST'])    #For POST method add - methods=['POST'] -
def instapageForm():
    json = request.get_json()
    print("***** JSON FROM POST ******")
    print(json)
    odooJson = getFormKeys(json)
    print("***** JSON FOR ODOO *****")
    print(odooJson)
    return "Inserted to Odoo"


def getFormKeys(json):
    formKeys = []
    for key, values in json.copy().items():
        k = getOdooKey(key)
        if k != None:
            if k == key:
                json[k] = json[key]
                formKeys.append(k)
            else:
                json[k] = json[key]
                del json[key]
        else:
            del json[key]
    return json

def getOdooKey(formKey):
    with open('./integration-api/odoo_mappings.json') as json_data:
        odooMapping = json.load(json_data)

    for key, values in odooMapping.items():
        if formKey == key:
            return values

if __name__ == "__main__":
    app.run()
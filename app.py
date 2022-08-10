from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gfg():
    if request.method == "POST": 

        textBox = request.form['food']
        print(textBox)

        url = f'https://api.edamam.com/search?q={textBox}&app_id=58a5fc66&app_key=94edcba2f758d8d2a5921ec7db528382'
        response = requests.get(url)
        hits = response.json()['hits']
        more = response.json()['more']
        print(more)
        count = len(hits)


        return render_template('index.html', test=hits, valid=textBox, counter=count, exist=more, result=textBox)
    elif request.method == 'GET': 
        return render_template('index.html')

@app.route('/ingredients/', methods=['GET'])
def api_fetch_ingredients():
    name = request.args.get("query", None)
    print(f"got query {name}")

    response = {}

    if not name:
        response["ERROR"] = "ingredients not found, please try searching for ingredients"
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "Numbers are not allowed in this request."
    # Now the user entered a valid name
    else:
        url = f'https://api.edamam.com/search?q={name}&app_id=58a5fc66&app_key=94edcba2f758d8d2a5921ec7db528382'
        response2 = requests.get(url)
        hits = response2.json()['hits']
        for recipe in hits: 
                title = recipe['recipe']['label']
                source = recipe['recipe']['source']
                ingredients = recipe['recipe']['ingredientLines']
                website = recipe['recipe']['url']
                food = list(ingredients)
                response["Ingredients"] = f"Successfully Fetched: \n {food}"

    # Return the response in json format
    return jsonify(response)


if __name__ == '__main__': 
    app.run()
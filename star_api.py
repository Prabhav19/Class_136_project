from flask import Flask, jsonify, request
from star_gravity import star_gravity
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        star_gravity:'star_gravity',
        'messege':'success'


    })

@app.route('/star')
def star():
    name = request.args.get('name')
    star_data = next(item for item in star_gravity if item['name'] == name)
    return jsonify({
        'data': star_data,
        'messege':'success'
    })
if __name__ == '__main__':
    app.run(debug = True)
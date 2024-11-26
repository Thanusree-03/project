from flask import Flask, request, jsonify, redirect
import shortuuid

app = Flask(__name__)

# Store URLs (in-memory database)
urls = {}

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    url = data.get('url')
    short_id = shortuuid.uuid()
    urls[short_id] = url
    short_url = f'http://localhost:5000/api/{short_id}'
    return jsonify({'shortUrl': short_url})

@app.route('/api/<short_id>', methods=['GET'])
def redirect_url(short_id):
    original_url = urls.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)

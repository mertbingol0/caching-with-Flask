from flask import Flask, request
from werkzeug.contrib.cache import SimpleCache

# Initialize a Flask application
app = Flask(__name__)

# Create a cache object
cache = SimpleCache()

# Define a route for the endpoint that we want to cache
@app.route('/cached-endpoint')
def cached_endpoint():
    # Check if the response is already in the cache
    response = cache.get(request.path)
    if response is not None:
        # If the response is in the cache, return it directly
        return response
    else:
        # If the response is not in the cache, generate it and store it in the cache
        response = generate_response()
        cache.set(request.path, response, timeout=60)
        return response

def generate_response():
    # This function generates the response that we want to cache
    # For simplicity, we just return a string here
    return "This is a cached response!"

if __name__ == '__main__':
    app.run(debug=True)

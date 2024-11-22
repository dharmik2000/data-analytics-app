from flask import Flask, jsonify
import analysis

app = Flask(__name__)

@app.route('/')
def index():
    # Run the analysis function and get results
    results = analysis.run_analysis()
    return jsonify(results)  # Return the results as JSON

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

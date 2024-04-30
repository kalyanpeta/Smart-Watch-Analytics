from flask import request, jsonify, render_template
from app import app
from app.utils import load_model
from app.recommendations import *


# Load models on start
sleep_model = load_model('models/random_forest_sleep_model.joblib')
stress_model = load_model('models/random_forest_stress_model.joblib')

stress_level_labels = {
    0: "Low/Normal",
    1: "Medium",
    2: "High",
}

def categorize_sleep(score):
    """Categorize sleep quality based on the score."""
    if score > 85:
        return "The Dream Catcher"
    elif score > 70:
        return "The Napper"
    elif score > 55:
        return "The Toss-and-Turner"
    else:
        return "The All-Nighter"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index1.html')
def index1():
    return render_template('index1.html')

@app.route('/index2.html')
def index2():
    return render_template('index2.html')

@app.route('/predict/sleep_quality', methods=['POST'])
def predict_sleep_quality():
    data = request.get_json()
    expected_features = ['Total Minutes Asleep', 'Total Time in Bed', 'Minutes REM Sleep', 'Minutes Light Sleep']
    
    try:
        if not all(feature in data for feature in expected_features):
            return jsonify({'error': 'Missing or extra features provided.'}), 400

        features = [data[feature] for feature in expected_features]
        prediction = sleep_model.predict([features])[0]
        
        # Generate the sleep category
        category = categorize_sleep(prediction)

        return jsonify({
            'sleep_quality_score': prediction,
            'sleep_category': category
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict/stress_level', methods=['POST'])
def predict_stress_level():
    data = request.get_json()
    try:
        features = [data.get(feature) for feature in ['Recovery Score', 'Heart Rate Variability', 'Resting Heart Rate', 'Blood Oxygen', 'REM Duration']]
        prediction = stress_model.predict([features])[0]
        stress_label = stress_level_labels[prediction]
        return jsonify({'stress_level': str(prediction), 'stress_label': str(stress_label)}),200
    except KeyError as e:
        return jsonify({'error': f'Missing data: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_questions/<category>', methods=['GET'])
def fetch_questions(category):
    # Implementation depends on your existing function
    questions = get_questions(category)
    return jsonify({'questions': questions}), 200



@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    data = request.get_json()
    try:
        category = data['category']
        answers = data['answers']
        if len(answers) != 5:
            return jsonify({'error': 'Exactly 5 answers are required.'}), 400
        recommendation = get_recommendations(category, answers)
        return jsonify({'recommendation': recommendation}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing data: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/get_stress_questions/<category>', methods=['GET'])
def fetch_stress_questions(category):
    # Implementation depends on your existing function
    questions = get_stress_questions(category)
    return jsonify({'questions': questions}), 200

@app.route('/submit_stress_answers', methods=['POST'])
def submit_stress_answers():
    data = request.get_json()
    try:
        category = data['stressLevel']
        answers = data['answers']
        if len(answers) != 5:
            return jsonify({'error': 'Exactly 5 answers are required.'}), 400
        recommendation = get_stress_recommendations(category, answers)
        return jsonify({'recommendation': recommendation}), 200
    except KeyError as e:
        return jsonify({'error': f'Missing data: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
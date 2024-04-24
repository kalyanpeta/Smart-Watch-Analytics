from flask import request, jsonify
from app import app
from app.utils import load_model
from app.recommendations import get_questions, get_recommendations

# Load models on start
sleep_model = load_model('models/random_forest_sleep_model.joblib')

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

@app.route('/get_questions/<category>', methods=['GET'])
def fetch_questions(category):
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

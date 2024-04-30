document.addEventListener('DOMContentLoaded', function() {
    // Handle stress level form submission
    const stressLevelForm = document.getElementById('stressLevelForm');
    const stressResultsDiv = document.getElementById('stressResults');
    const takeStressQuizButton = document.getElementById('takeStressQuizButton');
    const stressQuestionnaireSection = document.getElementById('stressQuestionnaireSection');
    const stressQuestionnaireForm = document.getElementById('stressQuestionnaireForm');
    const stressRecommendationDiv = document.getElementById('stressRecommendation');
    const stressDataSection = document.getElementById('stressDataSection');

    stressLevelForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const recoveryScore = document.getElementById('recoveryScore').value;
        const heartRateVariability = document.getElementById('heartRateVariability').value;
        const restingHeartRate = document.getElementById('restingHeartRate').value;
        const bloodOxygen = document.getElementById('bloodOxygen').value;
        const remDuration = document.getElementById('remDuration').value;

        
        fetch('http://127.0.0.1:5000/predict/stress_level', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                "Recovery Score": recoveryScore,
                "Heart Rate Variability": heartRateVariability,
                "Resting Heart Rate": restingHeartRate,
                "Blood Oxygen": bloodOxygen,
                "REM Duration": remDuration
            })
        })
        .then(response => response.json())
        .then(data => {
            stressResultsDiv.innerHTML = `Stress Level Prediction: ${data.stress_label}`;
            takeStressQuizButton.style.display = 'block';
            sessionStorage.setItem('stressLevel', data.stress_label);
        })
        .catch(error => console.error('Error:', error));
    });

    takeStressQuizButton.addEventListener('click', function() {
        stressDataSection.style.display = 'none';
        stressQuestionnaireSection.style.display = 'block';
        loadStressQuestions();
    });

    stressQuestionnaireForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // const answers = Array.from(stressQuestionnaireForm.querySelectorAll('select')).map(select => select.value);
        const answers = Array.from(document.querySelectorAll('#stressQuestionnaireForm select')).map(select => select.value);
        const stressLevel = sessionStorage.getItem('stressLevel');
        
        fetch('/submit_stress_answers', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ stressLevel, answers })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            stressRecommendationDiv.innerHTML = data.recommendation;
        })
        .catch(error => console.error('Error:', error));
    });

    function loadStressQuestions() {
        // Add the API endpoint to get stress-related questions
        const stressLevel = sessionStorage.getItem('stressLevel');
        fetch(`/get_stress_questions/${stressLevel}`)
        .then(response => response.json())
        .then(data => {
            // const form = document.getElementById('stressQuestionnaireForm');
            const form = stressQuestionnaireForm;
            form.innerHTML = ''; // Clear existing content
            data.questions.forEach((question, index) => {
                console.log('question:',question," index:",index);
                const formGroup = document.createElement('div');
                formGroup.className = 'form-group';
                
                const label = document.createElement('label');
                label.textContent = question; // Assuming the question text is in a property named 'text'
                label.htmlFor = 'stress-question-' + index;
                formGroup.appendChild(label);
    
                const select = document.createElement('select');
                select.id = 'stress-question-' + index;
                select.className = 'form-control';
                // question.options.forEach(option => {
                //     const optionElement = document.createElement('option');
                //     optionElement.value = option.value;
                //     optionElement.textContent = option.text;
                //     select.appendChild(optionElement);
                // });
                select.innerHTML = `<option value="">Select an answer</option><option value="yes">Yes</option><option value="no">No</option>`;
                formGroup.appendChild(select);
    
                form.appendChild(formGroup);
            });
    
            const submitButton = document.createElement('button');
            submitButton.type = 'submit';
            submitButton.textContent = 'Submit Answers';
            submitButton.className = 'btn btn-primary btn-block';
            form.appendChild(submitButton);
        })
        .catch(error => console.error('Error loading stress questions:', error));
    }
});

document.addEventListener('DOMContentLoaded', function() {
    // Handle sleep data form submission
    const sleepDataForm = document.getElementById('sleepDataForm');
    const resultsDiv = document.getElementById('results');
    const takeQuizButton = document.getElementById('takeQuizButton');
    const questionnaireSection = document.getElementById('questionnaireSection');
    const sleepDataSection = document.getElementById('sleepDataSection');
    const questionnaireForm = document.getElementById('questionnaireForm');
    const recommendationDiv = document.getElementById('recommendation');

    sleepDataForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const totalMinutesAsleep = document.getElementById('totalMinutesAsleep').value;
        const totalTimeInBed = document.getElementById('totalTimeInBed').value;
        const minutesREM = document.getElementById('minutesREM').value;
        const minutesLightSleep = document.getElementById('minutesLightSleep').value;

        // Call the API to predict sleep quality
        fetch('http://127.0.0.1:5000/predict/sleep_quality', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                "Total Minutes Asleep": totalMinutesAsleep,
                "Total Time in Bed": totalTimeInBed,
                "Minutes REM Sleep": minutesREM,
                "Minutes Light Sleep": minutesLightSleep
            })
        })
        .then(response => response.json())
        .then(data => {
            resultsDiv.innerHTML = `Sleep Quality Score: ${data.sleep_quality_score}, Category: ${data.sleep_category}`;
            takeQuizButton.style.display = 'block';
            sessionStorage.setItem('sleepCategory', data.sleep_category);
        })
        .catch(error => console.error('Error:', error));
    });

    takeQuizButton.addEventListener('click', function() {
        sleepDataSection.style.display = 'none';
        questionnaireSection.style.display = 'block';
        loadQuestions();
    });

    questionnaireForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const answers = Array.from(document.querySelectorAll('#questionnaireForm select')).map(select => select.value);
        const category = sessionStorage.getItem('sleepCategory');
        
        fetch('/submit_answers', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ category, answers })
        })
        .then(response => response.json())
        .then(data => {
            recommendationDiv.innerHTML = data.recommendation;
        })
        .catch(error => console.error('Error:', error));
    });

    function loadQuestions() {
        const category = sessionStorage.getItem('sleepCategory');
        fetch(`/get_questions/${category}`)
        .then(response => response.json())
        .then(data => {
            const form = document.getElementById('questionnaireForm');
            form.innerHTML = ''; // Clear existing content
            data.questions.forEach((question, index) => {
                const formGroup = document.createElement('div');
                formGroup.className = 'form-group';
                
                const label = document.createElement('label');
                label.textContent = question;
                label.htmlFor = 'question-' + index;
                formGroup.appendChild(label);
    
                const select = document.createElement('select');
                select.id = 'question-' + index;
                select.className = 'form-control';
                select.innerHTML = `<option value="">Select an answer</option><option value="yes">Yes</option><option value="no">No</option>`;
                formGroup.appendChild(select);
    
                form.appendChild(formGroup);
            });
    
            const submitButton = document.createElement('button');
            submitButton.type = 'submit';
            submitButton.textContent = 'Submit Answers';
            submitButton.className = 'btn btn-primary btn-block';
            form.appendChild(submitButton);
        });
    }
    
});

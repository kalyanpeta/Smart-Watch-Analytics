# Define questions and recommendations for each category of sleeper

SLEEP_QUESTIONS = {
    "The Dream Catcher": [
        "Do you generally wake up feeling refreshed?",
        "Do you maintain a consistent sleep schedule?",
        "Do you avoid caffeine and heavy meals before bedtime?",
        "Is your sleeping environment quiet and dark?",
        "Do you engage in relaxing activities before bedtime?"
    ],
    "The Napper": [
        "Do you often take long naps during the day that affect your nighttime sleep?",
        "Do you struggle to fall asleep even when you feel tired?",
        "Do you use electronic devices right before bed?",
        "Do you find yourself waking up frequently during the night?",
        "Do you consume caffeine late in the day?"
    ],
    "The Toss-and-Turner": [
        "Do you often worry or feel anxious when trying to sleep?",
        "Do you have trouble staying asleep throughout the night?",
        "Do you use your bed for activities other than sleep?",
        "Do you exercise within three hours of your bedtime?",
        "Do you feel uncomfortable or in pain when you wake up?"
    ],
    "The All-Nighter": [
        "Do you often work or study late into the night?",
        "Do you consume energy drinks or significant caffeine to stay awake?",
        "Do you sleep less than 4 hours most nights?",
        "Is your sleep schedule inconsistent due to work or social activities?",
        "Do you feel drowsy or fatigued during the day?"
    ]
}

RECOMMENDATIONS = {
    "yes": {
        "The Dream Catcher": "Maintain your good habits and perhaps focus even more on relaxation techniques.",
        "The Napper": "Try limiting naps and establishing a soothing bedtime routine to improve sleep quality.",
        "The Toss-and-Turner": "Address stress and anxiety as possible, and create a more sleep-focused environment.",
        "The All-Nighter": "Consider restructuring your daytime responsibilities to prioritize sleep."
    },
    "no": {
        "The Dream Catcher": "Keep up your excellent sleep practices and ensure your sleeping environment remains ideal.",
        "The Napper": "Develop a consistent sleep schedule and avoid stimulants in the evening.",
        "The Toss-and-Turner": "Try to establish a calming pre-sleep routine and make your bedroom conducive to sleep.",
        "The All-Nighter": "Aim to gradually increase your sleep hours and stabilize your sleep schedule."
    }
}

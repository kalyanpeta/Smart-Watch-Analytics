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

STRESS_QUESTIONS = {
    "Low": [
        "Do you feel relaxed for most of the day?",
        "Do you find it easy to unwind and relax when you have free time?",
        "Do you engage in regular physical activity?",
        "Do you feel that you manage stress well through hobbies or activities?",
        "Are you able to disconnect from work-related thoughts during personal time?"
    ],
    "Medium": [
        "Do you often feel pressures from work or home life?",
        "Do you struggle to maintain a work-life balance?",
        "Do you find it hard to concentrate because of your worries?",
        "Do you sometimes skip meals or eat irregularly due to stress?",
        "Do you feel fatigued even after resting or sleeping?"
    ],
    "High": [
        "Do you often feel overwhelmed by your responsibilities?",
        "Do you experience physical symptoms of stress such as headaches or muscle tension?",
        "Is it difficult for you to relax even in a comfortable environment?",
        "Do you feel anxious or agitated frequently?",
        "Do you often feel that you cannot cope with all the demands of daily life?"
    ]
}

STRESS_RECOMMENDATIONS = {
    "yes": {
        "Low": "Continue practicing good stress management techniques and maintain your balanced lifestyle.",
        "Medium": "Consider adopting more relaxation techniques and possibly seek professional help if stress persists.",
        "High": "It is crucial to seek strategies for stress reduction and professional counseling might be beneficial."
    },
    "no": {
        "Low": "Keep up your excellent habits but remain aware of how stress affects you to prevent it from increasing.",
        "Medium": "Try to incorporate more stress-reduction techniques into your daily routine and consider professional advice.",
        "High": "Immediate action to reduce stress is important. Professional help or counseling is highly recommended."
    }
}

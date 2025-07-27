# Test data for OctoFit Tracker

def get_test_data():
    return {
        "users": [
            {"email": "student1@example.com", "name": "Student One", "age": 16, "team": "Team A"},
            {"email": "student2@example.com", "name": "Student Two", "age": 17, "team": "Team B"},
        ],
        "teams": [
            {"name": "Team A", "members": ["student1@example.com"]},
            {"name": "Team B", "members": ["student2@example.com"]},
        ],
        "activities": [
            {"user": "student1@example.com", "type": "running", "duration": 30, "calories": 300},
            {"user": "student2@example.com", "type": "cycling", "duration": 45, "calories": 450},
        ],
        "leaderboard": [
            {"team": "Team A", "points": 300},
            {"team": "Team B", "points": 450},
        ],
        "workouts": [
            {"name": "Morning Run", "type": "running", "duration": 30},
            {"name": "Evening Cycle", "type": "cycling", "duration": 45},
        ],
    }

# Bot Configuration
WHATSAPP_CONFIG = {
    "PHONE_NUMBER": "your_phone_number",
    "API_KEY": "your_api_key",
    "GROUP_ID": "your_group_id"
}

# Point System Configuration
POINTS_CONFIG = {
    "INITIAL_POINTS": 100,      # Starting points for new members
    "NO_PLAY_PENALTY": -5,      # Penalty for saying "no"
    "NO_RESPONSE_PENALTY": -10,  # Penalty for not responding
    "LATE_CANCEL_PENALTY": -15,  # Penalty for late cancellation
    "MIN_PLAYERS": 3,           # Minimum players for game night
    "ATTENDANCE_BONUS": 3,      # Points earned for attending a game
    "MAX_POINTS": 100          # Maximum points a player can have
}

# Time Configuration
TIME_CONFIG = {
    "POLL_TIME": "20:00",      # When daily poll is sent (8 PM ART)
    "GAME_TIME": "22:00",      # Default game time (10 PM ART)
    "CHECK_TIME": "21:00"      # When to check final responses (9 PM ART)
} 
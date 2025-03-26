from datetime import datetime, timedelta
import json
import schedule
import time
from whatsapp import Client

class GamingBot:
    def __init__(self):
        self.client = Client(
            phone="your_phone_number",  # Replace with your number
            key="your_whatsapp_key"     # Get this from WhatsApp Business API
        )
        self.group_id = "your_group_id" # Replace with your group ID
        self.players = self.load_players()
        self.poll_responses = {}
        self.game_time = "21:00"  # Default game time
        
        # Point System Constants
        self.INITIAL_POINTS = 100       # Starting points for new members
        self.NO_PLAY_PENALTY = -5       # Penalty for saying "no"
        self.NO_RESPONSE_PENALTY = -10  # Penalty for not responding
        self.LATE_CANCEL_PENALTY = -15  # Penalty for late cancellation
        self.MIN_PLAYERS = 3            # Minimum players for game night
        
        # Point Recovery Constants
        self.ATTENDANCE_BONUS = 3       # Points earned for attending a game
        self.MAX_POINTS = 100          # Maximum points a player can have
        
    def load_players(self):
        try:
            with open('players.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
            
    def save_players(self):
        with open('players.json', 'w') as f:
            json.dump(self.players, f)

    def create_daily_poll(self):
        poll_message = "🎮 Gaming Night Poll!\nWill you join tonight's gaming session?\n\n" \
                      f"Game Time: {self.game_time}\n\n" \
                      "Reply with:\n" \
                      "1️⃣ - Yes, I'm in!\n" \
                      "2️⃣ - No, can't make it\n"
        
        self.client.send_message(self.group_id, poll_message)
        self.poll_responses = {}

    def process_response(self, player_id, response):
        if player_id not in self.players:
            self.players[player_id] = {
                "points": self.INITIAL_POINTS,
                "name": "Player"  # You should update this with actual player name
            }
        
        self.poll_responses[player_id] = {
            "response": response,
            "timestamp": datetime.now().isoformat()
        }

    def check_game_status(self):
        positive_responses = sum(1 for r in self.poll_responses.values() 
                               if r["response"] == "1")
        
        if positive_responses >= self.MIN_PLAYERS:
            self.announce_game_night()
        else:
            self.announce_cancelled_night()

    def penalize_no_responses(self):
        for player_id in self.players:
            if player_id not in self.poll_responses:
                self.players[player_id]["points"] -= self.NO_RESPONSE_PENALTY
                self.log_penalty(player_id, "no response", self.NO_RESPONSE_PENALTY)
                
        self.check_eliminations()
        self.save_players()

    def log_penalty(self, player_id, reason, points):
        message = f"⚠️ Point Penalty Log:\n" \
                 f"Player: {self.players[player_id]['name']}\n" \
                 f"Reason: {reason}\n" \
                 f"Points deducted: {abs(points)}\n" \
                 f"Current points: {self.players[player_id]['points']}"
        
        self.client.send_message(self.group_id, message)

    def check_eliminations(self):
        for player_id, data in self.players.items():
            if data["points"] <= 0:
                self.create_elimination_poll(player_id)

    def create_elimination_poll(self, player_id):
        poll_message = f"⚠️ Elimination Poll ⚠️\n" \
                      f"Player {self.players[player_id]['name']} has run out of points!\n" \
                      f"Should they be removed from the group?\n\n" \
                      "Reply with:\n" \
                      "1️⃣ - Yes, remove them\n" \
                      "2️⃣ - No, give them another chance"
        
        self.client.send_message(self.group_id, poll_message)

    def announce_game_night(self):
        confirmed_players = [player_id for player_id, response in self.poll_responses.items() 
                           if response["response"] == "1"]
        
        message = "🎮 Game Night is ON! 🎮\n\nConfirmed players:"
        for player_id in confirmed_players:
            message += f"\n- {self.players[player_id]['name']}"
        
        self.client.send_message(self.group_id, message)
        
        # Schedule attendance recording
        game_hour = int(self.game_time.split(":")[0])
        game_minute = int(self.game_time.split(":")[1])
        schedule.every().day.at(f"{game_hour+1}:00").do(
            self.record_attendance, confirmed_players
        )

    def record_attendance(self, confirmed_players):
        """Record attendance and award points to players who showed up"""
        for player_id in confirmed_players:
            # Award points up to the maximum
            current_points = self.players[player_id]["points"]
            new_points = min(current_points + self.ATTENDANCE_BONUS, self.MAX_POINTS)
            points_earned = new_points - current_points
            
            if points_earned > 0:
                self.players[player_id]["points"] = new_points
                self.log_points_earned(player_id, "game attendance", points_earned)
        
        self.save_players()

    def log_points_earned(self, player_id, reason, points):
        message = f"✨ Points Earned:\n" \
                 f"Player: {self.players[player_id]['name']}\n" \
                 f"Reason: {reason}\n" \
                 f"Points earned: {points}\n" \
                 f"Current points: {self.players[player_id]['points']}"
        
        self.client.send_message(self.group_id, message)

def main():
    bot = GamingBot()
    
    # Schedule daily poll at 20:00 ART (8 PM Argentina Time)
    schedule.every().day.at("20:00").do(bot.create_daily_poll)
    
    # Check responses and game status at 21:00 ART (1 hour after poll)
    schedule.every().day.at("21:00").do(bot.check_game_status)
    
    # Game time at 22:00 ART
    bot.game_time = "22:00"
    
    # Penalize no responses at 23:59 ART
    schedule.every().day.at("23:59").do(bot.penalize_no_responses)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main() 
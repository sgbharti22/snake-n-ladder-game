import random
from typing import Dict, List, Tuple

class SnakeAndLadder:
    """
    A class to manage the Snake and Ladder game logic.
    
    The board has 100 squares. More snakes than ladders are placed to make the game difficult.
    """
    
    def __init__(self, num_players: int = 2, player_names: Dict[int, str] = None, player_icons: Dict[int, str] = None):
        """
        Initialize the game with specified number of players.
        
        Args:
            num_players (int): Number of players (2-4). Defaults to 2.
            player_names (Dict[int, str]): Dictionary mapping player ID to player name.
            player_icons (Dict[int, str]): Dictionary mapping player ID to player icon/emoji.
            
        Raises:
            ValueError: If num_players is not between 2 and 4.
        """
        if num_players < 2 or num_players > 4:
            raise ValueError("Number of players must be between 2 and 4")
        
        self.num_players = num_players
        self.board_size = 100
        self.players_position = {i: 0 for i in range(1, num_players + 1)}
        self.current_player = 1
        self.game_over = False
        self.winner = None
        
        # Player names and icons
        self.player_names = player_names or {i: f"Player {i}" for i in range(1, num_players + 1)}
        self.player_icons = player_icons or {i: "🔵" for i in range(1, num_players + 1)}
        
        # More snakes than ladders for difficulty
        self.snakes = {
            16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 73: 58, 87: 64,
            93: 73, 95: 75, 98: 79, 92: 71, 78: 52, 84: 74, 59: 38, 77: 45
        }  # 15 snakes
        
        self.ladders = {
            2: 38, 7: 15, 21: 42, 28: 84, 36: 55, 51: 67, 72: 91, 80: 98
        }  # 8 ladders
        
        self.move_history = {i: [] for i in range(1, num_players + 1)}
    
    def roll_dice(self) -> int:
        """
        Simulate rolling a standard 6-sided dice.
        
        Returns:
            int: Random number between 1 and 6.
        """
        return random.randint(1, 6)
    
    def move_player(self, dice_value: int) -> Dict:
        """
        Move the current player based on the dice value.
        Handles snakes and ladders landing.
        
        Args:
            dice_value (int): Value from dice roll (1-6).
            
        Returns:
            Dict: Movement details including new position and any snake/ladder encountered.
        """
        if self.game_over:
            return {"error": "Game is already over"}
        
        player_id = self.current_player
        old_position = self.players_position[player_id]
        new_position = old_position + dice_value
        move_result = {
            "player": player_id,
            "old_position": old_position,
            "dice_value": dice_value,
            "position_after_roll": new_position,
            "snake_or_ladder": None,
            "final_position": new_position
        }
        
        # Check if position exceeds board size
        if new_position > self.board_size:
            move_result["final_position"] = old_position
            move_result["out_of_bounds"] = True
            self.move_history[player_id].append(move_result)
            self._next_player()
            return move_result
        
        # Check for snakes
        if new_position in self.snakes:
            ladder_or_snake_end = self.snakes[new_position]
            move_result["snake_or_ladder"] = f"Snake: {new_position} → {ladder_or_snake_end}"
            new_position = ladder_or_snake_end
        
        # Check for ladders
        elif new_position in self.ladders:
            ladder_or_snake_end = self.ladders[new_position]
            move_result["snake_or_ladder"] = f"Ladder: {new_position} → {ladder_or_snake_end}"
            new_position = ladder_or_snake_end
        
        move_result["final_position"] = new_position
        self.players_position[player_id] = new_position
        self.move_history[player_id].append(move_result)
        
        # Check if player won
        if new_position == self.board_size:
            self.game_over = True
            self.winner = player_id
            move_result["won"] = True
        
        # Move to next player
        if not self.game_over:
            self._next_player()
        
        return move_result
    
    def _next_player(self) -> None:
        """
        Move to the next player's turn in round-robin fashion.
        """
        self.current_player = (self.current_player % self.num_players) + 1
    
    def get_game_status(self) -> Dict:
        """
        Get the current game status.
        
        Returns:
            Dict: Current positions of all players, current player, and game state.
        """
        return {
            "players_position": self.players_position.copy(),
            "current_player": self.current_player,
            "game_over": self.game_over,
            "winner": self.winner
        }
    
    def get_all_snakes_and_ladders(self) -> Tuple[Dict, Dict]:
        """
        Get all snakes and ladders on the board.
        
        Returns:
            Tuple[Dict, Dict]: Snakes and ladders dictionaries.
        """
        return self.snakes, self.ladders
    
    def get_player_move_history(self, player_id: int) -> List[Dict]:
        """
        Get the move history of a specific player.
        
        Args:
            player_id (int): ID of the player.
            
        Returns:
            List[Dict]: List of moves made by the player.
        """
        return self.move_history.get(player_id, [])
    
    def reset_game(self) -> None:
        """
        Reset the game to initial state.
        """
        self.players_position = {i: 0 for i in range(1, self.num_players + 1)}
        self.current_player = 1
        self.game_over = False
        self.winner = None
        self.move_history = {i: [] for i in range(1, self.num_players + 1)}
    
    def get_player_name(self, player_id: int) -> str:
        """
        Get the name of a specific player.
        
        Args:
            player_id (int): ID of the player.
            
        Returns:
            str: Player's name.
        """
        return self.player_names.get(player_id, f"Player {player_id}")
    
    def get_player_icon(self, player_id: int) -> str:
        """
        Get the icon/emoji of a specific player.
        
        Args:
            player_id (int): ID of the player.
            
        Returns:
            str: Player's icon/emoji.
        """
        return self.player_icons.get(player_id, "🔵")
    
    def set_player_info(self, player_id: int, name: str, icon: str) -> None:
        """
        Set player name and icon.
        
        Args:
            player_id (int): ID of the player.
            name (str): Player's name.
            icon (str): Player's icon/emoji.
        """
        self.player_names[player_id] = name
        self.player_icons[player_id] = icon

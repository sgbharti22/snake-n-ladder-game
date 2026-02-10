# 🐍 Snake & Ladder Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-green?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-green?style=flat-square)

A challenging **Snake & Ladder** board game web application built with Python and Streamlit. Play with 2-4 players on a 100-square board with more snakes than ladders to increase difficulty!

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Game Rules](#game-rules) • [Project Structure](#project-structure) • [Contributing](#contributing)

</div>

---

## 🎮 Features

- ✅ **2-4 Player Support**: Play with friends locally
- ✅ **100-Square Board**: Classic board game format
- ✅ **Dynamic Board**: Real-time visualization with interactive board
- ✅ **15 Snakes vs 8 Ladders**: Challenging gameplay with more hazards than rewards
- ✅ **Green-Based Streamlit UI**: Beautiful, customized green theme interface
- ✅ **Move History**: Track all player movements throughout the game
- ✅ **Dice Rolling**: Realistic 6-sided dice simulation
- ✅ **Win Condition**: First player to reach square 100 wins!
- ✅ **Responsive Design**: Works on desktop and tablets
- ✅ **Session State Management**: Persistent game state during session

---

## 📋 Requirements

- Python 3.8 or higher
- Streamlit 1.28.0 or higher
- Pip (Python package manager)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sgbharti22/snake-n-ladder-game.git
cd snake-n-ladder-game
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Game Flow

1. **Start Screen**: Welcome page with game instructions
2. **Player Selection**: Choose 2-4 players from the sidebar
3. **Start Game**: Click "START NEW GAME" to begin
4. **Game Board**: View the 100-square board with current positions
5. **Roll Dice**: Players take turns clicking "ROLL" button
6. **Move**: Automatic movement based on dice value
7. **Snakes & Ladders**: 
   - Land on a snake → slide down (bad luck!)
   - Land on a ladder → climb up (good fortune!)
8. **Win**: First player reaching square 100 wins!

---

## 🎲 Game Rules

### Basic Rules

1. **Starting Position**: All players start at square 0 (outside the board)
2. **Turn Order**: Players take turns in order (Player 1 → Player 2 → ... → Player N)
3. **Dice Roll**: Each player rolls a standard 6-sided dice (values 1-6)
4. **Movement**: Move forward by the number shown on the dice
5. **Snakes**: Moving to a snake's head → slide down to the snake's tail
6. **Ladders**: Moving to a ladder's base → climb up to the ladder's top
7. **Exceeding 100**: If you roll more than needed to reach 100, you stay at your current position (turn passes to next player)
8. **Winning**: First player to land exactly on or pass square 100 wins!

### Game Difficulty

- **15 Snakes** (More obstacles)
- **8 Ladders** (Fewer shortcuts)
- **Ratio**: 1.875:1 (snakes to ladders)
- This makes the game challenging and unpredictable!

### Snake Positions

| Position | Landing Spot | Position | Landing Spot |
|----------|-------------|----------|-------------|
| 16 | 6 | 78 | 52 |
| 47 | 26 | 84 | 74 |
| 49 | 11 | 87 | 64 |
| 56 | 53 | 92 | 71 |
| 62 | 19 | 93 | 73 |
| 73 | 58 | 95 | 75 |
| 77 | 45 | 98 | 79 |

### Ladder Positions

| Position | Landing Spot | Position | Landing Spot |
|----------|-------------|----------|-------------|
| 2 | 38 | 36 | 55 |
| 7 | 15 | 51 | 67 |
| 21 | 42 | 72 | 91 |
| 28 | 84 | 80 | 98 |

---

## 📁 Project Structure

```
snake-n-ladder-game/
│
├── app.py                 # Main Streamlit application
├── game.py               # Game logic and mechanics
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

### File Descriptions

#### `game.py`
Core game logic module containing the `SnakeAndLadder` class with methods:
- `__init__(num_players)`: Initialize the game
- `roll_dice()`: Simulate dice roll (1-6)
- `move_player(dice_value)`: Process player movement
- `get_game_status()`: Get current game state
- `get_all_snakes_and_ladders()`: Get board layout
- `get_player_move_history(player_id)`: Get player's move history
- `reset_game()`: Reset game to initial state

#### `app.py`
Streamlit UI application featuring:
- Green-based custom CSS styling
- Sidebar game controls
- Real-time board visualization
- Player status display
- Dice rolling interface
- Move results and animations
- Game statistics and winner announcement

#### `requirements.txt`
Python package dependencies:
```
streamlit>=1.28.0
python>=3.8
```

---

## 🛠️ Methods and Classes

### SnakeAndLadder Class

#### Constructor
```python
def __init__(self, num_players: int = 2)
```
- **Parameter**: `num_players` (2-4)
- **Raises**: ValueError if players < 2 or > 4

#### roll_dice()
```python
def roll_dice(self) -> int
```
- **Returns**: Random integer 1-6
- **Use**: Get dice value for current player's turn

#### move_player()
```python
def move_player(self, dice_value: int) -> Dict
```
- **Parameter**: `dice_value` (1-6 from dice roll)
- **Returns**: Dictionary with movement details
- **Handles**: Snake/ladder landing, win condition, board boundaries

#### get_game_status()
```python
def get_game_status(self) -> Dict
```
- **Returns**: Current positions of all players and game state
- **Keys**: `players_position`, `current_player`, `game_over`, `winner`

#### get_all_snakes_and_ladders()
```python
def get_all_snakes_and_ladders(self) -> Tuple[Dict, Dict]
```
- **Returns**: Tuple of (snakes_dict, ladders_dict)

#### get_player_move_history()
```python
def get_player_move_history(self, player_id: int) -> List[Dict]
```
- **Parameter**: `player_id` (1 to num_players)
- **Returns**: List of all moves made by that player

#### reset_game()
```python
def reset_game(self) -> None
```
- **Effect**: Resets game to initial state

---

## 🎨 UI Features

### Green Theme Customization
- Primary Color: **#2ecc71** (Emerald Green)
- Secondary Color: **#27ae60** (Dark Green)
- Background: **#f0fdf4** (Light Green)
- Snake Color: **Red** (#d32f2f)
- Ladder Color: **Blue** (#1976d2)

### UI Components
1. **Main Title**: Large green header with game title
2. **Sidebar**: Game settings and options
3. **Player Positions**: Real-time display of each player's position
4. **Current Turn Indicator**: Shows whose turn it is
5. **Progress Bars**: Visual representation of player progress (0-100%)
6. **Game Board**: 10x10 interactive grid showing:
   - Player positions (green squares with player number)
   - Snake positions (red snake emoji)
   - Ladder positions (blue ladder emoji)
   - Empty squares (light green)
7. **Dice Roll Button**: Large, prominent button to roll dice
8. **Move Results**: Messages showing movement outcome
9. **Expander**: View all snakes and ladders reference
10. **Footer**: Game information and credits

---

## 🚀 How to Build and Deploy

### Local Testing

```bash
# Clone and setup
git clone https://github.com/sgbharti22/snake-n-ladder-game.git
cd snake-n-ladder-game

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository
5. Set main file to `app.py`
6. Click "Deploy"

### Deploy on Other Platforms

- **Heroku**: Use Streamlit's Heroku buildpack
- **AWS**: Deploy using EC2 with Streamlit
- **Docker**: Create a Dockerfile for containerization
- **DigitalOcean**: Use app platform for quick deployment

---

## 📝 Example Usage

```python
from game import SnakeAndLadder

# Create game for 3 players
game = SnakeAndLadder(num_players=3)

# Roll dice and move
dice_result = game.roll_dice()  # Returns 1-6
move_result = game.move_player(dice_result)

# Get game status
status = game.get_game_status()
print(f"Player 1 position: {status['players_position'][1]}")

# Get all snakes and ladders
snakes, ladders = game.get_all_snakes_and_ladders()
print(f"Snakes: {snakes}")
print(f"Ladders: {ladders}")

# Get player history
history = game.get_player_move_history(1)
print(f"Player 1 moves: {history}")

# Reset game
game.reset_game()
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Install requirements
```bash
pip install -r requirements.txt
```

### Issue: "ValueError: Number of players must be between 2 and 4"
**Solution**: Select 2-4 players in the sidebar before starting

### Issue: App runs but board doesn't display
**Solution**: Refresh the browser or restart Streamlit
```bash
streamlit run app.py --logger.level=debug
```

### Issue: Session state not persisting
**Solution**: This is normal - Streamlit reruns on interaction. Game state is maintained using `st.session_state`

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/snake-n-ladder-game.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Follow PEP 8 style guide
   - Add docstrings to new functions
   - Test your changes

4. **Commit Changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```

5. **Push to Branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open Pull Request**
   - Describe your changes clearly
   - Reference related issues
   - Wait for review

---

## 💡 Feature Ideas for Future Versions

- [ ] Multiplayer over network (WebSocket support)
- [ ] Sound effects and animations
- [ ] Different difficulty levels (more/fewer snakes)
- [ ] AI opponent option
- [ ] Game statistics and leaderboard
- [ ] Save and resume games
- [ ] Power-ups and special tiles
- [ ] Mobile app version
- [ ] Dark mode toggle
- [ ] Customizable board themes

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

**Bharthi Sreenivas**
- GitHub: [@sgbharti22](https://github.com/sgbharti22)

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) - The fastest way to build data apps
- Inspired by the classic Snake and Ladder board game
- Thanks to all contributors and players!

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review existing [Issues](https://github.com/sgbharti22/snake-n-ladder-game/issues)
3. Create a new Issue with:
   - Clear description
   - Steps to reproduce
   - Your environment (OS, Python version, etc.)
   - Screenshots if applicable

---

## 🎯 Quick Start Summary

```bash
# 1. Clone repository
git clone https://github.com/sgbharti22/snake-n-ladder-game.git && cd snake-n-ladder-game

# 2. Create virtual environment
python -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the game
streamlit run app.py

# 5. Open browser to http://localhost:8501
```

**Enjoy the game! 🐍🪜🎲**

---

<div align="center">

Made with ❤️ using Python and Streamlit

⭐ If you like this project, please give it a star on GitHub!

</div>

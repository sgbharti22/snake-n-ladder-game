import streamlit as st
from game import SnakeAndLadder
import time

# Set page configuration
st.set_page_config(
    page_title="🐍 Snake & Ladder Game",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Available player icons
PLAYER_ICONS = {
    "🔴": "Red Circle",
    "🔵": "Blue Circle",
    "🟢": "Green Circle",
    "🟡": "Yellow Circle",
    "🟣": "Purple Circle",
    "🟠": "Orange Circle",
    "⭐": "Star",
    "❤️": "Heart",
    "💎": "Diamond",
    "👑": "Crown",
    "🦁": "Lion",
    "🐯": "Tiger",
    "🚀": "Rocket",
    "🎯": "Target",
    "🎲": "Dice",
    "🍕": "Pizza",
}

# Custom CSS for green-based theme
st.markdown("""
    <style>
    :root {
        --primary-color: #2ecc71;
        --secondary-color: #27ae60;
        --background-color: #f0fdf4;
    }
    
    .main {
        background-color: #f0fdf4;
    }
    
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #27ae60;
    }
    
    .player-box {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
    
    .game-board {
        background: linear-gradient(135deg, #e8f8f5 0%, #d5f4e6 100%);
        padding: 20px;
        border-radius: 10px;
        border: 3px solid #2ecc71;
    }
    
    .player-info {
        font-weight: bold;
        font-size: 18px;
    }
    
    .snake-color {
        color: #d32f2f;
    }
    
    .ladder-color {
        color: #1976d2;
    }
    
    .board-cell {
        border: 1px solid #27ae60;
        padding: 0px;
        border-radius: 3px;
        text-align: center;
        font-weight: bold;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        margin: 0px;
        gap: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'game' not in st.session_state:
    st.session_state.game = None
    st.session_state.game_initialized = False
    st.session_state.num_players = 2
    st.session_state.players_setup = False
    st.session_state.player_names = {}
    st.session_state.player_icons = {}

# Main Title
st.markdown("<h1 style='text-align: center; color: #2ecc71;'>🐍 SNAKE & LADDER GAME 🪜</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #27ae60; font-size: 16px;'>"
            "A challenging game where snakes outnumber ladders - will you reach 100?</p>",
            unsafe_allow_html=True)

# Sidebar for game settings
with st.sidebar:
    st.markdown("<h2 style='color: #2ecc71;'>⚙️ GAME SETTINGS</h2>", unsafe_allow_html=True)
    
    if not st.session_state.players_setup:
        num_players = st.slider(
            "Select number of players (2-4):",
            min_value=2,
            max_value=4,
            value=2,
            step=1,
            help="Choose how many players will play the game"
        )
        
        if st.button("➡️ NEXT: Setup Players", key="next_setup", use_container_width=True):
            st.session_state.num_players = num_players
            st.session_state.players_setup = True
            st.rerun()
    
    elif not st.session_state.game_initialized:
        st.markdown(f"<p style='color: #27ae60;'><b>👥 Players:</b> {st.session_state.num_players}</p>", 
                    unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<h3 style='color: #2ecc71;'>👤 PLAYER SETUP</h3>", unsafe_allow_html=True)
        
        # Player setup form
        for i in range(1, st.session_state.num_players + 1):
            st.markdown(f"<p style='color: #27ae60; font-weight: bold;'>Player {i}</p>", 
                       unsafe_allow_html=True)
            
            player_name = st.text_input(
                f"Name for Player {i}:",
                value=st.session_state.player_names.get(i, f"Player {i}"),
                key=f"player_name_{i}",
                placeholder=f"Enter Player {i} name"
            )
            
            icon_selection = st.selectbox(
                f"Choose icon for Player {i}:",
                options=list(PLAYER_ICONS.keys()),
                format_func=lambda x: f"{x} - {PLAYER_ICONS[x]}",
                key=f"player_icon_{i}",
                index=i-1 if i <= len(PLAYER_ICONS) else 0
            )
            
            st.session_state.player_names[i] = player_name
            st.session_state.player_icons[i] = icon_selection
            st.markdown("---")
        
        if st.button("🎮 START GAME", key="start_game", use_container_width=True, help="Begin the game with selected players"):
            try:
                game = SnakeAndLadder(
                    num_players=st.session_state.num_players,
                    player_names=st.session_state.player_names,
                    player_icons=st.session_state.player_icons
                )
                st.session_state.game = game
                st.session_state.game_initialized = True
                st.rerun()
            except Exception as e:
                st.error(f"Error initializing game: {str(e)}")
        
        if st.button("⬅️ BACK", key="back_setup", use_container_width=True):
            st.session_state.players_setup = False
            st.rerun()
    
    else:
        st.markdown(f"<p style='color: #27ae60;'><b>👥 Players:</b> {st.session_state.num_players}</p>", 
                    unsafe_allow_html=True)
        
        for i in range(1, st.session_state.num_players + 1):
            player_icon = st.session_state.game.get_player_icon(i)
            player_name = st.session_state.game.get_player_name(i)
            st.markdown(f"<p style='color: #27ae60; margin: 5px 0;'>{player_icon} <b>{player_name}</b></p>", 
                       unsafe_allow_html=True)
        
        st.markdown("---")
        
        if st.button("🔄 RESET GAME", use_container_width=True, key="reset_game"):
            st.session_state.game.reset_game()
            st.rerun()
        
        if st.button("🏠 NEW GAME", use_container_width=True, key="new_game"):
            st.session_state.game_initialized = False
            st.session_state.players_setup = False
            st.session_state.game = None
            st.session_state.player_names = {}
            st.session_state.player_icons = {}
            st.rerun()
    
    # Display Snakes and Ladders info
    if st.session_state.game_initialized or st.session_state.players_setup:
        st.markdown("---")
    st.markdown("<h3 style='color: #2ecc71;'>📋 BOARD INFO</h3>", unsafe_allow_html=True)
    st.info("🎯 **Objective:** Be the first to reach square 100!")
    st.warning("⚠️ **Difficulty:** More snakes (15) than ladders (8) - This game is challenging!")

# Main game area
if st.session_state.game_initialized and st.session_state.game:
    game = st.session_state.game
    status = game.get_game_status()
    
    # Check for winner
    if status['game_over']:
        winner_name = game.get_player_name(status['winner'])
        winner_icon = game.get_player_icon(status['winner'])
        st.markdown(f"<div style='background: #2ecc71; padding: 30px; border-radius: 10px; text-align: center;'>"
                   f"<h1 style='color: white;'>🎉 {winner_icon} {winner_name} WINS! 🏆</h1>"
                   f"</div>", unsafe_allow_html=True)
        st.balloons()
        
        # Show final rankings
        st.markdown("<h3 style='color: #2ecc71;'>Final Standings:</h3>", unsafe_allow_html=True)
        sorted_positions = sorted(status['players_position'].items(), key=lambda x: x[1], reverse=True)
        
        cols = st.columns(len(sorted_positions))
        for idx, (player_id, position) in enumerate(sorted_positions):
            player_name = game.get_player_name(player_id)
            player_icon = game.get_player_icon(player_id)
            with cols[idx]:
                if player_id == status['winner']:
                    st.markdown(f"<div class='player-box'><h2>🥇 {player_icon} {player_name}</h2><p>Position: {position}</p></div>",
                              unsafe_allow_html=True)
                else:
                    place = ["🥈", "🥉"][idx - 1] if idx < 3 else f"{idx + 1}."
                    st.markdown(f"<div class='player-box' style='background: linear-gradient(135deg, #95a5a6 0%, #7f8c8d 100%);'>"
                              f"<h2>{place} {player_icon} {player_name}</h2><p>Position: {position}</p></div>",
                              unsafe_allow_html=True)
    
    else:
        # Display current game state
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            st.markdown("<h3 style='color: #2ecc71;'>📊 POSITIONS</h3>", unsafe_allow_html=True)
            for player_id in range(1, st.session_state.num_players + 1):
                pos = status['players_position'][player_id]
                player_name = game.get_player_name(player_id)
                player_icon = game.get_player_icon(player_id)
                is_current = " 👉" if player_id == status['current_player'] else ""
                st.markdown(f"<p style='font-size: 16px; color: #27ae60;'>"
                          f"{player_icon} <b>{player_name}:</b> {pos}/100{is_current}</p>",
                          unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h3 style='color: #2ecc71;'>🎲 CURRENT TURN</h3>", unsafe_allow_html=True)
            current_player_name = game.get_player_name(status['current_player'])
            current_player_icon = game.get_player_icon(status['current_player'])
            st.markdown(f"<div style='background: #27ae60; color: white; padding: 20px; border-radius: 10px; text-align: center;'>"
                       f"<h2 style='margin: 0;'>{current_player_icon} {current_player_name}'s Turn</h2>"
                       f"<p style='margin: 10px 0 0 0; font-size: 16px;'>Roll the dice to move</p>"
                       f"</div>", unsafe_allow_html=True)
        
        with col3:
            st.markdown("<h3 style='color: #2ecc71;'>🎯 PROGRESS</h3>", unsafe_allow_html=True)
            for player_id in range(1, st.session_state.num_players + 1):
                pos = status['players_position'][player_id]
                progress = (pos / 100) * 100
                player_icon = game.get_player_icon(player_id)
                st.progress(progress / 100, text=f"{player_icon} {int(progress)}%")
        
        # Game board visualization (without gaps)
        st.markdown("<h3 style='color: #2ecc71;'>🎮 GAME BOARD</h3>", unsafe_allow_html=True)
        
        for row in range(10):
            cols = st.columns(10, gap="small")
            for col_idx in range(10):
                i = row * 10 + col_idx + 1
                
                cell_content = str(i)
                cell_color = "#f0fdf4"
                player_here = None
                
                # Check if any player is on this square
                for player_id, pos in status['players_position'].items():
                    if pos == i:
                        player_icon = game.get_player_icon(player_id)
                        cell_content = player_icon
                        cell_color = "#2ecc71"
                        break
                
                # Check for snakes
                if i in game.snakes:
                    cell_color = "#ffebee"
                    cell_content = "🐍"
                # Check for ladders
                elif i in game.ladders:
                    cell_color = "#e3f2fd"
                    cell_content = "🪜"
                
                with cols[col_idx]:
                    st.markdown(
                        f"<div style='background: {cell_color}; border: 1px solid #27ae60; "
                        f"padding: 0px; border-radius: 3px; text-align: center; "
                        f"font-weight: bold; width: 100%; height: 50px; display: flex; "
                        f"align-items: center; justify-content: center; "
                        f"font-size: 20px; margin: 0px; line-height: 50px;'>{cell_content}</div>",
                        unsafe_allow_html=True
                    )
        
        # Dice roll button
        st.markdown("---")
        st.markdown("<h3 style='text-align: center; color: #2ecc71;'>🎲 ROLL THE DICE</h3>", 
                    unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🎲 ROLL", use_container_width=True, key="roll_button"):
                with st.spinner("Rolling dice..."):
                    time.sleep(0.3)
                    dice_value = game.roll_dice()
                    
                    # Show dice result
                    st.markdown(f"<div style='background: #2ecc71; color: white; padding: 20px; "
                              f"border-radius: 10px; text-align: center;'>"
                              f"<h2 style='margin: 0;'>Dice: {dice_value}</h2>"
                              f"</div>", unsafe_allow_html=True)
                    
                    # Process move
                    move_result = game.move_player(dice_value)
                    
                    # Display move results
                    if "error" in move_result:
                        st.error(move_result["error"])
                    else:
                        time.sleep(0.5)
                        
                        current_player_name = game.get_player_name(move_result['player'])
                        current_player_icon = game.get_player_icon(move_result['player'])
                        
                        if "out_of_bounds" in move_result and move_result["out_of_bounds"]:
                            st.warning(f"⚠️ {current_player_icon} {current_player_name} moved from {move_result['old_position']} + "
                                     f"{move_result['dice_value']} = {move_result['position_after_roll']} (exceeds 100) "
                                     f"❌ Turn skipped!")
                        else:
                            st.success(f"✅ {current_player_icon} {current_player_name} moved from {move_result['old_position']} "
                                     f"to {move_result['final_position']}")
                            
                            if move_result['snake_or_ladder']:
                                if "Snake" in move_result['snake_or_ladder']:
                                    st.error(f"🐍 {move_result['snake_or_ladder']} - Oh no!")
                                else:
                                    st.success(f"🪜 {move_result['snake_or_ladder']} - Great luck!")
                            
                            if move_result.get('won'):
                                st.balloons()
                    
                    time.sleep(0.5)
                    st.rerun()
    
    # Show snakes and ladders reference
    with st.expander("📋 View All Snakes & Ladders"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4 style='color: #d32f2f;'>🐍 SNAKES (More difficult!)</h4>", 
                       unsafe_allow_html=True)
            snakes_dict, _ = game.get_all_snakes_and_ladders()
            snakes_info = ""
            for start, end in sorted(snakes_dict.items()):
                snakes_info += f"**{start}** → {end}\n\n"
            st.markdown(snakes_info)
        
        with col2:
            st.markdown("<h4 style='color: #1976d2;'>🪜 LADDERS (Less helpful!)</h4>", 
                       unsafe_allow_html=True)
            _, ladders_dict = game.get_all_snakes_and_ladders()
            ladders_info = ""
            for start, end in sorted(ladders_dict.items()):
                ladders_info += f"**{start}** → {end}\n\n"
            st.markdown(ladders_info)

else:
    # Initial screen
    st.markdown("<div class='game-board'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #2ecc71;'>Welcome to Snake & Ladder! 🎮</h2>", 
               unsafe_allow_html=True)
    st.markdown("""
    ### How to Play:
    1. **Select Players**: Choose 2-4 players
    2. **Setup Players**: Enter names and choose icons for each player
    3. **Start Game**: Click the "START GAME" button
    4. **Roll Dice**: Players take turns rolling the dice
    5. **Move Pieces**: Move according to dice value (1-6) with your chosen icon
    6. **Snakes & Ladders**: 
       - 🪜 Ladder takes you UP (good luck!)
       - 🐍 Snake takes you DOWN (watch out!)
    7. **Win**: First player to reach square 100 wins!
    
    ### Game Difficulty:
    - **15 Snakes** vs **8 Ladders** - This game is CHALLENGING!
    - Strategic play and luck are both important
    
    ### Features:
    - ✨ Personalize your experience with your own name and custom icon
    - 📊 Real-time board visualization
    - 🎲 Fair cube-based dice rolling
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Show statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 Board Size", "100 Squares")
    with col2:
        st.metric("🐍 Snakes", "15 (Difficult)")
    with col3:
        st.metric("🪜 Ladders", "8 (Rare)")


# Footer
st.markdown("---")
st.markdown("""
<p style='text-align: center; color: #7f8c8d; font-size: 12px;'>
🐍 Snake & Ladder Game | Made with ❤️ using Streamlit | 2-4 Players | Board Size: 1-100 | Custom Icons & Names
</p>
""", unsafe_allow_html=True)

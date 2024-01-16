import pytest
from bowling_logic import calculate_score

def test_simple_game():
    rolls = [3] * 20  # Simple game with 3 pins down in each roll
    assert calculate_score(rolls) == 60

def test_strike_game():
    rolls = [10, 0] * 10  # Game with a strike in each frame
    assert calculate_score(rolls) == 200

def test_spare_game():
    rolls = [5, 5] * 10 + [5]  # Game with a spare in each frame and a final extra roll
    assert calculate_score(rolls) == 150

# Additional test cases can be added here

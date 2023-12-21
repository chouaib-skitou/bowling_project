
import pytest
from unittest.mock import patch
import party


def test_check_coherent_skittles():
    assert party.checkCoherentSkittles(5, [3]) == 5  # Cas normal
    assert party.checkCoherentSkittles(7, [3]) == 7  # Cas où le total dépasse 10

def test_check_spare():
    frame_score = [5]
    party.checkSpare(frame_score, 5)
    assert frame_score == [5, "|"]  # Test pour un spare

def test_check_strike_last_frame():
    frame_score = []
    party.checkStrikeLastFrame(frame_score, 10)
    assert frame_score == ["X"]  # Test pour un strike

# Mock pour les fonctions demandant une entrée utilisateur
@patch('builtins.input', return_value='5')
def test_check_skittles_in_ten(mock_input):
    assert party.checkSkittlesInTen() == 5
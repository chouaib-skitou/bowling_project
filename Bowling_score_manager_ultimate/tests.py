import unittest
from main import calculate_frame_scores

class TestSimpleBowlingScoring(unittest.TestCase):
    def test_single_open_frame(self):
        # Test with one open frame (e.g., knocking down 4 then 3 pins)
        rolls = [4, 3]
        frame_scores = calculate_frame_scores(rolls)
        self.assertEqual(frame_scores, [7])  # The frame score should be 7

if __name__ == '__main__':
    unittest.main()

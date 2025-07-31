import time
import random
import json
import os
from collections import defaultdict
import scripts.load_drills as load_drills

drill_names = [
    "home_row",
    "left_hand",
    "right_hand",
    "top_row",
    "bottom_row",
    "mixed"
]
target_text = load_drills.get_drill_text(random.choice(drill_names))


def compute_wpm(self):
    """
    Calculates the Words Per Minute (WPM) based on typed characters and duration.

    Returns:
        float: The calculated WPM, rounded to two decimal places. Returns 0.0 if not started/finished.
    """
    if self.start_time is None or self.end_time is None:
        return 0.0
    duration_sec = self.end_time - self.start_time
    num_chars = len(target_text)
    words = num_chars / 5  # Standard WPM calculation (5 characters per "word")
    return round(words / (duration_sec / 60), 2)
    
def compute_worst_chars(self):
    """
    Identifies the top 5 characters with the slowest average typing speed.

    This is based on the time taken to type each *correct* character.

    Returns:
        list: A list of tuples, each containing (character, average_delay_in_seconds).
                Sorted from slowest to fastest.
    """
    deltas = defaultdict(list)
    last_time = 0.0
    for entry in self.output_data:
        # Calculate the time taken for *this* character
        delta = entry['time'] - last_time
        deltas[entry['expected']].append(delta)
        last_time = entry['time']

    avg_times = {char: sum(times) / len(times) for char, times in deltas.items()}
    # Sort by slowest average time (descending order)
    sorted_chars = sorted(avg_times.items(), key=lambda x: -x[1])
    return sorted_chars[:5]  # Return top 5 slowest

def export_to_json(self):
    """
    Exports the entire typing session data to a JSON file.

    The file is named with a timestamp and saved in the current directory.

    Returns:
        str: The filepath of the exported JSON file.
    """
    data = {
        "text": target_text,
        "start_time": self.start_time,
        "end_time": self.end_time,
        "duration_sec": round(self.end_time - self.start_time, 4),
        "wpm": self.compute_wpm(),
        "slowest_chars": self.compute_worst_chars(),
        "keystrokes": self.output_data
    }
    # Ensure the directory exists (though current directory always exists)
    os.makedirs(".", exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(".", f"typing_session_{timestamp}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)  # Use indent for pretty-printing JSON
    return filepath

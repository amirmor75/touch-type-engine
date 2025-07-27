import random
from sklearn.datasets import fetch_20newsgroups


def create_texts():
    """
    Create a list of text documents for testing purposes.
    """
    data = fetch_20newsgroups(subset='train', categories=['sci.space', 'comp.graphics'])
    texts = data.data[:50]
    return texts


def create_drills(base_chars="asdf jkl;", min_len=3, max_len=6, count=10):
    """
    Generates pseudo-word typing drills from base characters.

    Args:
        base_chars (str): Characters to construct drills from.
        min_len (int): Minimum length of a drill string.
        max_len (int): Maximum length of a drill string.
        count (int): Number of drills to generate.

    Returns:
        list[str]: A list of generated typing drills.
    """
    drills = set()
    base_chars = base_chars.replace(" ", "")  # remove spaces for generation
    while len(drills) < count:
        length = random.randint(min_len, max_len)
        drill = ''.join(random.choices(base_chars, k=length))
        if not all(c == drill[0] for c in drill):  # avoid 'aaa', 'sss'
            drills.add(drill)
    return sorted(drills)


def generate_all_drills():
    """Generates all typing drills.

    Returns:
        dict[str, list[str]]: A dictionary mapping drill names to their corresponding texts.
    """
    return {
        "home_row": create_drills("asdf jkl;", count=20),
        "left_hand": create_drills("asdfg", count=20),
        "right_hand": create_drills("hjkl;", count=20),
        "top_row": create_drills("qwert yuiop", count=20),
        "bottom_row": create_drills("zxcvb nm,.", count=20),
        "mixed": create_drills("asdf jkl; qwer uiop zxcv nm,.", count=20),
    }

def get_random_paragraph():
    """
    Fetches a random paragraph from the 20 Newsgroups dataset.

    Returns:
        str: A random paragraph.
    """
    texts = create_texts()
    return random.choice(texts)

def get_drill_text(drill_name):
    """
    Returns a specific drill text based on the drill name.

    Args:
        drill_name (str): The name of the drill.

    Returns:
        str: The corresponding drill text.
    """
    drills = generate_all_drills()
    return f'{drill_name}:{drills.get(drill_name, [])}'
from collections import Counter

import pandas as pd


def get_heuristics(words_list):
    """
    A function to calculate heuristic given the list of words.
    The heuristics are calculated based on their frequency. h(x) is equal to max(frequencies)-frequency(word).
    Parameters
    ----------
    words_list: list

    Returns
    -------
    dict
        Dictionary with keys as words and values as heuristics.
    """
    heuristics_dict = Counter(words_list)
    categorize_counts = pd.DataFrame()
    counts = list(range(1, max(heuristics_dict.values()) + 1))
    categorize_counts["counts"] = counts
    categorize_counts["cost"] = counts[::-1]
    categorize_counts = categorize_counts.set_index("counts")["cost"].to_dict()
    for key, val in heuristics_dict.items():
        heuristics_dict[key] = categorize_counts[val]
    return heuristics_dict

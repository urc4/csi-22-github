def contains_all_characters(text, subtext):
    """Checks if characters in string subtext are in string text"""
    subtext_list = list(subtext)
    for char in text:
        while char in subtext_list:
            subtext_list.remove(char)

    return len(subtext_list) == 0


str = "palmeiras"
ystr = "amliaspalmeiras"

print(contains_all_characters(str, ystr))

def contains_characters(og_string, yg_string):
    yg_list = list(yg_string)
    for char in og_string:
        while char in yg_list:
            yg_list.remove(char)

    return len(yg_list) == 0


str = "palmeiras"
ystr = "amlias"

print(contains_characters(str, ystr))

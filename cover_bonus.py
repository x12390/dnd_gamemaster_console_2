def cover_calculation(cover_category):
    ret = 0
    if cover_category == "full":
        #volle Deckung, kein Angriff moeglich.
        ret = -1
    elif cover_category == "big":
        #3/4 Deckung
        ret = 5
    elif cover_category == "half":
        #1/2 Deckung
        ret = 2
    elif cover_category == "none":
        ret = 0
    else:
        #keine Deckung
        ret = 0

    return ret


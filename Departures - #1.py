def flap_display(lines, rotors):
    result = []
    for l,r in zip(lines,rotors):
        spun, line = 0, ""
        for c,n in zip(l,r):
            spun += n
            line += ALPHABET[(ALPHABET.index(c)+spun)%len(ALPHABET)]
        result.append(line)
    return result
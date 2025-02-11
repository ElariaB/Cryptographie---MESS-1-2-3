def decalage_caractere_plus_present(phrase):
    occurrences = {}

    for caractere in phrase:
        if caractere in occurrences:
            occurrences[caractere] += 1
        else:
            occurrences[caractere] = 1

    caractere_plus_present = max(occurrences, key=occurrences.get)

    print(" le plus présent :", caractere_plus_present)
    decalage = ord(' ') - ord(caractere_plus_present)
    print(decalage)
    phrase_decalee = ''
    for caractere in phrase:
        nouveau_code = ord(caractere) + decalage
        nouveau_caractere = chr(nouveau_code)
        phrase_decalee += nouveau_caractere
    print("Phrase décalée :", phrase_decalee)


phrase = """ōǰųŰŪŰŻŨŻŰŶŵźĵħŔŨŰźħŨŽŶżŶŵźħŸżŨŵūħŴǱŴŬħŸżŬħűżźŸżĮŰŪŰħŪĮǰŻŨŰŻħżŵħŷŬżħŻŹŶŷħŭŨŪŰųŬħŷŶżŹħŽŶżźĳħŵĮŬźŻĴŪŬħŷŨźħņħőŬħźŨŰźħŸżŬħŽŶżźħŨŻŻŬŵūŬƁħżŵħŽǰŹŰŻŨũųŬħūǰŭŰĵđđŉŶŵĳħŴŨŰŵŻŬŵŨŵŻħŸżŬħŽŶżźħŴŨŰŻŹŰźŬƁħųŬħūǰŪůŰŭŭŹŬŴŬŵŻħūżħŪŶūŬħūŬħŊǰźŨŹĳħŵŶżźħŨųųŶŵźħŵŶżźħŨŻŻŨŸżŬŹħǧħżŵħŷŹŶũųǯŴŬħűżźŻŬħżŵħũŹŰŵħŷųżźħūŰŭŭŰŪŰųŬĵħœŬħŴŬźźŨŮŬħźżŰŽŨŵŻħŨħǰŻǰħŪůŰŭŭŹǰħźŬųŶŵħųŬħŪŶūŬħūŬħŊǰźŨŹĳħŴŨŰźħŨŽŬŪħżŵŬħŷŬŻŰŻŬħŽŨŹŰŨŵŻŬħŷŶżŹħŪŶŹźŬŹħųŬźħŪůŶźŬźħŁħŪůŨŸżŬħŪŨŹŨŪŻǯŹŬħŬŵħŷŶźŰŻŰŶŵħŷŨŰŹŬħǰŻǰħŪůŰŭŭŹǰħŨŽŬŪħżŵŬħŪŬŹŻŨŰŵŬħŪųǰĳħŬŻħŪůŨŸżŬħŪŨŹŨŪŻǯŹŬħŬŵħŷŶźŰŻŰŶŵħŰŴŷŨŰŹŬħŨŽŬŪħżŵŬħźŬŪŶŵūŬħŪųǰħĨħŚŨżŹŬƁĴŽŶżźħŻŹŶżŽŬŹħųŬħŴŬźźŨŮŬħŶŹŰŮŰŵŨųħņđđĴĴđőŶǲų"""
decalage_caractere_plus_present(phrase)
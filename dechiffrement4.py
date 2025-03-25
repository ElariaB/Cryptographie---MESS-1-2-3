  def decalage_caractere_plus_present(phrase):
      occurrences_paire = {}
      occurrences_impaire = {}

      for i, caractere in enumerate(phrase):
          if i % 2 == 0:
              occurrences_paire[caractere] = occurrences_paire.get(caractere, 0) + 1
          else:
              occurrences_impaire[caractere] = occurrences_impaire.get(caractere, 0) + 1

      for i, caractere in enumerate(phrase):
          if i % 2 == 0:
              decalage = ord(' ') - ord(max(occurrences_paire, key=occurrences_paire.get))
          else:
              decalage = ord(' ') - ord(max(occurrences_impaire, key=occurrences_impaire.get))

          nouveau_code = (ord(caractere) + decalage) % 0x110000
          nouveau_caractere = chr(nouveau_code)
          print(nouveau_caractere, end='')
with open("message4.txt", "r", encoding="utf8") as fichier:
    phrase = fichier.read()


decalage_caractere_plus_present(phrase)

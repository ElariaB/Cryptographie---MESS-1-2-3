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


phrase = """*Jzi~w()(^w}{(i~m(lñkpqnnzñ(tm({mkwvl(um{{iom6^w}{(i}zm(xm}|5ò|zm(zmuizy}ñ(y}mty}m(kpw{m(liv{(tm(|m|m(y}m(~w}{(~mvm(lm(lñkpqnnzmz(B(tm({ujwtm(ixw{|zwxpm(ixxiziö|(|zð{({w}~mv|6(È(y}wq(kmti(m{|5qt(lă(è(~w|zm(i~q{(G(Kmti(kwv{|q|}m(}vm(niqjtm{{m(y}q(m{|(}vm(xwz|m(l/mv|zñm(xw}z(tm(kzx|ivit{|m6Ittm4(rm(~w}{(xzwxw{m(l/m{{imz(lm(lñkpqnnzmz(}v(i}|zm(|m|m4(|w}rw}z{({}z(tm(uòum(xzqvkqxm(l}(kwlm(lm(Kñ{iz6(Qt(v/m{|(~ziqumv|(xt}{(y}m{|qwv(lm(niqzm(tm(|zi~iqt(è(ti(uiqv6(Ïi(vm(lm~ziq|(xi{(~w}{(xw{mz(|zwx(lm(lqnnqk}t|ñ(lñ{wzuiq{655Rwót"""
decalage_caractere_plus_present(phrase)

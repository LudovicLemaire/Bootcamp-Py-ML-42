from generator import generator

txt = ' '.join([
    "Ich liebe dich",
    "Ich brauche dich",
    "Gib mir mehr",
    "Komm, fütter' mich",
    "Ich liebe dich",
    "Ich brauch' dich sehr",
    "Und mit Musik geht alles besser"])

print("\n\x1b[1;34;40mDefault\x1b[0m")
for word in generator(txt, sep="Ich"):
    print(word)

print("\n\x1b[1;34;40mUnique\x1b[0m")
for word in generator(txt, sep=" ", option="unique"):
    print(word)

print("\n\x1b[1;34;40mOrdered\x1b[0m")
for word in generator(txt, sep=" ", option="ordered"):
    print(word)

print("\n\x1b[1;34;40mShuffle\x1b[0m")
for word in generator(txt, sep=" ", option="shuffle"):
    print(word)
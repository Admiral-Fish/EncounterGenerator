from . import hgss, dp, pt

def create_encounters(text: bool):
    hgss.encounters(text)
    hgss.bug()
    hgss.headbutt()
    hgss.safari()

    dp.encounters(text)

    pt.encounters()

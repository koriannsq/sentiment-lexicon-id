POS = {'bagus', 'keren', 'mantap', 'suka', 'puas'}
NEG = {'jelek', 'kecewa', 'parah', 'buruk'}
def analyze(t: str) -> str:
    w = set(t.lower().split())
    p, n = len(w & POS), len(w & NEG)
    return 'positive' if p > n else 'negative' if n > p else 'neutral'

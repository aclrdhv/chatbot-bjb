from fuzzywuzzy import fuzz # type: ignore

def detect_intent(query):
    intents = {
        'greeting': ['halo', 'hai', 'hello'],
        'goodbye': ['bye', 'selamat tinggal', 'sampai jumpa', 'gak', 'tidak', 'engga', 'tidak ada', 'gaada', 'nggak ada'],
        'requirement': ['requirement', 'cara menggunakan', 'syarat'],
        'request_headers': ['request headers'],
        'signature_format': ['format signature', 'signature format'],
        'inquiry_balance': ['cek saldo', 'saldo', 'cek sald', 'balance', 'inquiry balance']
    }

    if len(query) < 3:
        return 'unknown'

    for intent, patterns in intents.items():
        for pattern in patterns:
            if fuzz.partial_ratio(query.lower(), pattern) > 80:
                return intent
    return 'unknown'
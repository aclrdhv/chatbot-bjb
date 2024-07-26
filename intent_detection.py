from fuzzywuzzy import fuzz # type: ignore

def detect_intent(query):
    intents = {
        'greeting': ['halo', 'hai', 'hello'],
        'goodbye': ['bye', 'selamat tinggal', 'sampai jumpa', 'gak', 'tidak', 'engga', 'tidak ada', 'gaada', 'nggak ada'],
        'requirement': ['requirement', 'cara menggunakan', 'syarat', 'diperlukan'],
        'request_headers': ['request headers'],
        'signature_format': ['format signature', 'signature format', 'tanda tangan'],
        'inquiry_balance': ['cek saldo', 'saldo', 'balance', 'inquiry balance'],
        'transaction_history': ['transaction history', 'riwayat transaksi', 'transaksi', 'riwayat', 'history'],
        'account_internal': ['internal account', 'account internal', 'internal'],
        'account_external': ['external account', 'account external', 'eksternal'],
        'overbooking': ['overbooking'],
        'transfer_online': ['transfer online'],
        'card_registration': ['card registration', 'registrasi kartu', 'debit'],
        'payment': ['payment', 'pembayaran'],
        'validate_otp': ['validate', 'otp', 'validasi']
    }

    if len(query) < 3:
        return 'unknown'

    for intent, patterns in intents.items():
        for pattern in patterns:
            if fuzz.partial_ratio(query.lower(), pattern) > 80:
                return intent
    return 'unknown'
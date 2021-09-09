import hashlib
import pyotp
from avanza import Avanza

totp = pyotp.TOTP('MY_TOTP_SECRET', digest=hashlib.sha1)
print(totp.now())


avanza = Avanza({
    'username': 'MY_USERNAME',
    'password': 'MY_PASSWORD',
    'totpSecret': 'MY_TOTP_SECRET'
})

overview = avanza.get_overview()
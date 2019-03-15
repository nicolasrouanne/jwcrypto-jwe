from pprint import pprint
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode

public_key_dict = {"alg": "RSA-OAEP",
                   "e": "AQAB",
                   "kid": "rsa-5ofWP09ChW4qop6P43XbF7_F2PnEJ7_hBhXAarwQfnQ",
                   "kty": "RSA",
                   "n": "pZsjTGAeeIV4uvHvFj1U3Pry5RF26MdCYGNUVVr5XJLEuWE0wAe7TBzR-QcOpH0fpo1nK6sf3AYWjJVHSEZWX2v_v7MlyPOihcoy95LEOTpILa3arzMRPuxJD9tuF999VZkRtqNjDlEDCO_tKA0WizhxXtwx7SmuooU93M5JSkw5R-1GslF76J_Lx-bXc6u7zk77ImtLipS6NghRjMYOgsQwZ0mCNWSjq-IdsnGNyYuWrH9IBXXy3cZ8B8bnwQ1LzTepBq2Ai5lkotUuRIkY2Jj0CDkGEDTKjh5rfuprYT0luRy7E15l3UGLUpQ5L4t90vjpMd9JO2sF657H-QleNQ",
                   "use": "enc"
                   }

public_key = jwk.JWK(**public_key_dict)
payload = "My Encrypted message"
protected_header = {
    "alg": "RSA-OAEP",
    "enc": "A256GCM",
    "kid": public_key.thumbprint(),
}
jwetoken = jwe.JWE(payload.encode('utf-8'),
                   recipient=public_key,
                   protected=protected_header)
enc_JSON = jwetoken.serialize()
enc = jwetoken.serialize(compact=True)
print("JSON:\n", enc_JSON, "\n")
print("Compact:\n", enc)

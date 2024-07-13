import datetime
from typing import Optional, Dict, Any, List

import jwt as jwt_original_lib
import pytz

def encode(payload: Dict[str, Any], secret: str, algorithm: str, expiration: Optional[int] = None, **kwargs) -> str:

    if expiration:
        payload['exp'] = datetime.datetime.now(tz=pytz.UTC) + datetime.timedelta(seconds=expiration)
    payload.update(kwargs)
    token = jwt_original_lib.encode(payload, secret, algorithm=algorithm)
    return token

def decode(token: str, secret: str, algorithms: Optional[List[str]] = None, verify: bool = True, **kwargs) -> Dict[str, Any]:
    try:
        decoded = jwt_original_lib.decode(token, secret, algorithms=algorithms, options={'verify_signature': verify}, **kwargs)
        return decoded
    except jwt_original_lib.exceptions.ExpiredSignatureError:
        raise jwt_original_lib.exceptions.ExpiredSignatureError("The token has expired.")
    except jwt_original_lib.exceptions.InvalidTokenError as e:
        raise jwt_original_lib.exceptions.InvalidTokenError(f"Invalid token: {str(e)}")

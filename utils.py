from functools import wraps
from flask import request
from models import Token

# this decorator takes email and token from headers and verifies before letting user enter into route...
def user_auth(f):
    def decorated(self):
        email = request.headers.get('email')
        token = request.headers.get('token')
        if not email or not token:
            return {"error": "Token and email required in headers"}, 400
        email_token = Token.query.filter_by(email=email).first()
        if not email_token:
            return {'error':'Email Not Found!'}, 400
        # print(f"Header token: {token} (type: {type(token)})")
        # print(f"DB token: {email_token.token} (type: {type(email_token.token)})")
        if token == str(email_token.token):
            print("Done Returning Values!")
            print(f"/{email}/")
            return f(self, email)
        return {"error": "Invalid Token!"}, 401
    return decorated
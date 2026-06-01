Python
class AuthMiddleware:

    def validate(self,token):

        if token:

            return True

        return False

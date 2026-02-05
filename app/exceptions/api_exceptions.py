class ApiException(Exception):
    status_code = 400

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BadRequestException(ApiException):
    status_code = 400

class InvalidFilterException(ApiException):
    status_code = 400
        
class InvalidSortException(ApiException):
   status_code = 400

class UnauthorizedException(ApiException):
    status_code = 401


class NotFoundException(ApiException):
    status_code = 404


class VoterxBaseExceptions(Exception):
    default_detail = 'Unknown Error'

    def __init__(self, detail=None, status_code=400):
        if detail is not None:
            self.detail = detail
        else:
            self.detail = self.default_detail
        self.status_code = status_code


class MethodNotImplementedError(VoterxBaseExceptions):
    default_detail = 'Method Not Implemented Error'


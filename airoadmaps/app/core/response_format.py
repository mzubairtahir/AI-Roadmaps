from abc import ABC, abstractmethod

class ResponseFormatBase(ABC):
    
    def __init__(self) -> None:
        pass
    
    
    @abstractmethod
    def to_dict(self):
        pass
    
    
    
class ErrorResponseFormat(ResponseFormatBase):

    def __init__(self, status, message) -> None:
        self.status = status
        self.message = message

    
    def to_dict(self):
        return {
            "error":{
                "status":self.status,
                "message":self.message
            }
        }
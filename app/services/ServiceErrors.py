# app/services/ServiceErrors.py

# exceptions.py

class ServiceException(Exception):
    """Classe base para todas as exceções customizadas dos serviços"""
    def __init__(self, message: str, status_code: int = 400, 
                 payload: dict | None = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

    def to_dict(self):
        """Converte a exceção em um dicionário."""
        rv = dict(self.payload)
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv

class UserCreationException(ServiceException):
    """Erro em criação de novos usuários"""
    pass

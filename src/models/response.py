from pydantic import BaseModel

class Value(BaseModel):
    value: str | int


def response_Value(val: str | int ) -> dict:

    value = Value(
        value = val
    )

    return value.dict()


class Custom(BaseModel):
    code: int       # codigo http 200, 400, 500, etc.
    state: int      # estado 1 -> Exitosa, 2 -> Exitosa pero basia para los modelos, 3 -> Fallida para trabajar con codigos http diferente de 200
    message: str    

def response_Custom(message: str, code: int = 200, state: int = 1,  ) -> dict:

    custom = Custom(
        code = code,
        state = state,
        message = message
    )

    return custom.dict()


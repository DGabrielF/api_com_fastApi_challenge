from typing import Annotated
from pydantic import UUID4, Field, PositiveFloat

from contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome de categoria", example="Scale", max_length=10)
    ]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador")]

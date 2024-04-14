from typing import Annotated
from pydantic import UUID4, Field, PositiveFloat

from contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do centro de treinamento", example="CT Fight Club", max_length=30)
    ]
    endereco: Annotated[
        str, Field(description="Endereço do centro de treinamento", example="rua X, 13", max_length=60)
    ]
    proprietario: Annotated[str, Field(description="Proprietário do centro de treinamento", example="Marcelo")]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do centro de treinamento", example="CT Fight Club", max_length=30)
    ]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador")]
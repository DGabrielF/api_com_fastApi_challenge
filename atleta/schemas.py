from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from categorias.schemas import CategoriaIn
from centro_treinamento.schemas import CentroTreinamentoAtleta
from contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="Chuck", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="CPF do atleta", example="11111111111", max_length=11)
    ]
    idade: Annotated[int, Field(description="Idade do atleta", example="19")]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=72.3)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do atleta", example=1.76)
    ]
    genero: Annotated[
        str, Field(description="genero do atleta", example="M", max_length=1)
    ]
    categoria: Annotated[
        CategoriaIn,
        Field(description="Categoria do atleta", example="Scale", max_length=11),
    ]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta,
        Field(
            description="Centro de treinamento do atleta",
            example="Scale",
            max_length=11,
        ),
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


class AtletaUpdate(BaseSchema):
    idade: Annotated[
        Optional[str],
        Field(None, description="Idade do atleta", example="João", max_length=50),
    ]
    peso: Annotated[
        Optional[PositiveFloat], Field(None, description="Peso do atleta", example=72.3)
    ]
    categoria: Annotated[
        Optional[CategoriaIn],
        Field(None, description="Categoria do atleta", example="Scale", max_length=11),
    ]
    centro_treinamento: Annotated[
        Optional[CentroTreinamentoAtleta],
        Field(
            None,
            description="Centro de treinamento do atleta",
            example="Scale",
            max_length=11,
        ),
    ]

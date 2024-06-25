from typing import Annotated

from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Queen', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Rua y, Q05', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do centro de treinamento', example='R2-D2', max_length=30)]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Centro de treinamento', example='MLB Gym', max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]    
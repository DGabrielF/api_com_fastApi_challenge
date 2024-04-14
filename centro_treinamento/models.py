from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from contrib.models import BaseModel
from atleta.models import AtletaModel


class CentroTreinamentoModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[int] = mapped_column(String(50),unique=True , nullable=False)
    endereco: Mapped[int] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[int] = mapped_column(String(30), nullable=False)
    atleta: Mapped["AtletaModel"] = relationship(back_populates="centro_treinamento")


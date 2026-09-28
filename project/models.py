from sqlmodel import Field, Relationship, SQLModel
from typing import List

class Oficina(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    direccion: str| None = Field(default=None)    
    
    persona: List["Persona"] = Relationship(back_populates="oficina")
    
class Persona(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    edad: int | None = Field(default=None)
    puesto: str = Field(index=True)
    
    oficina_id: int | None = Field(default=None, foreign_key="oficina.id")
    oficina: Oficina| None = Relationship(back_populates="persona")
    

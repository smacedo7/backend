from pydantic import BaseModel


class EstudanteBase(BaseModel):
    nome: str
    age: int


class EstudanteCreate(EstudanteBase):
    pass


class EstudanteResponse(EstudanteBase):
    id: int

    class Config:
        from_attributes = True


class MatriculaBase(BaseModel):
    student_id: int
    nome_disciplina = str


class CreateMatricula(MatriculaBase):
    pass


class MatriculaResponse(MatriculaBase):
    id: int

    class Config:
        from_atributtes = True

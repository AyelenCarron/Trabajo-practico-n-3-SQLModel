from sqlmodel import Session
from .database import create_db_and_tables, engine
from .models import Persona, Oficina

def create_persona():
    with Session(engine) as session:
        
        oficina_administracion= Oficina(name="Administracion",direccion= "San Martin 778 ")
        oficina_ventas= Oficina(name="Ventas", direccion= "25 de Mayo 200")
        oficina_rrhh= Oficina(name="RRHH", direccion= "9 de Julio 430")
                                        
        session.add(oficina_administracion)
        session.add(oficina_ventas)
        session.add(oficina_rrhh)
        
        session.commit()
        session.refresh(oficina_administracion)
        session.refresh(oficina_ventas)
        session.refresh(oficina_rrhh)
        

        persona_adm = Persona(name= "Juan Perez", oficina= oficina_administracion)
        persona_vta = Persona(name= "Viviana Olivera", oficina= oficina_ventas)
        persona_rh = Persona(name= "Paola Mejia", oficina= oficina_rrhh)
        
        session.add(persona_adm)
        session.add(persona_vta)
        session.add(persona_rh)
        
        session.commit()
        session.refresh(persona_adm)
        session.refresh(persona_vta)
        session.refresh(persona_rh)

        print("Created person:", persona_adm)
        print("Lista de personas", persona_adm.oficina)


def main():
    create_db_and_tables()
    create_persona()


if __name__ == "__main__":
    main()


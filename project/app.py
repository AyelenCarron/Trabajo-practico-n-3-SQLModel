from sqlmodel import Session, select
from .database import create_db_and_tables, engine
from .models import Persona, Oficina

def create_oficina():
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
        
    print("Oficinas creadas:", oficina_administracion, oficina_ventas, oficina_rrhh)

def create_persona():
    with Session(engine) as session:
        oficina_administracion= session.exec(select(Oficina).where(Oficina.name == "Administracion")).first()
        oficina_ventas= session.exec(select(Oficina).where(Oficina.name == "Ventas")).first()
        oficina_rrhh= session.exec(select(Oficina).where(Oficina.name == "RRHH")).first()
        
        persona_adm = Persona(name= "Juan Perez", edad = 35, puesto= "Contador", oficina= oficina_administracion)
        persona_vta = Persona(name= "Viviana Olivera", edad = 37, puesto= "Gerente de ventas", oficina= oficina_ventas)
        persona_rh = Persona(name= "Paola Mejia", edad = 31, puesto= "Analista de RRHH",oficina= oficina_rrhh)
        
        session.add(persona_adm)
        session.add(persona_vta)
        session.add(persona_rh)
        
        session.commit()
        session.refresh(persona_adm)
        session.refresh(persona_vta)
        session.refresh(persona_rh)
    print("Personas creadas:", persona_adm, persona_vta, persona_rh)


def select_personas_por_oficina(oficina_name: str):
    with Session(engine) as session:
        statement = select(Persona).join(Oficina).where(Oficina.name == oficina_name)
        personas = session.exec(statement).all()
        
        if not personas:
            print(f"No se encontraron personas registradas en la oficina '{oficina_name}'")
            return
        
        print(f"Personas encontradas en la oficina '{oficina_name}': ")
        for persona in personas:
            print(f"{persona.name}")



def select_personas_por_puesto(puesto_name: str):
    with Session(engine) as session:
        statement = select(Persona).where(Persona.puesto == puesto_name)
        personas = session.exec(statement).all()
        if not personas:
            print(f" No se encontró ninguna persona con el puesto '{puesto_name}'.\n")
            return
        print(f"Resultados de búsqueda para el puesto '{puesto_name}':")
        for persona in personas:
            print(f" - ID: {persona.id} | Nombre: {persona.name} | Edad: {persona.edad}")


def update_persona_oficina(persona_name: str, nueva_oficina: str):
    with Session(engine) as session:
        
        persona = session.exec(select(Persona).where(Persona.name == persona_name)).first()
        if not persona:
            print(f" No se encontró la persona '{persona_name}'")
            return
        
        nueva_oficina = session.exec(select(Oficina).where(Oficina.name == nueva_oficina)).first()
        if not nueva_oficina:
            print(f"No se encontró la oficina '{nueva_oficina}'")
            return
        
        persona.oficina = nueva_oficina 
        session.add(persona)
        session.commit()
        session.refresh(persona)
        
        print(f"'{persona.name}' ha sido reasignado/a con éxito a la oficina '{nueva_oficina.name}'")


def delete_persona(persona_name: str):
    with Session(engine) as session:
        persona = session.exec(select(Persona).where(Persona.name == persona_name)).first()
        if not persona:
            print(f"No se encontró la persona '{persona_name}' para eliminar.")
            return
        
        session.delete(persona)
        session.commit()
        print(f"Persona '{persona_name}' eliminada correctamente.")


def main():
    create_db_and_tables()
    create_oficina()
    create_persona()
    
    select_personas_por_oficina("Administracion")
    select_personas_por_puesto("Contador")
    
    update_persona_oficina("Juan Perez", "Ventas")
    
    delete_persona("Paola Mejia")
    


if __name__ == "__main__":
    main()


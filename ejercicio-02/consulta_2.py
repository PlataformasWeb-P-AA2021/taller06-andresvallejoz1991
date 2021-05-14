from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_base import Paises 

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///basepersonas.db')


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad docentes 
asia = session.query(Paises).all()


# Obtener todos los registros de 
# la tabla docentes que tengan como valor en 
# el atributo especifico 
asia_dos = session.query(Paises).filter(Paises.continente=="AS").order_by(Paises.dial).all()
print(asia_dos)

print("--------------------------------")

from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepersonas.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)

    def __repr__(self):
        return "Paises: nombre_pais: %s capital: %s continente: %s dial: %s geoname: %s itu: %s lenguajes: %s independiente: %s" % (
                          self.nombre_pais, 
                          self.capital, 
                          self.continente,
                          self.dial,
                          self.geoname,
                          self.itu,
                          self.lenguajes,
                          self.independiente)


Base.metadata.create_all(engine)


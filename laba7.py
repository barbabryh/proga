from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Определение базы
Base = declarative_base()

# Таблица Species (виды животных)
class Species(Base):
    __tablename__ = "species" 
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Таблица Animal (животные)
class Animal(Base):
    __tablename__ = "animals"  
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    species_id = Column(Integer, ForeignKey("species.id"))

# Подключение к базе данных SQLite

engine = create_engine("sqlite:///proga.db")  
# Создание таблиц
Base.metadata.create_all(engine)

# Сессия для работы с данными
Session = sessionmaker(bind=engine)
session = Session()


# Добавляем вид животного и животное
species = Species(name="Dogs")
session.add(species)
session.commit()

animal = Animal(name="Bobik", age=3, species_id=species.id)
session.add(animal)
session.commit()

# Чтение данных
species_list = session.query(Species).all()
for sp in species_list:
    print(f"Species: {sp.name}")

animals = session.query(Animal).all()
for anim in animals:
    print(f"Animal: {anim.name}, Age: {anim.age}, Species: {anim.species_id}")

# Обновляем данные (возраст животного)
animal = session.query(Animal).filter_by(name="Bobik").first()
if animal:
    animal.age = 4  
    session.commit()

# Удаляем данные (удаляем вид и животное)
species = session.query(Species).filter_by(name="Dogs").first()
if species:
    session.delete(species)  
    session.commit()


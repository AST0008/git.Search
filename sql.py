from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Set up the base class for declarative class definitions
Base = declarative_base()

# Define the MainString table
class MainString(Base):
    __tablename__ = 'main_string'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_string = Column(String, nullable=False)
    
    # One-to-many relationship with StringArray
    string_array = relationship("StringArray", back_populates="main_string", cascade="all, delete-orphan")

# Define the StringArray table
class StringArray(Base):
    __tablename__ = 'string_array'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_string_id = Column(Integer, ForeignKey('main_string.id', ondelete="CASCADE"))
    array_element = Column(String, nullable=False)
    
    # Many-to-one relationship with MainString
    main_string = relationship("MainString", back_populates="string_array")

# Create a SQLite engine
engine = create_engine('sqlite:///strings.db')

# Create the tables
Base.metadata.create_all(engine)

# Set up session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a MainString and its array elements
def add_main_string_with_array(main_string_value, array_elements):
    # Create a new MainString object
    main_string = MainString(main_string=main_string_value)
    
    # Add string array elements
    for element in array_elements:
        string_array_item = StringArray(array_element=element)
        main_string.string_array.append(string_array_item)
    
    # Add to session and commit
    session.add(main_string)
    session.commit()

# Example usage
# add_main_string_with_array("Example String", ["element1", "element2", "element3"])

# Querying the database
def get_main_strings():
    return session.query(MainString).all()

# main_strings = get_main_strings()
# for ms in main_strings:
#     print(f"Main String: {ms.main_string}")
#     for element in ms.string_array:
#         print(f"  Array Element: {element.array_element}")

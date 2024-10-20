from sqlalchemy import create_engine, Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class WeatherSummary(Base):
    __tablename__ = 'weather_summary'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    average_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    dominant_condition = Column(String)


def setup_database():
    engine = create_engine('sqlite:///weather.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


Session = setup_database()
session = Session()

class DatabaseService:
    def __init__(self, db_uri='sqlite:///lineage_data.db'):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        from sqlalchemy import Column, Integer, String, Table, MetaData

        metadata = MetaData()

        self.lineage_table = Table('lineage', metadata,
            Column('id', Integer, primary_key=True),
            Column('source', String),
            Column('destination', String),
            Column('transformation', String)
        )

        metadata.create_all(self.engine)

    def add_lineage_record(self, source, destination, transformation):
        session = self.Session()
        try:
            session.execute(self.lineage_table.insert().values(
                source=source,
                destination=destination,
                transformation=transformation
            ))
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_lineage_records(self):
        session = self.Session()
        try:
            result = session.execute(self.lineage_table.select()).fetchall()
            return result
        finally:
            session.close()
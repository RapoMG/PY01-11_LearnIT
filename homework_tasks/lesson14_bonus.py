"""Convert csv to DB"""

from dataclasses import dataclass,field
import csv
import sqlite3

@dataclass
class CSVtoDB:
    csv_name : str
    db_name: str
    table_name: str
    delimiter: str = ","
    columns_names: str = field(init=False, default="")

    # add test if strings aren't empty

    def read_csv(self):
        """Reads CSV file line by line. Calls DB methods"""
        header_read = True
        header_types = True
        data_types = []

        with open(self.csv_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=self.delimiter)
            for line in reader:
                # prepare header
                if header_read:
                    header = line  # save header before assigment
                    header_read = False
                    continue
                if header_types:
                    data_types = self.prepare_header_types(line)
                    header_types = False
                    self.create_table(header, data_types)

                self.populate_table(line)

    def prepare_header_types(self, record: list[str]) -> list[str]:
        data_types = []

        for data in record:
            # All numbers go as float
            if data.replace("-", "", 1).replace(".", "", 1).isdigit():
                data_types.append("REAL")
                continue
                
            # Everything else is text
            data_types.append("TEXT")
        
        return data_types

    def validate_name(self, name: str):
       name = name.replace("'","").replace('"', "").strip().replace(" ","_")
       return f"'{name}'"

    def create_table(self, header: list[str], types: list[str]):
        table = self.validate_name(self.table_name)
    
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        # List of columns
        columns_names = []  # columns names 
        columns_sql = []  # part of command
        for name, type_ in zip(header, types):
            col = self.validate_name(name.lower())  # validate name
            columns_names.append(col)  # columns names list
            columns_sql.append(f'{col} {type_}')  # 'name' TYPE

        all_col = ", ".join(columns_sql)  # join commands into sequence

        self.columns_names =  ", ".join(columns_names)  # columns names as one string to future use

        # full command
        create = f"""
        CREATE TABLE IF NOT EXISTS {table} (
            {all_col}
        )
        """
        
        c.execute(create)
        
        conn.commit()
        conn.close()

    def populate_table(self, record: list):
        table = self.validate_name(self.table_name)
        columns = self.columns_names

        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        # markers 
        markers_pt1 = "?, " * (len(record)-1)  #what about missing data?
        markers_pt2 = f"{markers_pt1}?"
        
        c.execute(f"INSERT INTO {table} ({columns}) VALUES ({markers_pt2})", (record))

        conn.commit()
        conn.close()

    def read_table(self):
        """Just for test if it's working"""
        table = self.validate_name(self.table_name)
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute(f"SELECT * FROM {table}")

        records = c.fetchall()

        for record in records:
            print(record)
        
        conn.close()


class_ = CSVtoDB("customers-100.csv","_cust.db","cust_table")
class_.read_csv()
class_.read_table()

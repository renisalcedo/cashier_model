class Employee:
    def __init__(self, db):
        """ Employee Class for handling Employee data
        :type db: SQL instance
        """
        self.db = db
        self.cursor = db.cursor()
        self.table = "EMPLOYEE"
        self.table_cols = (self.table, "FIRSTNAME", "USERNAME", "PASSWORD")

    def new(self, name, username, password):
        """ Creates a new Employee with provided data
        :type name: str
        :type username: str
        :type password: str
        """
        data = (name, username, password)
        self.cursor.execute('INSERT INTO {0[0]} ({0[1]}, {0[2]}, {0[3]}) \
                            VALUES (\"{1[0]}\", \"{1[1]}\", \"{1[2]}\")'.format(self.table_cols, data))

    def delete(self, id):
        """ Will delete an Employee from the database
        :type id: int
        """
        sql = 'DELETE FROM {0[0]} WHERE ID = {0[1]}'
        data = (self.table, id)

        self.cursor.execute(sql.format(data))

    def update(self, id, data):
        """ Will update an Employee in the database
        :type id: int
        :type data: Tuple(str)
        """
        sql = 'UPDATE {0[0]} SET {0[1]} = {2[0]}, \
              {0[2]} = {2[1]}, {0[3]} = {2[2]} WHERE ID = {1[1]}'

        self.cursor.execute(sql.format(self.table_cols, id, data))

    def get_by_id(self, id):
        """ Will return an Employee from the database
        :type id: int
        :rtype data: dict(int, str)
        """
        sql = 'SELECT * FROM {0} WHERE ID = {1}'
        self.cursor.execute(sql.format(self.table, id))
        data = self.cursor.fetchall()

        if data:
            _,name,username,password = data[0]
            return {'firstname':name, 'username': username, 'password': password}

        return {'Error':'ID NOT FOUND'}

    def get_by_username(self, username):
        """ Will return an Employee from the database
        :type username: str
        :rtype data: dict(int, str)
        """
        sql = 'SELECT * FROM {0} WHERE USERNAME = \"{1}\"'
        self.cursor.execute(sql.format(self.table, username))
        data = self.cursor.fetchall()

        if data:
            _,name,username,password = data[0]
            return {'firstname':name, 'username': username, 'password': password}

        return {'Error':'USERNAME NOT FOUND'}

    def save(self):
        """ Will save the employee created and return how many were created
        :rtype data: dict(int)
        """
        self.db.commit()
        return {'users': self.cursor.rowcount }
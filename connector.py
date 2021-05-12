import pypyodbc

class Connector:
    def __init__(self, database_url):
        conn = pypyodbc.connect(database_url)
        self.cursor = conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        if len(res) == 1:
            res = "".join(str(x) for x in res).replace("(", "").replace(")", "")
            res = res[:-2]
        else:
            res = "".join(str(x) for x in res)

        return res
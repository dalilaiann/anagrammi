from zipfile import structEndArchive64

from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def check_parola(parola: str) -> bool:
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM parola WHERE nome=%s """


        cursor.execute(query, (parola, ))

        results=cursor.fetchall()

        cursor.close()
        conn.close()

        if len(results)>0:
            return True
        else:
            return False

    @staticmethod
    def check_prefisso(parola: str) -> bool:
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from parola
                    where INSTR(nome, %s)>0"""

        cursor.execute(query, (parola,) )

        results = cursor.fetchall()

        cursor.close()
        conn.close()

        if len(results) > 0:
            return True
        else:
            return False




if __name__=="__main__":
    myDAO=DAO()
    print (myDAO.check_prefisso("cas"))




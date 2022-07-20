import psycopg2
from datetime import datetime

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            host="postgres",
            database="terminal_db",
            user="terminal_user",
            password="terminal")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute("""
            INSERT INTO transactions 
            (
                user_id, ts, transaction_amount
            )
            VALUES (33, '2022-06-03 03:33:33', 3333);
        """)


        # commit the changes to the database
        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

        time_stamp = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")

        print(time_stamp + ' Job completed')


if __name__ == '__main__':
    connect()

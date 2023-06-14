import mysql.connector

def run_sql_script(filename):
    with open(filename, 'r', encoding="utf-16") as sql_file:
        sql_script = sql_file.read()

    cnx = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='spotifyDataset'
    )

    cursor = cnx.cursor()
    try:
        index = 0
        sql_commands = sql_script.split(';')
        for command in sql_commands:
            if command.strip():
                cursor.execute(command)
                index += 1
                if(index % 1000 == 0):
                    print(index)
 
        cnx.commit()    

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        cursor.close()
        cnx.close()

print("Running sql scripts...")
#run_sql_script('data/spotify_songs.sql')

print("Running sql scripts 2...")
run_sql_script('data/spotify_songs_single_table.sql')
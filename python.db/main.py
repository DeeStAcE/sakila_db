from psycopg2 import connect, OperationalError, sql, DatabaseError

try:
    cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='postgres')
    cursor = cnx.cursor()
    print('CONNECTED')
except OperationalError as error:
    print('CONNECTION ERROR')
    raise ValueError(f'Connection error: {error}')

query_create_table_user = sql.SQL('''
    CREATE table IF NOT EXISTS {table_name} (
        ID SERIAL,
        name VARCHAR(50),
        email VARCHAR(120) UNIQUE,
        password VARCHAR(60) DEFAULT 'password',
        PRIMARY KEY (ID)
    );
''').format(table_name=sql.Identifier('User'))

query_insert_user = sql.SQL('''
    INSERT INTO {table_name} (name, email, password, price)
    VALUES (%s, %s, %s, %s);
''').format(table_name=sql.Identifier('User'))

query_update = sql.SQL('''
    UPDATE {table_name}
    SET email = %s
    WHERE ID = %s;
''').format(table_name=sql.Identifier('User'))

query_delete = sql.SQL('''
    DELETE
    FROM {table_name}
    WHERE id = %s;
''').format(table_name=sql.Identifier('User'))

query_create_table_address = sql.SQL('''
    CREATE table IF NOT EXISTS {table_name} (
        ID SERIAL PRIMARY KEY,
        street VARCHAR(85),
        city VARCHAR(85),
        notes TEXT,
        user_id SMALLINT,
        FOREIGN KEY (user_id) REFERENCES {foreign_table_name} (ID)
    );
''').format(table_name=sql.Identifier('Address'), foreign_table_name=sql.Identifier('User'))

query_alter = sql.SQL('''
    ALTER TABLE {table_name} ADD COLUMN price DECIMAL(7, 2) DEFAULT 0
''').format(table_name=sql.Identifier('User'))

query_alter2 = sql.SQL('''
    ALTER TABLE {table_name} ADD COLUMN dateOfCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
''').format(table_name=sql.Identifier('User'))

with cnx:
    # try:
    #     cursor.execute(query_create_table_user)
    #     cursor.execute(query_create_table_address)
    # except DatabaseError as error:
    #     print(error)
    try:
        cursor.execute(query_insert_user, ('Janusz', 'janusz2@wp.pl', 'haslo123', 21.37))
    except DatabaseError as error:
        print(error)
    # try:
    #     cursor.execute(query_update, ('janusz@onet.pl', 1))
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_delete, (1,))
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_alter)
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_alter2)
    # except DatabaseError as error:
    #     print(error)

cnx.close()

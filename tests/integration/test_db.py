import psycopg2


def test_connection():
    conn = psycopg2.connect(
        host='db',
        user='postgres',
        dbname='postgres',
    )
    cur = conn.cursor()
    cur.execute('''
    SELECT table_schema, table_name
    FROM information_schema.tables
    WHERE table_schema = 'information_schema'
    AND table_name = 'tables'
    ''')
    results = cur.fetchall()
    assert len(results) == 1
    assert results[0] == ('information_schema', 'tables')

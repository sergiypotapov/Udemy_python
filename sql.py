import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, SKILL TEXT)")

def insert_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Jun')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Mid')")
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Expert')")
    conn.commit()

def dynamic_data():
    lang = input("what is lang? ")
    version = input("what version? ")
    skill = input("Skill? ")

    c.execute("INSERT INTO example (Language, Version, Skill ) VALUES(?, ?, ?)", (lang, version, skill))
    conn.commit()

def select():
    lang = input("what is lang? ")
    skill = input("What skill? ")
    sql = "SELECT * FROM example WHERE Language = ? AND Skill = ? "
    for row in c.execute(sql, [(lang), (skill)]):
        print(row)

#dynamic_data()
select()
#insert_data()
#conn.close()
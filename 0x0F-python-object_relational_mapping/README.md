# Python - Object-Relational Mapping

In this project, I will be linking to amazing world: Databases and Python! In the first part, I will use the MySQLdb module to connect to a MySQL database and
execute SQL queries, and in the second part I will use the SQLAlchemy that is an **Object Relational Mapper (ORM)**.

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, my biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. I won’t write any SQL queries only Python code. Last thing, I code won’t be “storage type” dependent. I will be able to change your storage easily without re-writing my entire project.

![ORM Python](https://miro.medium.com/max/640/0*3uedj0JV8LWYNc8Q)

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

try:
    import psycopg2
except psycopg2.DatabaseError:
    print("AN ERROR OCCOURRED WHILE IMPORTING PSYCOPG2") #TO HELP YOU DEBUG


try:
    # CONEXÃO 
    global con, cur
    con = psycopg2.connect(host="localhost", database="YOUR DATABASE", user="YOUR USER", password="YOUR PASSWORD")
    cur = con.cursor()
    print("CONNECTED WITH DATABASE!")
except:
    print("NOT CONNETED WITH DATABASE!")
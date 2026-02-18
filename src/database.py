import sqlite3

PATH_DB = "data/crypto_news.db"

# This function creates the empty table
def init_db():
    con = sqlite3.connect(PATH_DB) #create connection with the database on disk
    cur = con.cursor()  #create a cursor to fill the database with the data
    cur.execute("""CREATE TABLE IF NOT EXISTS news (id_news INTEGER PRIMARY KEY AUTOINCREMENT,
                                   title TEXT, 
                                   link TEXT UNIQUE, 
                                   published TEXT, 
                                   sentiment REAL)""")
    con.commit()  #save the operation
    con.close()    #close the connection with the database


#This function save each news in the db, avoiding duplicates
def save_news(news_list):
    con = sqlite3.connect(PATH_DB)
    cur = con.cursor()
    for news in news_list:

        try:
            cur.execute("INSERT INTO news (title,link,published,sentiment) VALUES (?,?,?,?)", (news['title'],news['link'],news['published'],news['sentiment']))
        
        except sqlite3.IntegrityError:
            pass

    con.commit()
    con.close()

#TESTING

if __name__ == "__main__":
    init_db()
    # 2. Creiamo una lista di notizie "finte" per il test
    # Nota: Usiamo le stesse chiavi che si aspetta la tua funzione save_news
    test_list = [
        {
            "title": "Bitcoin sale alle stelle",
            "link": "https://esempio.com/news-1",
            "published": "Tue, 18 Feb 2024 10:00:00 GMT",
            "sentiment": 0.85
        },
        {
            "title": "Crypto in calo",
            "link": "https://esempio.com/news-2",
            "published": "Tue, 18 Feb 2024 11:00:00 GMT",
            "sentiment": -0.4
        }
    ]

    print("--- PRIMO TENTATIVO DI SALVATAGGIO ---")
    save_news(test_list)
    print("Salvataggio completato (se non vedi errori sopra).")

    # 3. Verifichiamo cosa c'è dentro il database
    con = sqlite3.connect(PATH_DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM news")
    articoli = cur.fetchall()
    
    print(f"\nNel database ci sono {len(articoli)} articoli:")
    for art in articoli:
        print(art)

    print("\n--- SECONDO TENTATIVO (TEST DUPLICATI) ---")
    # Proviamo a salvare di nuovo la STESSA lista.
    # Se il try/except funziona, non deve succedere nulla e non devono aumentare le righe.
    save_news(test_list)
    
    cur.execute("SELECT count(*) FROM news")
    conteggio = cur.fetchone()[0]
    print(f"Numero totale articoli dopo il secondo tentativo: {conteggio}")
    
    if conteggio == 2:
        print("TEST SUPERATO: I duplicati sono stati ignorati!")
    else:
        print(f"TEST FALLITO: Ci sono {conteggio} righe invece di 2.")

    con.close()
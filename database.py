import os
import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_connection():
    return psycopg.connect(DATABASE_URL)

def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS commandes (
                    id SERIAL PRIMARY KEY,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telephone TEXT NOT NULL,
                    adresse TEXT NOT NULL,
                    produit TEXT NOT NULL,
                    prix INTEGER NOT NULL,
                    remise INTEGER NOT NULL,
                    total INTEGER NOT NULL,
                    rating INTEGER
                )
            """)
            conn.commit()

def ajouter_commande(nom, prenom, email, telephone, adresse, produit, prix, remise, total, rating):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO commandes
                (nom, prenom, email, telephone, adresse, produit, prix, remise, total, rating)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nom, prenom, email, telephone, adresse, produit, prix, remise, total, rating))
            conn.commit()

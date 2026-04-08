import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_kurs_daten():
  with sqlite3.connect("Alici_Emir_fitnessstudio.db") as conn:
    cursor = conn.cursor()

    query = """
        SELECT Kurs.Bezeichnung ,Kurs.Wochentag,Kurs.Uhrzeit, Trainer.Vorname || ' ' || Trainer.Nachname AS Name,Kurs.Max_Teilnehmer
        FROM Kurs
        LEFT JOIN Trainer
        ON Kurs.TrainerId = Trainer.TrainerId
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@anvil.server.callable
def get_kunde():
  with sqlite3.connect("Alici_Emir_fitnessstudio.db") as conn:
    cursor = conn.cursor()
    query = """SELECT Vorname || Nachname AS name FROM Mitglied"""
    cursor.execute(query)
    result = cursor.fetchall()
  return result
    
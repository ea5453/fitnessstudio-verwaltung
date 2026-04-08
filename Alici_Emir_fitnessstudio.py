import sqlite3

# Verbindung zur SQLite-Datenbank (Datei wird erstellt, falls sie nicht existiert)
conn = sqlite3.connect(r"E:\Dbi_PLF\Alici_Emir_fitnessstudio.db")
cursor = conn.cursor()

cursor.executescript("""
DELETE FROM Trainer;
DELETE FROM Kurs;
DELETE FROM Mitglied;
DELETE FROM MeldetAn;
""")
# Tabellen erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS Trainer (
    TrainerId INTEGER PRIMARY KEY,
    Vorname TEXT,
    Nachname TEXT,
    Spezialgebiet TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Kurs (
    KursId INTEGER PRIMARY KEY,
    Wochentag TEXT,
    Uhrzeit TEXT,
    Bezeichnung TEXT,
    Max_Teilnehmer INTEGER,
    TrainerId INTEGER,
    FOREIGN KEY (TrainerId) REFERENCES Trainer(TrainerId)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Mitglied (
    MitgliedId INTEGER PRIMARY KEY,
    Beitrittsdatum DATE,
    Vorname TEXT,
    Nachname TEXT,
    Email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS MeldetAn (
    MitgliedId INTEGER,
    KursId INTEGER,
    AnmeldeDatum DATE,
    PRIMARY KEY (MitgliedId, KursId),
    FOREIGN KEY (MitgliedId) REFERENCES Mitglied(MitgliedId),
    FOREIGN KEY (KursId) REFERENCES Kurs(KursId)
)
""")

# Beispieldaten einfügen

# ≥ 3 Trainer
trainer = [
    (1, "Anna", "Müller", "Yoga"),
    (2, "Max", "Schmidt", "Krafttraining"),
    (3, "Laura", "Weber", "Cardio")
]
cursor.executemany("INSERT INTO Trainer VALUES (?, ?, ?, ?)", trainer)

# ≥ 5 Kurse
kurse = [
    (1, "Montag", "08:00", "Yoga Anfänger", 15, 1),
    (2, "Dienstag", "10:00", "Power Yoga", 12, 1),
    (3, "Mittwoch", "18:00", "Kraft Basics", 10, 2),
    (4, "Donnerstag", "17:00", "HIIT", 20, 3),
    (5, "Freitag", "09:00", "Cardio Mix", 18, 3)
]
cursor.executemany("INSERT INTO Kurs VALUES (?, ?, ?, ?, ?, ?)", kurse)

# ≥ 6 Mitglieder
mitglieder = [
    (1, "2024-01-10", "Tom", "Becker", "tom@example.com"),
    (2, "2024-02-15", "Lisa", "Klein", "lisa@example.com"),
    (3, "2024-03-20", "Paul", "Fischer", "paul@example.com"),
    (4, "2024-04-05", "Sara", "Wolf", "sara@example.com"),
    (5, "2024-05-01", "Jan", "Hoffmann", "jan@example.com"),
    (6, "2024-06-12", "Nina", "Schulz", "nina@example.com")
]
cursor.executemany("INSERT INTO Mitglied VALUES (?, ?, ?, ?, ?)", mitglieder)

# ≥ 8 Anmeldungen
anmeldungen = [
    (1, 1, "2024-07-01"),
    (2, 1, "2024-07-02"),
    (3, 2, "2024-07-03"),
    (4, 3, "2024-07-04"),
    (5, 4, "2024-07-05"),
    (6, 5, "2024-07-06"),
    (1, 3, "2024-07-07"),
    (2, 4, "2024-07-08")
]
cursor.executemany("INSERT INTO MeldetAn VALUES (?, ?, ?)", anmeldungen)

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Datenbank erfolgreich erstellt und mit Beispieldaten gefüllt.")
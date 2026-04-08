import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server

@anvil.server.callable
def get_kurs_daten():
  with sqlite3.
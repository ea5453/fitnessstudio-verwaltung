from ._anvil_designer import AnmeldungTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Anmeldung(AnmeldungTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    anvil.server.call('get_kunde')
    # Any code you write here will run before the form opens.

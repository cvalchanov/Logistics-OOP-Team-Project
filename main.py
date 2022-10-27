
from src.core.application_data import ApplicationData
from src.core.engine import Engine
from src.core.command_factory import CommandFactory


app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

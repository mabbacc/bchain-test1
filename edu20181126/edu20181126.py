from iconservice import *

TAG = 'ABCToken'

class ABCToken(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello"

    @external(readonly=True)
    def getname(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "mabbacc12"

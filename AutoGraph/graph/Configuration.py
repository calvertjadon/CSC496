class Configuration:
    def __init__(self, cpu: str, gpu: str, ) -> None:
        self.cpu = cpu
        self.gpu = gpu

    def __str__(self) -> str:
        return f"< {self.cpu} | {self.gpu} >"

    def __repr__(self) -> str:
        return self.__str__()

from abc import ABC, abstractmethod
from datetime import datetime


class ManipuladorDeLog(ABC):
    """
    - O @classmethod permite a utilização do método log(), sem a necessidade
    instanciar-se um objeto a partir da classe abstrata ManipuladorDeLog.
    - O @abstractmethod define que o método não será implementado,
    apenas declarado.
    - Como log() é um @classmethod, deve-se utilizar cls ao invés de self.
    """
    @classmethod
    @abstractmethod
    def log(cls, msg):
        raise NotImplementedError


class LogEmArquivo(ManipuladorDeLog):
    """A classe LogEmArquivo está herdando métodos e atributos
    da classe abstrata ManipuladorDeLog."""
    @classmethod
    def log(cls, msg):
        with open("./Assets/log.txt", "a") as arquivo:
            print(msg, file=arquivo)  # print() também escreve em arquivos.


class LogEmTela(ManipuladorDeLog):
    """A classe LogEmTela está herdando métodos e atributos
    da classe abstrata ManipuladorDeLog."""
    @classmethod
    def log(cls, msg):
        print(msg)


class Log:
    def __init__(self, manipuladores_arr):
        self.__manipuladores_arr = manipuladores_arr

    def adicionar_manipulador(self, manipulador):
        self.__manipuladores_arr.append(manipulador)

    def info(self, msg):
        self.__log("INFO", msg)

    def alerta(self, msg):
        self.__log("ALERTA", msg)

    def erro(self, msg):
        self.__log("ERRO", msg)

    def debug(self, msg):
        self.__log("DEBUG", msg)

    def __formatar(self, tipo, msg):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # 10/05/2022 21:14:39
        return f"[{tipo} - {data}]: {msg}"

    def __log(self, tipo, msg):
        for manipulador in self.__manipuladores_arr:
            manipulador.log(self.__formatar(tipo, msg))


log_obj = Log([LogEmArquivo])
log_obj.info("Informação do JF")
log_obj.alerta("Alerta do JF")
log_obj.erro("Erro do JF")

log_obj.adicionar_manipulador(LogEmTela)
log_obj.debug("Debugação do JF")

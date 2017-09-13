from graficos import Graficos
from copy import deepcopy

def __init__(self):
    self.executaJogo()

def criaAnimaisInicial():
    return animais

def criaMatrizAnimaisInicial(animais):
    matrizAnimais = [[None]*64]*64

    return matrizAnimais

def verificaFimJogo():
    fim = False 
    return fim

def retornaRastrosAtualizados(matrizRastros):
    rastrosAtualizados = deepcopy(matrizRastros)
    def subtrai1Array
    return rastrosAtualizados

def retornaMatrizAnimaisAtualizada(acoes, matrizAnimais):
    return matrizAnimaisAtualizada

def executaJogo(self):
    graficos =
    animais = criaAnimaisInicial()
    matrizAnimais = criaMatrizAnimaisInicial(animais)
    matrizRastros = [[0]*64]*64
    ambiente = (matrizAnimais,matrizRastros)
    while(not self.verificaFimJogo(matrizAnimais)):
        acoes = map(lambda x : x.acoesIntraBloco(ambiente) ,animais)
        matrizAnimais = retornaMatrizAnimaisAtualizada(acoes,matrizAnimais)
        matrizRastros = retornaRastrosAtualizados(matrizRastros)
        acoes = map(lambda x : x.movimentar(ambiente) ,animais)
        matrizAnimais = retornaMatrizAnimaisAtualizada(acoes,matrizAnimais)
        matrizRastros = retornaRastrosAtualizados(matrizRastros)

from graficos import Graficos
from copy import deepcopy
from peixe import Peixe
from tubarao import Tubarao

def __init__(self):
    self.executaJogo()

def criaAnimaisInicial():
	#tuple (obj,id,linha,coluna)
    return animais

def criaMatrizAnimaisInicial(animais):
    matrizAnimais = [[None]*64]*64

    return matrizAnimais

def verificaFimJogo():
    fim = False 
    return fim

def atualizaAmbiente(ambiente,):
	
	def retornaRastrosAtualizados(matrizRastros):
	    def subtrai1Array(array):
	        arrayMenos1 = map(lambda x : x - 1, array)
	    return map(lambda x : subtrai1Array(x), matrizRastros)
	
	def retornaMatrizAnimaisAtualizada(matrizAnimais):
		return matrizAnimaisAtualizada
"""
def retornaMatrizAnimaisAtualizada(acoes, matrizAnimais):
    return matrizAnimaisAtualizada
"""
def executaJogo(self):
    graficos =
    animais = criaAnimaisInicial()
    matrizAnimais = criaMatrizAnimaisInicial(animais)
    matrizRastros = [[0]*64]*64
    ambiente = (matrizAnimais, matrizRastros)
    def retornaIdsMortos(acoes):
    def retornaIdsFecundados(acoes):
    def retornaOjtsNascidos(acoes):

    while(not self.verificaFimJogo(matrizAnimais)):
        animaisProxRodada = deepcopy(animais)
        idsMortos = []
        idsFecundados = []
        objtsNascidos = []
        for animal in animais:
            acoes = animal.acoesIntraBloco(ambiente)


        """
        acoes = map(lambda x : x.acoesIntraBloco(ambiente) ,animais)
        matrizAnimais = retornaMatrizAnimaisAtualizada(acoes,matrizAnimais)
        matrizRastros = retornaRastrosAtualizados(matrizRastros)
        acoes = map(lambda x : x.movimentar(ambiente) ,animais)
        matrizAnimais = retornaMatrizAnimaisAtualizada(acoes,matrizAnimais)
        matrizRastros = retornaRastrosAtualizados(matrizRastros)
        """

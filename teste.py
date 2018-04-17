import requests

from bs4 import BeautifulSoup
from base_de_dados import dicionario_de_topicos, lista_de_topicos,dicionario_geral


def request(endereco):
	page = requests.get(endereco)
	soup = BeautifulSoup(page.content, 'html.parser')
	return soup

def conta_ocorencias(procurada,soup):		

	#print(page.status_code)
	total_ocorencias=0
	for i in soup.find_all('p'):
		item=str(i)
		ocorencias=item.count(procurada)
		total_ocorencias+=ocorencias
	return total_ocorencias


def calcula_peso(dicionario_de_topicos,soup):
	for key_topico in dicionario_de_topicos.keys():

		if(key_topico!='urls'):

			total_de_ocorencias_de_um_topico=0		
			for key_sub_topico in dicionario_de_topicos[key_topico].keys():		
				if(key_sub_topico!='Total'):
					numero_ocorencias=conta_ocorencias(key_sub_topico,soup)
					dicionario_de_topicos[key_topico][key_sub_topico]=numero_ocorencias

					total_de_ocorencias_de_um_topico+=numero_ocorencias

			dicionario_de_topicos[key_topico]['Total']=total_de_ocorencias_de_um_topico
	return dicionario_de_topicos


	

		


def mostra(dicionario):
	for key in dicionario.keys():
		if(key!="urls"):
			for sub_key in dicionario[key].keys():
				print(sub_key, dicionario[key][sub_key])


def calcula_todos_os_pesos(dicionario):
	for key in dicionario.keys():
		for sub_key in dicionario[key].keys():
			print(sub_key, dicionario[key][sub_key])

def requisicao(dicionario,endereco):
	soup=request(endereco)

	calcula_peso(dicionario,soup)



def mostra2(dicionario_geral):							
	for key in dicionario_geral.keys():
		mostra(dicionario_geral[key])
	

#print(conta_ocorencias(i,"http://congressoemfoco.uol.com.br/eleicoes-2014/programa-de-governo-de-levy-fidelix/"))


for candidato in dicionario_geral.keys():
	for sub_key in dicionario_geral[candidato].keys():
		if(sub_key=="urls"):
			for url_key in dicionario_geral[candidato][sub_key].keys():
				requisicao(dicionario_geral[candidato],dicionario_geral[candidato][sub_key][url_key])




mostra2(dicionario_geral)





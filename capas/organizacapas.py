import requests, re, os, shutil
from pathlib import Path

arq_isbns = open("isbns.txt", 'r')
isbns = arq_isbns.readlines()

arq_ids = open("ids.txt", 'r')
ids = arq_ids.readlines()

ids_ok = open("ids_ok.txt", 'w')

linhas = len(isbns)
i = 0

while i < linhas:
	
	idproduct = ids[i]
	idproduct = re.sub("\n","",idproduct)

	isbnproduct = isbns[i]
	isbnproduct = re.sub("\n","",isbnproduct)
	isbnproduct = isbnproduct + ".jpg"

	f_isbnproduct = Path(isbnproduct)
	idproduct = str('(') + idproduct + str(')')

	if f_isbnproduct.is_file():
		os.makedirs(idproduct)
		print('pasta criada')
		shutil.copy(isbnproduct, idproduct)
		print('arquivo copiado')
		ids_ok.write(idproduct)
		ids_ok.write('\n')
	else:
		print('arquivo nao existe')

	i += 1
ids_ok.close()
arq_isbns.close()
arq_ids.close()
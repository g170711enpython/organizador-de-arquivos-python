from pathlib import Path
import shutil

Dicionario = {
# lista de produtos
".jpg" : "imagem",
".txt" : "documento",
".xlsx" : "documento",
".exe" : "programas",
".zip" : "Arquivos Zip",
".py" : "codigos",
".ipynb" : "codigos",
".png" : "imagem",
".pdf" : "documento",
".EXE" : "programas",
".jar" : "codigos",
".json" : "imagens",
".csv" : "documento",
".msi" : "programas",
".xmbclp" : "programas",
}

pasta = Path(r"D:/")
if pasta.exists():
    print(f"a seguinte pasta existe: {pasta}")
    lista_arquivos = pasta.iterdir()
    for item in lista_arquivos:
        if item.is_file():
            print(f"arquivo: {item.name}, extensão: {item.suffix}")
            pasta_destino = Path(r"D:\organizador")
            if item.suffix in Dicionario:
                pasta_final = pasta_destino / Dicionario[item.suffix]
                pasta_final.mkdir(parents=True, exist_ok=True)       
                caminho_final = pasta_final / item.name
                shutil.move(str(item), str(caminho_final))
                print(f"o arquivo {item.name} foi movido com exito para a pasta {caminho_final}")
            else:
                pasta_outros = pasta_destino / "outros"
                pasta_outros.mkdir(parents=True, exist_ok=True)
                caminho_final = pasta_outros / item.name
                shutil.move(str(item), str(caminho_final))
                print(f"o arquivo {item.name} foi movido com exito para a pasta {caminho_final}")
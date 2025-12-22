import os

# Pasta raiz do FastDL
pasta_fastdl = r"D:\tf2server\tf2\fastdl\tf2-fastdl"

# Extensões de arquivos para APAGAR (os originais não comprimidos)
extensoes_apagar = [
    '.wav', '.mp3',  # Sons
    '.mdl', '.vtx', '.vvd', '.phy',  # Modelos
    '.vtf', '.vmt',  # Materiais/Texturas
    '.bsp',  # Mapas
]

arquivos_apagar = []

print("Procurando arquivos para apagar...")
print("="*50)

# Percorre todas as pastas e subpastas
for pasta_atual, subpastas, arquivos in os.walk(pasta_fastdl):
    for arquivo in arquivos:
        # Pega a extensão do arquivo
        _, extensao = os.path.splitext(arquivo)
        
        # Se for uma extensão que queremos apagar (não é .bz2)
        if extensao.lower() in extensoes_apagar:
            caminho_completo = os.path.join(pasta_atual, arquivo)
            
            # Verifica se existe a versão .bz2 correspondente
            caminho_bz2 = caminho_completo + ".bz2"
            
            if os.path.exists(caminho_bz2):
                arquivos_apagar.append(caminho_completo)
                print(f"[APAGAR] {arquivo}")
            else:
                print(f"[MANTER] {arquivo} (sem .bz2 correspondente)")

print("="*50)
print(f"\nTotal de arquivos para apagar: {len(arquivos_apagar)}")

# Confirmação antes de apagar
if len(arquivos_apagar) > 0:
    print("\n⚠️  ATENÇÃO: Esta ação é irreversível!")
    resposta = input("\nDigite 'SIM' para confirmar a exclusão: ")
    
    if resposta.upper() == "SIM":
        print("\nApagando arquivos...")
        
        apagados = 0
        erros = 0
        
        for arquivo in arquivos_apagar:
            try:
                os.remove(arquivo)
                apagados += 1
                print(f"[OK] Apagado: {os.path.basename(arquivo)}")
            except Exception as e:
                erros += 1
                print(f"[ERRO] {os.path.basename(arquivo)}: {e}")
        
        print("\n" + "="*50)
        print(f"✅ Arquivos apagados: {apagados}")
        print(f"❌ Erros: {erros}")
        print("="*50)
    else:
        print("\n❌ Operação cancelada pelo usuário.")
else:
    print("\n✅ Nenhum arquivo para apagar!")

input("\nPressione ENTER para sair...")

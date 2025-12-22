import os

# Pasta raiz do FastDL
pasta_fastdl = r"D:\tf2server\tf2\fastdl\tf2-fastdl"

# Extensões de arquivos para comprimir
extensoes = [
    '.wav', '.mp3',  # Sons
    '.mdl', '.vtx', '.vvd', '.phy',  # Modelos
    '.vtf', '.vmt',  # Materiais/Texturas
    '.bsp',  # Mapas
]

# Arquivo de saída com os comandos
arquivo_saida = r"D:\tf2server\tf2\fastdl\comandos_bzip2.bat"

comandos = []

print("Procurando arquivos...")

# Percorre todas as pastas e subpastas
for pasta_atual, subpastas, arquivos in os.walk(pasta_fastdl):
    for arquivo in arquivos:
        # Pega a extensão do arquivo
        _, extensao = os.path.splitext(arquivo)
        
        # Se for uma extensão que queremos comprimir
        if extensao.lower() in extensoes:
            caminho_completo = os.path.join(pasta_atual, arquivo)
            
            # Não comprimir arquivos já comprimidos
            if not arquivo.endswith('.bz2'):
                comando = f'bzip2 -k "{caminho_completo}"'
                comandos.append(comando)
                print(f"Adicionado: {arquivo}")

# Salva os comandos em um arquivo .bat
with open(arquivo_saida, 'w', encoding='utf-8') as f:
    f.write("@echo off\n")
    f.write("echo Comprimindo arquivos com bzip2...\n")
    f.write("echo.\n\n")
    
    for comando in comandos:
        f.write(comando + "\n")
    
    f.write("\necho.\n")
    f.write(f"echo Concluido! {len(comandos)} arquivos comprimidos.\n")
    f.write("pause\n")

print(f"\n{'='*50}")
print(f"Total de arquivos encontrados: {len(comandos)}")
print(f"Comandos salvos em: {arquivo_saida}")
print(f"{'='*50}")

# Também mostra os comandos no console
print("\n--- COMANDOS GERADOS ---\n")
for cmd in comandos[:20]:  # Mostra os primeiros 20
    print(cmd)

if len(comandos) > 20:
    print(f"\n... e mais {len(comandos) - 20} comandos no arquivo .bat")

import json
import xml.etree.ElementTree as ET


def calcular_faturamento(faturamento_diario):

    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]

    if not dias_com_faturamento:
        return None, None, 0


    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)


    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)


    dias_acima_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

    return menor_faturamento, maior_faturamento, dias_acima_media


def ler_dados_xml(nome_arquivo):
    try:
        tree = ET.parse(nome_arquivo)
        root = tree.getroot()


        faturamento_diario = []
        for elemento in root.findall('.//faturamento'):
            try:
                faturamento_diario.append(float(elemento.text.strip().replace(',', '.')))
            except ValueError:
                print(f"Valor inválido encontrado no arquivo '{nome_arquivo}': {elemento.text}")

        return faturamento_diario
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except ET.ParseError:
        print(f"Erro ao analisar o arquivo '{nome_arquivo}'. Certifique-se de que o formato está correto.")
        return []


def ler_dados_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            dados = json.load(file)

            if isinstance(dados, list):
                return dados
            else:
                print(f"O arquivo '{nome_arquivo}' contém um formato inesperado.")
                return []
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo '{nome_arquivo}'. Certifique-se de que o formato está correto.")
        return []


def main():

    arquivo_xml = 'C:/Users/Bruno.DESKTOP-S4R80CM/Desktop/Desafio Estagio/FaturamentoDiario/dados (2).xml'
    arquivo_json = 'C:/Users/Bruno.DESKTOP-S4R80CM/Desktop/Desafio Estagio/FaturamentoDiario/dados.json'

   
    faturamento_diario_xml = ler_dados_xml(arquivo_xml)
    faturamento_diario_json = ler_dados_json(arquivo_json)

    # Combina os dados dos dois arquivos
    faturamento_diario = faturamento_diario_xml + faturamento_diario_json

    # Calcula os resultados
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

    if menor is not None:
        print(f"Menor valor de faturamento: {menor:.2f}")
        print(f"Maior valor de faturamento: {maior:.2f}")
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
    else:
        print("Não há faturamento registrado para o cálculo.")


if __name__ == "__main__":
    main()

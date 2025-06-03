import numpy as np
import pandas as pd
from tabulate import tabulate

class CalculaRatios:
    
    def __init__(self, tabela_path, fatores, bench_col):
        """
        Inicializa a classe com os parâmetros básicos
        
        Args:
            tabela_path (str): Caminho do arquivo Excel
            fatores (list): Lista de fatores/sheets a serem analisados
            bench_col (str): Nome da coluna benchmark
        """
        self.tabela_path = tabela_path
        self.fatores = fatores
        self.bench_col = bench_col
        self.resultados_consolidados = None
    
    def calcular_individual(self, fator):
        """
        Calcula os ratios para um único fator
        
        Returns:
            dict: Dicionário com os ratios calculados
        """
        try:
            df = pd.read_excel(self.tabela_path, sheet_name=fator)
            
            if fator not in df.columns or self.bench_col not in df.columns:
                raise ValueError(f"Colunas não encontradas na sheet {fator}")
                
            returns_fund = df[fator].values
            returns_bench = df[self.bench_col].values
            
            # Upside Capture
            up_mask = returns_bench > 0
            upside = (np.mean(returns_fund[up_mask]) / np.mean(returns_bench[up_mask])) * 100 if sum(up_mask) > 0 else np.nan
            
            # Downside Capture
            down_mask = returns_bench < 0
            downside = (np.mean(returns_fund[down_mask]) / np.mean(returns_bench[down_mask])) * 100 if sum(down_mask) > 0 else np.nan
            
            return {
                'fator': fator,
                'upside': upside,
                'downside': downside,
                'capture_ratio': upside / downside if downside != 0 else np.nan,
                'spread': upside - downside
            }
            
        except Exception as e:
            print(f"Erro no fator {fator}: {str(e)}")
            return None
    
    def consolidar_resultados(self):
        """
        Calcula e consolida os resultados para todos os fatores
        
        Returns:
            pd.DataFrame: DataFrame com todos os resultados
        """
        dados = []
        
        for fator in self.fatores:
            resultado = self.calcular_individual(fator)
            if resultado:
                dados.append(resultado)
        
        df = pd.DataFrame(dados)
        df.rename(columns={
            'fator': 'Fator',
            'upside': 'Upside Ratio (%)',
            'downside': 'Downside Ratio (%)',
            'capture_ratio': 'Capture Ratio',
            'spread': 'Spread (%)'
        }, inplace=True)
        
        self.resultados_consolidados = df.sort_values('Capture Ratio', ascending=False)
        return self.resultados_consolidados
    

    def mostrar_resultados(self):
        """Exibe os resultados formatados em tabela"""
        if self.resultados_consolidados is None:
            self.consolidar_resultados()
            
        print(tabulate(
            self.resultados_consolidados,
            headers='keys',
            tablefmt='grid',
            showindex=False,
            floatfmt=".2f"
        ))
    
    
    def exportar_excel(self, caminho_saida):
        """
        Exporta os resultados para Excel
        
        Args:
            caminho_saida (str): Caminho do arquivo de saída
        """
        if self.resultados_consolidados is None:
            self.consolidar_resultados()
            
        self.resultados_consolidados.to_excel(caminho_saida, index=False)
        print(f"Arquivo exportado com sucesso para: {caminho_saida}")


# Exemplo de uso:
if __name__ == "__main__":
    # Configurações
    dir_excel = r'C:\Users\dieggo.araujo\Documents\Analise_FIA_Capture_Rateio\dados_raw\Retorno dos Fatores 2023 a 2024.xlsx'
    fatores = ['Defensive', 'Valor', 'Momentum', 'Growth', 'SB', 'Size']
    benchmark = 'IBOV'
    
    # Cria e usa a classe
    analisador = CalculaRatios(dir_excel, fatores, benchmark)
    
    # Opção 1: Obter DataFrame consolidado
    resultados = analisador.consolidar_resultados()
    
    # Opção 2: Visualizar diretamente
    analisador.mostrar_resultados()
    
    # Opção 3: Exportar para Excel
    analisador.exportar_excel(r"C:\Users\dieggo.araujo\Documents\Analise_FIA_Capture_Rateio\dados_processados\Resultados_Capture_Ratios.xlsx")
    
    
    
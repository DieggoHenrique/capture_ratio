import numpy as np
import pandas as pd
from tabulate import tabulate


class CalculaRatios:
    
    
    def __init__(self, tabela_path, sheet, bench):
        self.tabela_path = tabela_path
        self.sheet = sheet
        self.bench = bench
        self.leitura_tabela = self.leitura_tabela()
        self.calculate_capture_ratios = self.calculate_capture_ratios()
    
    
    def leitura_tabela(self):
        for fator in self.tabela_path:
            dataset = pd.read_excel(self.tabela_path, self.sheet)
            #dataset = pd.DataFrame(dataset)
            fund_return = dataset[self.sheet].values
            bench_return = dataset[self.bench].values
        return fund_return, bench_return
    
    def calculate_capture_ratios(self):
        
        # Upside Capture 
        up_mask = bench_return > 0
        upside_fund = fund_return[up_mask]
        upside_bench = bench_return[up_mask]
        upside_ratio = (np.mean(upside_fund) / np.mean(upside_bench)) * 100 if len(upside_bench) > 0 else np.nan
        
        # Downside Capture
        dow_mask = bench_return < 0
        downside_fund = fund_return[dow_mask]
        downside_bench = fund_return[dow_mask]
        downside_ratio = (np.mean(downside_fund) / np.mean(downside_bench)) * 100 if len(downside_bench) > 0 else np.nan
        
        # Capture Ratio
        capture_ratio = upside_ratio / downside_ratio if downside_ratio != 0 else np.nan
        
        # Spread
        spread_ratio = upside_ratio - downside_ratio
                
        return upside_ratio, downside_ratio, capture_ratio, spread_ratio
    
    


dir = r'C:\Users\dieggo.araujo\Documents\Analise_FIA_Capture_Rateio\dados_raw\Retorno dos Fatores 2023 a 2024.xlsx'
key_fatores = ['Defensive', 'Valor', 'Momentum', 'Growth', 'SB']
bench = 'IBOV'
fatores_dict = {}

dados_sb = CalculaRatios(tabela_path=dir, sheet='SB', bench='IBOV')
dados_sb.calculate_capture_ratios()
print(dados_sb)
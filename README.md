# Capture Ratio
Capture ratio, uma métrica que mostra como um fundo se comporta em relação ao seu índice de referência. 
Em essência, ela ajuda a entender se o fundo entrega mais retorno nas altas ou preserva melhor o capital nas quedas, quando comparado ao benchmark. O upside capture ratio representa o desempenho do fundo em momentos positivos do mercado. Quando está acima de 100, indica que o fundo superou o índice durante as altas. Já o downside capture ratio avalia o comportamento em períodos negativos do mercado, e valores abaixo de 100 sugerem que o fundo sofreu menos do que o benchmark. Quando ambos os indicadores estão próximos de 100, significa que o fundo tende a replicar o comportamento do próprio índice.

### 1. Upside Capture

O Upside Capture Ratio é uma métrica que mede a capacidade de um fundo ou estratégia de capturar os movimentos positivos do mercado em relação ao seu benchmark. Um ratio acima de 100% indica que o fundo tende a superar o benchmark em períodos de alta, enquanto um valor abaixo sugere underperformance nesses cenários.

#### 1.1 Filtre os Períodos de Alta do Benchmark
Identifique os períodos em que o benchmark teve retornos positivos:
$$R_{bench} > 0$$

#### 1.2 Calcule o Upside Capture Ratio
A fórmula é:

$$Upside\ Capture\ Ratio =    \frac{média\ dos\ retornos\ do\ fundo\ nos\ periodos\ de\ alta\ do\ benchmar}{média\ dos\ retornos\ de\ alta\ do\ benchmark}$$

#### 1.2 Interpretação
 `> 100%`: Seu fundo captura mais ganhos que o benchmark em rallies.

`= 100%`: Performance igual ao benchmark em alta.

`< 100%`: Seu fundo sobe menos que o benchmark em alta.


#### 2. Implementação do Downside Capture Ratio

O Downside Capture Ratio mede o desempenho do seu fundo em relação ao benchmark durante períodos negativos. Um valor abaixo de 100% é desejável, pois indica que seu fundo perde menos que o benchmark em quedas.

  $$Downside\ Capture\ Ratio =    \frac{média\ dos\ retornos\ do\ fundo\ nos\ periodos\ de\ baixa\ do\ benchmar}{média\ dos\ retornos\ de\ baixa\ do\ benchmark}$$

####  2.1 Filtre os Períodos de Baixa do Benchmark
Identifique os períodos em que o benchmark teve retornos negativos:
$$R_{bench} < 0$$

#### Interpretação
`< 100%` Fundo cai menos que o benchmark (ideal)

 `= 100%` Comportamento igual ao benchmark

 `> 100%` Fundo cai mais que o benchmark.


#### 3. Capture Ratio (Relação de Captura)
A forma mais comum de combinar os dois indicadores:
Indice de Captura  = Upside Capture Ratio / Downside Capture Ratio

 
#### 3.1 Interpretação:

`> 1`: O fundo captura mais ganhos em altas do que perdas em baixas (ideal)

`= 1`: Comportamento simétrico

`< 1`: Sofre mais nas quedas do que ganha nas altas;


#### 4. Capture Spread (Diferencial de Captura)
Indicador simples de diferença:

Spread = Upside Capture − Downside Capture

#### 4.1 Interpretação:

`Positivo`: Bom (ganha mais do que perde)

`Negativo`: Ruim (perde mais do que ganha)


#### 5 Capture Efficiency (Eficiência de Captura)

Eficiencia = Upside Capture - 100%/ Downside Capture - 100% 
Interpretação:

`> 1`: Cada 1% de risco adicional traz mais de 1% de retorno extra

`< 1`: Risco não compensado por retorno

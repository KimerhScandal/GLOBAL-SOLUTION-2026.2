# 🌍 SERS: Neighborhood Action Dashboard - CitizenTech

**Disciplina:** Soluções em Energias Renováveis e Sustentáveis (SERS)
**Turma:** 1CCPA - Ciência da Computação
**Grupo:**
* Fernando Costa e Silva (RM: 574637)
* Henrique Shimada Pimenta (RM: 570721)
* Maria Eduarda Farias Lira (RM: 575504)

> **Nota:** Esta é a contribuição específica da disciplina de SERS para o projeto integrador.

## 1. Diagnóstico do Problema e Solução
**Espaço Escolhido:** Centro Comunitário e Cozinha Solidária na periferia de São Bernardo do Campo.
**Problema:** Alto desperdício de energia com equipamentos ineficientes, quedas constantes de energia da rede pública e acúmulo de lixo orgânico nas ruas.
**Solução Proposta (BioGrid Periférico):** Troca de lâmpadas para LED, automação com sensores IoT e implementação de um biodigestor comunitário para transformar lixo orgânico em biogás e energia elétrica local.

## 2. Dados Utilizados e Fontes
* **Tarifa de Energia:** R$ 0,85/kWh (Média Grupo B).
* **Consumo Atual:** 1.052,4 kWh/mês (Baseado em potências médias do Inmetro para lâmpadas antigas e freezers comerciais).
* **Geração de Biogás:** 90 kg/dia de resíduos geram aprox. 270 m³/mês de gás. Aplicando um fator de eficiência real de 60% (considerando perdas térmicas, umidade dos resíduos e rendimento mecânico do motor), a produção líquida é de 243,0 kWh/mês.

## 3. Estimativas de Consumo e Cálculos
Utilizamos a fórmula `E = (P * t) / 1000`:
* **Cenário Atual:** 1.052,4 kWh/mês (Custo: R$ 894,54).
* **Cenário Otimizado (LED + IoT):** 466,7 kWh/mês.
* **Energia Renovável Gerada (Biogás):** 243,0 kWh/mês.
* **Consumo Residual da Rede:** 223,7 kWh/mês (Custo: R$ 190,15).
* **Economia Total:** R$ 704,39/mês.

## 4. Comparação de Alternativas
Comparamos duas fontes para suprir a demanda otimizada (466,7 kWh/mês):
1. **Energia Solar + Eficiência:** Custo inicial de ~R$ 12.000,00. Gera energia limpa, mas não atende à noite sem baterias caras e não resolve a questão do lixo local.
2. **Biogás Comunitário + Eficiência (Selecionada):** Custo inicial de ~R$ 11.000,00. Trata os resíduos orgânicos do bairro, gera biofertilizante e fornece energia de forma contínua, mesmo à noite ou em dias nublados.

## 5. Diagrama Conceitual de Funcionamento
O fluxo de energia e dados funciona da seguinte forma:

[ LIXO ORGÂNICO ] -> [ BIODIGESTOR / GERADOR ] -> [ ENERGIA ] -> [ EQUIPAMENTOS DO CENTRO ]
                                                                      ^
                                                                      |
[ DASHBOARD ] <- [ PROCESSAMENTO PYTHON/ESP32 ] <- [ SENSORES IOT (PRESENÇA/CORRENTE) ]

## 6. Indicadores Energéticos e Ambientais
1. **Consumo líquido da rede:** 223,7 kWh/mês
2. **Economia energética estimada:** 78,7% (Economia de R$ 704,39/mês)
3. **Participação de energia renovável:** 52% da demanda
4. **Resíduos orgânicos tratados:** 2.700 kg/mês

## 7. Referências e Limitações
* **Limitações:** O biodigestor exige manutenção mecânica periódica do motor e depende de uma triagem bem feita do lixo orgânico pela comunidade para evitar a contaminação do processo de geração do biogás.
* **Referências Técnicas:** 
  * **ANEEL (Agência Nacional de Energia Elétrica):** Dados de tarifas de energia (Grupo B) e regras de microgeração distribuída.
  * **EPE (Empresa de Pesquisa Energética):** Parâmetros de geração de biogás a partir de fração orgânica de resíduos sólidos.
  * **MCTI (Ministério da Ciência, Tecnologia e Inovação):** Fatores de emissão de CO2 do Sistema Interligado Nacional (utilizado para o cálculo de emissões evitadas).
  * **PROCEL / Inmetro:** Tabelas de eficiência energética e potência nominal para iluminação LED e equipamentos de refrigeração.
  * **CIBiogás:** Coeficientes de rendimento elétrico em motogeradores de pequeno porte movidos a biogás.

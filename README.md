# Atividade de Máquina 

Este repositório contém um projeto que visa obter informação através da analise de dados de um relatório de posicionamento de máquina com suas coordenadas e informações básicas de sua atividade permitir obter sobre a **rotina** e **comportamento**. Essas informações podem ser de grande utilidade para julgar se o comportamento foi adequado com o planejamento ou se correram **desvios**.

Os dados foram obtidos através de relatório emitido por uma retroescavadeira jbc modelo 3cx, durante atividade de serviço de pavimentação e drenagem realizados durante o ano de 2022.

## Objetivos Principais

1. Converter dados em informações através da publicação dos resultados em um formato web acessível a qualquer dispositivo. 

## Objetivos Secundários

1. **Mapear a atividade por período com visualização no mapa**

2. **Permitir visualização se houve desvios de operação** Através do mapeamento do gps mostrar quando houve serviços ocorridos fora da atividade principal

3. **Aferir a quantidade e qualidade de registros obtidos** o fluxo de informação enviado pela máquina 

4. **Entimento das Atividades** Como as atividades registradas podem ser utilizadas, identificar e filtrar as **atividades principais**

5. identificar **rotina** e **comportamento** da máquina 

## Visão Geral

Este projeto demostra mostra aplicação a engenharia de dados para automatizar a coleta e análise de dados para fornecer informações valiosas sobre a utilização de máquina.

### Etapas do Processo 

- **Extrair Dados** de GPS: O sistema lê arquivos CSV ou gsheet contendo coordenadas GPS de equipamentos em campo. Esses dados são essenciais para rastrear a localização e movimento dos equipamentos ao longo do tempo.

- **Entendimento Dataframe** A compreender as informações dos dados identificar quais informações são relevantes, como elas estão distribuídas, qual a relação entre demais variáveis como o tempo (hora, dia, mês) ou coordenadas lat+lon.

- **Tamanho dos Dados** verificar a quantidade de linhas registradas por um intervalo de hora, dia e mês 

- **Qualidade dos Dados** entender como os dados disponíveis podem ser úteis para......

Qualidade as condições devem ser verdadeira
3.3 Quantidade a chave liga = motor ligado
3.4 Quantidade a chave desliga= motor desligado 


- **Normalizar Dados** de tempo data e hora, como de local as coordenadas,

- **Transformar dados**, aplicar funções de cálculo de distância, filtrar variáveis relevantes

- **Relatório** a partir de agregação, e responder algumas questões sobre comportamento do equipamento:

- Aplicação Web (Streamlit): Uma aplicação web construída com o Streamlit permite que os usuários visualizem os relatórios em qualquer dispositivo em formato web:

- descrever o funcionamento:
qual o dia funcionamento com mais tempo
qual a maior distância percorrida, no dia, mês, ano
qual dia o menor horas de funcionamento?
quais dias maior horas de funcionamento?

- Dashboards 
gráfico horas semana: seg,ter,quar,quin,sex,sab,dom
gráfico distância semana: seg,ter,quar,quin,sex,sab,dom

- Mapa de localização
permitir através do filtro saber qual o local máquina esteve presente em um determinado período 


## Próximos Passos:
Para uma análise completa é necessário coletar dados que envolve o ambiente no qual o utilizado e através da data fazer uma ligação temporal para verificar de que forma esse ambiente afetou a produção da atividade

### 1.Incluir mais datasets com isso criar um **datalake**, com informações relevantes das quais podem afetar a atividade do equipamento tais como:

- identificao do operador
- Ocorrencia de Chuva
- Realização de abastecimento
- Manutenção preventiva
- Manutenção corretiva
- Tipo de atividade realizada: exemplo:(drenagem com tubo concreto Ø40cm)
- condições climáticas
- locais conhecidos 
  
### 2. Análise de Dados
Os dados de GPS e de apontamento são combinados e analisados pelo sistema. Isso permite calcular a produtividade dos equipamentos, identificar gargalos operacionais e criar relatórios detalhados.

### 3. Geração de Prazo de Término
Com base na produtividade real calculada, o sistema gera um prazo de término otimista, realista e pessimista. Isso ajuda na gestão de projetos e na identificação de possíveis atrasos.

### 4. Lições Aprendidas 
Fazer coleta de tomada de decisão do gestor para  medir se ação foi efetiva.

### 5. Melhores Práticas 
Sugerir as melhores práticas para auxiliar em futuras tomadas de decisão, com base em eventos passados

### 6. Preparo AI
Fornecer um dataset normalizado e com ações consideradas como as **BEST PRACTICES** afim de gerar dados confiáveis para criar um ambiente de aprendizado de máquina

### 7. Utilizar AI
Sugerir ações que otmizem a produtividade através de um modelo **treinado** tanto durante a operação como nas tomadas de decisão. 

## Requisitos de Configuração
Para configurar e executar este projeto, você precisará das seguintes dependências:

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- Pandas



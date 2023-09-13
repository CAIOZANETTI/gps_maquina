# Produtividade de Equipamento

Este repositório contém um projeto que visa obter informação através da analise de relatório de posicionamento de máquina com suas coordenadas e informações básicas de sua atividade permitir a filtrar os dados por período e obter informações através de cálculo como distância percorrida e tempo de operação 

## Objetivos Principais

1. **Obter informações de funcionamento de equipamento e permitir a visualização e consulta em uma interface web** 

## Objetivos Secundários

1. **Mapear a atividade por período com visualização no mapa**

2. **Permitir visualização se houve desvios de operação** Através do mapeamento do gps mostrar quando houve serviços ocorridos fora da atividade principal


## Visão Geral

Este projeto busca mostrar que pode ser aplicada a engenheira de dados para automatizar a coleta e análise de dados para fornecer informações valiosas sobre a utilização de máquina.

- Extrair Dados de GPS: O sistema lê arquivos CSV ou gsheet contendo coordenadas GPS de equipamentos em campo. Esses dados são essenciais para rastrear a localização e movimento dos equipamentos ao longo do tempo.

- normalizar os dados de tempo data e hora, como de local as coordenadas,

- transformar dados, aplicar funções de cálculo de distância, filtrar variáveis relevantes

- extrair relatório a partir de agregação, e responder algumas questões sobre comportamento do equipamento:

qual o dia de maior funcionamento
qual a maior distância percorrida
qual dia menos trabalhados
equipamento funcionou aos domingos?

- Aplicação Web (Streamlit): Uma aplicação web construída com o Streamlit permite que os usuários visualizem os relatórios em qualquer dispositivo em formato web

## Próximos Passos:

### Realizar apontamento das atividades do equipamento através de registro em uma aplicação web, tais como:
- Ocorrencia de Chuva
- Realização de abastecimento
- Manutenção preventiva
- Manutenção corretiva
- Tipo de atividade realizada: exemplo:(drenagem com tubo concreto Ø40cm)
  
### 3. Análise de Dados

Os dados de GPS e de apontamento são combinados e analisados pelo sistema. Isso permite calcular a produtividade dos equipamentos, identificar gargalos operacionais e criar relatórios detalhados.

### 4. Geração de Prazo de Término

Com base na produtividade real calculada, o sistema gera um prazo de término otimista, realista e pessimista. Isso ajuda na gestão de projetos e na identificação de possíveis atrasos.

## Fluxo de Trabalho

1. Importe os arquivos CSV de coordenadas GPS do

2. Acesse a aplicação web (Streamlit) para registrar atividades relacionadas aos equipamentos.

3. O sistema realiza análises automáticas e gera relatórios de produtividade.

4. Utilize os insights obtidos para tomar decisões informadas e melhorar a eficiência operacional.

5. Consulte o prazo de término otimista, realista e pessimista para planejar o projeto de forma adequada.

## Requisitos de Configuração

Para configurar e executar este projeto, você precisará das seguintes dependências:

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- Pandas



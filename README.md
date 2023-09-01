# Produtividade de Equipamento

Este repositório contém um projeto que visa obter a produtividade real de equipamentos por hora, bem como gerar um prazo de término baseado na produtividade real. O prazo pode ser otimista, realista e pessimista, permitindo uma melhor gestão de projetos e tomada de decisões informadas. O sistema também combina dados de coordenadas GPS e registros de apontamento coletados no campo. Os dados podem ser fornecidos por operadores, encarregados e engenheiros através de uma aplicação web.

## Objetivos Principais

1. **Obter Produtividade Real do Equipamento por Hora:** O objetivo principal deste projeto é calcular a produtividade real dos equipamentos por hora, fornecendo informações precisas sobre o desempenho operacional. Isso é essencial para a gestão eficaz de recursos e tomada de decisões informadas.

## Objetivos Secundários

1. **Calcular estimativa de termino da atividade** Além de calcular a produtividade real, o sistema também gera um prazo de término baseado na produtividade real. Esse prazo pode ser otimista, realista e pessimista, permitindo uma gestão de projetos mais flexível e a identificação de possíveis atrasos.
2. **Calcular o consumo de combustivel por atividade:** Além de calcular a produtividade real, o sistema também gera um prazo de término baseado na produtividade real. Esse prazo pode ser otimista, realista e pessimista, permitindo uma gestão de projetos mais flexível e a identificação de possíveis atrasos.
3. **Sinalizar desvios de operação** Através do mapeamento do gps mostrar quando houve serviços ocorridos fora da atividade principal
4. **Comparar desempenho por operador** Caso exista mais de um operador, mostrar a produtividade de cada um em uma mesma atividade
5. **Comparar avanço por tipo de serviço** Exemplo a execução de rede de acordo com o tipo e dimensão do tubo e produtividade da vala

## Visão Geral

A produtividade de equipamentos é essencial para o sucesso de projetos de construção e operações industriais. Este projeto busca automatizar a coleta e análise de dados para fornecer informações valiosas sobre a eficiência operacional. Ele incorpora as seguintes funcionalidades:

- Coleta de Dados de GPS: O sistema lê arquivos CSV contendo coordenadas GPS de equipamentos em campo. Esses dados são essenciais para rastrear a localização e movimento dos equipamentos ao longo do tempo.

- Registro de Apontamento: Operadores, encarregados e engenheiros podem fornecer informações detalhadas sobre as atividades realizadas pelos equipamentos. Esses registros são essenciais para entender como os equipamentos estão sendo utilizados.

- Aplicação Web (Streamlit): Uma aplicação web construída com o Streamlit permite que os usuários insiram e atualizem os dados de apontamento facilmente. Os dados são armazenados de forma segura e podem ser acessados a qualquer momento.

- Análise de Dados: O sistema realiza análises sofisticadas para calcular a produtividade dos equipamentos com base nos dados de GPS e de apontamento. Isso inclui a identificação de ineficiências e oportunidades de melhoria.

- Geração de Prazo de Término: Com base na produtividade real calculada, o sistema gera um prazo de término otimista, realista e pessimista. Isso ajuda na gestão de projetos e na identificação de possíveis atrasos.

## Como Funciona

### 1. Coleta de Dados de GPS

Os dados de GPS são lidos a partir de arquivos CSV fornecidos como entrada. Cada entrada contém informações de data, hora, coordenadas geográficas e identificação do equipamento.

### 2. Registro de Apontamento

Os operadores, encarregados e engenheiros acessam a aplicação web (Streamlit) para registrar suas atividades relacionadas aos equipamentos. Eles podem fornecer informações como
- Improdutividade por Ocorrencia de Chuva
- Realização de abastecimento ou manutenção
- Tipo de atividade realizada: exemplo:(drenagem com tubo concreto Ø40cm)
  
### 3. Análise de Dados

Os dados de GPS e de apontamento são combinados e analisados pelo sistema. Isso permite calcular a produtividade dos equipamentos, identificar gargalos operacionais e criar relatórios detalhados.

### 4. Geração de Prazo de Término

Com base na produtividade real calculada, o sistema gera um prazo de término otimista, realista e pessimista. Isso ajuda na gestão de projetos e na identificação de possíveis atrasos.

## Fluxo de Trabalho

1. Importe os arquivos CSV de coordenadas GPS dos equipamentos.

2. Acesse a aplicação web (Streamlit) para registrar atividades relacionadas aos equipamentos.

3. O sistema realiza análises automáticas e gera relatórios de produtividade.

4. Utilize os insights obtidos para tomar decisões informadas e melhorar a eficiência operacional.

5. Consulte o prazo de término otimista, realista e pessimista para planejar o projeto de forma adequada.

## Requisitos de Configuração

Para configurar e executar este projeto, você precisará das seguintes dependências:

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- Pandas



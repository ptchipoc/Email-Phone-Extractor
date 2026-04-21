# Email-Phone-Extractor

Projeto simples para extrair emails e telefones de arquivos TXT/CSV/JSON. A ideia e praticar um pipeline completo (entrada -> extracao -> transformacao -> saida), construindo base para estudos em engenharia de dados.

## Objetivo pessoal

Quero construir uma base forte em pipelines porque quero ser engenheiro de dados. Este projeto serve como laboratorio para:
- Ler arquivos de diferentes formatos.
- Extrair informacoes com regex.
- Transformar e padronizar saidas.
- Gerar um arquivo final para consumo (CSV).

## Estrutura do projeto

- feed/ -> arquivos de entrada (TXT, CSV, JSON)
- src/ -> codigo principal (extracao, utilitarios, tipos)
- tests/ -> script simples de execucao

## Como rodar o projeto

Requisitos: Python 3.10+.

1) Entre na pasta do projeto:
```bash
cd /home/ptchipoc/projects/python/Email-Phone-Extractor
```

2) Rode o script de teste apontando para um arquivo de entrada:
```bash
python3 -m tests.test feed/feed.txt
```

O resultado sera gravado em `results.csv` na raiz do projeto.

## Como funciona o pipeline

1) `load_text` le o arquivo de entrada.
2) `extract_email_phone` aplica regex para capturar emails e telefones.
3) `transform` gera um CSV com duas colunas: Type e Value.

## O que eu aprendi (ate agora)

- Como lidar com importacoes Python e rodar modulos corretamente.
- Como trabalhar com regex para extrair informacoes.
- Como construir um pipeline simples de dados fim a fim.
- Como gerar um arquivo CSV a partir dos dados extraidos.

## Proximos passos

- Melhorar a validacao de emails e telefones.
- Criar testes automatizados reais.
- Suportar mais formatos e grandes volumes de dados.
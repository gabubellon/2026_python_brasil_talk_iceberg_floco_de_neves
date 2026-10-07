---
marp: true
theme: pybr2026
lang: pt-BR
paginate: true
footer: Python Brasil 2026
title: O Iceberg Foi pro Snowflake
---

<!-- _class: capa -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="selo">14 a 19<br>de outubro<br>de 2026<br>{Floripa/SC}</div>

# O Iceberg Foi pro Snowflake

A jornada real de uma migração de dados em produção

**Gabu Bellon** · @gabubellon

<!--
- Adaptado da versão apresentada na Caipyra 2026.
-->

---

<!-- _class: frase -->

# O design e a estrutura visual tiveram apoio de Inteligência Artificial.

O conteúdo técnico é inteiramente da experiência do palestrante.

---

<!-- _class: palestrante -->

![Foto de Gabu Bellon](img/foto-exemplo.png)

# Gabu Bellon

### Lead Data Engineer · phData

- Pronomes: Nenhum / Ele / Dele
- Nerd/Geek & Comunista · Papai orgulhoso da Ceci
- Entusiasta de Comunidade · Migração e Consolidação de Dados

<!--
- Trocar img/foto-exemplo.png por uma foto real antes da palestra.
- @gabubellon
-->

---

<!-- _class: cartoes -->

## Uma Jornada em Três Gerações

1. **G0 · Lake** Monólito Apache Iceberg, o jeito que tudo começou.
2. **G1 · Warehouse** Snowflake e dbt, via Datapipe.
3. **G2 · Batch** Airflow + Kubernetes, a arquitetura atual.

<!--
- Nenhuma geração substitui a anterior de uma vez: as três convivem durante a migração.
- Migração feed a feed, com corte controlado, sem big-bang.
-->

---

<!-- _class: numeros -->

## A Plataforma de Dados

- **30+** fontes de dados de fornecedores do mercado financeiro
- **50+** DAGs em produção
- **3** gerações de arquitetura convivendo

<!--
- A plataforma consolida preços, índices, derivativos e referências do mercado financeiro.
-->

---

<!-- _class: destaque -->

## O que funciona nem sempre é o que escala.

- Crescimento sem governança virou o produto de fato: manutenção
- Cada geração tentou resolver o gargalo que a anterior deixou
- A saída não é um big-bang: é feed a feed, com corte controlado

---

<!-- _class: duas-colunas -->

## As Tecnologias

### Ingestão & Orquestração

- **Python + Airflow** orquestram ingestão e transformação
- **Apache Iceberg** formato de tabela aberto: snapshots e partições

### Armazenamento & Transformação

- **Snowflake** warehouse elástico para consulta e consumo
- **dbt** transformação declarativa em SQL, com testes e docs

---

<!-- _class: secao -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# _01_ G0 · O Monólito Apache Iceberg

<!--
- Como tudo começou.
-->

---

<!-- _class: fluxo -->

## Fluxo Legado: do Arquivo ao Lake

1. Fornecedor envia o arquivo
2. Airflow dispara o `main_*.py`
3. Builders em `jgdata/datasets/` transformam os dados
4. Commit no Iceberg (snapshot)

<!--
- Execução manual: python main_.py --procdate YYYYMMDD.
- initDataset() decide se precisa rodar backfill, via executeBuild().
-->

---

## Builders com Decoradores

```python
@DataLakeTable(
    dataset="precos", name="fechamento"
)
def build(procdate):
    ...
```

<!--
- @DataLakeCache e @DataLakeTable registram o builder no SchemaRegistry.
- FileLock em /var/tmp/iceberg/{table} serializa as escritas do Spark.
-->

---

<!-- _class: duas-colunas -->

## Dois Catálogos

### cache (jg_datacache)

- Chave `dataset.tabela.mk1`
- S3: `{root}/cache/{dataset}/{name}/`

### lake (jg_datalake)

- Chave `{região}.tabela`
- S3: `{root}/lake/{region}/{name}/`

---

## Perfil Define o Modo de Escrita

| Perfil | Partição/Freq | Modo |
|---|---|---|
| Série diária | date/daily | append |
| Snapshot/SCD | blob/latest | overwrite_all |
| Reenvio de arquivo | — | overwrite_file |
| Idempotente | — | upsert + joinkey |

<!--
- Cada dataset é descrito num TOML em conf/datasets/*.toml.
-->

---

<!-- _class: secao -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# _02_ G1 · Snowflake, dbt e o Datapipe

---

<!-- _class: duas-colunas -->

## Datapipe: Config em YAML

### Um arquivo por feed

- `.datapipe.yaml` descreve `raw_data` (S3 + `$DATE`)
- `table_map`: regex → tabela RAW, formato, colunas

### Sem builder Python

- Mapeamento por posição de coluna
- `RAW` vira a única fonte da verdade bruta

---

<!-- _class: fluxo -->

## Pipeline de Carga v1

1. `pipeline_rawdata.py` descobre arquivos e envia ao S3
2. `pipeline_sf_copy.py` roda o COPY INTO
3. Carrega em `VENDOR_RAW` com metadados automáticos
4. DAG `jgetl-dbt-*` orquestra tudo via SSH

<!--
- Metadados automáticos: filename e start_scan_time.
- Um pool_dbt limita a concorrência das cargas.
-->

---

## Camadas do dbt

| Camada | Prefixo | O que faz |
|---|---|---|
| Staging | `stage/raw_*` | Limpeza e casts |
| Integration | `integration/int_*` | Regras de negócio em SQL |
| Publication | `publication/pub_*` | Views para quem consome |

<!--
- Consumidores só leem publication, nunca RAW diretamente.
- sources/*.yml liga os models às tabelas RAW.
-->

---

<!-- _class: secao -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# _03_ G2 · dp_batch, a Arquitetura Atual

---

<!-- _class: fluxo -->

## Ingestão no dp_batch

1. `sftp_ingest` traz o arquivo do fornecedor
2. Grava em S3 Raw, particionado ao estilo Hive
3. `MetadataService` registra ingest_id e idempotência
4. Buckets separados para dev e prod

<!--
- A ingestão ainda não conhece o Snowflake.
-->

---

## Preprocess com Polars

```python
Column(
    name_in_file="PRECO",
    name_in_snowflake="preco",
    snowflake_type=SnowflakeTyping.FLOAT,
    polars_type=PolarsTyping.FLOAT,
)
```

<!--
- CsvReader (lazy) → transforma → Parquet.
- orchestrate_preprocess usa SCHEMA_BY_DATASET para tipar cada coluna.
-->

---

<!-- _class: fluxo -->

## Orquestração: Airflow + Kubernetes

1. `@task.kubernetes` roda ingest/preprocess em pods isolados
2. COPY INTO grava no schema `*_DP_BATCH`
3. `KubernetesPodOperator` roda `dbt run --select +tag:dataset+`
4. `task_factory.make_validation_task` garante testes com Elementary

<!--
- As tags do dbt ligam cada dataset à sua DAG, ex. +tag:ice_mft_futures+.
-->

---

## Três Gerações, Lado a Lado

| | Ingestão | Transformação | Orquestração |
|---|---|---|---|
| G0 Iceberg | Builder Python | Pandas + snapshot | Airflow SSH |
| G1 Snowflake | YAML → COPY INTO | dbt_data_platform | Airflow SSH + pool |
| G2 dp_batch | sftp_ingest → S3 | Polars + dbt_dp_batch | Airflow + K8s |

<!--
- Nenhuma geração some de uma vez: convivem até o corte feed a feed.
-->

---

<!-- _class: cartoes -->

## Próximos Passos

1. **Completar a migração** Feed a feed, com corte controlado de schema.
2. **Consolidar práticas** src layout, testes, CI/CD, dbt como padrão.
3. **Visão de longo prazo** Plataforma única, governança com Elementary.

---

<!-- _class: encerramento -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# Perguntas?

**Gabu Bellon**
_@gabubellon_
_bllon.co_

![QR code para bllon.co](img/qr.png)

gabubellon.me · loucuradevaneia.com

<!--
- Gerar o QR code real: uv run scripts/qr.py https://bllon.co (troca img/qr.png).
-->

---

<!-- _class: figurinhas -->
<!-- _paginate: false -->
<!-- _footer: "" -->

## Figurinhas

### Dazumbanho! Chegasse ao fim, ixtepô!

![w:290](img/lockup-on-dark.png) ![w:190](img/sticker-witch.png) ![w:220](img/sticker-mago-ola.png) ![w:130](img/sticker-mago.png) ![w:120](img/magia-explosao.png)

![w:280](img/logo-assinatura.png) <span class="circulo">olha aqui</span> <mark>marca-texto</mark> ![w:96](img/icone-seta.png) ![w:96](img/icone-codigo.png)

Identidade visual de Ana Terhorst, [anaterhorstdesign.com](https://anaterhorstdesign.com). Valeu, Ana!
</content>

# Premissas adotadas no memorando executivo

Documento de trabalho com as premissas do memorando sobre o Grupo Meridiano, revisado com base nos apêndices da pasta `Apêndices/` (A1 a H1). Cada premissa indica a origem: **apêndice** (dado do material), **case** (texto do business case), **escolha** (decisão da autora), **suposição** (não confirmada pelo material), **calculado** (derivado dos apêndices) ou **externo** (fonte fora do case). Edite livremente.

Códigos das iniciativas, conforme o inventário (A1): **P01** agente de SAC · **P02** recompra e campanhas · **P03** agente de atrasos · **P04** app de escala · **P05** assinaturas individuais de IA · **P06** crédito a sellers · **P07** antifraude · **P08** assistente de RH.

**Onde estão as respostas às perguntas-chave**

| Pergunta | Seção |
|---|---|
| Quais projetos mais impactaram em receita? | 3.1 |
| O que já está deployado? | 3.2 |
| Quais são os dados disponíveis? | 4.1 |
| A infraestrutura está centralizada? | 2.1 |
| Quais são os guardrails do modelo? | 2.2 |

---

## 1. Custos

### 1.1 Quanto e onde se gasta

- **O gasto é o reconstruído por Finanças.** *(Apêndice E1)* R$ 143 mil em set/2025, R$ 519 mil em ago/2026 e R$ 3,88 milhões em doze meses. É uma estimativa montada a partir de faturas, contratos, cartão corporativo e métricas de uso, não um razão contábil.
- **Composição de agosto de 2026.** *(Apêndice E1)*

  | Item | R$ mil/mês | Total em 12 meses (R$ mil) |
  |---|---:|---:|
  | P03 Agente de atrasos | 119,4 | 607,7 |
  | P01 Agente de SAC | 107,1 | 693,7 |
  | P07 Antifraude | 95,0 | 1.140,0 |
  | X1 Nuvem sem piloto atribuído | 85,0 | 425,0 |
  | P05 Assinaturas individuais (420) | 46,2 | 356,4 |
  | P06 Crédito a sellers | 35,0 | 420,0 |
  | P02 Recompra | 17,8 | 177,9 |
  | P08 Assistente de RH | 13,4 | 53,4 |
  | P04 App de escala | 0,6 | 3,0 |
  | **Total** | **519,4** | **3.877,1** |

- **O custo da consultoria de Logística não está na conta.** *(Apêndice E1, nota do P03)* A planilha inclui só a licença da plataforma W e os tokens; a consultoria é contratada à parte. Por isso o custo real do P03 é maior do que o exibido e o valor que a não renovação libera é desconhecido.
- **Contratos sem valor informado.** *(Apêndice D1)* O mapa de contratos não traz valores. A economia da unificação do Provedor X e das renegociações não pode ser estimada com o material.

### 1.2 Onde está o desperdício

- **P01 envia contexto demais.** *(Apêndices A2 e E1)* Cerca de 180 mil tokens de entrada por conversa (6 trocas de cerca de 30 mil), porque a política de reembolso inteira vai em cada mensagem. Os tokens são R$ 95 mil dos R$ 107 mil do mês. *(Calculado)* Isso dá cerca de R$ 2 de tokens por conversa.
- **P03 usa o modelo mais caro em todas as etapas.** *(Apêndices A3 e E1)* As oito etapas usam o modelo de fronteira, inclusive consultar status e redigir mensagem. Na tabela de preços do E1, o modelo leve custa 8 vezes menos por token, tanto na entrada quanto na saída.
- **Nuvem ligada sem dono.** *(Apêndices D1, E1 e C1)* R$ 85 mil/mês desde abr/2026 em ambientes de teste e GPUs da Nuvem A sem piloto associado. A pesquisa confirma: ambientes de teste ficam ligados e ninguém é dono de desligá-los.
- **Ferramenta homologada já paga e pouco usada.** *(Apêndice D1, item 9)* A suíte de produtividade inclui um assistente de IA desde jan/2026, com uso baixo. As 420 assinaturas individuais (P05) duplicam algo que o grupo já paga.
- **Provedor X contratado duas vezes.** *(Apêndice D1, itens 3 e 4)* Uma pelo Digital, outra faturada pela consultoria, sem desconto por volume.
- **Perdas operacionais causadas pelos agentes.** *(Apêndice G1)* Cerca de R$ 312 mil em 1.840 reembolsos indevidos do P01 entre mar e jun/2026, e cerca de R$ 490 mil em 9.800 cupons de R$ 50 emitidos em duplicidade pelo P03 em mar/2026, que não foram cancelados.

### 1.3 Premissas de custo para a decisão

- **O CFO só aceita estrutura nova depois de economia.** *(Apêndice C2)* Por isso a área central começa com 6 a 8 pessoas, a maioria cedida, e novas vagas dependem de economia certificada pela Controladoria. *(Escolha)*
- **Duas contratações pagas com a verba da consultoria.** *(Suposição)* Depende de a consultoria não ser renovada nas mesmas condições; o valor não consta dos apêndices.
- **Desligar o antifraude custa mais do que manter.** *(Apêndice D1)* Contrato de 36 meses com multa até ago/2028.
- **Preço do modelo intermediário dobra em 01/01/2027.** *(Apêndice E1)* Passa de US$ 0,75/US$ 3,75 para US$ 1,50/US$ 7,50 por milhão de tokens. Afeta o P02.
- **A Nuvem B tem compromisso mínimo anual.** *(Apêndice D1)* A escolha da plataforma de referência precisa considerar esse compromisso, que vence em jun/2027.

---

## 2. Segurança e governança

### 2.1 A infraestrutura está centralizada?

**Não.** *(Apêndices A1 e D1)* Cada iniciativa nasceu na sua unidade e usa a sua própria pilha:

| Componente | Situação |
|---|---|
| Nuvem | Nuvem A (contratada pelo Digital, fora de Compras de TI): P01, P02, data lake. Nuvem B (TI): P06, P08, data warehouse |
| Modelos de linguagem | Provedor X duas vezes (Digital e consultoria): P01, P02, P03. Provedor Y (TI): P08 |
| Banco vetorial | Gerenciado na Nuvem A (P01) e próprio na Nuvem B (P08) |
| Fora das nuvens corporativas | Plataforma W em nome da consultoria (P03); conta pessoal do criador (P04); SaaS do fornecedor (P07); ferramentas externas em contas pessoais (P05) |
| Identidade e chaves | Cada time guarda as próprias chaves. P02 usa a mesma chave de API do P01. P04 usa senha única compartilhada por 45 gerentes |
| Dados entre áreas | Extração mensal de arquivo do data lake para o data warehouse, preparada pelo Digital |
| Catálogo e homologação | Não existe catálogo de modelos, prompts ou bases. Não existe ambiente de homologação compartilhado |

**Premissa:** o comitê não precisa escolher a plataforma agora. Até a renovação da Nuvem A (mar/2027) valem padrões de interface comuns às duas nuvens, e a escolha usa as janelas de dez/2026, jan, mar e jun/2027. *(Escolha)*

### 2.2 Quais são os guardrails do modelo?

**Hoje, quase nenhum.** *(Apêndices A2 a A5 e G1)*

| Iniciativa | Ação autônoma | Limite existente | O que falta |
|---|---|---|---|
| P01 SAC | Emite reembolso, abre troca | Até R$ 300 por pedido | Limite por cliente e por dia; checar status de entrega antes de reembolsar; filtro de dados pessoais na base de conhecimento; teste de aderência às políticas; avaliação de qualidade; prazo de retenção dos logs |
| P03 Atrasos | Troca transportadora, emite cupom, avisa cliente | Cupom de até R$ 50 | Aprovação humana para troca de transportadora; proteção contra reexecução da etapa de cupom; registro das decisões |
| P06 Crédito | Aprova ou recusa pedidos | Até R$ 50 mil automático; acima, comitê | Revisão humana das recusas; explicação ao seller; canal de contestação (LGPD art. 20); retreino definido; monitoramento de efeito por região |
| P04 Escala | Publica e envia escala | Nenhum | Acesso individual; registro de acesso; credenciais fora do código; cópia de segurança |
| P05 Assinaturas | Recebe dados colados pelo usuário | Nenhum | Política de uso e ferramenta homologada |

**Guardrails propostos no memorando** (os oito padrões do portão de entrada, Anexo 2). *(Escolha, alinhada aos requisitos do Jurídico no Apêndice H1)*

1. Registro no inventário único, com dono de negócio e dono técnico.
2. Contas, credenciais e acesso corporativos, com segredos em cofre.
3. Base legal e relatório de impacto quando houver dado pessoal; minimização de dados.
4. Limites de ação autônoma por valor, frequência e cliente; revisão humana em decisões de alto impacto.
5. Avaliação de qualidade com conjunto de teste independente da equipe, incluindo testes de vazamento.
6. Monitoramento em produção, critérios de suspensão e resposta a incidentes no prazo da ANPD.
7. Ficha de valor com linha de base e contrafactual aprovados pela Controladoria.
8. Custo identificado por iniciativa e por unidade de resultado.

Os requisitos do Jurídico que o portão também precisa cobrir: participação do DPO com poder de bloqueio; cláusulas com fornecedores (sem treino com os dados, transferência internacional, retenção, notificação de incidente); política de uso de IA com lista de ferramentas homologadas. *(Apêndice H1)*

### 2.3 Risco jurídico e incidentes

- **Situação por iniciativa.** *(Apêndice H1)* Nenhuma iniciativa tem relatório de impacto. Base legal ausente em P01, P03, P04 e P05; parcial em P02 (consentimento não verificado antes de set/2025); registrada em P06, P07 e P08. Risco jurídico alto em P01, P04, P05 e P06; médio em P02 e P03; baixo em P07 e P08.
- **Sete incidentes registrados entre mar e set/2026.** *(Apêndice G1)* Três no P01 (exposição de dados em 37 conversas, reembolsos indevidos, regra de troca errada levada ao Procon), um no P03, um no P04 (repositório público com senha do banco e chave de API de abr a ago/2026), um no P05 (lista de cerca de 2.000 clientes colada em ferramenta externa) e um no P06 (diferença de aprovação por região).
- **O incidente de julho tem causa conhecida.** *(Apêndice G1)* Manuais do SAC copiados de chamados reais, com dados de clientes, foram carregados na base de conhecimento sem revisão. Os manuais foram removidos em 16/07, mas o fluxo de carga não mudou.
- **Prazo de comunicação à ANPD: 3 dias úteis.** *(Apêndice H1, Resolução CD/ANPD nº 15/2024)* O caso de julho levou 22 dias.
- **O P04 pode exigir nova comunicação.** *(Apêndices G1 e H1)* Sem registro de acesso, não se descarta que os dados de cerca de 1.300 colaboradores tenham sido consultados. Após nov/2026, um ex-colaborador continuaria com acesso se nada mudar.
- **O crédito tem uma camada regulatória a mais.** *(Apêndice H1)* A operação é feita com instituição financeira parceira regulada pelo Banco Central, que exige modelos documentados e auditáveis. A ficha do modelo não é atualizada desde ago/2025.
- **Afastamentos podem incluir dados de saúde.** *(Suposição)* O A4 lista "afastamentos" sem detalhar o motivo.
- **O Jurídico não comporta aprovar tudo.** *(Apêndice H1)* Tem 2 advogados de privacidade e pede priorização por nível de risco. Por isso as alçadas do memorando variam por risco. *(Escolha)*

### 2.4 Modelo de governança

- **Hub-and-spoke com autonomia graduada.** *(Escolha)* Sustentado pela pesquisa: entre as equipes, a opção "área central define padrões e plataforma, unidades desenvolvem" teve 37%; a centralização total foi defendida por 73% das lideranças do Corporativo; a autonomia das unidades por 60% das lideranças do Digital e 57% das de Serviços Financeiros. *(Apêndice C1)*
- **A autoavaliação de governança é otimista onde há mais risco.** *(Apêndice C1)* A diferença entre lideranças e equipes em governança é 1,4 ponto no Digital (3,6 contra 2,2) e em Serviços Financeiros (4,2 contra 2,7). As notas são percepção, não diagnóstico.

---

## 3. Escalabilidade e receita

### 3.1 Quais projetos mais impactaram em receita?

**Nenhum tem impacto em receita comprovado.** Só dois declaram benefício de receita; os demais declaram custo ou perda evitados. Finanças não validou nenhum número. *(Apêndice E2)*

| Iniciativa | Tipo declarado | Valor declarado/ano | Por que não se sustenta |
|---|---|---:|---|
| P03 Atrasos | Custo evitado | R$ 65,0 mi | Atribui ao agente toda a queda de 23% para 6%, que coincide com a volta da transportadora anterior (C2). O atraso voltou a 10,3% em ago/2026 com o agente em operação (B1) |
| P07 Antifraude | Perda evitada | R$ 30,0 mi | Considera fraude toda transação bloqueada; os dados são do próprio fornecedor |
| **P02 Recompra** | **Receita** | **R$ 25,1 mi** | Soma todas as compras de quem recebeu a campanha, sem grupo de controle. O modelo escolhe os clientes mais propensos, então a conversão maior (2,0% contra 0,9%) já era esperada. É valor de compra (GMV), não receita do grupo |
| **P06 Crédito** | **Receita** | **R$ 15,6 mi** | Soma toda a receita de juros da carteira, como se não existisse sem o modelo, e ignora o saldo inadimplente de R$ 3,9 mi |
| P01 SAC | Custo evitado | R$ 3,2 mi | O quadro do SAC não foi reduzido desde fev/2026 |
| P08 RH | Custo evitado | R$ 1,6 mi | Supõe que cada consulta substitui um contato com o RH |
| P04 Escala | Custo evitado | R$ 0,8 mi | Relato do criador e de gerentes, sem medição |
| P05 Assinaturas | — | Não informado | Sem área responsável |
| **Total** | | **R$ 141,4 mi** | Equivale a 39% do lucro líquido (R$ 360 mi) e a 4,4% do GMV |

**Premissas adotadas:**

- **P06 é a iniciativa com receita mais observável**, porque a carteira cresceu de R$ 38,5 mi para R$ 63,7 mi entre set/2025 e ago/2026 (F1). Mas o ganho atribuível ao modelo é desconhecido, e o risco cresce junto: inadimplência de 3,1% para 6,1% (pico de 6,6% em jun) e saldo inadimplente de R$ 1,2 mi para R$ 3,9 mi. *(Apêndice F1)*
- **P02 não mostra efeito no indicador que prometeu mover.** *(Apêndices A1 e B1)* A meta era dobrar a recompra em 12 meses. A participação de clientes recorrentes nos pedidos ficou entre 3,3% e 4,0% desde nov/2025, na mesma faixa dos meses anteriores (3,1% a 3,6% entre jun e out/2025). *(Calculado)* Isso não prova ausência de efeito, mas não sustenta o valor declarado.
- **A receita do grupo no marketplace é a comissão, não o GMV.** *(Apêndice E2, Referências)* Comissão média de 12% sobre as vendas de sellers. Qualquer benefício de receita precisa ser convertido para essa base.
- **Benefícios não certificados ficam fora das apresentações oficiais.** *(Escolha)*

### 3.2 O que já está deployado?

*(Apêndice A1)*

| Status | Iniciativas | Desde |
|---|---|---|
| **Produção** | P06 Crédito a sellers (decisão automática até R$ 50 mil) | set/2025 |
| | P07 Antifraude (todas as transações do marketplace) | set/2025 |
| | P01 Agente de SAC, **produção parcial**: 40% dos contatos do chat | fev/2026 |
| **Piloto** | P02 Recompra (cerca de 500 mil clientes/mês) | nov/2025 |
| | P03 Agente de atrasos (na prática, todos os pedidos atrasados) | mar/2026 |
| | P08 Assistente de RH | mai/2026 |
| **Em uso, sem conhecimento da TI** | P04 App de escala (45 lojas do Sudeste) | abr/2026 |
| | P05 Assinaturas individuais (420 em ago/2026) | set/2025 |

**Premissa:** "piloto" no inventário não significa escopo limitado. P02 e P03 operam em escala completa e são tratados no memorando como produção. *(Escolha)*

### 3.3 Premissas de escala

- **Escalar é passar por portões, não ampliar já.** *(Escolha)* Nenhuma iniciativa é ampliada em 5/11. O P01 fica em 40% e sobe a 60% e 80% por dois portões; o P04 é transferido para a empresa e só vai a outras regionais depois de RIPD e piloto medido.
- **Dobrar o P01 tende a dobrar o custo variável.** *(Calculado, Apêndice E1)* O custo de tokens é proporcional ao volume de conversas. Sem reduzir o contexto, ir de 40% a 80% levaria os R$ 95 mil/mês de tokens a cerca de R$ 190 mil.
- **A ampliação do P01 já tinha sido aprovada.** *(Apêndice A2)* Aprovada em mai/2026 e suspensa desde jul/2026. O pedido da pauta é uma retomada.
- **Há demanda declarada para escalar P03 e P04.** *(Apêndices A4 e C2)* Logística quer levar o P03 às entregas das lojas físicas; gerentes de outras regiões pediram o P04. O P04 está em 45 das cerca de 320 lojas.
- **A consolidação acontece dentro da escala.** *(Escolha)* Um único núcleo faz as correções, e cada iniciativa corrigida migra para o padrão comum, já que o grupo não tem pessoas para dois times.
- **Capacidade técnica por unidade.** *(Apêndices A2 a A5 e C2)* Digital tem cerca de 25 pessoas de dados; Serviços Financeiros, 2 cientistas de dados e 1 analista de risco no P06; Logística, 1 analista de automação; Lojas, nenhuma após a saída do criador do P04; a TI não tem especialistas em IA.

---

## 4. Outros

### 4.1 Quais são os dados disponíveis?

**Material de análise (apêndices):**

| Apêndice | Conteúdo | Limitação |
|---|---|---|
| A1 | Inventário das 8 iniciativas: status, tecnologia, dados pessoais, monitoramento | Levantamento de set/2026 |
| A2 a A5 | Fichas do P01, P03, P04 e P06 | P02, P05, P07 e P08 não têm ficha; a do P06 está desatualizada desde ago/2025 |
| B1 | Painel mensal do marketplace, jan/2025 a ago/2026: pedidos, GMV, atraso, nota, recompra | Amostra multiplicada por 200 (base pública Olist adaptada) |
| C1 | Pesquisa de maturidade: 247 respondentes de 495 | Autoavaliação anônima, não auditada |
| C2 | Entrevistas com 7 lideranças | Opiniões não verificadas |
| D1 | Mapa de tecnologia e 11 contratos | Sem valores de contrato |
| E1 | Custos mensais por iniciativa, set/2025 a ago/2026 | Reconstruídos por Finanças; consultoria de Logística fora da conta; preços de referência de mercado |
| E2 | Benefícios declarados pelas áreas | Não validados por Finanças |
| F1 | Monitoramento do P06: estabilidade das variáveis (PSI), aprovação, inadimplência, AUC | AUC com 3 meses de defasagem; estabilidade das variáveis só medida a partir de set/2026 |
| G1 | Registro de 7 incidentes | Casos anteriores a ago/2026 reconstituídos de chamados e mensagens |
| H1 | Nota do Jurídico sobre LGPD e requisitos mínimos | — |

**Dados operacionais que as iniciativas usam:** *(Apêndice D1)* data lake do marketplace (P01, P02); data warehouse corporativo abastecido por extração mensal (P06); APIs do sistema de transporte e de 4 transportadoras, cada uma em formato diferente (P03); planilha exportada do sistema de RH (P04, P08); transações do gateway de pagamento (P07).

**Dados que faltam para medir valor:** grupo de controle em qualquer iniciativa; registro das decisões do P03; métricas de qualidade das respostas do P01; indicadores independentes do P07; valores dos contratos; custo da consultoria. *(Apêndices A1 a A5, D1 e E1)*

### 4.2 Leitura dos dados

- **A queda do atraso tem outra explicação.** *(Apêndices B1 e C2)* O atraso caiu de 23,0% em mar/2026 para 6,3% em abr/2026, mês da volta à transportadora anterior. Depois oscilou entre 1,3% e 10,3%, com o agente em operação o tempo todo.
- **O modelo de crédito perdeu discriminação e o corte não reagiu.** *(Apêndice F1)* AUC de 0,79 para 0,71; aprovação parada entre 62% e 63%. A variável "% de pedidos com atraso" teve PSI de 0,95 em mar/2026, bem acima do limite de mudança significativa (0,25). O time chamou isso de "oscilação pontual, já normalizada".
- **O modelo de crédito pune sellers pelo erro logístico da própria empresa.** *(Apêndice G1)* Nos três estados da troca de transportadora, a aprovação caiu de 61% em fev para 43–45% de abr a ago/2026. Na mesma faixa de faturamento e nota, a aprovação vai de 67% (Sul e Sudeste) a 39% (Norte).
- **Uso de ferramentas externas.** *(Apêndice C1)* 61% dos respondentes usam; dos usuários, 24% já inseriram dados de clientes ou colaboradores (38% nas Lojas; 74% de uso no Digital).

### 4.3 Fontes e formato

- **Nenhuma fonte externa é necessária.** *(Apêndice H1)* O prazo de 3 dias úteis da ANPD, que antes vinha de fonte externa, consta da nota do Jurídico.
- **Valores e modelagem financeira ficam de fora.** *(Enunciado)* Alçadas e portões são qualitativos; os números aparecem só como fundamento.
- **Datas sem dia exato** (congelamento, saída do criador do P04, renovações) foram tratadas pelo mês. *(Escolha)*
- **"Oficializar" o P04 significa transferi-lo para a empresa**, não estendê-lo como está. *(Escolha)*
- **A oitava iniciativa é o P05.** *(Apêndice A1)* Confirmado pelo inventário.

---

## Anotações

<!-- Use este espaço para comentários, dúvidas ou premissas novas. -->

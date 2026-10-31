# MEMORANDO EXECUTIVO

| | |
|---|---|
| **Para** | Comitê Executivo do Grupo Meridiano |
| **De** | Marina Toledo, Head de IA |
| **Reunião** | 5 de novembro de 2026 |
| **Assunto** | Retomada das iniciativas de IA: recomendação, modelo operacional, mandato da área central e direcionamento do portfólio |
| **Classificação** | Confidencial. Uso restrito ao comitê |

## 1. Recomendação: escalar com guardrails

**Recomendo que o comitê escolha escalar com guardrails.** O congelamento de agosto deixa de ser uma proibição geral e passa a ser um portão de entrada: nenhuma iniciativa nova entra em produção, e nenhuma iniciativa existente amplia volume, escopo ou base de usuários, sem cumprir os oito padrões mínimos do Anexo 2 e sem um plano de medição aprovado pela Controladoria. Escalar com guardrails não significa ampliar já. Significa trocar uma regra que proíbe tudo e não controla nada por uma regra que libera apenas o que passa pelo portão.

**Por que não consolidar primeiro.** Consolidar primeiro tem uma vantagem real: as economias de duplicidade (Provedor X contratado duas vezes, R$ 85 mil/mês em nuvem sem dono, até R$ 46 mil/mês em 420 assinaturas sem centro de custo) são imediatas e verificáveis. Essas economias, porém, não dependem do congelamento e estão incorporadas à recomendação. Contra consolidar primeiro pesam quatro fatos:

- **O risco já está em produção.** Manter o congelamento não desliga o aplicativo de escala (CPF e afastamentos de cerca de 1.300 colaboradores em conta pessoal, com senha compartilhada por 45 gerentes), não limita os reembolsos do agente de atendimento (1.840 indevidos em junho, cerca de R$ 312 mil) e não corrige o modelo de crédito (inadimplência de 3,1% para 6,6%). Um plano que só fica de pé em fevereiro deixa esses riscos sem dono por mais três meses.
- **O calendário decide por nós.** O analista que mantém o aplicativo de escala sai em novembro; o contrato da consultoria que opera o agente de atrasos vence em 31 de dezembro, com as credenciais das transportadoras em nome dela. Não decidir até fevereiro equivale a decidir por omissão.
- **A proibição não contém o uso.** 61% dos respondentes já usam ferramentas de IA não fornecidas pela empresa e 24% inseriram nelas dados de clientes ou colaboradores (38% nas Lojas). Seis meses de congelamento aumentam o uso fora do controle, não o reduzem.
- **Governança escrita sem casos reais tende a ser contornada.** Os padrões ficam melhores quando são testados nas correções das oito iniciativas existentes.

**Como evitamos o modo de falha de escalar.** O risco de escalar é ampliar iniciativas cujos defeitos estão documentados. Por isso os guardrails são condição de entrada, não meta de chegada: o primeiro ciclo é de correção, a ampliação acontece por etapas com critérios de passagem definidos antes, e a Head de IA e o Encarregado de Dados (DPO) têm autoridade para suspender qualquer iniciativa em caso de incidente. A consolidação não é abandonada. Ela passa a ser feita dentro da escala: cada iniciativa corrigida migra para o padrão comum, e o inventário, o controle de custos e as renegociações de contrato avançam com o mesmo núcleo que conduz as correções. Não serão necessários dois times.

### Resposta aos dois pedidos da pauta

| Pedido | Decisão | Condições |
|---|---|---|
| **Digital:** ampliar o agente de atendimento de 40% para 80% do chat | **Não aprovado como apresentado. Aprovado em duas etapas condicionadas** (40%, depois 60% e por fim 80%). | Permanece em 40%. Autonomia de reembolso retirada de imediato até existirem limite por cliente e por dia e verificação de status do pedido. Passa a 60% após o Portão 1 (isolamento de dados entre sessões testado por equipe independente, conjunto de avaliação externo à equipe, métricas de qualidade, redução do contexto enviado por mensagem). Passa a 80% após o Portão 2 (ciclo estável em 60%, com grupo de controle demonstrando ganho certificado pela Controladoria). |
| **Lojas:** oficializar e estender o aplicativo de escala | **Oficialização aprovada já, entendida como transferência para a empresa. Extensão condicionada.** | Antes da saída do analista: código e dados migrados para repositório e nuvem corporativos, senha compartilhada substituída por acesso individual, dono de negócio nomeado nas Lojas e sustentação assumida pela área central. Extensão a outras regionais após relatório de impacto (RIPD) aprovado e piloto medido nas 45 lojas contra lojas comparáveis sem o aplicativo. |

### Resposta às condições do CFO

- **"Ninguém tem grupo de controle, ninguém tem linha de base."** A sistemática da Seção 5 torna obrigatório um contrafactual para qualquer ampliação. Comparações de antes e depois deixam de ser aceitas como evidência. Os R$ 141 milhões declarados saem das apresentações oficiais até serem certificados pela Controladoria.
- **"Economia nas iniciativas existentes antes de um centro de custo novo."** O primeiro ciclo é desenhado para gerar economia verificável sem criar estrutura: redução do contexto enviado ao modelo no agente de atendimento (hoje cerca de 30 mil tokens por mensagem), uso de modelos menores nas etapas triviais do agente de atrasos, desligamento da nuvem sem dono, unificação do contrato do Provedor X, cancelamento das assinaturas individuais e bloqueio dos reembolsos indevidos. A área central começa com pessoas cedidas pelas áreas e cresce somente contra economia certificada (Seção 3).
- **Disciplina de contratos.** Nenhum contrato de IA plurianual ou com multa rescisória é assinado sem aprovação conjunta de CFO, CIO e Head de IA. O antifraude, com 36 meses e multa até agosto de 2028, é o exemplo que não queremos repetir.

## 2. Modelo operacional de IA

### Alternativas avaliadas

| Critério | Centralizado na TI (proposta do CIO) | Padrão do Digital com autonomia das unidades (proposta do Digital) | Descentralizado (situação atual) | **Hub-and-spoke com autonomia graduada (recomendado)** |
|---|---|---|---|---|
| Controle de risco | Alto no papel, limitado pela falta de especialistas | Baixo: o padrão vem da área do incidente de julho | Baixo: gerou o portfólio atual | Alto: padrões e portão centrais, aplicados por nível de risco |
| Velocidade | Baixa: gargalo único | Alta no Digital, nula em Lojas e Logística | Alta e sem controle | Alta onde há maturidade, apoiada onde não há |
| Pessoas e orçamento | Exige parceiro externo e plataforma de fornecedor único | Usa o time de 25 pessoas do Digital | Sem custo novo visível | Núcleo pequeno, com pessoas cedidas pelas áreas |
| Aderência à maturidade (1,6 a 3,2) | Ignora o time do Digital | Lojas (1,6) não absorve o padrão | Ignora a diferença | Autonomia proporcional à maturidade demonstrada |
| Aceitação | 73% das lideranças corporativas; rejeitado pelas unidades | 60% do Digital, 57% de Serv. Financeiros | Nenhuma área a defende | Modelo mais votado pelas equipes (37%) |

**Justificativa.** A centralização na TI concentraria a decisão em uma área que reconhece não ter especialistas e que propõe resolver a falta com um fornecedor único, repetindo a dependência contratual do antifraude. Adotar o padrão do Digital colocaria o padrão nas mãos da área com o incidente de julho e com a maior divergência de autoavaliação em governança (1,4 ponto), e não serve a Lojas e Logística, que não têm equipe técnica. O modelo hub-and-spoke separa três papéis: quem define e verifica o padrão (área central), quem opera a infraestrutura (TI) e quem é dono do caso de uso e do benefício (unidade).

### Desenho e papéis

- **Área central de IA (hub), ligada à presidência:** padrões, inventário único, portão de entrada, classificação de risco, sistemática de medição, gestão do portfólio, gestão de custos de IA e parecer sobre contratos.
- **TI corporativa:** opera a plataforma comum, identidade e acesso, cofre de segredos, segurança e integração de dados. O CIO é dono da operação da plataforma; a área central é dona do padrão.
- **Unidades (spokes):** cada iniciativa tem um dono de negócio na unidade, responsável pelo benefício, pelo orçamento do caso e pela adoção. O custo é alocado ao centro de custo da unidade.
- **Segunda linha:** Jurídico/DPO e Riscos aprovam base legal, RIPD e riscos regulatórios. A Auditoria Interna verifica o cumprimento por amostragem.

**Autonomia graduada.** A autonomia de cada unidade depende da maturidade demonstrada, não do porte da área:

| Nível | Unidades hoje | Quem constrói | Quem aprova risco baixo e médio |
|---|---|---|---|
| 1. Apoiado | Lojas, Logística | Célula de entrega da área central | Área central |
| 2. Assistido | Corporativo (TI, RH) | Unidade, com revisão de desenho pela área central | Área central |
| 3. Delegado | Digital, Serviços Financeiros | Unidade | Unidade, com auditoria por amostra da área central |

O risco alto sobe sempre ao Comitê de IA, qualquer que seja o nível. Uma unidade sobe de nível após dois ciclos trimestrais sem desvio grave e com medição certificada, e desce de nível em caso de incidente com causa em descumprimento de padrão.

**Plataforma.** O comitê não precisa escolher hoje entre a arquitetura do Digital e uma plataforma de fornecedor único. Até a renovação da primeira nuvem, em março, valem padrões de interface nas duas nuvens: cofre de segredos corporativo, registro centralizado de chamadas aos modelos, identificação de custo por iniciativa e acesso por identidade corporativa. A plataforma de referência será escolhida até março por critérios explícitos (segurança, custo por transação, portabilidade e cláusula de saída), aproveitando os vencimentos de dezembro, janeiro, março e junho. Componentes do Digital podem ser adotados como padrão do grupo se vencerem essa avaliação.

### Diretrizes de relacionamento entre os times

1. Toda iniciativa entra pelo inventário único e recebe classificação de risco em até dez dias úteis.
2. Cada iniciativa tem um dono de negócio e um dono técnico nomeados. Sem os dois, não passa pelo portão.
3. A área central não executa o roadmap das unidades de nível 2 e 3. Ela define o padrão, verifica e apoia.
4. Antes de construir, a unidade verifica no inventário se já existe componente reutilizável. Duplicar uma função existente, como o assistente de RH em relação ao agente de atendimento, exige justificativa aprovada.
5. O custo de IA é mostrado mensalmente por iniciativa e por unidade. Recurso sem dono identificado é desligado após aviso.
6. Divergências entre unidade e área central sobem ao Comitê de IA, que decide na reunião seguinte.
7. Um fórum mensal de portfólio reúne donos de iniciativa, TI, Jurídico e Controladoria para acompanhar indicadores e decidir portões.

## 3. Mandato da área central e alçadas

### Mandato

A área central de IA responde por cinco entregas: (1) **inventário único** de iniciativas, modelos, dados, contratos e ferramentas; (2) **padrões e portão de entrada**; (3) **classificação e acompanhamento de risco**, com o Jurídico/DPO; (4) **sistemática de medição** de custo e valor, com a Controladoria; (5) **gestão do portfólio**, com a recomendação trimestral de manter, corrigir, desligar ou ampliar cada iniciativa. Além disso, opera a célula de entrega das unidades de nível 1. A área central não é dona dos benefícios das unidades nem uma fábrica de projetos.

**Poderes necessários:** registro obrigatório de toda iniciativa e ferramenta de IA; acesso a custos, contratos e registros técnicos; suspensão imediata de iniciativa em incidente (compartilhada com o DPO); parecer obrigatório em contratos de IA; e bloqueio de compra de ferramentas de IA fora do catálogo homologado, inclusive por cartão corporativo.

### Pessoas e orçamento

Para respeitar a restrição do CFO, a área central não cria um centro de custo com dezenas de pessoas. A estrutura cresce em duas fases:

- **Fase 1 (novembro a março), núcleo de seis a oito pessoas, majoritariamente cedidas:** Head de IA; arquiteto de plataforma cedido pela TI; engenheiro de ML/LLM cedido pelo Digital; analista de valor e custos cedido pela Controladoria, o que dá a Finanças a autoria da medição; um dos dois advogados de privacidade com dedicação parcial; e duas contratações para a célula de entrega, que absorvem a sustentação do aplicativo de escala e a internalização do agente de atrasos. Essas contratações são financiadas com parte do orçamento hoje destinado à consultoria de Logística, que não será renovada nas mesmas condições.
- **Fase 2 (a partir de abril):** novas contratações apenas em tranches aprovadas pelo CFO contra economia certificada pela Controladoria. Sem economia certificada, não há tranche.

### Comitê de IA e matriz de alçadas

O Comitê de IA é um subcomitê do comitê executivo. Reúne-se mensalmente com CFO, CIO, Jurídico/DPO, Head de IA (que o secretaria) e o diretor da unidade proponente, e reporta à CEO.

| Decisão | Propõe | Aprova | Consultado | Informado |
|---|---|---|---|---|
| Classificação de risco de iniciativa | Unidade | Head de IA | Jurídico/DPO | Comitê de IA |
| Iniciativa de risco baixo (sem dado pessoal, sem ação autônoma perante terceiros) | Unidade | Dono da unidade (nível 3) ou Head de IA (níveis 1 e 2) | TI | Inventário |
| Iniciativa de risco médio (dado pessoal ou contato com cliente sob supervisão humana) | Unidade | Head de IA + DPO | TI, Controladoria | Comitê de IA |
| Iniciativa de risco alto (decisão automatizada sobre pessoas, sellers ou crédito; ação financeira autônoma; dado sensível) | Unidade | Comitê de IA | Jurídico, Riscos | CEO |
| Ampliação de volume, escopo ou usuários | Dono da iniciativa | Mesma alçada do risco, após portão de medição certificado | Controladoria | Comitê de IA |
| Contrato de IA de até 12 meses e sem multa | Unidade/Compras | CIO | Head de IA | Controladoria |
| Contrato plurianual, com multa ou exclusividade | Unidade/Compras | CFO + CIO + Head de IA | Jurídico | Comitê executivo |
| Suspensão por incidente | Qualquer pessoa | Head de IA ou DPO, de imediato | Dono da iniciativa | Comitê de IA e CEO |
| Reativação após suspensão | Dono da iniciativa | Comitê de IA | DPO, TI | CEO |
| Certificação de benefício | Dono da iniciativa | Controladoria | Head de IA | Comitê de IA |
| Padrões técnicos e exceções | Head de IA e CIO | Head de IA (padrão); Comitê de IA (exceção) | Unidades | Todos os times |

**Incidentes.** Todo incidente com dado pessoal é comunicado ao DPO em até 24 horas da detecção. A comunicação à ANPD e aos titulares segue o prazo de três dias úteis da Resolução CD/ANPD nº 15/2024; o caso de julho levou 22 dias.

## 4. Direcionamento das oito iniciativas

**Critérios.** Cada iniciativa foi avaliada em cinco critérios (detalhe no Anexo 1): risco não controlado, evidência de valor, sustentabilidade operacional (dono, pessoas e dependência de terceiros), eficiência de custo e restrição contratual. A regra de decisão é sequencial. Primeiro, risco não controlado leva a **corrigir**, com suspensão da parte arriscada, qualquer que seja o valor ou o custo; é por isso que a iniciativa mais barata, o aplicativo de escala, é tratada como prioridade. Segundo, sem valor plausível e sem dono, a iniciativa é **desligada**. Terceiro, com risco controlado e valor plausível, é **mantida** com medição. Por fim, **ampliar** só ocorre depois do portão de medição. Nesta reunião, nenhuma iniciativa é ampliada; duas recebem caminho condicionado de ampliação.

| # | Iniciativa (unidade) | Direção | Fundamento e ações |
|---|---|---|---|
| 1 | Agente de atendimento (Digital) | **Corrigir**; ampliação condicionada | Incidente de dados em julho e reembolsos sem limite. Retirar já a autonomia de reembolso; isolar dados entre sessões; avaliar com conjunto independente; substituir o envio da política completa por recuperação dos trechos pertinentes. Medir resolução verificada (sem recontato), satisfação e custo por conversa resolvida, com grupo de controle. |
| 2 | Modelo de recompra (Digital) | **Manter**; corrigir a medição | Risco baixo, mas o benefício declarado soma o GMV de quem recebeu a campanha, sem contrafactual. Instituir grupo de controle aleatório permanente; benefício passa a ser a receita incremental contra esse grupo. Confirmar base legal para uso de dados de clientes. |
| 3 | Modelo de limite de crédito a sellers (Serv. Financeiros) | **Corrigir com urgência** | AUC de 0,79 para 0,70, inadimplência de 3,1% para 6,6% e aprovação fixa em 62–63%, sinal de corte que não reage ao risco. Novos limites e aumentos passam a ter revisão humana com política conservadora; validação independente do modelo; recalibração; retirada ou justificativa documentada da variável estado; explicação das recusas e canal de revisão (LGPD, art. 20), começando pelo seller sem resposta desde junho. Reclassificado como risco alto. |
| 4 | Antifraude de fornecedor (Serv. Financeiros) | **Manter**; medir de forma independente | Contrato até agosto de 2028 com multa: desligar custa mais do que manter. Maior item de custo, medido só pelo painel do fornecedor. Criar medição própria (perdas por fraude, falsos positivos, amostra revisada manualmente) e preparar com antecedência a decisão de renovação ou saída. |
| 5 | Assistente de RH (TI corporativa) | **Manter sem ampliar**; migrar | Duplica a função do agente de atendimento em outra nuvem e com outro provedor. Mantido no escopo atual, com base legal confirmada para dados de colaboradores, e migrado para a plataforma de referência na janela de renovação da nuvem. |
| 6 | Agente de tratativa de atrasos (Logística) | **Corrigir (internalizar)**; extensão às lojas suspensa | Credenciais e plataforma em nome da consultoria, nenhuma pessoa interna opera o fluxo, contrato vence em 31/12. Transferir credenciais para o cofre corporativo em novembro; renovar a consultoria por prazo curto, só para transição; usar modelos menores nas etapas triviais. O benefício declarado ignora que o atraso caiu de 23% para 6% com a volta da transportadora anterior: medir com amostra de pedidos atrasados sem tratativa automática. |
| 7 | Aplicativo de escala de turnos (Lojas) | **Corrigir já (oficializar)**; extensão condicionada | Maior risco do portfólio: dados de cerca de 1.300 colaboradores, possivelmente incluindo dados de saúde em afastamentos, em conta pessoal com senha compartilhada, e autor de saída. Migrar antes da saída do analista; acesso individual; minimizar dados; RIPD. Medir contra lojas comparáveis sem o aplicativo. |
| 8 | Assinaturas individuais de IA (todas as unidades)¹ | **Desligar** e substituir | 420 assinaturas sem centro de custo e 24% de usuários inserindo dados pessoais. Cancelar as assinaturas pagas por cartão, bloquear a compra e oferecer ferramenta homologada, negociada na renovação da suíte de produtividade em janeiro, com orientação de uso de dados. |

¹ Tratamos como oitava iniciativa o uso de ferramentas de IA por assinatura individual registrado no inventário. Se o Apêndice A classificar a oitava iniciativa de outra forma, a regra de decisão se aplica da mesma maneira.

Fora das oito iniciativas, a área central também desliga os recursos de nuvem sem dono identificado e unifica os dois contratos do Provedor X.

## 5. Como os resultados passarão a ser medidos

1. **Ficha de valor antes do portão.** Toda iniciativa registra hipótese de valor, métrica principal ligada a uma linha do resultado (custo de SAC, perdas de crédito, reembolsos, receita incremental, horas de gestão nas lojas), linha de base, desenho do contrafactual, custo total e indicadores de risco e qualidade.
2. **Hierarquia de evidência.** Em ordem de preferência: grupo de controle aleatório (recompra, atendimento); implantação escalonada comparada entre grupos (lojas, regionais); comparação com grupo pareado (atrasos, antifraude). Comparações de antes e depois não são aceitas para certificação.
3. **Quatro estágios de benefício.** Declarado (pela unidade), mensurado (pela ficha), certificado (pela Controladoria) e realizado (visível no orçamento, como redução de quadro, hora extra ou perda). Só benefício certificado sustenta ampliação; só benefício realizado entra no orçamento.
4. **Custo por unidade de resultado.** Toda chamada a modelo passa pelo registro central com identificação da iniciativa. Cada iniciativa tem um custo por unidade de resultado, como custo por conversa resolvida ou por pedido tratado.
5. **Risco com o mesmo peso do valor.** O painel mostra, ao lado do valor, incidentes, reembolsos indevidos, desempenho e desvio dos modelos, efeitos por grupo e reclamações.
6. **Cadência e critérios de parada.** Painel mensal no Comitê de IA; revisão trimestral do portfólio com nova decisão para cada iniciativa. Os critérios de suspensão e desligamento são definidos na ficha antes da entrada em produção, não depois do problema.

### Deliberações solicitadas ao comitê

1. Substituir o congelamento pelo portão de entrada e pelos padrões mínimos do Anexo 2.
2. Aprovar as respostas aos pedidos do Digital e das Lojas (Seção 1).
3. Aprovar o modelo hub-and-spoke, o mandato da área central e a matriz de alçadas.
4. Autorizar a Fase 1 da área central com pessoas cedidas e duas contratações financiadas pela redução da consultoria.
5. Aprovar o direcionamento das oito iniciativas e o bloqueio de compra de ferramentas de IA fora do catálogo.

<!-- pagebreak -->

## Anexo 1. Matriz de avaliação das oito iniciativas

Leitura: **Crítico** exige ação antes de qualquer outra decisão; **Atenção** exige correção dentro do ciclo; **Adequado** não impede a direção proposta.

| # | Iniciativa | Risco não controlado | Evidência de valor | Sustentabilidade operacional | Eficiência de custo | Restrição contratual | Direção |
|---|---|---|---|---|---|---|---|
| 1 | Agente de atendimento | **Crítico**: exposição de dados em julho; reembolsos sem limite | Atenção: 55% de resolução declarada, sem métrica de qualidade, homologação com 50 perguntas da própria equipe; quadro do SAC inalterado | Adequado: time do Digital | Atenção: cerca de 30 mil tokens por mensagem | Adequado | Corrigir; ampliar por portões |
| 2 | Modelo de recompra | Adequado; base legal a confirmar | Atenção: benefício calculado sobre GMV dos expostos | Adequado: time do Digital | Adequado | Adequado | Manter |
| 3 | Limite de crédito a sellers | **Crítico**: desempenho em queda, variável geográfica, recusas sem explicação | Atenção: perda crescente de carteira | Atenção: equipe trata a queda como oscilação | Atenção: saldo inadimplente de R$ 1,2 mi para R$ 3,9 mi | Adequado | Corrigir com urgência |
| 4 | Antifraude de fornecedor | Atenção: desempenho visto só pelo fornecedor | Atenção: sem medição independente | Atenção: dependência do fornecedor | Atenção: maior item do portfólio | **Crítico**: 36 meses com multa até ago/2028 | Manter e medir |
| 5 | Assistente de RH | Atenção: base legal de dados de colaboradores | Atenção: sem medição | Adequado: TI | Atenção: nuvem e provedor duplicados | Atenção: vencimento de nuvem em 2027 | Manter sem ampliar; migrar |
| 6 | Agente de atrasos | Atenção: credenciais com terceiro | Atenção: benefício confundido com a volta da transportadora | **Crítico**: ninguém interno opera; contrato vence em 31/12 | Atenção: modelo de maior capacidade em todas as oito etapas | **Crítico**: vencimento em dezembro | Corrigir e internalizar |
| 7 | Aplicativo de escala | **Crítico**: dados de 1.300 pessoas em conta pessoal, senha compartilhada | Atenção: uso comprovado, valor não medido | **Crítico**: autor sai em novembro | Adequado: R$ 600/mês | Adequado | Corrigir já; ampliar por portão |
| 8 | Assinaturas individuais | **Crítico**: dados de clientes e colaboradores em ferramentas externas | Atenção: sem medição | Atenção: sem dono | Atenção: até R$ 46 mil/mês sem centro de custo | Adequado | Desligar e substituir |

## Anexo 2. Portão de entrada e calendário

### Padrões mínimos (guardrails) exigidos para entrar em produção ou ampliar

| # | Padrão | Verificação |
|---|---|---|
| 1 | Registro no inventário único, com dono de negócio e dono técnico nomeados | Área central |
| 2 | Contas, repositórios e credenciais corporativos; segredos no cofre corporativo; acesso individual por identidade corporativa | TI |
| 3 | Base legal documentada e RIPD quando houver dado pessoal; minimização de dados | Jurídico/DPO |
| 4 | Limites de ação autônoma (valor, frequência, por cliente) e revisão humana para decisões de alto impacto | Área central |
| 5 | Avaliação de qualidade com conjunto de teste independente da equipe construtora, incluindo testes de vazamento de dados | Área central |
| 6 | Monitoramento em produção, critérios de suspensão definidos e plano de resposta a incidentes alinhado ao prazo da ANPD | TI + DPO |
| 7 | Ficha de valor com linha de base e contrafactual aprovados pela Controladoria | Controladoria |
| 8 | Custo identificado por iniciativa, com centro de custo da unidade e custo por unidade de resultado | Controladoria + TI |

### Calendário

| Quando | Marco |
|---|---|
| Novembro de 2026 | Autonomia de reembolso retirada; aplicativo de escala migrado antes da saída do analista; credenciais das transportadoras no cofre corporativo; revisão humana no crédito; assinaturas individuais bloqueadas; nuvem sem dono desligada |
| Dezembro de 2026 | Inventário único completo; consultoria de Logística renovada só para transição; contratos do Provedor X unificados; fichas de valor das oito iniciativas |
| Janeiro de 2027 | Ferramenta de IA homologada incluída na renovação da suíte de produtividade; Portão 1 do agente de atendimento |
| Março de 2027 | Plataforma de referência escolhida na renovação da primeira nuvem; primeira certificação de economia pela Controladoria; decisão sobre a Fase 2 |
| Junho de 2027 | Migração na renovação da segunda nuvem; Portão 2 do agente de atendimento e decisão de extensão do aplicativo de escala, conforme medição |

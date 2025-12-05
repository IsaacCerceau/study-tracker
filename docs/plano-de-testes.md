# Plano de Testes — Study Tracker

## Objetivo
Definir casos de teste para verificar o funcionamento das principais funcionalidades da aplicação.

---

## Casos de Uso Considerados
1. UC01 — Registrar Estudo
2. UC02 — Ver Gráficos
3. UC03 — Definir Meta Semanal
4. UC04 — Visualizar Alerta de Progresso

---

## UC01 — Registrar Estudo

| ID  | Ação                          | Entrada                                   | Resultado Esperado                                        |
|-----|-------------------------------|-------------------------------------------|-----------------------------------------------------------|
| CT01 | Registrar estudo válido       | Matéria: Matemática, Horas: 2, Data: hoje | Registro salvo no CSV e mensagem “✅ Registro salvo...”   |
| CT02 | Matéria vazia                | Matéria: "", Horas: 2, Data: hoje         | Mensagem de erro: “Preencha a matéria...”                |
| CT03 | Horas = 0                    | Matéria: Matemática, Horas: 0, Data: hoje | Mensagem de erro: “...horas maiores que zero.”           |

---

## UC02 — Ver Gráficos

| ID  | Ação                                    | Entrada                          | Resultado Esperado                                  |
|-----|-----------------------------------------|----------------------------------|-----------------------------------------------------|
| CT04 | Visualizar gráfico geral               | Selecionar “Todas”               | Gráfico de barras com soma das horas por data      |
| CT05 | Visualizar gráfico por matéria         | Selecionar “Matemática”          | Gráfico apenas com registros de Matemática         |
| CT06 | Visualizar sem nenhum registro existente | CSV vazio                         | Mensagem “Nenhum dado registrado ainda!”           |

---

## UC03 — Definir Meta Semanal

| ID  | Ação                      | Entrada        | Resultado Esperado                            |
|-----|---------------------------|----------------|-----------------------------------------------|
| CT07 | Definir meta padrão       | Meta = 10      | Métrica mostra “Meta Semanal 10.0”            |
| CT08 | Alterar meta             | Meta = 15      | Campo atualizado e métrica mostra 15.0        |
| CT09 | Tentar meta inválida     | Meta negativa  | Campo não permite valores negativos (< 1)     |

---

## UC04 — Visualizar Alerta de Progresso

| ID  | Ação                               | Situação                  | Resultado Esperado                                   |
|-----|------------------------------------|---------------------------|------------------------------------------------------|
| CT10 | Abaixo da meta                    | 4h registradas, meta 10h  | Mensagem de aviso: “Você ainda não atingiu sua meta”|
| CT11 | Meta atingida ou superada         | 12h registradas, meta 10h | Mensagem de sucesso: “Parabéns!”                    |
| CT12 | Nenhum registro na semana         | 0h registradas            | Mensagem: “Nenhum registro de estudo nesta semana”  |

---

## Conclusão
Após a execução desses testes, espera-se que o sistema:
- Registre corretamente os estudos;
- Apresente gráficos consistentes com os dados cadastrados;
- Calcule o progresso semanal corretamente;
- Exiba mensagens adequadas de alerta e sucesso.

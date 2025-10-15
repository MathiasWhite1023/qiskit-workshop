# 📚 Estrutura Completa do Workshop - Guia Rápido

## ✅ Arquivos Principais do Workshop (USE ESTES!)

### 🌟 **DIA 1 - Fundamentos**
```
📓 notebooks/dia1_exercicio_guiado.ipynb
   └─ Para usar COM o instrutor
   └─ 4 exercícios progressivos sobre superposição e aleatoriedade

🏠 notebooks/dia1_exercicio_casa.ipynb
   └─ Para fazer SOZINHO em casa
   └─ 3 desafios + 1 projeto bônus avançado
```

### ⚡ **DIA 2 - Portas Lógicas**
```
📓 notebooks/dia2_exercicio_guiado.ipynb
   └─ Para usar COM o instrutor
   └─ 5 exercícios sobre CNOT, Toffoli, Rotações, Bell States

🏠 notebooks/dia2_exercicio_casa.ipynb
   └─ Para fazer SOZINHO em casa
   └─ 4 desafios incluindo projeto de calculadora quântica
```

---

## 📂 Arquivos Legados (Podem ser Ignorados)

Estes arquivos foram da iteração anterior e podem ser removidos ou arquivados:

```
❌ notebooks/aula1_gerador_aleatorio.ipynb
   └─ Versão antiga (antes da reorganização)
   
❌ notebooks/aula1_teoria_e_pratica.ipynb
   └─ Tentativa de separação teoria/prática (descontinuada)
   
❌ notebooks/exercicios/exercicios_para_casa.ipynb
   └─ Estrutura antiga de exercícios
```

**Recomendação:** Mover para pasta `notebooks/legado/` ou deletar.

---

## 🎯 Fluxo de Uso Correto

### Para Instrutores:

```
DIA 1:
1. Apresentar palestras sobre fundamentos
2. Abrir notebooks/dia1_exercicio_guiado.ipynb
3. Executar células junto com alunos
4. Explicar conceitos enquanto roda código
5. Ao final, mostrar notebooks/dia1_exercicio_casa.ipynb
6. Explicar os desafios para casa

DIA 2:
1. Revisar exercícios casa do Dia 1
2. Apresentar palestras sobre portas lógicas
3. Abrir notebooks/dia2_exercicio_guiado.ipynb
4. Executar células junto com alunos
5. Ao final, mostrar notebooks/dia2_exercicio_casa.ipynb
6. Explicar os desafios finais
```

### Para Alunos:

```
DIA 1:
📖 Manhã: Assistir palestras
💻 Tarde: Acompanhar dia1_exercicio_guiado.ipynb
🏠 Noite/Casa: Resolver dia1_exercicio_casa.ipynb

DIA 2:
📖 Manhã: Assistir palestras + revisar exercícios casa
💻 Tarde: Acompanhar dia2_exercicio_guiado.ipynb
🏠 Noite/Casa: Resolver dia2_exercicio_casa.ipynb
```

---

## 📊 Conteúdo Detalhado

### 🌟 Dia 1 - Fundamentos

#### Exercício Guiado (dia1_exercicio_guiado.ipynb):
- ✅ **Ex 1:** Primeira moeda quântica
  - Conceito: Superposição com Hadamard
  - Código: minha_primeira_moeda_quantica()
  
- ✅ **Ex 2:** Teste estatístico 1000 jogadas
  - Conceito: Validação estatística
  - Código: teste_moeda_1000_vezes()
  
- ✅ **Ex 3:** Gerador multi-bit (2-4 bits)
  - Conceito: Múltiplos qubits
  - Código: gerador_numeros_quanticos(n_bits)
  
- ✅ **Ex 4:** Análise qui-quadrado
  - Conceito: Teste de uniformidade
  - Código: analisar_distribuicao(n_bits)

#### Exercício Casa (dia1_exercicio_casa.ipynb):
- 🎲 **Desafio 1:** Dado quântico (1-6)
  - Implementar: dado_quantico_inteligente()
  
- 📈 **Desafio 2:** Testes estatísticos
  - Implementar: DetetiveAleatoriedade class
  
- 🎰 **Projeto Bônus:** Loteria quântica
  - Implementar: LoteriaQuantica class

---

### ⚡ Dia 2 - Portas Lógicas

#### Exercício Guiado (dia2_exercicio_guiado.ipynb):
- ✅ **Ex 1:** Demonstração CNOT
  - Conceito: Entrelaçamento controlado
  - Código: demonstrar_cnot()
  
- ✅ **Ex 2:** XOR quântico
  - Conceito: Porta lógica com CNOT
  - Código: xor_quantico()
  
- ✅ **Ex 3:** AND reversível
  - Conceito: Porta Toffoli (CCX)
  - Código: and_quantico_reversivel()
  
- ✅ **Ex 4:** Moeda customizada
  - Conceito: Rotações RY
  - Código: moeda_personalizada(prob)
  
- ✅ **Ex 5:** Estados de Bell
  - Conceito: Entrelaçamento máximo
  - Código: criar_estado_bell_phi_plus()

#### Exercício Casa (dia2_exercicio_casa.ipynb):
- 🔧 **Desafio 1:** Kit de portas lógicas
  - Implementar: NOT, AND, OR, XOR, NAND, NOR
  
- 🎰 **Desafio 2:** Probabilidades controladas
  - Implementar: moeda_customizada(), dado_enviesado()
  
- 🧬 **Desafio 3:** Entrelaçamento multi-qubit
  - Implementar: criar_estado_ghz(), criar_estado_w()
  
- 🏆 **Projeto Final:** Calculadora quântica
  - Implementar: meio_somador(), somador_completo(), somar_numeros()

---

## 🎓 Conceitos Cobertos

### Fundamentos (Dia 1):
- [x] Qubits e estados quânticos
- [x] Superposição
- [x] Porta Hadamard
- [x] Medição e colapso
- [x] Aleatoriedade quântica
- [x] Estatística qui-quadrado
- [x] Múltiplos qubits

### Avançado (Dia 2):
- [x] Porta CNOT (CX)
- [x] Porta Toffoli (CCX)
- [x] Rotações (RX, RY, RZ)
- [x] Estados de Bell
- [x] Entrelaçamento controlado
- [x] Portas lógicas reversíveis
- [x] Estados GHZ e W
- [x] Aritmética quântica

---

## 🛠️ Comandos Úteis

### Limpar Arquivos Legados:
```bash
# Criar pasta de legado
mkdir -p notebooks/legado

# Mover arquivos antigos
mv notebooks/aula1_gerador_aleatorio.ipynb notebooks/legado/
mv notebooks/aula1_teoria_e_pratica.ipynb notebooks/legado/
mv notebooks/exercicios/exercicios_para_casa.ipynb notebooks/legado/

# Remover pasta vazia
rmdir notebooks/exercicios
```

### Verificar Estrutura:
```bash
# Listar apenas arquivos principais
find notebooks -maxdepth 1 -name "dia*.ipynb" | sort

# Contar linhas de código
wc -l notebooks/dia*.ipynb
```

### Testar Notebooks:
```bash
# Executar todos os notebooks
jupyter nbconvert --to notebook --execute notebooks/dia1_exercicio_guiado.ipynb
jupyter nbconvert --to notebook --execute notebooks/dia2_exercicio_guiado.ipynb
```

---

## 📋 Checklist para Instrutor

### Antes do Evento:
- [ ] Revisar todos os 4 notebooks principais
- [ ] Testar execução completa de guiados
- [ ] Preparar slides das palestras
- [ ] Verificar tempo de cada exercício
- [ ] Preparar soluções dos exercícios casa
- [ ] Limpar arquivos legados (opcional)

### Dia 1:
- [ ] Abrir dia1_exercicio_guiado.ipynb
- [ ] Executar células junto com alunos
- [ ] Responder perguntas em tempo real
- [ ] Mostrar dia1_exercicio_casa.ipynb ao final
- [ ] Explicar prazo de entrega

### Dia 2:
- [ ] Discutir soluções casa Dia 1
- [ ] Abrir dia2_exercicio_guiado.ipynb
- [ ] Executar células junto com alunos
- [ ] Mostrar dia2_exercicio_casa.ipynb ao final
- [ ] Fornecer recursos para continuar

### Após Evento:
- [ ] Coletar feedback
- [ ] Revisar exercícios entregues
- [ ] Enviar certificados
- [ ] Email follow-up com recursos
- [ ] Arquivar materiais do evento

---

## 💡 Dicas Pedagógicas

### Para Exercícios Guiados:
1. **Execute célula por célula** com os alunos
2. **Explique o código** linha por linha
3. **Mostre visualizações** em tela grande
4. **Pause para perguntas** após cada exercício
5. **Incentive experimentação** (mudar parâmetros)

### Para Exercícios Casa:
1. **Deixe claro** que são desafios progressivos
2. **Indique** quais são obrigatórios vs. bônus
3. **Forneça prazo** realista (2-3 dias mínimo)
4. **Disponibilize** canal para dúvidas
5. **Reconheça** soluções criativas

---

## 🎯 Objetivos de Aprendizado

Ao final do workshop, o aluno deve ser capaz de:

### Dia 1:
- ✅ Criar circuitos quânticos básicos
- ✅ Usar porta Hadamard para superposição
- ✅ Realizar medições quânticas
- ✅ Gerar números aleatórios quânticos
- ✅ Validar resultados estatisticamente

### Dia 2:
- ✅ Implementar portas lógicas quânticas
- ✅ Usar CNOT para entrelaçamento
- ✅ Aplicar Toffoli em computação reversível
- ✅ Controlar probabilidades com rotações
- ✅ Criar estados entrelaçados complexos
- ✅ Projetar circuitos multi-qubit

---

## 📞 Suporte

**Dúvidas sobre estrutura:**
- Consulte: `PLANEJAMENTO_EVENTO.md`
- GitHub Issues: [Link do repositório]

**Problemas técnicos:**
- Verificar: `.devcontainer/devcontainer.json`
- Reinstalar: `pip install -r requirements.txt`

**Comunidade:**
- Qiskit Slack: https://qiskit.slack.com/
- Stack Exchange: https://quantumcomputing.stackexchange.com/

---

✨ **Boa sorte com o workshop!** ✨

*Estrutura criada para maximizar aprendizado progressivo com mínima confusão!* 🚀

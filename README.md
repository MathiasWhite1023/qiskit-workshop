# 🌟 Qiskit Workshop - Computação Quântica

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/MathiasWhite1023/qiskit-workshop)

Este é um workshop introdutório sobre computação quântica usando Qiskit, configurado para funcionar diretamente no **GitHub Codespaces** - sem necessidade de instalação local!

## 🚀 Começar Rapidamente

### Opção 1: GitHub Codespaces (Recomendado)
1. **Clique no botão "Open in GitHub Codespaces" acima**
2. **Aguarde o ambiente carregar** (aproximadamente 2-3 minutos)
3. **Abra o notebook do Dia 1**: `notebooks/dia1_exercicio_guiado.ipynb`
4. **Comece a aprender!** 🎉

> ⚠️ **IMPORTANTE para eventos**: Para economizar recursos, **pare o Codespace** quando terminar usando o menu "..." → "Stop Codespace"

### Opção 2: Instalação Local
1. Clone este repositório:
   ```bash
   git clone https://github.com/MathiasWhite1023/qiskit-workshop.git
   cd qiskit-workshop
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o Jupyter:
   ```bash
   jupyter notebook
   ```

## 📁 Estrutura do Projeto

```
qiskit-workshop/
├─ .devcontainer/                        # ⚙️ Configuração do Codespace
│   └─ devcontainer.json                 # Ambiente pré-configurado
├─ notebooks/                            # 📚 Materiais do workshop
│   ├─ dia1_exercicio_guiado.ipynb       # 🌟 Dia 1: Exercício com instrutor
│   ├─ dia1_exercicio_casa.ipynb         # 🏠 Dia 1: Para casa
│   ├─ dia2_exercicio_guiado.ipynb       # ⚡ Dia 2: Exercício com instrutor
│   └─ dia2_exercicio_casa.ipynb         # 🏠 Dia 2: Para casa
├─ requirements.txt                      # 📦 Dependências Python
├─ welcome.sh                            # 👋 Script de boas-vindas
├─ .gitignore                            # 🚫 Arquivos ignorados
└─ README.md                             # 📖 Este arquivo
```

## 🎓 Conteúdo do Workshop

Este workshop é organizado em **2 dias completos** com palestras, exercícios guiados e desafios para casa.

---

### 🌟 **DIA 1: Fundamentos da Computação Quântica**

#### 📊 Palestras:
- Qubits e estados quânticos
- Superposição: o poder da simultaneidade
- Entrelaçamento quântico
- Medição e colapso de estado
- Aleatoriedade quântica verdadeira

#### 📓 **Exercício Guiado** - `notebooks/dia1_exercicio_guiado.ipynb`
Trabalhe junto com o instrutor:
- 🎯 Exercício 1: Sua primeira moeda quântica
- 🧪 Exercício 2: Teste estatístico com 1000 jogadas
- 🔢 Exercício 3: Gerador de números aleatórios (2-4 bits)
- 📊 Exercício 4: Análise de distribuição (teste qui-quadrado)

#### 🏠 **Para Casa** - `notebooks/dia1_exercicio_casa.ipynb`
Pratique e consolide o aprendizado:
- 🎲 **Desafio 1:** Dado quântico inteligente (1-6)
- 📈 **Desafio 2:** Detetive da aleatoriedade (testes estatísticos)
- 🎰 **Projeto Bônus:** Loteria quântica avançada

---

### ⚡ **DIA 2: Portas Lógicas e Circuitos Quânticos**

#### � Palestras:
- Portas lógicas quânticas fundamentais
- CNOT e entrelaçamento controlado
- Porta Toffoli e computação reversível
- Rotações quânticas (RX, RY, RZ)
- Estados de Bell e aplicações

#### 📓 **Exercício Guiado** - `notebooks/dia2_exercicio_guiado.ipynb`
Trabalhe junto com o instrutor:
- 🔧 Exercício 1: Demonstração completa da porta CNOT
- 🧮 Exercício 2: Implementando XOR quântico
- 🎯 Exercício 3: AND reversível com Toffoli
- 🎰 Exercício 4: Controle de probabilidades com rotações
- 🧬 Exercício 5: Estados de Bell (entrelaçamento)

#### 🏠 **Para Casa** - `notebooks/dia2_exercicio_casa.ipynb`
Projetos desafiadores:
- 🔧 **Desafio 1:** Kit completo de portas lógicas (NOT, AND, OR, XOR, NAND, NOR)
- 🎰 **Desafio 2:** Sistema de probabilidades controladas
- 🧬 **Desafio 3:** Estados GHZ e W (entrelaçamento multi-qubit)
- 🏆 **Projeto Final:** Calculadora lógica quântica com somadores

---

### 📅 Como Seguir o Workshop

**Sequência Recomendada:**

1. **Dia 1 Manhã:** Palestras sobre fundamentos
2. **Dia 1 Tarde:** `dia1_exercicio_guiado.ipynb` com instrutor
3. **Dia 1 Noite/Casa:** `dia1_exercicio_casa.ipynb` individualmente
4. **Dia 2 Manhã:** Palestras sobre portas lógicas
5. **Dia 2 Tarde:** `dia2_exercicio_guiado.ipynb` com instrutor
6. **Dia 2 Noite/Casa:** `dia2_exercicio_casa.ipynb` individualmente

## 🛠 Ambiente Pré-configurado

O Codespace inclui:
- ✅ **Python 3.11**
- ✅ **Qiskit completo** (simuladores e visualizações)
- ✅ **Jupyter Notebooks** com extensões
- ✅ **GitHub Copilot** (se disponível)
- ✅ **Todas as bibliotecas** necessárias
- ✅ **VS Code** otimizado para Python

## 🎯 Para Educadores

Este workshop foi projetado para ser:
- **Acessível**: Zero configuração para estudantes
- **Interativo**: Notebooks com exemplos práticos
- **Escalável**: Funciona para uma pessoa ou classe inteira
- **Moderno**: Usa as melhores práticas de desenvolvimento

### Como usar em sala de aula:
1. **Compartilhe o link** do repositório
2. **Estudantes clicam** em "Open in Codespaces"
3. **Começam imediatamente** - sem instalações!

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:
1. Fork este repositório
2. Crie uma branch para sua feature
3. Faça commit das suas mudanças
4. Abra um Pull Request

## 📚 Recursos Adicionais

- **[Documentação do Qiskit](https://qiskit.org/documentation/)**
- **[Qiskit Textbook](https://qiskit.org/textbook/)**
- **[IBM Quantum Experience](https://quantum-computing.ibm.com/)**
- **[Qiskit Community](https://qiskit.org/advocates/)**

## ⚡ Solução de Problemas

### Codespace não iniciou?
- Verifique se você tem acesso ao GitHub Codespaces
- Tente atualizar a página
- Entre em contato com suporte se persistir

### Jupyter não funciona?
- Reinicie o Codespace
- Execute: `pip install -r requirements.txt`
- Abra um terminal e digite: `jupyter --version`

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

---

**🌟 Desenvolvido com ❤️ para democratizar o ensino de computação quântica**

[![Made with Qiskit](https://img.shields.io/badge/Made%20with-Qiskit-6929C4.svg)](https://qiskit.org/)
[![Powered by GitHub Codespaces](https://img.shields.io/badge/Powered%20by-GitHub%20Codespaces-181717.svg)](https://github.com/features/codespaces)
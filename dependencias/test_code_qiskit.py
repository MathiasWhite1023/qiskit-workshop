#!/usr/bin/env python3
"""
Teste simples do código Qiskit no Codespace
Execute este arquivo para verificar se o ambiente está funcionando
"""

def test_qiskit_basic():
    """Teste básico do Qiskit com um circuito simples"""
    print("🔬 Testando ambiente Qiskit...")
    
    # Importações básicas
    try:
        from qiskit import QuantumCircuit, execute
        from qiskit_aer import AerSimulator
        from qiskit.visualization import plot_histogram
        import matplotlib.pyplot as plt
        import numpy as np
        print("✅ Todas as bibliotecas importadas com sucesso!")
    except ImportError as e:
        print(f"❌ Erro na importação: {e}")
        return False
    
    # Criar circuito quântico
    try:
        qc = QuantumCircuit(2, 2)
        qc.h(0)  # Hadamard no qubit 0
        qc.cx(0, 1)  # CNOT entre qubits 0 e 1
        qc.measure_all()  # Medir todos os qubits
        print("✅ Circuito quântico criado!")
    except Exception as e:
        print(f"❌ Erro ao criar circuito: {e}")
        return False
    
    # Executar no simulador
    try:
        simulator = AerSimulator()
        job = execute(qc, simulator, shots=1000)
        result = job.result()
        counts = result.get_counts(qc)
        print(f"✅ Simulação executada: {counts}")
    except Exception as e:
        print(f"❌ Erro na simulação: {e}")
        return False
    
    # Testar visualização (sem mostrar)
    try:
        fig = plot_histogram(counts)
        plt.close(fig)  # Fechar para não mostrar
        print("✅ Visualização funcionando!")
    except Exception as e:
        print(f"❌ Erro na visualização: {e}")
        return False
    
    print("\n🎉 SUCESSO! O ambiente Qiskit está funcionando perfeitamente!")
    print("🚀 Você pode começar o workshop!")
    return True

def show_environment_info():
    """Mostra informações do ambiente"""
    print("\n📋 Informações do Ambiente:")
    print("=" * 40)
    
    import sys
    print(f"Python: {sys.version}")
    
    try:
        import qiskit
        print(f"Qiskit: {qiskit.__version__}")
    except:
        print("Qiskit: Não instalado")
    
    try:
        import numpy as np
        print(f"NumPy: {np.__version__}")
    except:
        print("NumPy: Não instalado")
    
    try:
        import matplotlib
        print(f"Matplotlib: {matplotlib.__version__}")
    except:
        print("Matplotlib: Não instalado")

if __name__ == "__main__":
    print("🌟" + "="*50 + "🌟")
    print("         TESTE DO CODESPACE QISKIT")
    print("🌟" + "="*50 + "🌟")
    
    show_environment_info()
    print()
    
    success = test_qiskit_basic()
    
    if success:
        print("\n📚 Próximos passos:")
        print("1. Abra: notebooks/aula1_gerador_aleatorio.ipynb")
        print("2. Execute as células sequencialmente")
        print("3. Divirta-se com computação quântica! 🎯")
    else:
        print("\n🔧 Se houver problemas:")
        print("1. Aguarde o Codespace terminar de carregar")
        print("2. Execute: pip install -r requirements.txt")
        print("3. Tente novamente")
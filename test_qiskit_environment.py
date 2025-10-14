#!/usr/bin/env python3
"""
Teste completo do ambiente Qiskit
Execute este script para verificar se tudo está funcionando
"""

import sys

def test_python_version():
    """Testa a versão do Python"""
    print("🐍 Testando Python...")
    print(f"   ✅ Python {sys.version}")
    return True

def test_qiskit_installation():
    """Testa se o Qiskit está instalado e funcionando"""
    print("🔬 Testando Qiskit...")
    try:
        import qiskit
        print(f"   ✅ Qiskit {qiskit.__version__} instalado")
        return True
    except ImportError as e:
        print(f"   ❌ Erro: {e}")
        return False

def test_qiskit_aer():
    """Testa o simulador Qiskit Aer"""
    print("⚡ Testando Qiskit Aer...")
    try:
        from qiskit_aer import AerSimulator
        simulator = AerSimulator()
        print(f"   ✅ AerSimulator funcionando")
        return True
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def test_basic_circuit():
    """Testa criação e execução de um circuito básico"""
    print("🔧 Testando circuito quântico básico...")
    try:
        from qiskit import QuantumCircuit, execute
        from qiskit_aer import AerSimulator
        
        # Criar circuito simples
        qc = QuantumCircuit(1, 1)
        qc.h(0)  # Hadamard gate
        qc.measure(0, 0)
        
        # Executar no simulador
        simulator = AerSimulator()
        job = execute(qc, simulator, shots=100)
        result = job.result()
        counts = result.get_counts(qc)
        
        print(f"   ✅ Circuito executado: {counts}")
        return True
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def test_visualization():
    """Testa bibliotecas de visualização"""
    print("📊 Testando bibliotecas de visualização...")
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        print("   ✅ Matplotlib funcionando")
        
        from qiskit.visualization import plot_histogram
        print("   ✅ Qiskit visualization funcionando")
        return True
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def test_other_dependencies():
    """Testa outras dependências importantes"""
    print("📦 Testando outras dependências...")
    dependencies = ['numpy', 'matplotlib', 'jupyter']
    all_good = True
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"   ✅ {dep}")
        except ImportError:
            print(f"   ❌ {dep} não encontrado")
            all_good = False
    
    return all_good

def run_full_test():
    """Executa todos os testes"""
    print("🌟" + "="*50 + "🌟")
    print("    TESTE COMPLETO DO AMBIENTE QISKIT")
    print("🌟" + "="*50 + "🌟")
    print()
    
    tests = [
        test_python_version,
        test_qiskit_installation,
        test_qiskit_aer,
        test_basic_circuit,
        test_visualization,
        test_other_dependencies
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
            print()
        except Exception as e:
            print(f"   ❌ Erro inesperado: {e}")
            results.append(False)
            print()
    
    # Resumo final
    print("📋 RESUMO DOS TESTES:")
    print("=" * 30)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Ambiente Qiskit está pronto para uso!")
    else:
        print(f"⚠️  {passed}/{total} testes passaram")
        print("❌ Alguns problemas foram encontrados")
    
    print()
    print("🚀 Se todos os testes passaram, você pode:")
    print("   1. Abrir o notebook: notebooks/aula1_gerador_aleatorio.ipynb")
    print("   2. Executar as células sequencialmente")
    print("   3. Explorar computação quântica!")
    print()

if __name__ == "__main__":
    run_full_test()
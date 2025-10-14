#!/usr/bin/env python3
"""
Teste rápido do Qiskit - versão simplificada
"""

print("🔬 Teste Rápido do Qiskit")
print("=" * 30)

# Teste 1: Importar Qiskit
try:
    import qiskit
    print(f"✅ Qiskit {qiskit.__version__}")
except Exception as e:
    print(f"❌ Qiskit: {e}")
    exit(1)

# Teste 2: Criar circuito simples
try:
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    print("✅ Circuito quântico criado")
except Exception as e:
    print(f"❌ Circuito: {e}")
    exit(1)

# Teste 3: Executar no simulador
try:
    from qiskit import execute
    from qiskit_aer import AerSimulator
    
    simulator = AerSimulator()
    job = execute(qc, simulator, shots=10)
    result = job.result()
    counts = result.get_counts(qc)
    print(f"✅ Simulação: {counts}")
except Exception as e:
    print(f"❌ Simulação: {e}")
    exit(1)

print("\n🎉 Qiskit está funcionando perfeitamente!")
print("🚀 Pronto para o workshop!")
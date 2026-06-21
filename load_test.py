import asyncio
import time
import httpx
from statistics import mean, median
import sys
import os

# Adicionar raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

async def simulate_user(user_id, num_requests):
    latencies = []
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))
    from main import app
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        for i in range(num_requests):
            start_time = time.time()
            response = await client.get("/")
            end_time = time.time()
            latencies.append((end_time - start_time) * 1000)  # em ms
            await asyncio.sleep(0.1)
    return latencies

async def run_load_test(concurrent_users=10, requests_per_user=10):
    print(f"Iniciando Teste de Carga: {concurrent_users} usuários simultâneos, {requests_per_user} requisições cada.")
    start_time = time.time()
    
    tasks = [simulate_user(i, requests_per_user) for i in range(concurrent_users)]
    results = await asyncio.gather(*tasks)
    
    total_time = time.time() - start_time
    
    all_latencies = []
    for user_latencies in results:
        all_latencies.extend(user_latencies)
        
    print("\n--- Resultados do Teste de Carga ---")
    print(f"Total de Requisições: {len(all_latencies)}")
    print(f"Tempo Total de Execução: {total_time:.2f} segundos")
    print(f"Latência Média: {mean(all_latencies):.2f} ms")
    print(f"Latência Mediana: {median(all_latencies):.2f} ms")
    print(f"Latência Máxima: {max(all_latencies):.2f} ms")
    print(f"Latência Mínima: {min(all_latencies):.2f} ms")
    print(f"Requests per Second (RPS aproximado): {len(all_latencies) / total_time:.2f}")
    
if __name__ == "__main__":
    asyncio.run(run_load_test())

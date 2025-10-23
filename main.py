from salesforce_api import conectar_salesforce, criar_lead, buscar_leads
import random

def main():
    # 1. Conecta ao Salesforce
    sf = conectar_salesforce()

    if not sf:
        print("\nO programa não pode prosseguir sem conexão com o Salesforce.")
        return

    # 2. Testa a criação de um novo Lead
    novo_lead_data = {
        'FirstName': 'Teste',
        'LastName': f'Python_{random.randint(100, 999)}',
        'Company': 'VSCode Integracoes',
        'Email': f'teste{random.randint(100, 999)}@vscodetech.com',
        'Status': 'New'
    }
    lead_id = criar_lead(sf, novo_lead_data)

    # 3. Testa a busca/leitura de Leads
    if lead_id:
        print("\n--- Listando Leads Recentes ---")
        buscar_leads(sf, limit=3)
    
if __name__ == "__main__":
    main()
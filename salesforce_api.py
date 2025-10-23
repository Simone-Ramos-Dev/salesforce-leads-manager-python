import os
from dotenv import load_dotenv
from simple_salesforce import Salesforce, SalesforceError

# Carrega as credenciais do arquivo .env
load_dotenv()

def conectar_salesforce():
    """Tenta estabelecer a conexão com o Salesforce e retorna o objeto SF."""
    try:
        sf = Salesforce(
            username=os.getenv('SF_USERNAME'),
            password=os.getenv('SF_PASSWORD'),
            security_token=os.getenv('SF_SECURITY_TOKEN'),
            domain='test' if os.getenv('SF_IS_SANDBOX') == 'True' else 'login'
        )
        print("✅ Conexão com Salesforce estabelecida!")
        return sf
    except Exception as e:
        print(f"❌ ERRO de Conexão: Verifique suas credenciais e token. {e}")
        return None

def criar_lead(sf_conn, dados_lead):
    """Cria um novo registro de Lead."""
    if not sf_conn: return None
    print(f"\nTentando criar Lead: {dados_lead.get('LastName')}")
    try:
        resultado = sf_conn.Lead.create(dados_lead)
        if resultado.get('success'):
            print(f"✔️ Lead criado com sucesso! ID: {resultado['id']}")
            return resultado['id']
        else:
            print(f"❌ Falha ao criar Lead. Erros: {resultado['errors']}")
            return None
    except SalesforceError as e:
        print(f"❌ Erro da API do Salesforce ao criar Lead: {e}")
        return None

def buscar_leads(sf_conn, limit=5):
    """Busca registros de Leads."""
    if not sf_conn: return []
    query = f"SELECT Id, Name, Company, Status FROM Lead ORDER BY CreatedDate DESC LIMIT {limit}"
    print(f"\nExecutando SOQL: {query}")
    try:
        resultados = sf_conn.query_all(query)
        print(f"✔️ {resultados['totalSize']} Leads encontrados.")
        for record in resultados['records']:
            print(f"   - ID: {record['Id']}, Nome: {record['Name']}, Empresa: {record['Company']}, Status: {record['Status']}")
        return resultados['records']
    except SalesforceError as e:
        print(f"❌ Erro da API do Salesforce ao buscar Leads: {e}")
        return []
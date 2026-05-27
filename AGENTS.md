# Regras Gerais do Projeto
stack obrigatória do projeto?
 - Python 3.11+
- FastAPI
- Pydantic v2
- SQLite (dev) — via sqlite3 nativo
- Uvicorn
- Pytest
O que nunca pode ser alterado sem autorização?
Nomes dos endpoints (/registrar-foco, /registros, /diagnostico-produtividade)
Estrutura do banco — colunas e tipos da tabela registros
Contratos dos modelos Pydantic de output

Quais são as convenções de código que você quer manter?

- Nunca criar funções gigantes (Small Functions)
- Nunca misturar regra de negócio com acesso ao banco (Separation of Concerns)
- Nunca repetir lógica (DRY — Don't Repeat Yourself)
- Sempre usar tipagem (Type Hinting)
- Sempre tratar erros (Error Handling)
- Sempre priorizar legibilidade (Readability First)
- Código deve ser fácil de manter (Maintainability)
- Código deve ser fácil de testar (Testability)
- Código deve ser fácil de escalar (Scalability)
- Cada função deve ter apenas uma responsabilidade (SRP — Single Responsibility Principle)
- Sempre usar nomes descritivos para variáveis e funções (Naming Conventions)
- Utilizar snake_case para funções e variáveis (snake_case)
- Utilizar PascalCase para classes (PascalCase)
- Utilizar UPPER_CASE para constantes (UPPER_CASE)
- Sempre usar context manager para conexões e arquivos (`with statement`)
- Evitar acoplamento excessivo (Low Coupling)
- Priorizar alta coesão entre responsabilidades (High Cohesion)
- Separar camadas da aplicação (Layered Architecture)
- Não deixar erros silenciosos (`except: pass`)
- Priorizar reutilização de código (Code Reusability)
- Escrever código pensando em manutenção futura (Clean Code)
Como os testes devem ser rodados?
Precisamos que os testes venham ser incrementados a cada nova função.
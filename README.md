# COPILOT GPT
**Especifique o que você deseja criar, a IA solicita esclarecimentos e, em seguida, cria.**

O COPILOT GPT foi feito para ser fácil de adaptar, estender e fazer com que seu agente aprenda como você deseja que seu código seja. Ele gera uma base de código inteira com base em um prompt.


## Filosofia do projeto
- Simples de obter valor
- Flexível e fácil de adicionar novas "etapas AI". Veja `steps.py`.
- Construa gradualmente em direção a uma experiência de usuário de:
  1. solicitação de alto nível
  2. dar feedback à IA de que ela se lembrará com o tempo
- Transferências rápidas entre IA e humanos
- Simplicidade, toda a computação é "resumível" e persistida no sistema de arquivos


## Uso

**Instalar**:

- `pip install -r requisitos.txt`
- `export OPENAI_API_KEY=[sua chave de API]`

**Correr**:
- Crie uma nova pasta vazia com um arquivo `main_prompt` (ou copie a pasta de exemplo `cp example -r my-new-project`)
- Preencha o `main_prompt` em sua nova pasta
- execute `python main.py my-new-project`

**Resultados**:
- Verifique os arquivos gerados em my-new-project/workspace_clarified

### Limitações
Implementar uma cadeia adicional de sugestões de pensamento, por ex. [Reflexion](https://github.com/noahshinn024/reflexion), deve ser capaz de torná-lo mais confiável e não perder a funcionalidade solicitada no prompt principal.


## Características
Você pode especificar a "identidade" do agente AI editando os arquivos na pasta `identity`.

Editar a identidade e evoluir o main_prompt é a forma como você faz o agente se lembrar de coisas entre os projetos.

Cada etapa em steps.py terá seu histórico de comunicação com GPT4 armazenado na pasta logs e poderá ser executado novamente com scripts/rerun_edited_message_logs.py.
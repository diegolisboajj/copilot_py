from ai import AI
from chat_to_files import to_files
from db import DBs
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

def setup_sys_prompt(dbs):
    return dbs.identity['setup'] + '\nÚtil saber:\n' + dbs.identity['philosophy']

def run(ai: AI, dbs: DBs):
    '''Execute o AI no prompt principal e salve os resultados'''
    messages = ai.start(setup_sys_prompt(dbs), dbs.input['main_prompt'])
    to_files(messages[-1]['content'], dbs.workspace)
    return messages

def clarify(ai: AI, dbs: DBs):
    '''Pergunte ao usuário se ele deseja esclarecer alguma coisa e salve os resultados no espaço de trabalho'''
    messages = [ai.fsystem(dbs.identity['qa'])]
    user = dbs.input['main_prompt']
    while True:
        messages = ai.next(messages, user)

        if messages[-1]['content'].strip().lower() == 'no':
            break

        print()
        user = input('(responda no texto, ou "q" para seguir em frente)\n')
        print()

        if not user or user == 'q':
            break

        user += (
            '\n\n'
            'Há algo mais que não está claro? Se sim, responda apenas na forma:\n'
            '{áreas restantes não claras} perguntas restantes.\n'
            '{Próxima pergunta}\n'
            'Se tudo estiver suficientemente claro, responda apenas "não".'
        )

    print()
    return messages

def run_clarified(ai: AI, dbs: DBs):
    # obter as mensagens da etapa anterior
    messages = json.loads(dbs.logs[clarify.__name__])

    messages = (
        [
            ai.fsystem(setup_sys_prompt(dbs)),
        ] +
        messages[1:]
    )
    messages = ai.next(messages, dbs.identity['use_qa'])
    to_files(messages[-1]['content'], dbs.workspace)
    return messages


STEPS=[
    clarify,
    run_clarified
]

# Etapas futuras que podem ser adicionadas:
# inclusao de arquivos,
# adicionar testes
# rodar testes e testar os arquivos,
# implementar sistema de feedback

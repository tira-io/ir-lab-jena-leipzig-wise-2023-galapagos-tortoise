#!/usr/bin/env python3
from tira.rest_api_client import Client
import requests
from pathlib import Path
import os
from shutil import copyfile

tira = Client()

team_name = 'galapagos-tortoise'
system_names = ['mild-duck', 'poky-claim', 'edible-status']

TIRA_DATASET_ID_TO_LONGEVAL_LAG = {
    'ir-lab-padua-2024/longeval-2023-01-20240426-training': 'lag1',
    'ir-lab-padua-2024/longeval-2023-06-20240422-training': 'lag6',
    'ir-lab-padua-2024/longeval-2023-08-20240422-training': 'lag8'
}

DESCRIPTION_FORM_URL = 'https://raw.githubusercontent.com/clef-longeval/IR-Participants/9709a89dc59b093e9a6fd99a29666ae05ebf1c9e/Submissions/team_system.meta'

description = requests.get(DESCRIPTION_FORM_URL).content.decode('utf-8')

for system_name in system_names:
    team_system = f'{team_name}_{system_name}'
    target_dir = Path(team_system)
    os.makedirs(target_dir, exist_ok=True)
    open(target_dir / f'{team_system}.meta', 'w').write(description)
    for tira_dataset_id, longeval_lag in TIRA_DATASET_ID_TO_LONGEVAL_LAG.items():
        run = tira.get_run_output(f'ir-lab-padua-2024/{team_name}/{system_name}', tira_dataset_id)
        copyfile(Path(run) / 'run.txt', target_dir / f'{team_system}.{longeval_lag}')
    print(f'Done. I downloaded the runs into the directory {team_system}. Please fill out the meta_description, make some last spot checks, then zip the directory and upload :)')


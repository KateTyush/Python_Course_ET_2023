import subprocess
import datetime

def parse_ps_aux():
    output = subprocess.check_output(['ps', 'aux'])

    lines = output.decode().split('\n')

    users = set()
    total_processes = 0
    user_processes = {}
    total_mem = 0.0
    total_cpu = 0.0
    max_mem_process = ''
    max_mem = 0.0
    max_cpu_process = ''
    max_cpu = 0.0

    for line in lines[1:]:
        if not line:
            continue
        parts = line.split()
        # ['USER', 'PID', '%CPU', '%MEM', 'VSZ', 'RSS', 'TT', 'STAT', 'STARTED', 'TIME', 'COMMAND']
        user = parts[0]
        cpu = float(parts[2])
        mem = float(parts[3])
        command = parts[10] if len(parts) > 10 else ''

        users.add(user)
        total_processes += 1
        user_processes[user] = user_processes.get(user, 0) + 1
        total_mem += mem
        total_cpu += cpu

        if mem > max_mem:
            max_mem = mem
            max_mem_process = command[:20]

        if cpu > max_cpu:
            max_cpu = cpu
            max_cpu_process = command[:20]

    sorted_users = sorted(users, reverse=True)
    sorted_user_processes = dict(sorted(user_processes.items(), reverse=True))

    report = []
    report.append('Отчёт о состоянии системы:')
    report.append('Пользователи системы: ' + ', '.join(sorted_users))
    report.append('Процессов запущено: ' + str(total_processes))
    report.append('Пользовательских процессов:')
    for user, count in sorted_user_processes.items():
        report.append(user + ': ' + str(count))
    report.append('Всего памяти используется: ' + str(total_mem) + ' mb')
    report.append('Всего CPU используется: ' + str(total_cpu) + '%')
    report.append('Больше всего памяти использует: ' + max_mem_process)
    report.append('Больше всего CPU использует: ' + max_cpu_process)

    print('\n'.join(report))

    with open(datetime.datetime.now().strftime('%d-%m-%Y-%H:%M-scan.txt'), 'w') as f:
        f.write('\n'.join(report))

parse_ps_aux()

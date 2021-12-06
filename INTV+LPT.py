from dataclasses import dataclass



@dataclass
class Job:
    proc_time: int
    time: int

@dataclass
class Machine:
    jobs: list
    load_sum: int


def init_machines(m):
    machines = []
    for idx in range(0, m):
        machines.append(Machine([], 0))
    return machines


def intv(jobs, m):
    phase = [jobs[0]]

    machine_phases = []
    makespan = 0

    for idx in range(1, len(jobs)):
        if jobs[idx].time <= makespan:
            phase.append(jobs[idx])
            continue
        machine_phases.append(lpt(phase, init_machines(m)))
        makespan += max(phase, key=lambda job: job.proc_time).proc_time
        phase.clear()
        phase.append(jobs[idx])

    # Process last phase
    machine_phases.append(lpt(phase, init_machines(m)))

    return machine_phases


def lpt(phase, machines):
    phase.sort(key=lambda job: job.proc_time, reverse=True)

    for job in phase:
        machine_with_least_load = min(machines, key=lambda machine: machine.load_sum)
        machine_with_least_load.jobs.append(job)
        machine_with_least_load.load_sum += job.proc_time

    return machines

# Az optimum >= mint 6 mert az lesz a leghosszabb job
# Online LPT kiadhatja az optimumot
jobs = [Job(1, 0),
        Job(1, 0),
        Job(2, 0),
        Job(3, 0),
        Job(2, 1),
        Job(2, 2),
        Job(3, 2),
        Job(1, 3),
        Job(2, 4),
        Job(1, 5)]

machine_phases = intv(jobs, 3)

machines = init_machines(3)
for machine_phase in machine_phases:
    for i, machine in enumerate(machine_phase):
        machines[i].load_sum += machine.load_sum
        machines[i].jobs.extend(machine.jobs)

for i, machine in enumerate(reversed(machines)):
    print(f'Machine: #{i} Makespan: {machine.load_sum} Jobs: {machine.jobs}')
import random
from nomad import Nomad

def terminate_random_allocation():
    global terminated_allocation_id
    nomad_client = Nomad(host="localhost")

    # Get all running jobs
    jobs = nomad_client.jobs.get_jobs()

    if not jobs:
        print("No jobs found in the Nomad cluster.")
        return

    # Select a random job
    random_job = random.choice(jobs)

    # Get allocations for the selected job
    allocations = nomad_client.job.get_allocations(random_job["ID"])

    if not allocations:
        print(f"No allocations found for job {random_job['ID']}.")
        return

    # Select a random allocation
    random_allocation = random.choice(allocations)

    terminated_allocation_id = random_allocation["ID"]
    nomad_client.allocation.stop_allocation(random_allocation["ID"])

def restart_random_allocation():
    nomad_client = Nomad(host="localhost")

    jobs = nomad_client.jobs.get_jobs()

    if not jobs:
        print("No jobs found in the Nomad cluster.")
        return

    random_job = random.choice(jobs)
    allocations = nomad_client.job.get_allocations(random_job["ID"])

    if not allocations:
        print(f"No allocations found for job {random_job['ID']}.")
        return

    random_allocation = random.choice(allocations)
    nomad_client.allocation.restart_allocation(random_allocation["ID"])

def increase_random_job_resources():
    nomad_client = Nomad(host="localhost")
    global cpu_mem_increased_job_id

    jobs = nomad_client.jobs.get_jobs()

    if not jobs:
        print("No jobs found in the Nomad cluster.")
        return

    random_job = random.choice(jobs)
    cpu_mem_increased_job_id = random_job["ID"]
    job_spec = nomad_client.job.get_job(random_job["ID"])

    if not job_spec:
        print(f"Job spec not found for job {random_job['ID']}.")
        return

    # Modify the job spec by increasing the resource requirements
    for task_group in job_spec["TaskGroups"]:
        for task in task_group["Tasks"]:
            resources = task["Resources"]
            resources["CPU"] += 100
            resources["MemoryMB"] += 100
    
    job = {'Job': job_spec }
    # Update the job with the modified resource requirements
    nomad_client.job.register_job(job_spec["Name"],job)
    

def decrease_random_job_resources():
    nomad_client = Nomad(host="localhost")
    global cpu_mem_increased_job_id
    if cpu_mem_increased_job_id is None:
        print("No job id found.")
        return

    job_spec = nomad_client.job.get_job(cpu_mem_increased_job_id)

    job = {'Job': job_spec }

    if not job_spec:
        print(f"Job spec not found for job {cpu_mem_increased_job_id}")
        return

    # Modify the job spec by increasing the resource requirements
    for task_group in job_spec["TaskGroups"]:
        for task in task_group["Tasks"]:
            resources = task["Resources"]
            resources["CPU"] -= 100
            resources["MemoryMB"] -= 100

    # Update the job with the modified resource requirements
    nomad_client.job.register_job(job_spec["Name"],job)

def drain_node():
    global random_node_id
    
    nomad_client = Nomad(host="localhost")

    nodes = nomad_client.nodes.get_nodes()

    if not nodes:
        print("No nodes found in the Nomad cluster.")
        return

    random_node_id = random.choice(nodes)

    # Enable Drain Node
    nomad_client.node.drain_node(random_node_id)
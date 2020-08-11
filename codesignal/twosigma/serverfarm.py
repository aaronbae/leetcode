def serverFarm(jobs, servers):
  results = [[] for _ in range(servers)] 
  server_status = [(0, i) for i in range(servers)]
  jobs = sorted([(j, i) for i, j in enumerate(jobs)], key=lambda tup: tup[0], reverse=True)
  for job, job_index in jobs:
    (tp, i) = server_status.pop(0)
    tp += job
    results[i].append(job_index)
    server_status.append((tp, i))
    server_status = sorted(server_status)
  return results

print(serverFarm([15, 30, 15, 5, 10], 3))
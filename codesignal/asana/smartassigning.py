def smartAssigning(names, statuses, projects, tasks):
  sortable = [(tasks[i], projects[i], n) for i, n in enumerate(names) if not statuses[i]]
  sortable = sorted(sortable)
  return sortable[0][2]

print(smartAssigning(["john", "martin"], [False, False],[1, 2],[1,1]))
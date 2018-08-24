movies=["mv1","mv2","mv3","mv1","mv3","mv2","mv4","mv5","mv1","mv5","mv3"]
for x in range(len(movies)):
	print(f"Running loop for {x+1} time")
	movies.remove("mv1")
	print("Removed 'mv1'")
	if not "mv1" in movies
		print("mv1 is not in the list")
		break
	print(movies)

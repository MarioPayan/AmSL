import subprocess

process = subprocess.Popen('php stemm_es.php "canciones"', shell=True, stdout=subprocess.PIPE)

for line in iter(process.stdout.readline,''):
	print(line)
import subprocess
import time
import argparse
import os

aimsunExe = 'C:/Program Files/Aimsun/Aimsun Next 8.3/aconsole.exe'

def run_sim(num_sim, num_threads, parallel_run, base_name, repl_id):
	subprocesses = []
	start = time.time()
	for i in range(num_sim):
		cmd = [aimsunExe, '-script']
		cmd.append('aimsun_wrapper.py')
		cmd.append(base_name+str(i)+".ang")
		cmd.append(repl_id)
		cmd.append('-nt')
		cmd.append(str(num_threads))
		#print(cmd)
		subprocesses.append(subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,
							stdout=subprocess.PIPE,stderr=subprocess.STDOUT))
		if not parallel_run:
			subprocesses[-1].wait()

	if parallel_run:
		for ps in subprocesses:
			ps.wait()
	end = time.time()
	return end - start


if __name__ == '__main__':
	'''
		py .\parallel_sim.py advanced_control_.ang 1209 -n 1
	'''
	argParser = argparse.ArgumentParser(
		description = 'Run multiple microsimulation replications\n'
					  'Example: aconsole.exe --script aimsun_wrapper.py <args>')
	argParser.add_argument('ang_file',
							help='Aimsun model')
	argParser.add_argument('repl_id',
							help='Replication(s) ID(s) separated by commas')
	argParser.add_argument('-n', "--num_sim", default=1, type=int,
							help='Number of simulations')
	argParser.add_argument('-p', "--parallel_run", action='store_true',
							help='Run simulations in parallel')
	argParser.add_argument('-nt', "--num_threads", type=int, default=1, 
							choices=range(1,9),
							help='Number of threads that Aimsun can use (max 8)')
	args = argParser.parse_args()
	
	exec_time = run_sim(args.num_sim, args.num_threads, args.parallel_run, 
						args.ang_file.split('.')[0], args.repl_id)
	print("Threads:{} \tTotal Sim:{} \tParallel Sim:{} \tExecution Time (Sec):{}".format(
						args.num_threads, args.num_sim, 
						args.num_sim if args.parallel_run else 1, exec_time))
	print("Done")
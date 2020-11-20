from parallel_sim import run_sim
import pandas as pd
import numpy as np

num_threads = [1,2,4,8]
num_sim = [1,2,4,8]
num_dup = 5
'''
for i in num_threads:
	for j in num_sim:
		exec_time = 0
		for k in range(num_dup):
			exec_time += run_sim(j, i, True, 'advanced_control_', str(1209))
		print("Threads:{} \tTotal Sim:{} \tParallel Sim:{} \tExecution Time (Sec):{}".format(
						i, j, j, exec_time/num_dup))
		exec_time = 0
		for k in range(num_dup):
			exec_time += run_sim(j, i, False, 'advanced_control_', str(1209))
		print("Threads:{} \tTotal Sim:{} \tParallel Sim:{} \tExecution Time (Sec):{}".format(
						i, j, 1, exec_time/num_dup))
print("Done...")

'''
tuples=[(i,j) for i in num_threads for j in num_sim]
index=pd.MultiIndex.from_tuples(tuples)
df = pd.DataFrame(np.zeros((len(index),2)), columns=['Sequential','Parallel'], 
					index=index)
for i in num_threads:
	for j in num_sim:
		exec_time = 0
		for k in range(num_dup):
			exec_time += run_sim(j, i, True, 'advanced_control_', str(1209))
		df.loc[(i,j),'Parallel'] = exec_time/num_dup
		#print("Threads:{} \tTotal Sim:{} \tParallel Sim:{} \tExecution Time (Sec):{}".format(
		#				i, j, j, exec_time/num_dup))
		exec_time = 0
		for k in range(num_dup):
			exec_time += run_sim(j, i, False, 'advanced_control_', str(1209))
		df.loc[(i,j),'Sequential'] = exec_time/num_dup
		#print("Threads:{} \tTotal Sim:{} \tParallel Sim:{} \tExecution Time (Sec):{}".format(
		#				i, j, 1, exec_time/num_dup))

print(df)
#df.plot()
print("Done...")

''' 8.3.2 Results
     Sequntial   Parallel  Sequential
1 1        0.0  13.171449   11.110361
  2        0.0  11.401396   21.771673
  4        0.0  12.301269   43.780560
  8        0.0  14.421477   87.905264
2 1        0.0  12.504326   12.382712
  2        0.0  12.747265   24.951856
  4        0.0  13.872598   49.850483
  8        0.0  16.276755  100.750886
4 1        0.0  11.875221   11.926268
  2        0.0  12.553838   24.354824
  4        0.0  13.805612   49.949516
  8        0.0  16.458393   95.558612
8 1        0.0  12.170972   12.153319
  2        0.0  12.754156   24.338603
  4        0.0  14.051184   48.649094
  8        0.0  18.233622   97.392014
Done...
'''
''' 20.0.1 Results
     Sequential   Parallel
1 1   15.307470  15.247441
  2   30.458450  16.602734
  4   61.081821  19.216864
  8  121.953687  25.260036
2 1   14.228382  14.263848
  2   28.412335  15.514620
  4   56.775710  18.001172
  8  113.876329  22.653785
4 1   14.062801  14.060297
  2   28.015708  15.317083
  4   56.161505  17.933037
  8  112.173765  23.259606
8 1   14.494396  14.459797
  2   28.956165  16.477575
  4   57.847262  18.471825
  8  116.137882  24.917816
Done...
'''
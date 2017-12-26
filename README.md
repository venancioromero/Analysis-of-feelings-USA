# Analysis of feelings of USA
#
#
Example of MapReduce wrote in python that analyse the feelings of 95.580 twits from USA.

for execute : 

- In shell:
```$ cat twits | ./mapper.py | sort | ./reducer.py```

- In haddop:

```hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar  -files mapper.py,reducer.py,states,dic.txt -mapper mapper.py -reducer reducer.py -input twits -output output ```

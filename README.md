# Analysis of feelings of USA
#
#
Example of MapReduce wrote in python that analyse the feelings of 95.580 twits from USA.

- [Map chart](https://venancioromero.github.io/Analysis-of-feelings-USA/)
- [video](https://www.youtube.com/watch?v=421QxMqSIno&feature=youtu.be)

for execute : 

- In shell:
```bash
$ cat twits | ./mapper.py | sort | ./reducer.py
```

- In haddop:

```bash
$ hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar  -files mapper.py,reducer.py,states,dic.txt -mapper mapper.py -reducer reducer.py -input twits -output output 
```

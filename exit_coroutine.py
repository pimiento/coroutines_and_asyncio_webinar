#!/usr/bin/python
class Task:
    task_id = 0
    def __init__(self, target):
        Task.task_id += 1
        self.tid = Task.task_id
        # target coroutine
        self.target = target
        # value to send
        self.sendval = None
    def run(self):
        return self.target.send(
            self.sendval
        )
from queue import Queue

class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self,target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self,task):
        print(f"Task {task.tid} terminated")
        del self.taskmap[task.tid]

    def schedule(self, task):
        self.ready.put(task)

    def mainloop(self):
         while self.taskmap:
            task = self.ready.get()
            try:
                _ = task.run()
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)
def foo(n):
    for i in range(n):
        print("I'm foo")
        yield

def bar(n):
    for i in range(n):
        print("I'm bar")
        yield

sched = Scheduler()
sched.new(foo(2))
sched.new(bar(2))
sched.mainloop()

- [Что такое асинхронное программирование?](#org47ac6df)
- [Пример синхронного программирования](#org08a044a)
- [Пример асинхронного программирования](#org8af2ab8)
- [Что такое генераторы в Python](#orgbf6384c)
- [Генераторы](#org807bba7)
- [Генераторы](#orgc4c5ecc)
- [Генераторы](#org16c79a1)
- [Генераторы как контекстные менеджеры](#orgc1f148f)
- [Пример использования генераторов](#orgb4ff5b8)
- [Пример использования генераторов](#orgee6308b)
- [Пример использования генераторов](#org603bc38)
- [Пример использования генераторов](#org3344cad)
- [Пример использования генераторов](#org238497c)
- [Корутины это генераторы](#orgb7a9e3b)
- [Корутины](#org1dea153)
- [Пример использования корутин](#org43655cb)
- [Пример использования корутин](#orge568d35)
- [Task scheduling](#orgfeee604)
- [Task](#org4175018)
- [Task example](#org959ffd0)
- [Scheduler](#org9d94e5f)
- [Scheduler](#orgc17de91)
- [Scheduler example](#orgc26c327)
- [Scheduler Exit](#orga388d39)
- [Scheduler example](#org0d1a50c)
- [Дополнительные материалы](#org04fc62b)
- [AsyncIO](#org46d7a71)
- [AsyncIO event loop](#org991ddf7)
- [Запуск sync в async](#org359de9f)
- [Запуск async в sync](#org2813db7)
- [Запуск async в sync](#org2acd1df)
- [Запуск async в Jupyter](#org5a7c2e6)
- [Дополнительная литература](#org9bff094)
- [Вопросы-ответы](#org2af5c81)



<a id="org47ac6df"></a>

# Что такое асинхронное программирование?

> концепция программирования, которая заключается в том, что результат выполнения функции доступен не сразу же, а через некоторое время в виде некоторого асинхронного (нарушающего обычный порядок выполнения) вызова.  

<div class="org-center">
<p>
<span class="underline"><span class="underline"><a href="https://ru.wikipedia.org/wiki/%25D0%2590%25D1%2581%25D0%25B8%25D0%25BD%25D1%2585%25D1%2580%25D0%25BE%25D0%25BD%25D0%25BD%25D0%25BE%25D0%25B5_%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5">Wiki</a></span></span><br />
</p>
</div>


<a id="org08a044a"></a>

# Пример синхронного программирования

```python

def func(x, y):
  import time
  time.sleep(1)
  return x + y
def run():
  fut = pool.submit(func, 2, 3)
  r = fut.result()
  print('Got:', r)
run()
print("DONE")
```

    - Got: 5
    - DONE


<a id="org8af2ab8"></a>

# Пример асинхронного программирования

```python

def result_handler(fut):
    result = fut.result()
    print('Got:', result)
def run():
    fut = pool.submit(func, 2, 3)
    fut.add_done_callback(
        result_handler
    )
run()
print("DONE")
```

    - DONE
    - Got: 5


<a id="orgbf6384c"></a>

# Что такое генераторы в Python

**Генератор** это функция, которая производит *последовательность результатов* а не единичный ответ.  

```python
print(str(x) for x in range(10))
```

    - <generator object <genexpr> at 0x7fcecba3bac0>

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for i in countdown(3):
    print(i, sep='', end='...')
```

    - 3...2...1...


<a id="org807bba7"></a>

# Генераторы

Python понимает, что функция это генератор по наличию в функции метода **yield**.  
  
Генераторы не запускаются автоматически при вызове, а только инициализируются  

```python
def countdown(n):
    print(f"Обратный отсёт для {n}")
    while n > 0:
        yield n
        # точка остановки
        n -= 1
g = countdown(3)
print(g)
```

    - <generator object countdown at 0x7f6aae07ee40>


<a id="orgc4c5ecc"></a>

# Генераторы

Чтобы запустить генератор, надо вызывать метод **next**  

```python

g = countdown(3)
next(g)
```

    - Обратный отсёт для 3


<a id="org16c79a1"></a>

# Генераторы

Генератор будет работать до тех пор пока не случится **return**  

```python

g = countdown(2)
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration:
    print("КОНЕЦ")
```

    - Обратный отсёт для 2
    - 2
    - 1
    - КОНЕЦ


<a id="orgc1f148f"></a>

# Генераторы как контекстные менеджеры

```python
from contextlib import contextmanager
import time

@contextmanager
def timeit():
    import time
    try:
        start = time.time()
        yield start
    finally:
        end = time.time()
        print(f"{end-start:.2f}")
with timeit():
    time.sleep(2)
```

    2.00


<a id="orgb4ff5b8"></a>

# Пример использования генераторов

В Bash можно направлять результат работы одной программы в другую, причём данные в первую программу могут поступать даже после запуска *пайпа*  

```shell
# на случай если такого файла
# не существовало
# или в нём что-то уже было,
# запишем в него пустоту
:> /tmp/t.txt
# tail -f => "follow" новые строки
#                     в файле
# grep -i python => искать вхождение
#                   подстроки python
tail -f /tmp/t.txt | grep -i python
```


<a id="orgee6308b"></a>

# Пример использования генераторов

Как реализовать такое на Python?  

```python
def follow(filepath, grepper):
    with open(filepath, "r") as fd:
        # "сикнемся" в конец файла
        fd.seek(0, 2)
        while True:
            line = fd.readline()
            if not line:
                # небольшая пауза
                time.sleep(0.1)
                continue
            grepper(line)

```


<a id="org603bc38"></a>

# Пример использования генераторов

```python

def grep(pattern, lines):
    pattern = pattern.lower()
    for line in lines:
        if pattern in line.lower():
            yield line
```


<a id="org3344cad"></a>

# Пример использования генераторов

```python

def follow(filepath):
    with open(filepath, "r") as fd:
        fd.seek(0, 2)
        while True:
            line = fd.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
```

```python

for line in grep(
    "python", follow("/tmp/t.txt")
):
    print(line)
```


<a id="org238497c"></a>

# Пример использования генераторов

```python

with open(
  "/usr/share/doc/python3.10/copyright"
) as fd:
  print(
    '\n'.join(grep(
        "http",
        grep("python", fd.readlines())
      )
    )
  )
```


<a id="orgb7a9e3b"></a>

# Корутины это генераторы

На самом деле **yield** принимает значение и возвращает его внутрь генератора.  

```python

# docs.python.org/3/library/typing.html
G = Generator[int, int, None]
def countdown(n) -> G:
    while n > 0:
        shift = (yield n)
        n -= 1
        if shift is not None:
            n += shift
g = countdown(1)
print(next(g))
print(g.send(10))
```

    - 1
    - 10


<a id="org1dea153"></a>

# Корутины

В корутины можно передать эксепшен  

```python
def cor(n):
    while n > 0:
        try:
            yield n
            n -= 1
        except ValueError:
            print("Поймал!")
g = cor(3)
next(g)
g.throw(ValueError, "foobar")
```

    - Поймал!


<a id="org43655cb"></a>

# Пример использования корутин

```python

def follow(filepath, target):
    with open(filepath, "r") as fd:
        fd.seek(0,2)
        while True:
            line = fd.readline()
            if not line:
                time.sleep(0.1)
                continue
            target.send(line)
```


<a id="orge568d35"></a>

# Пример использования корутин

```python

@coroutine
def printer():
    while True:
        line = (yield)
        print(line)
```

```python

@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
follow("/tmp/t.txt", broadcast(
    [printer(), printer()]))
```


<a id="orgfeee604"></a>

# Task scheduling

![img](task_scheduling.png)  


<a id="org4175018"></a>

# Task

```python
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
```


<a id="org959ffd0"></a>

# Task example

```python

def foo():
    for i in range(2):
        yield i
t1 = Task(foo())
print(t1.run())
print(t1.run())
```

    - 0
    - 1


<a id="org9d94e5f"></a>

# Scheduler

```python
from queue import Queue

class Scheduler:
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] \
            = newtask
        self.schedule(newtask)
        return newtask.tid
```


<a id="orgc17de91"></a>

# Scheduler

```python
def schedule(self,task):
    self.ready.put(task)

def mainloop(self):
    while self.taskmap:
        task = self.ready.get()
        result = task.run()
        self.schedule(task)
```


<a id="orgc26c327"></a>

# Scheduler example

```python

def foo():
    while True:
        print("I'm foo")
        yield

def bar():
    while True:
        print("I'm bar")
        yield

sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()
```


<a id="orga388d39"></a>

# Scheduler Exit

```python
def exit(self,task):
    print(f"Task {task.tid} terminated")
    del self.taskmap[task.tid]

def mainloop(self):
     while self.taskmap:
        task = self.ready.get()
        try:
            _ = task.run()
        except StopIteration:
            self.exit(task)
            continue
        self.schedule(task)
```


<a id="org0d1a50c"></a>

# Scheduler example

```python

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
```


<a id="org04fc62b"></a>

# Дополнительные материалы

<span class="underline"><span class="underline">[dabeaz.com](http://www.dabeaz.com/coroutines/)</span></span>  
  
*презентация старая, там используется Python2, будьте внимательны, синтаксис немного отличается!*  


<a id="org46d7a71"></a>

# AsyncIO

```python
import time
import asyncio
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
async def main():
    await asyncio.gather(
        count(), count()
    )
asyncio.run(main())
```

    - One
    - One
    - Two
    - Two


<a id="org991ddf7"></a>

# AsyncIO event loop

```python
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```


<a id="org359de9f"></a>

# Запуск sync в async

```python
import asyncio
from requests import get
from contextlib import asynccontextmanager

@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    yield await loop.run_in_executor(
        None, get, url)
async def main():
    async with web_page(
            "https://ya.ru") as data:
        print(data.content.decode("utf-8"))
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```


<a id="org2813db7"></a>

# Запуск async в sync

```python
# async downloader
async def rng(n):
    for i in range(n):
        yield i

async def foo(n):
    async for i in rng(n):
        print(i)
```


<a id="org2acd1df"></a>

# Запуск async в sync

```python

# sync scheduler
def task(n):
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(foo(n))

# register sync task in the sceduler
task(5)
```

    0
    1
    2
    3
    4


<a id="org5a7c2e6"></a>

# Запуск async в Jupyter

<span class="underline"><span class="underline">[Проблема](https://colab.research.google.com/drive/1uEcXaw_YCPLN2o8X0LefR7EZ_0hog0Tq#scrollTo=5yzPk0x9k23g)</span></span>  
<span class="underline"><span class="underline">[Обсуждение](https://stackoverflow.com/questions/47518874/how-do-i-run-python-asyncio-code-in-a-jupyter-notebook)</span></span>  

```python
# скорее всего даже не надо
%autowait asyncio

await foo(5)
```


<a id="org9bff094"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[AsyncIO in Python](https://realpython.com/async-io-python/)</span></span>
-   <span class="underline"><span class="underline">[Using AsyncIO in Python](https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/)</span></span>


<a id="org2af5c81"></a>

# Вопросы-ответы

![img](questions.jpg)

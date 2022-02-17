# Process vs Thread




## Process

```python
from multiprocessing import Process
from os import getpid
from random import uniform
from time import time, sleep


def download_task(filename):
    print('start process，process id = [%d].' % getpid())
    print('download %s start...' % filename)
    time_to_download = uniform(1, 10)   
    sleep(time_to_download)
    print('%s download done! spend %.2f sec' % (filename, time_to_download))


def main():

    start = time()
    p1 = Process(target = download_task, args=('file1', ))    
    p2 = Process(target = download_task, args=('file2', ))    
    p1.start()
    p2.start()
    p1.join()    
    p2.join()    
    print('total spend %.2f sec.' % (end - start))
    
    
    
if __name__ == '__main__': 
    main()

```

```
start process，process id = [17152].
download file1 start...
start process，process id = [14368].
download file2 start...
file1 download done! spend 8.24 sec
file2 download done! spend 9.24 sec
total spend 8.47 sec.
```



using Pool
Pool自然會等

```python
def main():
    start = time()
    files = ['file1','file2']
    pool = Pool() # Pool()
    pool.map(download_task,files)  
    end = time()
    print('total spend %.2f sec.' % (end - start))
```

這邊要注意多process的資料結構是不夠用的,並不會輸出Ping和Pong合起來10個,而是會個別輸出10個


```python
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    #counter = 0
    while counter < 10:
        #print(string, end='', flush=True)
        print(string)
        counter += 1
        sleep(0.01)

        
def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


if __name__ == '__main__':
    main()
```

result
```
Ping
Ping
Ping
Pong
Ping
Pong
Ping
Pong
Ping
Pong
Pong
Ping
Ping
Pong
Ping
Pong
Pong
Ping
Pong
Pong
```


## Thread

```
from threading import Thread
from random import uniform
from time import time, sleep


def download_task(filename):   
    print('download %s start...' % filename)
    time_to_download = uniform(1, 10)   
    sleep(time_to_download)
    print('%s download done! spend %.2f sec' % (filename, time_to_download))


def main():

    start = time()
    t1 = Thread(target = download_task, args=('file1', ))    
    t2 = Thread(target = download_task, args=('file2', ))
    
    t1.start()
    t2.start()
    t1.join()    
    t2.join()  
    end = time()
    print('total spend %.2f sec.' % (end - start))
    
    
    
if __name__ == '__main__': 
    main()
```

thread 是共用線程
```
from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先?取?才能?行后?的代?
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中?行?放?的操作保?正常异常?都能?放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('??余??: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
```





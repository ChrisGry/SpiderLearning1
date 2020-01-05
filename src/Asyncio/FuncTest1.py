import time

#正常情况下的函数运行时间
def job(t):
    print('Start job:',t)
    time.sleep(t)
    print('Job ',t,' takes ',t,' s')

def main():
    [job(t) for t in range(1,3)]

t1 = time.time()
main()
print('No Asyncio Total time: ',time.time()-t1)

#使用Asyncio的函数运行时间
import asyncio

async def job(t):
    print('Start job:',t)

    #await关键字：主程序可以去做其他事
    await asyncio.sleep(t)

    print('Job ',t,' takes ',t,' s')

async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1,3)]
    #tasks中的task在执行的过程中，需要main()函数等待它
    await asyncio.wait(tasks)

t1 = time.time()

#建立一个任务池
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()

#最终结果只需要2s，因为1s任务等待时，开始2s任务，2s任务等待的期间，1s任务已经完成了
print('Using Asyncio Total time: ',time.time()-t1)


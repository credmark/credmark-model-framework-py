from ModelTask import ModelTask, Pipe
from ModelRun import GraphClient

if __name__ == '__main__':
    t1 = ModelTask('token.price', 'AAVE', None, 'Price', 1231212)
    t2 = ModelTask('price*2', None, t1, 'Price', 1231212)
    t3 = ModelTask('price*3', None, t2, 'Price', 1231212)
    t4 = ModelTask('price*4', None, t2, 'Price', 1231212)

    p = Pipe([t1, t2, t3])

    sc = GraphClient()
    x = p.run(sc, [t3])
    print('t3:')
    print(x)

    print()
    print('t4:')
    p = Pipe([t1, t2, t3, t4])
    x = p.run(sc, [t4])
    print(x)

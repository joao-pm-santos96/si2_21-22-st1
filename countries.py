# from sympy import true
from zincbase import KB
from zincbase.web import GraphCaster
import time
import torch
torch.cuda.is_available()

if __name__ == '__main__': 
 
    kb = KB()
    g = GraphCaster(redis_address='redis://127.0.0.1:6379')
    g.reset()

    kb.from_csv('./countries_train.csv', delimiter='\t')


    print('-> The neighboors of Slovakia are:')
    for ans in kb.query('neighbor(slovakia, Country)'):
        print(ans['Country'])
    # python code
    kb.store('capitalofneighor(Z, X) :- neighbor(X, Y), capitalof(Z, Y)') # prolog function

    print()
    print('-> capitalofneighor(madrid, Country)')
    for ans in kb.query('capitalofneighor(madrid, Country)'):
        print(ans)

    print()
    print('-> capitalofneighor(City, germany)')
    for ans in kb.query('capitalofneighor(City, germany)'):
        print(ans)

    kb.build_kg_model(cuda=False, embedding_size=40)
    kb.train_kg_model(steps=4000, batch_size=1, verbose=True)

    print(kb.get_most_likely('austria', 'neighbor', '?', k=2)) 
    print(kb.get_most_likely('?', 'neighbor', 'austria', candidates=list(kb.entities), k=2))
    print(kb.estimate_triple_prob('fiji', 'locatedin', 'melanesia'))

    g.from_kb(kb)
    g.render(arrow_size=2,
         node_opacity=1, 
         node_label='id',
         label_node=True,
         edge_label='pred',
         label_edge=True, 
         label_edge_offset=1,
         bg_color='rgba(255,255,255,1)')

    print('Zincbase Graph Ready')
    while True:
        time.sleep(1)

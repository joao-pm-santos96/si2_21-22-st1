from sympy import true
from zincbase import KB
from zincbase.web import GraphCaster
import time
import torch
torch.cuda.is_available()

if __name__ == '__main':
    kb = KB()
    g = GraphCaster()
    g.reset()

    kb.from_csv('./countries_train.csv', delimiter='\t')
    for ans in kb.query('neighbor(slovakia, Country)'):
        print(ans['Country'])

    kb.store('capitalofneighor(Z, X) :- neighbor(X, Y), capitalof(Z, Y)')

    for ans in kb.query('capitalofneighor(madrid, Country)'):
        print(ans)


    for ans in kb.query('capitalofneighor(City, germany)'):
        print(ans)



    kb.build_kg_model(cuda=False, embedding_size=40)
    kb.train_kg_model(steps=4000, batch_size=1, verbose=True)
    kb.get_most_likely('austria', 'neighbor', '?', k=2) # doctest:+ELLIPSIS
    kb.get_most_likely('?', 'neighbor', 'austria', candidates=list(kb.entities), k=2)
    kb.get_most_likely('austria', '?', 'germany', k=3)

    print(kb.estimate_triple_prob('fiji', 'locatedin', 'melanesia'))


    exit()

#g.from_kb(kb)
#g.render(node_color='node => node.color',
#         arrow_size=2,
#         node_opacity=1, node_label='color',
#         label_node=True,
#         edge_label='edge_attr',
#         label_edge=True, label_edge_offset=1,
#         bg_color='rgba(255,255,255,1)')
#
#
#while True:
#    time.sleep(1)
#    g.batch_update()
#


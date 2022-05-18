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

    eu_contries = ['austria', 'belgium', 'bulgaria', 'croatia', 'republic_of_cyprus', 'czech_republic', 'denmark', 'estonia', 'finland', 'france', 'germany', 'greece', 'hungary', 'ireland', 'italy', 'latvia', 'lithuania', 'luxembourg', 'malta', 'netherlands', 'poland', 'portugal', 'romania', 'slovakia', 'slovenia', 'spain', 'sweden']
    for country in eu_contries:
        kb.store('partofEU('+ country +')')

    print('\n-> European Union cuntries are:')
    for ans in kb.query('partofEU(Country)'):
        print(ans['Country']) # prints 'portugal' and 'spain

    print('\n-> The neighboors of Slovakia are:')
    for ans in kb.query('neighbor(slovakia, Country)'):
        print(ans['Country'])
    
    
    # python code
    kb.store('capitalofneighbor(Z, X) :- neighbor(X, Y), capitalof(Z, Y)') # prolog function

    print('\n-> capitalofneighbor(madrid, Country)')
    for ans in kb.query('capitalofneighbor(madrid, Country)'):
        print(ans)

    print('\n-> capitalofneighbor(City, germany)')
    for ans in kb.query('capitalofneighbor(City, germany)'):
        print(ans)

    
    
    kb.store('capitalofneighborEU(Z, X) :- neighbor(X, Y), partofEU(Y), capitalof(Z, Y)') # prolog function

    print('\n-> capitalofneighbor(City, finland)')
    for ans in kb.query('capitalofneighbor(City, finland)'):
        print(ans)

    print('\n-> capitalofneighborEU(City, finland)')
    for ans in kb.query('capitalofneighborEU(City, finland)'):
        print(ans)


    #kb.store('capofneiEUbathedby(Z, X, O) :- neighbor(X, Y), partofEU(Y), bathedby(Y,O), capitalof(Z, Y)') # prolog function
    
    kb.store('countriesofcontbathedby(Z, X, O) :- locatedin(Z, X), bathedby(Z, O)') # prolog function
    
    print('\n-> countriesofcontbathedby(Country, western_europe, atlantic_ocean)')
    for ans in kb.query('countriesofcontbathedby(Country, western_europe, atlantic_ocean)'):
        print(ans)
    
    print('\n-> countriesofcontbathedby(Country, southern_europe, atlantic_ocean)')
    for ans in kb.query('countriesofcontbathedby(Country, southern_europe, atlantic_ocean)'):
        print(ans)

    
    kb.store('bathedby2(Z, O1, O2) :- bathedby(Z, O1), bathedby(Z, O2)') # prolog function
    
    print('\n-> bathedby2(Country, atlantic_ocean, pacific_ocean)')
    for ans in kb.query('bathedby2(Country, atlantic_ocean, pacific_ocean)'):
        print(ans)



    # kb.build_kg_model(cuda=False, embedding_size=40)
    # kb.train_kg_model(steps=4000, batch_size=1, verbose=True)

    # print(kb.get_most_likely('austria', 'neighbor', '?', k=2)) 
    # print(kb.get_most_likely('?', 'neighbor', 'austria', candidates=list(kb.entities), k=2))
    # print(kb.estimate_triple_prob('fiji', 'locatedin', 'melanesia'))

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

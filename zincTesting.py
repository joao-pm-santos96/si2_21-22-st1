from zincbase import KB
kb = KB()
kb.store('eats(tom, rice)')
for ans in kb.query('eats(tom, Food)'):
    print(ans['Food']) # prints 'rice'

kb.store('partofEU(portugal)')
kb.store('partofEU(spain)')
for ans in kb.query('partofEU(Country)'):
    print(ans['Country']) # prints 'portugal' and 'spain


# The included assets/countries_s1_train.csv contains triples like:
# (namibia, locatedin, africa)
# (lithuania, neighbor, poland)

kb = KB()
kb.from_csv('countries_train.csv', delimiter='\t')
kb.build_kg_model(cuda=False, embedding_size=40)
kb.train_kg_model(steps=8000, batch_size=1, verbose=False)
print(kb.estimate_triple_prob('fiji', 'locatedin', 'melanesia'))
#0.9607
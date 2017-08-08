# genes = ['he', 'she', 'hers', 'his']
trie = {}
outs = {}
failure = {}
prev = set()
big_q = []
states = 1

for gene in genes:
    prev = prev.union(set(gene))
    
for i in range(len(genes)):
    currentState = 0
    for j in range(len(genes[i])):
        ch = ord(genes[i][j]) - 96
        temp = '%s%s' % (currentState, genes[i][j],)
        if temp not in trie.keys():
            states = states + 1
            trie[temp] = [states, 0]
        currentState = trie[temp][0]
    outs[currentState] = genes[i] 
queue = []
for char in prev:
    temp = '%s%s' % (0, char,)
    if temp in trie.keys():
        queue.append('%s-%s' % (temp,trie[temp][0]))
        big_q.append('%s-%s' % (temp,trie[temp][0]))

while len(queue) > 0:
    state = queue[-1].split('-')[1]
    parent = queue[-1].split('-')[0]
    queue = queue[:-1]
    for pre in prev:
        temp = '%s%s' % (state, pre)
        if temp in trie.keys():
            queue.append('%s-%d' % (temp,trie[temp][0]))
            big_q.append('%s-%d' % (temp,trie[temp][0]))
            fail = trie[parent][1]
            temp2 = '%s%s' % (fail, pre)
            if temp2 in trie.keys():
                trie[temp][1] = trie[temp2][0]
            else:
                trie[temp][1] = fail
big_dict = {}
for l in big_q:
    if l.split('-')[0] not in big_dict.keys():
        big_dict[l.split('-')[0]] = l.split('-')[1]
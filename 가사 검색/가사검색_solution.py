def solution(words, queries):
    head, head_rev = {}, {}
    wc = []
    
    def add(head,word):
        node = head
        for w in word:
            if w not in node:
                node[w]={}
            node= node[w]
            if 'len' not in node:
                node['len'] = [len_word]
            else:
                node['len'].append(len_word)
        node['end']=True   
    
    for word in words:
        len_word = len(word)
        add(head,word)
        add(head_rev,word[::-1])
        wc.append(len_word)
        
    def search(head, querie):
        count=0
        node = head
        for q in querie:
            if q=='?':
                return node['len'].count(len_qu)
            elif q not in node:
                break
            node = node[q]
        return count

    answer=[]
    for querie in queries:
        len_qu = len(querie)
        if querie[0]=='?':
            if querie[-1]=='?': 
                answer.append(wc.count(len_qu))
            else: 
                answer.append(search(head_rev, querie[::-1]))
        else:
            answer.append(search(head, querie))
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                ["fro??", "????o", "fr???", "fro???", "pro?"]))

# result
# [3, 2, 4, 1, 0]
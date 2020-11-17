// Most similar music
match (m1: Music)-[r:Similarity]-> (m2: Music) where id(m1)=15 return m1, m2 order by r.weight desc limit 1

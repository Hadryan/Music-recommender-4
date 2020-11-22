// Most similar music
match (m1: Music)-[r:Similarity]- (m2: Music) where id(m1)=15 return m1, m2 order by r.weight desc limit 1

// most listened musics
match (p: Person)-[r:Listened]-> (m: Music) where id(p)=32 return p, m order by r.times desc limit 1

// liked musics
match (p: Person)-[r:Liked]-> (m: Music) where id(p)=50 return p, m

class UnionFind:
  def __init__(self,n):
    self.n=n
    self.parent=[i for i in range(n)] # 親
    self.rank=[1]*n # 木の高さ
    self.size=[1]*n # size[i]はiを根とするグループのサイズ
    
  def find(self,x): # xの根を返す
    if self.parent[x]==x:
      return x
    else:
      self.parent[x]=self.find(self.parent[x]) # 経路圧縮
      return self.parent[x]
  
  def unite(self,x,y): # x,yの属する集合を併合する
    x=self.find(x)
    y=self.find(y)
    if x != y:
      if self.rank[x]<self.rank[y]:
        self.parent[x]=y
        self.size[y]+=self.size[x]
      else:
        self.parent[y]=x
        self.size[x]+=self.size[y]
        if self.rank[x]==self.rank[y]:
          self.rank[x]+=1

  def group_size(self,x): # xが属する集合の大きさを返す
    return self.size[self.find(x)]

N, M =map(int,input().split())
A, B = [0]*M, [0]*M

direct = [[] for _ in range(N)]
uf = UnionFind(N)

for i in range(M):
    A[i], B[i] = map(int,input().split())
    A[i] -= 1
    B[i] -= 1
    uf.unite(A[i], B[i])

ans = 0
for i in range(N):
    ans = max(ans, uf.group_size(i))
print(ans)
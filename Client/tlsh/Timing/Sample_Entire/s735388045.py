field = input()

#%%
idxes = [] # \の位置を管理。一個/が追加されるたびに、その部分は水たまりになれるので、後ろからpopされる
v_lakes = [] # （その水たまりの最も左の\の位置、その水たまりの現時点での面積）の組を格納

for i, f in enumerate(field):
    if f == '\\':
        idxes.append(i) # \の位置を記録
    elif f == '/' and len(idxes) > 0:
        j = idxes.pop() # 最後尾の\の位置を抜き出す
        v = i - j   # \/間の長さがテンポラリの面積vに対応
        # 可能であるなら面積を統合する処理。螺旋本の19の面積みたいに、内側に2つ水たまりができるけどもっと大きく統合できるパターンがある
        # 今回新しく積み上げたj が すでに格納されてる水溜りの左端（v_lakes[-1][0]）よりも、小さい（より左側にある）場合は水溜りを統合してもよい
        while len(v_lakes) > 0 and v_lakes[-1][0] > j:
            v += v_lakes.pop()[1] # 統合する水溜りをpopして加える
        v_lakes.append((j, v))

ans = [v[1] for v in v_lakes]
print(sum(ans))
print(len(ans), *ans)

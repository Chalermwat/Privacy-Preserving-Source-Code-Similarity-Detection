import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n, k = map(int, input().split())

    v_s = list(map(int, input().split()))
    v_s_rev = list(reversed(v_s))

    ans = 0
    for i in range(min(n, k) + 1):
        left = i

        for j in range(min(n, k) + 1 - i):
            right = j
            remove = min(n, k) - i - j
            if k > n:
                remove += k - n

            val_list = v_s[0:left] + v_s_rev[0:right]
            val_list.sort()
            for loop_k in range(remove):
                if len(val_list) == 0:
                    break
                if len(val_list) < loop_k + 1:
                    break
                if val_list[loop_k] >= 0:
                    break
                val_list[loop_k] = 0

            ans = max(ans, sum(val_list))

    print(ans)


class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve(sys._getframe().f_back.f_code.co_name)
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """6 4
-10 8 2 1 2 6"""
        output = """14"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """6 4
-6 -100 50 -2 -5 -3"""
        output = """44"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """6 3
-6 -100 50 -2 -5 -3"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """6 1
-100 14 1 1 -1 10"""
        output = """10"""
        self.assertIO(test_input, output)

    def test_input_5(self):
        test_input = """6 2
-100 14 1 1 -1 10"""
        output = """10"""
        self.assertIO(test_input, output)

    def test_input_6(self):
        test_input = """6 3
-100 14 1 1 -1 10"""
        output = """14"""
        self.assertIO(test_input, output)

    def test_input_7(self):
        test_input = """6 4
-100 14 1 1 -1 10"""
        output = """24"""
        self.assertIO(test_input, output)

    def test_input_8(self):
        test_input = """6 5
-100 14 1 1 -1 10"""
        output = """25"""
        self.assertIO(test_input, output)

    def test_input_9(self):
        test_input = """6 6
-100 14 1 1 -1 10"""
        output = """26"""
        self.assertIO(test_input, output)

    def test_input_10(self):
        test_input = """6 7
-100 14 1 1 -1 10"""
        output = """26"""
        self.assertIO(test_input, output)

    def test_input_11(self):
        test_input = """7 100
-100 14 -40 1 1 -30 10"""
        output = """26"""
        self.assertIO(test_input, output)

    def test_input_20(self):
        test_input = """50 100
-764207 3102944 -2816278 3249966 5606865 -5997439 4365454 1776907 -1954736 1584162 -437416 -964246 -1828950 -9965518 8636253 -6232397 3421258 -7526570 -7457280 7482600 -1554803 1252 6781335 -3233072 9958581 2263691 -3088247 -2356190 7836991 -1918599 -164787 -9946145 -4801498 3171733 4929342 -6133400 1034826 3746419 -8038615 -7593315 -6791676 5749280 -6696702 6056324 1545511 -2745311 7686370 9321150 -140154 1709122"""
        output = """111018336"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()

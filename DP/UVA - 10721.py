import os
import sys
import time

DEBUG = os.getenv("_DEBUG")
if DEBUG:
    input = open("cmake-build-debug/input.txt", "r").readline
    # sys.stdout = open("output.txt", 'w')
else:
    input = sys.stdin.readline
    output = sys.stdout.write


def main(tc):
    while True:
        try:
            str = input().strip()
            if (str == ''):
                break
            n, k, m = map(int, str.split())
        except EOFError:
            break

        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def solve(n, k):
            if n == 0:
                return 1 if k == 0 else 0
            if k == 0:
                return 0
            if dp[n][k] != -1:
                return dp[n][k]

            dp[n][k] = 0
            for i in range(1, min(n, m) + 1):
                dp[n][k] += solve(n - i, k - 1)

            return dp[n][k]

        print(solve(n, k))



if __name__ == '__main__':
    start_time = time.time()
    T = 1
    # T = int(input())
    for tc in range(T):
        main(tc)
    if DEBUG:
        print("\n--- %s ms ---" % ((time.time() - start_time) * 1000))

import subprocess
import time

def benchmark():

    start = time.time()

    subprocess.run(["./build/Release/AIGeneratedGame.exe"])

    end = time.time()

    runtime = end - start

    print("Runtime:", runtime)

    return runtime


if __name__ == "__main__":
    benchmark()

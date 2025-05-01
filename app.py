from flask import Flask, render_template, request, jsonify
from functools import lru_cache
import time

app = Flask(__name__)

# Fibonacci with memoization (optimized)
@lru_cache(maxsize=None)
def recursive_fib(n):
    if n <= 1:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)

# Iterative Fibonacci (faster for large n)
def iterative_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Generate Fibonacci sequence
def generate_sequence(n, method="iterative"):
    sequence = []
    fib_func = iterative_fib if method == "iterative" else recursive_fib
    for i in range(n):
        sequence.append(fib_func(i))
    return sequence

# Benchmark different methods
def benchmark(n):
    results = {}
    
    # Time recursive (with memoization)
    start = time.time()
    recursive_fib(n)
    results["recursive"] = time.time() - start
    
    # Time iterative
    start = time.time()
    iterative_fib(n)
    results["iterative"] = time.time() - start
    
    return results

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        n = int(request.form["fib_num"])
        method = request.form.get("method", "iterative")
        sequence = generate_sequence(n, method)
        benchmarks = benchmark(n) if n <= 100 else None  # Avoid long benchmarks
        return render_template(
            "index.html", 
            sequence=sequence, 
            benchmarks=benchmarks,
            method=method
        )
    return render_template("index.html")

# API endpoint (optional)
@app.route("/api/fibonacci/<int:n>")
def api_fibonacci(n):
    return jsonify({
        "sequence": generate_sequence(n),
        "benchmark": benchmark(n)
    })

if __name__ == "__main__":
    app.run(debug=True)
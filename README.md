# Fibonacci Sequence Generator - Project Documentation

![image](https://github.com/user-attachments/assets/e8a83446-4198-4f4a-b782-b85f936eb601)

## Table of Contents
- [Project Overview](#project-overview)
- [Fibonacci Sequence Explained](#fibonacci-sequence-explained)
- [Technical Implementation](#technical-implementation)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Performance Comparison](#performance-comparison)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This is a web application that generates Fibonacci sequences using two different algorithmic approaches:
1. **Iterative method** (faster for large sequences)
2. **Recursive method with memoization** (optimized with caching)

The application provides a user-friendly interface to visualize the sequence and compare the performance of both methods.

## Fibonacci Sequence Explained

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

**Mathematical Definition:**
```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
```

**Sequence Visualization:**
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
```

### Fibonacci Spiral Diagram
![Fibonacci Spiral](https://media.geeksforgeeks.org/wp-content/uploads/20231013164044/Fibonacci-Spiral.jpg)

The Fibonacci sequence appears frequently in nature, art, and architecture, often seen in patterns of plant growth, spiral galaxies, and more.

## Technical Implementation

### Algorithm Comparison

#### 1. Iterative Approach
```python
def iterative_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Advantages:** Faster for large numbers, constant space usage

#### 2. Recursive Approach (with Memoization)
```python
@lru_cache(maxsize=None)
def recursive_fib(n):
    if n <= 1:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)
```
- **Time Complexity:** O(n) with memoization (O(2^n) without)
- **Space Complexity:** O(n) for call stack and cache
- **Advantages:** More mathematically elegant, demonstrates recursion

### Performance Benchmarking
The application includes a benchmarking function that compares execution times:
```python
def benchmark(n):
    results = {}
    # Time recursive
    start = time.time()
    recursive_fib(n)
    results["recursive"] = time.time() - start
    
    # Time iterative
    start = time.time()
    iterative_fib(n)
    results["iterative"] = time.time() - start
    
    return results
```

## Features

1. **User-Friendly Interface**
   - Clean, responsive design with animations
   - Input validation (1-1000 numbers)
   - Visual feedback during interactions

2. **Sequence Visualization**
   - Animated display of Fibonacci numbers
   - Clear labeling of generation method

3. **Performance Metrics**
   - Side-by-side comparison of algorithm speeds
   - Automatic benchmarking (disabled for n > 100)

4. **Web API**
   - JSON endpoint for programmatic access
   - Returns sequence and benchmark data

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/muzaffar401/Fibonacci-Sequence-Generator.git
   cd Fibonacci-Sequence-Generator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser to:
   ```
   http://localhost:5000
   ```

## Usage

1. Enter the number of Fibonacci numbers you want to generate (1-1000)
2. Select your preferred generation method:
   - Iterative (faster for large sequences)
   - Recursive (memoized implementation)
3. Click "Generate Sequence"
4. View the results and performance comparison

## API Endpoint

The application provides a REST API endpoint:

```
GET /api/fibonacci/<int:n>
```

**Example Response:**
```json
{
  "sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
  "benchmark": {
    "iterative": 0.000012,
    "recursive": 0.000045
  }
}
```

## Performance Comparison

### Time Complexity Analysis

| Method      | Best Case | Worst Case | Space Complexity |
|-------------|-----------|------------|-------------------|
| Iterative   | O(n)      | O(n)       | O(1)              |
| Recursive   | O(n)      | O(2^n)*    | O(n)              |

*Without memoization. With memoization (as implemented), recursive is O(n).

### Benchmark Results (n=35)

| Method      | Time (seconds) |
|-------------|----------------|
| Iterative   | 0.000012       |
| Recursive   | 0.000045       |

![Performance Chart](https://www.simplilearn.com/ice9/free_resources_article_thumb/Recursion_Call_Stack.png)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Python Package Manager ###
# PIP = Python Index Package

# Examples uwing NumPy
import numpy as np

# Print NumPy version
print(np.version.version) # 2.1.3

# Codigo extraido del sitio web de NumPy
x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99
print(x)
print(x.max(axis=1))

rng = np.random.default_rng()
samples = rng.normal(size=2500)
print(samples)

# Mas ejemplos usando NumPy
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.shape) # (2, 3)
print(a.ndim) # 2

# MoureDev
numpy_array = np.array([35, 24, 62, 30, 30, 17])
print(type(numpy_array))
print(numpy_array * 2)

# Examples using Pandas
import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnel, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)
print(df["Age"])

ages = pd.Series([22, 35, 58], name="Age")
print(ages)

# I want to know the maximum age
print(df["Age"].max()) # 58

print(df.describe())

# Example using requests
import requests as rq

response = rq.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

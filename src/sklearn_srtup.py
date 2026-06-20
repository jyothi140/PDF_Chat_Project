# Import the specialized 'metrics' module from scikit-learn
# This module contains the high-performance distance and similarity tools
from sklearn.metrics.pairwise import cosine_similarity
# Import numpy to handle the numerical lists (vectors)
import numpy as np

# 1. We create two dummy vectors (simulating 768D AI coordinates)
# We use small 3-item lists here just to keep the example simple
vector_a = np.array([[0.1, 0.2, 0.3]]) # The double brackets [[ ]] are required by sklearn
vector_b = np.array([[0.1, 0.2, 0.4]])

print("---  Scikit-Learn Toolkit Check ---")

try:
    # 2. Use sklearn's high-speed function to calculate similarity
    # Unlike our manual math, this function can handle thousands of vectors at once!
    similarity_score = cosine_similarity(vector_a, vector_b)
    
    # 3. Print the result (it returns a 'matrix', so we grab the first value)
    print(f" SUCCESS: Scikit-learn is installed and running.")
    print(f"Similarity Calculation Result: {similarity_score[0][0]:.4f}")

except Exception as e:
    # 4. Catch any errors if the library isn't found
    print(f" ERROR: Scikit-learn check failed. {e}")

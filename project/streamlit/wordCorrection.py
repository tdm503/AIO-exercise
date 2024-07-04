def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

def levenshtein_distance(token1, token2):
    # Initialize a 2D list to store distances
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    # Initialize the first row and column with sequential values
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    # Loop through the tokens and compute distances
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            # Calculate minimum of insert, delete, or substitution
            distances[t1][t2] = min(distances[t1][t2 - 1] + 1,   # Insert
                                    distances[t1 - 1][t2] + 1,   # Delete
                                    distances[t1 - 1][t2 - 1] + substitution_cost)  # Substitute

    # Return the final Levenshtein distance
    return distances[len(token1)][len(token2)]


import streamlit as st
def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):
        # Replace with your own logic to load vocabularies
        vocabs = ['apple', 'banana', 'orange', 'grape', 'melon']

        # Compute Levenshtein distances
        leven_distances = {}
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # Sort by distance
        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))

        # Get the correct word with the smallest distance
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word:', correct_word)

        # Display vocabulary and distances
        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distances)

if __name__ == "__main__":
    main()
import numpy as np

class AI_RNA_Secondary_Structure:
    def __init__(self, rna_sequence):
        self.rna_sequence = rna_sequence
        self.sequence_length = len(rna_sequence)
        self.base_pairing_rules = {"A": "U", "U": "A", "C": "G", "G": "C"}
        self.min_loop_length = 4
        self.optimal_pairs_matrix = self.compute_optimal_pairs()

    def compute_optimal_pairs(self):
        rows = self.sequence_length
        cols = self.sequence_length
        opt_matrix = np.zeros((rows, cols))
        
        # Step through all substrings longer than minimum loop length
        for substring_length in range(self.min_loop_length + 1, self.sequence_length):
            for i in range(self.sequence_length - substring_length):
                j = i + substring_length
                
                # Option 1: exclude the j-th nucleotide
                option_exclude_j = opt_matrix[i][j-1]
                
                # Option 2: try pairing j with some t
                option_pair_list = [0]
                for t in range(i+1, j):
                    if self.rna_sequence[t] == self.base_pairing_rules[self.rna_sequence[j]]:
                        temp_pairs = 1 + opt_matrix[i][t-1] + opt_matrix[t+1][j-1]
                        option_pair_list.append(temp_pairs)
                
                # Step 3: take the maximum of all considered options
                opt_matrix[i][j] = max(option_exclude_j, max(option_pair_list))
        
        return opt_matrix

    def display_results(self):
        print("Optimal pairing matrix:")
        print(self.optimal_pairs_matrix)
        max_pairs = self.optimal_pairs_matrix[0][-1]
        print("Maximum number of base pairs =", max_pairs)

# Example usage
if __name__ == "__main__":
    RNA_sequence = "GUCGAUUGAGCGAAUGUAACAACGUGGCUACGGCGAGA"
    ai_solution = AI_RNA_Secondary_Structure(RNA_sequence)
    ai_solution.display_results()

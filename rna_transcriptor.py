def to_rna(dna_strand):
    DNA = ['G', 'C', 'T', 'A']
    RNA = ['C', 'G', 'A', 'U']
    rna_strand = [RNA[DNA.index(nucleotide)] for nucleotide in dna_strand]
    return ''.join(rna_strand)

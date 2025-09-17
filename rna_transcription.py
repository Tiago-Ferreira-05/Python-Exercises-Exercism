def to_rna(dna_strand):
    dna = "GCTA"
    rna = "CGAU"

    translation_table = str.maketrans(dna, rna)

    return dna_strand.translate(translation_table)

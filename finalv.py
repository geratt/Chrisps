# Chrisps

gen = str(input("Genome code:"))
seq = str(input('Restriction Sequence:'))
x = gen.find(seq)
if x >= 0:
    print('restriction site is found')
    print(x)
    a = len(gen)
    i = 1
    b = len(seq)
    if x%3==0:
        while i <= b//3:
            def codon_type (codon):
                match codon:
                    case ("TTT"|"TTC"):
                        print ("Phe. Your options: TTT, TTC")
                    case ("TTA"|"TTG"|"CTT"|"CTC"|"CTA"|"CTG"):
                        print ("Leu. Your options: TTA, TTG, CTT, CTC, CTA, CTG")
                    case ("ATT"|"ATC"|"ATA"):
                        print ("Ile. Your options: ATT, ATC, ATA")
                    case ("GTT"|"GTC"|"GTA"|"GTG"):
                        print ("Val. Your options: GTT, GTC, GTA, GTG")
                    case ("TCT"|"TCC"|"TCA"|"TCG"|"AGT"|"AGC"):
                        print ("Ser. Your options: TCT, TCC, TCA, TCG, AGT, AGC")
                    case ("CCT"|"CCC"|"CCA"|"CCG"):
                        print ("Pro. Your options: CCT, CCC, CCA, CCG")
                    case ('ACT'|'ACC'|'ACA'|'ACG'):
                        print ("Thr. Your options: ACT, ACC, ACA, ACG")
                    case ('GCT'|'GCC'|'GCA'|'GCG'):
                        print ("Ala. Your options: GCT, GCC, GCA, GCG")
                    case ('TAT'|'TAC'):
                        print ("Tyr. Your options: TAT, TAC")
                    case ('CGT'|'CGC'|'CGA'|'CGG'|'AGA'|'AGG'):
                        print ("Arg. Your options: CGT, CGC, CGA, CGG, AGA, AGG")
                    case ('GGT'|'GGC'|'GGA'|'GGG'):
                        print ("Gly. Your options: GGT, GGC, GGA, GGG")
                    case ('CAT'|'CAC'):
                        print ("His. Your options: CAT, CAC")
                    case ('CAA'|'CAG'):
                        print ("Gin. Your options: CAA, CAG")
                    case ('AAT'|'AAC'):
                        print ("Asn. Your options: AAT, AAC")
                    case ('AAA'|'AAG'):
                        print ("Lys. Your options: AAA, AAG")
                    case ('GAT'|'GAC'):
                        print ("Asp. Your options: GAT, GAC")
                    case ('GAA'|'GAG'):
                        print ("Glu. Your options: GAA, GAG")
                    case ('TGT'|'TGC'):
                        print ("Cys. Your options: TGT, TGC")
                    case _:
                        print ("There is no other option")
            i+=1        
            codon_type (gen[x+3*i-3 : x+3*i])
    if x%3==1:
        if b%3==2:
            while i<=b//3+1:
                def codon_type (codon):
                    match codon:
                        case ("TTT"|"TTC"):
                            print ("Phe. Your options: TTT, TTC")
                        case ("TTA"|"TTG"|"CTT"|"CTC"|"CTA"|"CTG"):
                            print ("Leu. Your options: TTA, TTG, CTT, CTC, CTA, CTG")
                        case ("ATT"|"ATC"|"ATA"):
                            print ("Ile. Your options: ATT, ATC, ATA")
                        case ("GTT"|"GTC"|"GTA"|"GTG"):
                            print ("Val. Your options: GTT, GTC, GTA, GTG")
                        case ("TCT"|"TCC"|"TCA"|"TCG"|"AGT"|"AGC"):
                            print ("Ser. Your options: TCT, TCC, TCA, TCG, AGT, AGC")
                        case ("CCT"|"CCC"|"CCA"|"CCG"):
                            print ("Pro. Your options: CCT, CCC, CCA, CCG")
                        case ('ACT'|'ACC'|'ACA'|'ACG'):
                            print ("Thr. Your options: ACT, ACC, ACA, ACG")
                        case ('GCT'|'GCC'|'GCA'|'GCG'):
                            print ("Ala. Your options: GCT, GCC, GCA, GCG")
                        case ('TAT'|'TAC'):
                            print ("Tyr. Your options: TAT, TAC")
                        case ('CGT'|'CGC'|'CGA'|'CGG'|'AGA'|'AGG'):
                            print ("Arg. Your options: CGT, CGC, CGA, CGG, AGA, AGG")
                        case ('GGT'|'GGC'|'GGA'|'GGG'):
                            print ("Gly. Your options: GGT, GGC, GGA, GGG")
                        case ('CAT'|'CAC'):
                            print ("His. Your options: CAT, CAC")
                        case ('CAA'|'CAG'):
                            print ("Gin. Your options: CAA, CAG")
                        case ('AAT'|'AAC'):
                            print ("Asn. Your options: AAT, AAC")
                        case ('AAA'|'AAG'):
                            print ("Lys. Your options: AAA, AAG")
                        case ('GAT'|'GAC'):
                            print ("Asp. Your options: GAT, GAC")
                        case ('GAA'|'GAG'):
                            print ("Glu. Your options: GAA, GAG")
                        case ('TGT'|'TGC'):
                            print ("Cys. Your options: TGT, TGC")
                        case _:
                            print ("There is no other option")
                i+=1        
                codon_type (gen[x+3*i-4 : x+3*i-1])
        else:
            while i<=b//3:
                def codon_type (codon):
                    match codon:
                        case ("TTT"|"TTC"):
                            print ("Phe. Your options: TTT, TTC")
                        case ("TTA"|"TTG"|"CTT"|"CTC"|"CTA"|"CTG"):
                            print ("Leu. Your options: TTA, TTG, CTT, CTC, CTA, CTG")
                        case ("ATT"|"ATC"|"ATA"):
                            print ("Ile. Your options: ATT, ATC, ATA")
                        case ("GTT"|"GTC"|"GTA"|"GTG"):
                            print ("Val. Your options: GTT, GTC, GTA, GTG")
                        case ("TCT"|"TCC"|"TCA"|"TCG"|"AGT"|"AGC"):
                            print ("Ser. Your options: TCT, TCC, TCA, TCG, AGT, AGC")
                        case ("CCT"|"CCC"|"CCA"|"CCG"):
                            print ("Pro. Your options: CCT, CCC, CCA, CCG")
                        case ('ACT'|'ACC'|'ACA'|'ACG'):
                            print ("Thr. Your options: ACT, ACC, ACA, ACG")
                        case ('GCT'|'GCC'|'GCA'|'GCG'):
                            print ("Ala. Your options: GCT, GCC, GCA, GCG")
                        case ('TAT'|'TAC'):
                            print ("Tyr. Your options: TAT, TAC")
                        case ('CGT'|'CGC'|'CGA'|'CGG'|'AGA'|'AGG'):
                            print ("Arg. Your options: CGT, CGC, CGA, CGG, AGA, AGG")
                        case ('GGT'|'GGC'|'GGA'|'GGG'):
                            print ("Gly. Your options: GGT, GGC, GGA, GGG")
                        case ('CAT'|'CAC'):
                            print ("His. Your options: CAT, CAC")
                        case ('CAA'|'CAG'):
                            print ("Gin. Your options: CAA, CAG")
                        case ('AAT'|'AAC'):
                            print ("Asn. Your options: AAT, AAC")
                        case ('AAA'|'AAG'):
                            print ("Lys. Your options: AAA, AAG")
                        case ('GAT'|'GAC'):
                            print ("Asp. Your options: GAT, GAC")
                        case ('GAA'|'GAG'):
                            print ("Glu. Your options: GAA, GAG")
                        case ('TGT'|'TGC'):
                            print ("Cys. Your options: TGT, TGC")
                        case _:
                            print ("There is no other option")
                i+=1        
                codon_type (gen[x+3*i-4 : x+3*i-1])
    if x%3==2:
        if b%3==0:
            while i<=b/3:
                def codon_type (codon):
                    match codon:
                        case ("TTT"|"TTC"):
                            print ("Phe. Your options: TTT, TTC")
                        case ("TTA"|"TTG"|"CTT"|"CTC"|"CTA"|"CTG"):
                            print ("Leu. Your options: TTA, TTG, CTT, CTC, CTA, CTG")
                        case ("ATT"|"ATC"|"ATA"):
                            print ("Ile. Your options: ATT, ATC, ATA")
                        case ("GTT"|"GTC"|"GTA"|"GTG"):
                            print ("Val. Your options: GTT, GTC, GTA, GTG")
                        case ("TCT"|"TCC"|"TCA"|"TCG"|"AGT"|"AGC"):
                            print ("Ser. Your options: TCT, TCC, TCA, TCG, AGT, AGC")
                        case ("CCT"|"CCC"|"CCA"|"CCG"):
                            print ("Pro. Your options: CCT, CCC, CCA, CCG")
                        case ('ACT'|'ACC'|'ACA'|'ACG'):
                            print ("Thr. Your options: ACT, ACC, ACA, ACG")
                        case ('GCT'|'GCC'|'GCA'|'GCG'):
                            print ("Ala. Your options: GCT, GCC, GCA, GCG")
                        case ('TAT'|'TAC'):
                            print ("Tyr. Your options: TAT, TAC")
                        case ('CGT'|'CGC'|'CGA'|'CGG'|'AGA'|'AGG'):
                            print ("Arg. Your options: CGT, CGC, CGA, CGG, AGA, AGG")
                        case ('GGT'|'GGC'|'GGA'|'GGG'):
                            print ("Gly. Your options: GGT, GGC, GGA, GGG")
                        case ('CAT'|'CAC'):
                            print ("His. Your options: CAT, CAC")
                        case ('CAA'|'CAG'):
                            print ("Gin. Your options: CAA, CAG")
                        case ('AAT'|'AAC'):
                            print ("Asn. Your options: AAT, AAC")
                        case ('AAA'|'AAG'):
                            print ("Lys. Your options: AAA, AAG")
                        case ('GAT'|'GAC'):
                            print ("Asp. Your options: GAT, GAC")
                        case ('GAA'|'GAG'):
                            print ("Glu. Your options: GAA, GAG")
                        case ('TGT'|'TGC'):
                            print ("Cys. Your options: TGT, TGC")
                        case _:
                            print ("There is no other option")
                i+=1        
                codon_type (gen[x+3*i-5 : x+3*i-2])
        else:
            while i<=b//3+1:
                def codon_type (codon):
                    match codon:
                        case ("TTT"|"TTC"):
                            print ("Phe. Your options: TTT, TTC")
                        case ("TTA"|"TTG"|"CTT"|"CTC"|"CTA"|"CTG"):
                            print ("Leu. Your options: TTA, TTG, CTT, CTC, CTA, CTG")
                        case ("ATT"|"ATC"|"ATA"):
                            print ("Ile. Your options: ATT, ATC, ATA")
                        case ("GTT"|"GTC"|"GTA"|"GTG"):
                            print ("Val. Your options: GTT, GTC, GTA, GTG")
                        case ("TCT"|"TCC"|"TCA"|"TCG"|"AGT"|"AGC"):
                            print ("Ser. Your options: TCT, TCC, TCA, TCG, AGT, AGC")
                        case ("CCT"|"CCC"|"CCA"|"CCG"):
                            print ("Pro. Your options: CCT, CCC, CCA, CCG")
                        case ('ACT'|'ACC'|'ACA'|'ACG'):
                            print ("Thr. Your options: ACT, ACC, ACA, ACG")
                        case ('GCT'|'GCC'|'GCA'|'GCG'):
                            print ("Ala. Your options: GCT, GCC, GCA, GCG")
                        case ('TAT'|'TAC'):
                            print ("Tyr. Your options: TAT, TAC")
                        case ('CGT'|'CGC'|'CGA'|'CGG'|'AGA'|'AGG'):
                            print ("Arg. Your options: CGT, CGC, CGA, CGG, AGA, AGG")
                        case ('GGT'|'GGC'|'GGA'|'GGG'):
                            print ("Gly. Your options: GGT, GGC, GGA, GGG")
                        case ('CAT'|'CAC'):
                            print ("His. Your options: CAT, CAC")
                        case ('CAA'|'CAG'):
                            print ("Gin. Your options: CAA, CAG")
                        case ('AAT'|'AAC'):
                            print ("Asn. Your options: AAT, AAC")
                        case ('AAA'|'AAG'):
                            print ("Lys. Your options: AAA, AAG")
                        case ('GAT'|'GAC'):
                            print ("Asp. Your options: GAT, GAC")
                        case ('GAA'|'GAG'):
                            print ("Glu. Your options: GAA, GAG")
                        case ('TGT'|'TGC'):
                            print ("Cys. Your options: TGT, TGC")
                        case _:
                            print ("There is no other option")
                i+=1        
                codon_type (gen[x+3*i-5 : x+3*i-2])
else:
    print('not found')

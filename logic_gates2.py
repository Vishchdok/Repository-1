import logic_gates as lg

# Test NANDgate functionality
print "NAND gate test"
print lg.NANDgate(0,0)
print lg.NANDgate(0,1)
print lg.NANDgate(1,0)
print lg.NANDgate(1,1)

# NOT gate from NAND gates
def NOTgate(a):
    return lg.NANDgate(a,a)

# Test NOTgate
print "NOT gate test"
print NOTgate(1)
print NOTgate(0)

# AND gate from NAND gates
def ANDgate(a,b):
    return lg.NANDgate(lg.NANDgate(a,b),lg.NANDgate(a,b))

# Test ANDgate
print "AND gate test"
print ANDgate(0,0)
print ANDgate(0,1)
print ANDgate(1,0)
print ANDgate(1,1)

# OR gate from NAND gates
def ORgate(a,b):
    nota = lg.NANDgate(a,a)
    notb = lg.NANDgate(b,b)
    nota_and_notb = lg.NANDgate(lg.NANDgate(nota,notb),lg.NANDgate(nota,notb))
    return lg.NANDgate(nota_and_notb,nota_and_notb)

# Test ORgate
print "OR gate test"
print ORgate(0,0)
print ORgate(0,1)
print ORgate(1,0)
print ORgate(1,1)

# XOR gate from NAND gates
def XORgate(a,b):
    return ORgate(ANDgate(NOTgate(a),b),ANDgate(NOTgate(b),a))

# Test XORgate
print "XOR gate test"
print XORgate(0,0)
print XORgate(1,0)
print XORgate(0,1)
print XORgate(1,1)

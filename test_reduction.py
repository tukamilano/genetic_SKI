from calculate.reduction import ski_calculator_reduce

Y = "AASAKAASIIAASAASAKSKAKAASII"

term = "A" + Y + "X"
for i in range(100):
    term, _= ski_calculator_reduce(term)
    print(term)


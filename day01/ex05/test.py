from eval import Evaluator

print("\n\x1b[1;34;40mZip\x1b[0m")
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)

print("\n\x1b[1;34;40mEnumerate\x1b[0m")
Evaluator.enumerate_evaluate(coefs, words)

print("\n\x1b[1;34;40mWrong length\x1b[0m")
words = []
Evaluator.enumerate_evaluate(coefs, words)

print("\n\x1b[1;34;40mWrong type\x1b[0m")
words = 12
Evaluator.zip_evaluate(coefs, words)

print("\n\x1b[1;34;40mWrong type in array\x1b[0m")
words = [42, 42, 42, 42, 42]
Evaluator.zip_evaluate(coefs, words)
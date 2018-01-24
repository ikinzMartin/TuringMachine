import turing

# This program detects whether the given word is a palindrome

data = '1001'
program = \
"""
004_>
011_>
0_x_>

1111>
1010>
1_2_<

4141>
4040>
4_5_<

213_<
2_x_>

503_<
5_x_>

3131<
3030<
3_0_>
"""

print ('Output data: ' + str(turing.Turing(program, data).Run(0.3)))


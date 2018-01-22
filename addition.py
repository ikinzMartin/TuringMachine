import turing

# This program replaces 1s by x until it meet '0'. All 1s are appended to the
# end of data

data = '1011'
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

503_<

3131<
3030<
3_0_>
"""

print ('Output data: ' + str(turing.Turing(program, data).Run(0.3)))


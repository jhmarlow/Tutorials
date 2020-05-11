# Tic tac toe

# ------ Game Function ----------

def tictactoe(x, y, t):
    if t == 0:
        t = 'X'
    elif t == 1:
        t = 'O'

    charar[y, x] = t
    pw_bytes.decode("utf-8")
    print(charar, pw_bytes)


# ------- Initialize game -----------
import numpy as np
charar = np.chararray((3, 3))
charar[:] = ''
print(charar[:])


# -------- Game play --------
# Marker type (t): 0 = 'X', 1 = 'O'
# Marker position: first row/column = 0, middle row/column 1 last row/column = 2
# Function: tictactoe(x position, y position, type)

# Run function to play
print(tictactoe(2, 0, 1))


import matplotlib.pyplot as plt

plt.plot(1,2,'rx')

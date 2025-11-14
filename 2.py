# -------------------------------
# PASS-II: MACRO PROCESSOR
# -------------------------------

# MNT (Macro Name Table)
mnt = {
    "INCR": 1,
    "DECR": 5
}

# MDT (Macro Definition Table)
mdt = {
    1: "LOAD A",
    2: "ADD 1",
    3: "STORE A",
    4: "MEND",
    5: "LOAD A",
    6: "SUB 1",
    7: "STORE A",
    8: "MEND"
}

# Intermediate Code (no macro definitions)
intermediate_code = [
    "START",
    "INCR",
    "DECR",
    "STOP",
    "END"
]

# -------------------------------
# PASS-II Processing
# -------------------------------

expanded_code = []   # final output

for line in intermediate_code:
    words = line.split()

    # Check if the first word is a macro name
    if len(words) > 0 and words[0] in mnt:
        print(f"Expanding macro: {words[0]}")
        index = mnt[words[0]]

        # Copy macro body from MDT until MEND
        while mdt[index] != "MEND":
            expanded_code.append(mdt[index])
            index += 1
    else:
        expanded_code.append(line)

# -------------------------------
# OUTPUT
# -------------------------------
print("\nExpanded Code after Pass-II:")
for line in expanded_code:
    print(line)

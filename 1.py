# Macro Processor Simulation (Predefined MACRO Code)

mnt = []   # Macro Name Table
mdt = []   # Macro Definition Table

# --- Predefined Macro Code ---
# Example macro: INCR increments a number by 1
macro_code = [
    "MACRO",
    "INCR",
    "LOAD A",
    "ADD 1",
    "STORE A",
    "MEND",
    "END"
]

# --- Processing Starts ---
i = 0
while i < len(macro_code):
    line = macro_code[i].strip()

    if line == "MACRO":
        name = macro_code[i + 1].strip()     # next line is macro name
        mnt.append([name, len(mdt) + 1])     # store name and MDT pointer
        i += 2

        # add macro body till MEND
        while macro_code[i].strip() != "MEND":
            mdt.append(macro_code[i].strip())
            i += 1
        mdt.append("MEND")
    i += 1

# --- Display Tables ---
print("\nMNT (Macro Name Table):")
print("Name\tMDT Index")
for name, index in mnt:
    print(f"{name}\t{index}")

print("\nMDT (Macro Definition Table):")
for index, line in enumerate(mdt, start=1):
    print(f"{index}\t{line}")

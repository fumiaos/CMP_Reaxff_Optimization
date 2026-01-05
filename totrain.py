def to_train(data,num):
    lines = data.strip().split('\n')
    output = ""
    energies = []
    for line in lines:
        if "E =" in line:
            energy = line.split('E =')[1].strip()
            energies.append(energy)
    print(energies)
    for i, energy in enumerate(energies, start=1):
        #print(f"CoO_{i} E={energy}")
        #print(i)
        #print(2**i)
        rel_E = 1+(float(energies[i-1])/(num)-float(energies[0])/num)*627.509474
        if i ==1:
            pass
        else:
            output+=(f" 1.00  +   co0001_{i}/{num}   -   co0001_1/{num}                                      {rel_E}\n")
    return output
    # 1.00  +   hsh-SH1.15/1   -   hshBase/1                                      15.98476




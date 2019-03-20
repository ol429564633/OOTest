class Config:
    dir = r"E:\TestHelper"
    diff_file = dir + r"\diff.txt"
    # input_file = r"D:\OneDrive\Workspace\Java\untitled12\testInput.txt"
    input_file = dir + r"\in.txt"
    Saber = dir + r"\Saberout.txt"
    Archer = dir + r"\Archerout.txt"
    Alterego = dir + r"\Alteregoout.txt"
    Berserker = dir + r"\Berserkerout.txt"
    Caster = dir + r"\Casterout.txt"
    Lancer = dir + r"\Lancerout.txt"
    Rider = dir + r"\Riderout.txt"
    Assassin = dir + r"\Assassinout.txt"
    zyc = dir + r"\zycout.txt"
    hdl = dir + r"\hdlout.txt"
    auto_cmd = dir + r"\auto.cmd"
    # output_files = {"Saber": Saber, "Archer": Archer, "Alterego": Alterego, "Berserker": Berserker, "Caster": Caster,
    #                 "Lancer": Lancer, "Rider": Rider, "Assassin": Assassin}
    # output_files = {"Archer": Archer, "Alterego": Alterego, "Berserker": Berserker, "Caster": Caster,
    #                 "Lancer": Lancer, "Rider": Rider, "Assassin": Assassin, "Saber": Saber}
    output_files = {"Alterego": Alterego, "Caster": Caster, "Rider": Rider, "Saber": Saber}
    # output_files = {"Alterego": Alterego, "Archer": Archer, "ZYC": zyc, "HDL": hdl}


config = Config()

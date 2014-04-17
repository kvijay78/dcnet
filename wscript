def build(bld):
    obj = bld.create_ns3_program('Experiment', ['core', 'network'])
    obj.source = 'SendPacket.cc'
    obj.env.append_value("CXXFLAGS", "-I/usr/include/crypto++")
    obj.env.append_value("LINKFLAGS", ["-L/usr/lib"])
    obj.env.append_value("LIB", ["integer"])


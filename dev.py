"""
Simple client code for development purposes.
"""

from __future__ import print_function
from __future__ import division

import random
import json
import time
import _msprime
import msprime

def print_sim(sim):
    print("sample_size = ", sim.get_sample_size())
    print("num_loci = ", sim.get_num_loci())
    print("recombination_rate = ", sim.get_recombination_rate())
    print("random_seed = ", sim.get_random_seed())
    print("time = ", sim.get_time())
    print("tree_file = ", sim.get_tree_file())
    print("num_ancestors = ", sim.get_num_ancestors())
    for segs in sim.get_ancestors():
        print(segs)
    print("population models = ")
    for model in sim.get_population_models():
        print(model)
    # print("X = ", sim.get_X())
    # print("X = ", sim.get_X())
    # print("X = ", sim.get_X())

def ll_main():
    treefile = "tmp__NOBACKUP__/tmp2.dat"
    j = 0
    while True:
        j += 1
        models = [{"type":_msprime.POP_MODEL_CONSTANT, "time":0.3, "size":0.2},
                {"type":_msprime.POP_MODEL_EXPONENTIAL, "time":0.5, "alpha":5}]
        sim = _msprime.Simulator(sample_size=400, random_seed=j,
                tree_file_name=treefile,
                num_loci=1000, recombination_rate=0.1,
                max_memory=1024**3, segment_block_size=10**6,
                population_models=models)
        before = time.time()
        print(sim.run())
        #print(sim.run(0.5))
        duration = time.time() - before
        print("Ran in", duration)
        print_sim(sim)

        before = time.time()
        tr = _msprime.TreeFile(treefile)
        tr.sort()
        duration = time.time() - before
        print("create tree_reader Ran in", duration)
        print(tr.get_num_loci())
        print(tr.get_sample_size())
        print(tr.get_num_trees())
        print(tr.get_metadata())
        s = json.loads(tr.get_metadata())
        # print(s)
        before = time.time()
        j = 0
        for r in tr:
            j += 1
        print(j)

        # for j in range(tr.get_num_trees()):
        #     breakpoint, pi, tau = tr.get_tree(j)
        #     #print(j, breakpoint)
        # duration = time.time() - before
        # print("tree loop Ran in", duration)
        # print(sim.run())
        # print_sim(sim)

    # tv = _msprime.TreeViewer(treefile)
    # for length, pi, tau in tv:
    #     print(length, pi, tau)

def hl_main():

    random.seed(1)
    pi, tau = msprime.simulate_tree(4)
    print(pi, tau)
    for l, pi, tau in msprime.simulate_trees(3, 100, 0.1):
        print(l, pi, tau)


if __name__ == "__main__":
    #hl_main()
    ll_main()
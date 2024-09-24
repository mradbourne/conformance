# Runs collation test on only on node
# Test data and output directories are under ~/DDT_DATA
python conformance.py run --test coll_shift_short --exec node --run_limit 27 --file_base ../DDT_DATA

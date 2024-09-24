# Runs collation test on only on python sample
# Test data and output directories are under ~/DDT_DATA
python conformance.py run --test number_fmt --exec "python3 ../executors/python/executor.py"  --run_limit 3 --file_base ~/DDT_DATA

#!/bin/bash
# This test script was originally part of the testdriver module

run='python conformance.py run'

$run --test_type collation_short
$run --test_type collation_short -t decimal_fmt
$run --test_type collation_short --test_type decimal_fmt number_fmt display_names lang_names likely_subtags plural_rules
$run --test collation_short ALL decimal_fmt

$run --test_type datetime_fmt
$run --test_type ALL
$run --type ALL decimal_fmt --exec a b c d

$run --exec node
$run --exec node rust /bin/mytes
$run --exec node --test_type decimal_fmt --icu 71 --cldr 40
$run --exec python3 py/exec.py
$run --test_random 1234
$run --exec --custom_testfile testData/customtest1.json
$run testData/customtest2.json
$run testData/customtest3.json

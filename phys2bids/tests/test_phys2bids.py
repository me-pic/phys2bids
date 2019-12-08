"""
Tests phys2bids.py
"""

import os
import json
from phys2bids import phys2bids


def test_print_summary(tmpdir):
    test_filename = 'input.txt'
    test_ntp_expected = 10
    test_ntp_found = 5
    test_samp_freq = 0.2
    test_time_offset = 0.8
    test_outfile = tmpdir.join('summary')
    test_outfile_log = tmpdir.join('summary.log')
    phys2bids.print_summary(test_filename, test_ntp_expected, test_ntp_found,
                            test_samp_freq, test_time_offset, str(test_outfile))
    assert os.path.isfile(str(test_outfile_log))
    os.remove(str(test_outfile_log))


def test_print_json(tmpdir):
    test_outfile = tmpdir.join('json_test')
    test_outfile_json = tmpdir.join('json_test.json')
    test_samp_freq = 0.1
    test_time_offset = -0.5
    test_ch_name = 'foo'
    phys2bids.print_json(str(test_outfile), test_samp_freq, test_time_offset, test_ch_name)
    assert os.path.isfile(test_outfile_json)
    test_json_data = dict(SamplingFrequency=0.1,
                          StartTime=0.5,
                          Columns='foo')
    with open(test_outfile_json, 'r') as src:
        loaded_data = json.load(src)
    assert test_json_data == loaded_data
    os.remove(str(test_outfile_json))


def test_use_heuristic(tmpdir):
    test_heur_file = 'heur_test_acq'
    test_sub = 'SBJ01'
    test_ses = 'S05'
    test_filename = 'inputfile.txt'
    test_outdir = tmpdir
    test_record_label = 'test'
    phys2bids.use_heuristic(str(test_heur_file), test_sub, test_ses, test_filename, test_outdir, test_record_label)

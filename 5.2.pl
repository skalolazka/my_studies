#!/usr/bin/perl

use strict;
use warnings;

sub swap_bits {
    my ($n, $i, $j) = @_;
    $n = oct("0b$n");
    printf("Input %b, will swap bits $i and $j\n", $n);
    my $q = ($n >> $i) & 1;
#    printf("i-th bit %b\n", $q);
    $q = ($n >> $j) & 1;
#    printf("j-th bit %b\n", $q);
    if ((($n >> $i) & 1) != (($n >> $j) & 1)) {
        $n ^= (1 << $i) | (1 << $j);
    }
    return $n;
}

die "I need a binary string and i and j" unless scalar(@ARGV) == 3;
my $res = swap_bits(@ARGV);
printf("Result: %b\n", $res);

#!/usr/bin/perl

use strict;
use warnings;

sub power_set {
    my @arr = split(//, $_[0]);
    my $ind = oct("0b".(1 x scalar(@arr)));
    print "Input: ".join(',', @arr).", power set:\n";
#    printf("indexes: %b\n", $ind);
    for (my $i = 0; $i <= $ind; $i++) {
        my $res = $ind & $i;
        my $length = scalar(@arr);
        my @res = split(//, sprintf("%0${length}b", $res));
        my $delimiter = '';
        for (my $j = 0; $j < scalar(@arr); $j++) {
            if ($res[$j]) {
                print $delimiter.$arr[$j];
                $delimiter = ',';
            }
        }
        print "empty" unless $res;
        print "\n";
    }
}

die "I need a set (as a string)" unless $ARGV[0];
power_set($ARGV[0]);

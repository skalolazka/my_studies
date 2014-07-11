#!/usr/bin/perl

use strict;

sub fizz_buzz {
    for (my $i = 1; $i <= 100; $i++) {
        if ($i % 3 == 0) { print "fizz" }
        if ($i % 5 == 0) { print "buzz" }
        if ($i % 3 && $i % 5) { print $i }
        print "\n"
    }
}

fizz_buzz();

#!/usr/bin/perl

use strict;
use warnings;

sub int_to_str {
    my $n = $_[0];
    return '0' unless $n;
    my $minus = 0;
    if ($n < 0) {
        $minus = 1;
        $n *= -1;
    }
    my $s = '';
    while ($n) {
        $s = ('0' + $n % 10) . $s;
        $n /= 10;
        last if $n < 1;
    }
    return $minus ? '-'.$s : $s;
}

sub str_to_int {
    my $s = $_[0];
    my $minus = 0;
    if ($s =~ /^\-/) {
        $minus = 1;
        $s =~ s/^\-//;
    }
    my @s = split(//, $s);
    my $n = 0;
    for (my $i = 0; $i < length($s); $i++) {
        if ($s[$i] =~ /^\d$/) {
            $n = $n * 10 + $s[$i];
        }
        else {
            die "Invalid argument $s!";
        }
    }
    return $minus ? $n * -1 : $n;
}

if ($ARGV[1] eq 'str') {
    print int_to_str($ARGV[0])
}
elsif ($ARGV[1] eq 'int') {
    print str_to_int($ARGV[0])
}
else {
    die "Specify 'int' (to convert to int) or 'str' (to convert to str) as a second argument";
}
print "\n";

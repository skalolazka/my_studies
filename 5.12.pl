#!/usr/bin/perl

use strict;
use warnings;

sub any_order {
    my ($one, $two) = @_;
    if ($one->{x} <= $two->{x} && $one->{x} + $one->{w} >= $two->{x}) {
        if ($one->{y} <= $two->{y} + $two->{h} && $one->{y} + $one->{h} >= $two->{y} + $two->{h}) {
            return 1
        }
    }
}

sub are_intersecting {
    my ($one, $two) = @_;
    my $res = any_order($one, $two);
    if ($res) { return (1, 1) }
    $res = any_order($two, $one);
    if ($res) { return (1, 0) }
    return (0, 0);
}

sub max {
    my ($one, $two) = @_;
    return $one >= $two ? $one : $two;
}

sub min {
    my ($one, $two) = @_;
    return $one <= $two ? $one : $two;
}

sub intersection {
    my ($one, $two) = @_;
    my ($x, $y) = (max($one->{x}, $two->{x}), max($one->{y}, $two->{y}));
    my $w = min($one->{x} + $one->{w}, $two->{x} + $two->{w}) - $x;
    my $h = min($one->{x} + $one->{w}, $two->{x} + $two->{w}) - $y;
    return "$x $y $w $h";
}

die "I need two rectangles! 8 numbers: (x, y, width, height) for each rectangle." unless scalar(@ARGV) == 8;
my ($one, $two);
($one->{x}, $one->{y}, $one->{w}, $one->{h}, $two->{x}, $two->{y}, $two->{w}, $two->{h}) = @ARGV;
my ($are, $order) = are_intersecting($one, $two);
if ($are) {
    print "Intersecting.\n";
    my @params = $order ? ($one, $two) : ($two, $one);
    print "Intersection is: ".intersection(@params);
}
else {
    print "Not intersecting.";
}
print "\n";

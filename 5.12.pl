#!/usr/bin/perl

use strict;
use warnings;

sub are_intersecting {
    my %one = %{$_[0]};
    my %two = %{$_[1]};
use Data::Dumper;
    if ($one{x} > $two{x}) {
        if ($one{x} > $two{x} + $two{w}) {
            return 0;
        }
    }
    else {
        if ($one{x} + $one{w} < $two{x}) {
            return 0;
        }
    }
    if ($one{y} > $two{y}) {
        if ($one{y} > $two{y} + $two{h}) {
            return 0;
        }
    }
    else {
        if ($one{y} + $one{h} < $two{y}) {
            return 0;
        }
    }
    return 1;
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
    my %one = %{$_[0]};
    my %two = %{$_[1]};
    my $x = max($one{x}, $two{x});
    my $y = max($one{y}, $two{y});
    my $w = min($one{x} + $one{w}, $two{x} + $two{w}) - $x;
    my $h = min($one{y} + $one{h}, $two{y} + $two{h}) - $y;
    return "$x $y $w $h";
}

die "I need two rectangles! 8 numbers: (x, y, width, height) for each rectangle." unless scalar(@ARGV) == 8;
my (%in_one, %in_two);
($in_one{x}, $in_one{y}, $in_one{w}, $in_one{h}, $in_two{x}, $in_two{y}, $in_two{w}, $in_two{h}) = @ARGV;
my $are = are_intersecting(\%in_one, \%in_two);
if ($are) {
    print "Intersecting.\n";
    print "Intersection is: ".intersection(\%in_one, \%in_two);
}
else {
    print "Not intersecting.";
}
print "\n";

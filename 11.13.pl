#!/usr/bin/perl

# task: k-order statistic

use strict;
use warnings;

sub kth_elem {
    my ($arr, $k, $start, $end) = @_;
    ($start, $end) = (0, scalar(@$arr)) unless defined($start);
    return undef if $k > scalar(@$arr) || $end - $start < 1;

    my $mid = int(($end - $start) / 2) + $start;
    my $mid_val = $arr->[$mid];
    ($arr->[$mid], $arr->[$end-1]) = ($arr->[$end-1], $arr->[$mid]);

    my $new_mid = $start;
    for (my $i = $start; $i < $end - 1; $i++) {
        if ($arr->[$i] < $mid_val) {
            ($arr->[$new_mid], $arr->[$i]) = ($arr->[$i], $arr->[$new_mid]);
            $new_mid++;
        }
    }
    ($arr->[$end-1], $arr->[$new_mid]) = ($arr->[$new_mid], $arr->[$end-1]);

    if ($new_mid == $k) {
        return $arr->[$new_mid];
    }
    elsif ($new_mid > $k) {
        return kth_elem($arr, $k, $start, $new_mid);
    }
    else { # <
        return kth_elem($arr, $k, $new_mid+1, $end);
    }
}


use Test::More;
use Data::Dumper;

is(kth_elem([0], 1), undef);
is(kth_elem([0], 0), 0);
is(kth_elem([0,1,2], 0), 0);
is(kth_elem([3,1,2], 0), 1);
is(kth_elem([3,9,2,4,8,1,11], 0), 1);
is(kth_elem([3,9,2,4,8,1,11], 1), 2);
is(kth_elem([3,9,2,4,8,1,11], 2), 3);
is(kth_elem([3,9,2,4,8,1,11], 3), 4);
is(kth_elem([3,9,2,4,8,1,11], 4), 8);
is(kth_elem([3,9,2,4,8,1,11], 5), 9);
is(kth_elem([3,9,2,4,8,1,11], 6), 11);
is(kth_elem([3,9,2,4,8,1,11], 7), undef);

done_testing;

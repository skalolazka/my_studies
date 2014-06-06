#!/usr/bin/perl

use strict;
use warnings;

package MyIncreasing;

sub new {
    return bless {} => shift;
}

sub increasing {
    my $self = shift;
    my (@arr) = @_;
    my ($start, $end, $cur_start, $max_len, $prev) = (0, 0, 0, 0, $arr[0]);

    for (my $i = 1; $i < scalar(@arr); $i++) {
        if ($arr[$i] <= $prev) { # new sequence starts
            my $len = $i - $cur_start;
            if ($len > $max_len) { # this is the longest sequence by far
                $start = $cur_start;
                $end = $i-1;
                $max_len = $len;
            }
            $cur_start = $i;
        }
        $prev = $arr[$i];
    }
    my $len = scalar(@arr) - $cur_start;
    if ($len > $max_len) { # this is the longest sequence by far
        $start = $cur_start;
        $end = scalar(@arr) - 1;
        $max_len = $len;
    }
    #return @arr[$start..$end];
    return [$start, $end];
}
#print join(',', increasing(@ARGV))."\n";

package TestMyIncreasing;
use Test::More;
use Test::Deep;

my $module = MyIncreasing->new;
is_deeply($module->increasing(), [0, 0], '() - OK');
is_deeply($module->increasing(0), [0, 0], '(0) - OK');
is_deeply($module->increasing(0, 1), [0, 1], '(0, 1) - OK');
is_deeply($module->increasing(0, 1, 2, 0, 1), [0, 2], '0 OK');
is_deeply($module->increasing(0, 1, 0, 1, 2, 0), [2, 4], '(0, 1, 0, 1, 2, 0) OK');
is_deeply($module->increasing(5, 4, 3, 2, 1), [0, 0], '(5, 4, 3, 2, 1) OK');

done_testing;

#!/usr/bin/perl

my @data = (1, 1);

sub bst_count {
    my ($level) = @_;
    return $data[$level] if ($data[$level]);
    my $count = 0;
    for (my $i = 0; $i < $level; $i++) {
        $count += bst_count($i) * bst_count($level - $i - 1);
    }
    $data[$level] = $count;
    return $count;
}

use Test::More;

is(bst_count(0), 1, 'zero');
is(bst_count(1), 1, 'one');
is(bst_count(2), 2, 'two');
is(bst_count(3), 5, 'three');
is(bst_count(4), 14, 'four');
is(bst_count(5), 42, 'five');

done_testing;

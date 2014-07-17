#!/usr/bin/perl

use strict;
use warnings;

sub from_preorder {
    my ($preorder) = @_;
    return undef unless defined($preorder) && scalar(@$preorder);
    my $value = shift(@$preorder);
    return undef unless defined($value);
    my $tree = { value => $value, left => undef, right => undef };
    $tree->{left} = from_preorder($preorder);
    $tree->{right} = from_preorder($preorder);
    return $tree;
}

use Test::More;
use Test::Deep;
use Data::Dumper;

my ($t, $compare);
$t = from_preorder(undef);
is($t, undef, 'undef for undef');
$t = from_preorder([]);
is($t, undef, 'undef for empty');

$t = from_preorder([1, undef, undef]);
$compare = { value => 1, left => undef, right => undef };
is_deeply($t, $compare, 'just root');

$t = from_preorder([2,1,undef,undef,undef]);
$compare = { value => 2, left => { value => 1, left => undef, right => undef }, right => undef };
is_deeply($t, $compare, 'root + left child');

$t = from_preorder([1,undef,2,undef,undef]);
$compare = { value => 1, right => { value => 2, left => undef, right => undef }, left => undef };
is_deeply($t, $compare, 'root + right child');

$t = from_preorder([2,1,undef,undef,3,undef,undef]);
$compare = { value => 2, left => { value => 1, left => undef, right => undef }, right => { value => 3, left => undef, right => undef }};
is_deeply($t, $compare, 'root + two children');

$t = from_preorder([4,2,1,undef,undef,3,undef,undef,6,undef,undef]);
$compare = { value => 4, left => { value => 2, left => { value => 1, left => undef, right => undef }, right => { value => 3, left => undef, right => undef } }, right => { value => 6, left => undef, right => undef }};
is_deeply($t, $compare, 'bigger tree');

$compare = {
    value => 6,
    left => {
        value => 4,
        left => {
            value => 2,
            left => { value => 1, left => undef, right => undef},
            right => { value => 3, left => undef, right => undef }
        },
        right => { value => 5, left => undef, right => undef }
    },
    right => {
        value => 9,
        left => {
            value => 7,
            left => undef,
            right => { value => 8, left => undef, right => undef },
        },
        right => undef,
    },
};
$t = from_preorder([6,4,2,1,undef,undef,3,undef,undef,5,undef,undef,9,7,undef,8,undef,undef,undef]);
is_deeply($t, $compare, 'big tree');

done_testing;

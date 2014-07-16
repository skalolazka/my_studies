#!/usr/bin/perl

use strict;
use warnings;

sub find_value {
    my ($arr, $value) = @_;
    for (my $i = 0; $i < scalar(@$arr); $i++) {
        if ($arr->[$i] == $value) {
            return $i
        }
    }
    return undef;
}

sub from_inorder {
    my ($inorder, $someorder, $what) = @_;
    $what = 'pre' unless defined($what);
    die "don't know mode $what" if $what ne 'pre' && $what ne 'post';
    return undef if (!defined($inorder) || !scalar(@$inorder) || !defined($someorder) || !scalar(@$someorder));
    die 'Lengths of arrays are different!' unless scalar(@$inorder) == scalar(@$someorder);
    my $value = $what eq 'pre' ? shift(@$someorder) : pop(@$someorder); # root
    my $tree = { value => $value, left => undef, right => undef };
    my $i = find_value($inorder, $value);
    die "Something's wrong with input data! Value $value not found in inorder!" unless defined($i);
    $tree->{left} = from_inorder([@$inorder[0..$i-1]], [@$someorder[0..$i-1]], $what);
    $tree->{right} = from_inorder([@$inorder[$i+1..scalar(@$inorder)-1]], [@$someorder[$i..scalar(@$inorder)-2]], $what);
    return $tree;
}

use Test::More;
use Test::Deep;

my ($t, $compare);
$t = from_inorder([1], undef);
is($t, undef, 'undef for undef');
$t = from_inorder(undef, [1]);
is($t, undef, 'undef for undef again');

$compare = { value => 1, left => undef, right => undef };
$t = from_inorder([1], [1]);
is_deeply($t, $compare, 'just root');
$t = from_inorder([1], [1], 'post');
is_deeply($t, $compare, 'just root - post');

$compare = { value => 2, left => { value => 1, left => undef, right => undef }, right => undef };
$t = from_inorder([1,2], [2,1]);
is_deeply($t, $compare, 'root + left child');
$t = from_inorder([1,2], [1,2], 'post');
is_deeply($t, $compare, 'root + left child - post');

$compare = { value => 1, right => { value => 2, left => undef, right => undef }, left => undef };
$t = from_inorder([1,2], [1,2]);
is_deeply($t, $compare, 'root + right child');
$t = from_inorder([1,2], [2,1], 'post');
is_deeply($t, $compare, 'root + right child - post');

$compare = { value => 2, left => { value => 1, left => undef, right => undef }, right => { value => 3, left => undef, right => undef }};
$t = from_inorder([1,2,3], [2,1,3]);
is_deeply($t, $compare, 'root + two children');
$t = from_inorder([1,2,3], [1,3,2], 'post');
is_deeply($t, $compare, 'root + two children - post');

$compare = { value => 4, left => { value => 2, left => { value => 1, left => undef, right => undef }, right => { value => 3, left => undef, right => undef } }, right => { value => 6, left => { value => 5, left => undef, right => undef }, right => undef }};
$t = from_inorder([1,2,3,4,5,6], [4,2,1,3,6,5]);
is_deeply($t, $compare, 'bigger tree');
$t = from_inorder([1,2,3,4,5,6], [1,3,2,5,6,4], 'post');
is_deeply($t, $compare, 'bigger tree - post');

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
$t = from_inorder([1,2,3,4,5,6,7,8,9], [6,4,2,1,3,5,9,7,8]);
is_deeply($t, $compare, 'big tree');
$t = from_inorder([1,2,3,4,5,6,7,8,9], [1,3,2,5,4,8,7,9,6], 'post');
is_deeply($t, $compare, 'big tree - post');

done_testing;

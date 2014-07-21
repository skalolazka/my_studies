#!/usr/bin/perl

use strict;
use warnings;

use MyBinTree;

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
    my $tree = MyBinTree->new($value);
    my $i = find_value($inorder, $value);
    die "Something's wrong with input data! Value $value not found in inorder!" unless defined($i);
    my $left = from_inorder([@$inorder[0..$i-1]], [@$someorder[0..$i-1]], $what);
    $tree->put_left($left) if defined($left);
    my $right = from_inorder([@$inorder[$i+1..scalar(@$inorder)-1]], [@$someorder[$i..scalar(@$inorder)-2]], $what);
    $tree->put_right($right) if defined($right);
    return $tree;
}

use Test::More;
use Test::Deep;

my ($t, $compare);
$t = from_inorder([1], undef);
is($t, undef, 'undef for undef');
$t = from_inorder(undef, [1]);
is($t, undef, 'undef for undef again');

$compare = MyBinTree->new(1);
#$compare = { value => 1, left => undef, right => undef };
#use Data::Dumper;
#warn Dumper($t);
sub check {
    my ($t, $compare, $text) = @_;
    $t = from_inorder(MyBinTree->inorder($compare), MyBinTree->preorder($compare));
    is_deeply($t, $compare, $text);
    $t = from_inorder(MyBinTree->inorder($compare), MyBinTree->postorder($compare), 'post');
    is_deeply($t, $compare, $text.' - post');
}

check($t, $compare, 'just root');

$compare = MyBinTree->new(2);
$compare->put_left(1);
check($t, $compare, 'root + left child');

$compare = MyBinTree->new(4);
$compare->put_right(6);
check($t, $compare, 'root + right child');

$compare->put_left(2);
check($t, $compare, 'root + two children');

$compare->{left}->put_left(1);
$compare->{left}->put_right(3);
$compare->{right}->put_left(5);
check($t, $compare, 'bigger tree - post');

$compare = MyBinTree->new(6);
$compare->put_left(4);
$compare->{left}->put_left(2);
$compare->{left}{left}->put_left(1);
$compare->{left}{left}->put_right(3);
$compare->{left}->put_right(5);
$compare->put_right(9);
$compare->{right}->put_left(7);
$compare->{right}{left}->put_right(8);
check($t, $compare, 'big tree');

done_testing;

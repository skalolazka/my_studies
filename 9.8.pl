#!/usr/bin/perl

use strict;
use warnings;

use MyBinTree;

sub from_preorder {
    my ($preorder) = @_;
    return undef unless defined($preorder) && scalar(@$preorder);
    my $value = shift(@$preorder);
    return undef unless defined($value);
    my $tree = MyBinTree->new($value);
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

my %trees = (
    'just_root' => MyBinTree->new(1),
);
$trees{left_child} = MyBinTree->new(2);
$trees{left_child}->put_left(1);
$trees{right_child} = MyBinTree->new(2);
$trees{right_child}->put_right(1);
$trees{children} = MyBinTree->new(2);
$trees{children}->put_left(1);
$trees{children}->put_right(3);
$trees{bigger_tree} = MyBinTree->new(4);
$trees{bigger_tree}->put_left(2);
$trees{bigger_tree}->{left}->put_left(1);
$trees{bigger_tree}->{left}->put_right(3);
$trees{bigger_tree}->put_right(6);
$trees{huge_tree} = MyBinTree->new(6);
$trees{huge_tree}->put_left(4);
$trees{huge_tree}->{left}->put_left(2);
$trees{huge_tree}->{left}{left}->put_left(1);
$trees{huge_tree}->{left}{left}->put_right(3);
$trees{huge_tree}->{left}->put_right(5);
$trees{huge_tree}->put_right(9);
$trees{huge_tree}->{right}->put_left(7);

for my $test (keys(%trees)) {
    is_deeply($trees{$test}, from_preorder(MyBinTree->preorder_with_undef($trees{$test})), $test);
}

done_testing;

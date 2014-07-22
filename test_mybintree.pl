#!/usr/bin/perl

use strict;
use warnings;

#use lib '.';
use MyBinTree;

use Test::More;
use Test::Deep;

use Data::Dumper;
my $t = MyBinTree->new(1);
$t->put_left(2);
$t->put_right(3);
$t->{left}->put_left(4);
$t->{left}->put_right(5);
#     1
#    / \
#   2   3
#  / \
# 4   5
is_deeply(MyBinTree->inorder($t), [4,2,5,1,3], 'in');
is_deeply(MyBinTree->preorder($t), [1,2,4,5,3],'pre');
is_deeply(MyBinTree->postorder($t), [4,5,2,3,1], 'post');

is_deeply(MyBinTree->check_subtree($t, $t->{left}), $t->{left}, 'subtree left child');
is_deeply(MyBinTree->check_subtree($t->{left}, $t->{left}{right}), $t->{left}{right}, 'left subtree, right child');
is_deeply(MyBinTree->check_subtree($t->{left}, $t->{right}), undef, 'subtree - not a child');
is_deeply(MyBinTree->check_subtree($t, $t->{left}{right}), $t->{left}{right}, 'subtree left-right child');


#    2       3
#  /   \    / \
# 4     5  9   10
#  \   / \     / \
#   6 7   8   11  12
$t->{left}{left}->put_right(6);
$t->{left}{right}->put_left(7);
$t->{left}{right}->put_right(8);
$t->{right}->put_left(9);
$t->{right}->put_right(10);
$t->{right}{right}->put_left(11);
$t->{right}{right}->put_right(12);
my ($f1, $f2, $lca);
($f1, $f2, $lca) = MyBinTree->lca($t, undef, undef);
is_deeply($lca, undef, 'undef');
($f1, $f2, $lca) = MyBinTree->lca($t, $t, $t);
#warn Dumper($lca);
#use Data::Dumper;
is_deeply($lca, $t, 'root');
($f1, $f2, $lca) = MyBinTree->lca($t, $t->{left}, $t);
is_deeply($lca, $t, 'root, child');
($f1, $f2, $lca) = MyBinTree->lca($t, $t->{left}{right}{left}, $t);
is_deeply($lca, $t, 'root, deep child');
($f1, $f2, $lca) = MyBinTree->lca($t, $t->{left}{right}{left}, $t->{right}{right}{left});
is_deeply($lca, $t, 'root, deep children');
($f1, $f2, $lca) = MyBinTree->lca($t, $t->{left}{right}{left}, $t->{left}{right}{right});
is_deeply($lca, $t->{left}{right}, 'child, leafs');
($f1, $f2, $lca) = MyBinTree->lca($t, $t->{left}{right}{left}, $t->{left}{left}{right});
is_deeply($lca, $t->{left}, 'child');
($f1, $f2, $lca) = MyBinTree->lca($t, $t->{right}{left}, $t->{right}{right}{right});
is_deeply($lca, $t->{right}, 'child, different levels');

done_testing;

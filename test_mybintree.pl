#!/usr/bin/perl

use strict;
use warnings;

#use lib '.';
use MyBinTree;

use Test::More;
use Test::Deep;

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
is_deeply(MyBinTree->preorder_with_undef($t), [1,2,4,undef,undef,5,undef,undef,3,undef,undef],'pre with undef');

done_testing;

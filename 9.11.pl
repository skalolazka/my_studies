#!/usr/bin/perl

use strict;
use warnings;

use MyBinTree;

sub lca {
    my ($t, $n1, $n2) = @_;
    return undef unless defined($t) && defined($n1) && defined($n2);
    return $n1 if $n1 == $n2;
    return $t if $t == $n1 || $t == $n2;
    my $left = lca($t->{left}, $n1, $n2);
    my $right = lca($t->{right}, $n1, $n2);
    if (defined($left) && defined($right)) { # found both
        if ($left != $n1 && $left != $n2) { # found lca here
            return $left;
        }
        elsif ($right != $n1 && $right != $n2) { # found lca here
            return $right;
        }
        else { # found just both nodes => lca is current node
            return $t;
        }
    }
    elsif (defined($left)) {
        return $left;
    }
    else {
        return $right; # defined or undef
    }
}

use Test::More;
use Test::Deep;

my $t = MyBinTree->new(1);
#        1
#      /   \
#    2       3
#  /   \    / \
# 4     5  9   10
#  \   / \     / \
#   6 7   8   11  12
$t->put_left(2);
$t->put_right(3);
$t->{left}->put_left(4);
$t->{left}->put_right(5);
$t->{left}{left}->put_right(6);
$t->{left}{right}->put_left(7);
$t->{left}{right}->put_right(8);
$t->{right}->put_left(9);
$t->{right}->put_right(10);
$t->{right}{right}->put_left(11);
$t->{right}{right}->put_right(12);

is_deeply(lca($t, undef, undef), undef, 'undef');
is_deeply(lca($t, $t, $t), $t, 'root');
is_deeply(lca($t, $t->{left}, $t), $t, 'root, child');
is_deeply(lca($t, $t->{left}{right}{left}, $t), $t, 'root, deep child');
is_deeply(lca($t, $t->{left}{right}{left}, $t->{right}{right}{left}), $t, 'root, deep children');
is_deeply(lca($t, $t->{left}{right}{left}, $t->{left}{right}{right}), $t->{left}{right}, 'child, leafs');
is_deeply(lca($t, $t->{left}{right}{left}, $t->{left}{left}{right}), $t->{left}, 'child');
is_deeply(lca($t, $t->{right}{left}, $t->{right}{right}{right}), $t->{right}, 'child, different levels');

done_testing;

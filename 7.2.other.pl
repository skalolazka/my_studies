#!/usr/bin/perl

use strict;
use warnings;

use MyLinkedList;

package MyLLCycle;

sub new {
    return bless {} => shift;
}

sub ll_cycle{
    my ($self, $ll) = @_;
    my ($big_iter, $count) = ($ll->{first}, 0);
    while (defined($big_iter->{next_node})) {
        my ($i, $iter) = ($count, $ll->{first});
        while (defined($iter->{next_node}) && $i > 0) {
            if ($big_iter == $iter) {
                return $iter;
            }
            $iter = $iter->{next_node};
            $i--;
        }
        $big_iter = $big_iter->{next_node};
        $count++;
    }
    return undef;
}

package TestMyLLCycle;
use Test::More;
use Test::Deep;

my $module = MyLLCycle->new;
my $ll = MyLinkedList->new();
is($module->ll_cycle($ll), undef, 'undef for empty');

$ll = MyLinkedList->new(1,2);
$ll->{first}{next_node}{next_node} = $ll->{first};
cmp_deeply($module->ll_cycle($ll), {value => 1, next_node => { value => 2, next_node => ignore }}, 'one big cycle');

$ll->{first}{next_node}{next_node} = $ll->{first}->{next_node};
cmp_deeply($module->ll_cycle($ll), {value => 2, next_node => { value => 2, next_node => ignore }}, 'cycle of one element');

$ll = MyLinkedList->new(1,2,1);
$ll->{first}{next_node}{next_node}{next_node} = $ll->{first};
cmp_deeply($module->ll_cycle($ll), {value => 1, next_node => { value => 2, next_node => ignore }}, 'same values');

$ll = MyLinkedList->new(2,2,1,3,1,4,2);
$ll->{first}{next_node}{next_node}{next_node}{next_node}{next_node} = $ll->{first}{next_node};
cmp_deeply($module->ll_cycle($ll), {value => 2, next_node => { value => 1, next_node => { value => 3, next_node => ignore }}}, 'long=)');

done_testing;

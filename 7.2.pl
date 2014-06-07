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
    my $iter = $ll->{first};
    my %seen = ();
    while (defined($iter->{next_node})) {
        for my $seen (@{$seen{$iter->{value}}}) {
            if ($seen == $iter) {
                return $iter;
            }
        }
        push(@{$seen{$iter->{value}}}, $iter);
        $iter = $iter->{next_node};
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

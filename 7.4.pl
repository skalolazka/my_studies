#!/usr/bin/perl

use strict;
use warnings;

use MyLinkedList;

package MyLLAreJoined;

sub new {
    return bless {} => shift;
}

sub ll_are_joined{
    my ($self, $ll1, $ll2) = @_;
    my ($big_iter1, $big_iter2, $count) = ($ll1->{first}, $ll2->{first}, 1);
    while (defined($big_iter1->{next_node}) || defined($big_iter2->{next_node})) { # FIXME we don't test last item then!!!
        my ($i, $iter) = ($count, $ll1->{first});
        while (defined($iter->{next_node}) && $i > 0) {
            if ($big_iter2 == $iter) {
                return $iter;
            }
            $iter = $iter->{next_node};
            $i--;
        }
        ($i, $iter) = ($count, $ll2->{first});
        while (defined($iter->{next_node}) && $i > 0) {
            if ($big_iter1 == $iter) {
                return $iter;
            }
            $iter = $iter->{next_node};
            $i--;
        }
        $big_iter1 = $big_iter1->{next_node};
        $big_iter2 = $big_iter2->{next_node};
        $count++;
    }
    if ($big_iter1 == $big_iter2) { return $big_iter1 }
    return undef;
}

package TestMyLLAreJoined;
use Test::More;
use Test::Deep;

my $module = MyLLAreJoined->new;

my ($ll1, $ll2) = (MyLinkedList->new(), MyLinkedList->new());
is($module->ll_are_joined($ll1, $ll2), undef, 'undef for empty');

($ll1, $ll2) = (MyLinkedList->new(1), MyLinkedList->new());
is($module->ll_are_joined($ll1, $ll2), undef, 'one is empty');

($ll1, $ll2) = (MyLinkedList->new(), MyLinkedList->new(2,3,4));
is($module->ll_are_joined($ll1, $ll2), undef, 'first is empty');

($ll1, $ll2) = (MyLinkedList->new(1,2,3), MyLinkedList->new(4,5));
use Data::Dumper;
is($module->ll_are_joined($ll1, $ll2), undef, "not joined anyway if I haven't joined them=)");

$ll2->{first}->{next_node} = $ll1->{first}->{next_node};
#warn Dumper($ll1);
#warn Dumper($ll2);
is_deeply($module->ll_are_joined($ll1, $ll2), {value => 2, next_node => { value => 3, next_node => undef }}, 'joined now!');

($ll1, $ll2) = (MyLinkedList->new(1,2), MyLinkedList->new(4,5));
$ll2->{first}->{next_node} = $ll1->{first}->{next_node};
is_deeply($module->ll_are_joined($ll1, $ll2), {value => 2, next_node => undef}, 'short, joined');

($ll1, $ll2) = (MyLinkedList->new(1,2,3,4), MyLinkedList->new(5,6,7));
$ll1->{first}->{next_node}->{next_node} = $ll2->{first};
is_deeply($module->ll_are_joined($ll1, $ll2), {value => 5, next_node => { value => 6, next_node => { value => 7, next_node => undef }}}, 'joined at the start');

done_testing;

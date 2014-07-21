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
    my ($slow, $fast) = ($ll, $ll);
    my $has_cycle = 0;
    while (defined($fast)) {
        $slow = $slow->{next_node};
        $fast = $fast->{next_node}{next_node};
        if ($fast == $slow) {
            $has_cycle = 1;
            last;
        }
    }
    if ($has_cycle) { # find start of cycle now
        $fast = $slow;
        my $counter = 0;
        while ($slow != $fast || !$counter) {
            $slow = $slow->{next_node};
            $fast = $fast->{next_node}{next_node};
            $counter++; # length of cycle
        }
        ($slow, $fast) = ($ll, $ll);
        while ($counter) {
            $fast = $fast->{next_node};
            $counter--;
        }
        while ($slow != $fast) {
            $slow = $slow->{next_node};
            $fast = $fast->{next_node};
        }
        return $slow;
    }
    else {
        return undef
    }
}

package TestMyLLCycle;
use Test::More;
use Test::Deep;

my $module = MyLLCycle->new;
is($module->ll_cycle(undef), undef, 'undef for empty');

my $ll = MyLinkedList->from_array(1,2);
is($module->ll_cycle($ll), undef, 'undef for no cycle');
$ll->{next_node}{next_node} = $ll;
cmp_deeply($module->ll_cycle($ll), noclass({value => 1, next_node => { value => 2, next_node => ignore }}), 'one big cycle');

$ll->{next_node}{next_node} = $ll->{next_node};
cmp_deeply($module->ll_cycle($ll), noclass({value => 2, next_node => { value => 2, next_node => ignore }}), 'cycle of one element');

$ll = MyLinkedList->from_array(1,2,1);
$ll->{next_node}{next_node}{next_node} = $ll;
cmp_deeply($module->ll_cycle($ll), noclass({value => 1, next_node => { value => 2, next_node => ignore }}), 'same values');

$ll = MyLinkedList->from_array(2,2,1,3,1,4,2);
$ll->{next_node}{next_node}{next_node}{next_node}{next_node} = $ll->{next_node};
cmp_deeply($module->ll_cycle($ll), noclass({value => 2, next_node => { value => 1, next_node => { value => 3, next_node => ignore }}}), 'long=)');

done_testing;

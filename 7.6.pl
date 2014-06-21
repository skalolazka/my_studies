#!/usr/bin/perl

# even-odd merge (0,2,4,...,1,3,5,...)

package EvenOddMerge;

sub new {
    return bless {} => shift;
}

sub even_odd {
    my ($self, $ll) = @_;
    return $ll unless defined($ll) && defined($ll->{next_node});

    my ($even, $odd, $odd_start) = ($ll, $ll->{next_node}, $ll->{next_node});
    my ($cur_even, $cur_odd) = ($even, $odd);
    while (defined($even->{next_node}) && defined($odd->{next_node})) {
        ($cur_even->{next_node}, $cur_odd->{next_node}) = ($even->{next_node}{next_node}, $odd->{next_node}{next_node});
        ($even, $odd) = ($cur_even->{next_node}, $cur_odd->{next_node});
        ($cur_even, $cur_odd) = ($cur_even->{next_node}, $cur_odd->{next_node});
    }
    $cur_even->{next_node} = $odd_start;
    return $ll;
}

package TestEvenOddMerge;

use Test::More;
use Test::Deep;

use lib '.';
use MyLinkedList;

my $m = EvenOddMerge->new;

my $l = $m->even_odd(MyLinkedList->from_array());
is($l, undef, 'none');

$l = $m->even_odd(MyLinkedList->from_array(1));
is_deeply([$l->to_array], [1], 'just one');

$l = $m->even_odd(MyLinkedList->from_array(1,2));
is_deeply([$l->to_array], [1,2], 'two');

$l = $m->even_odd(MyLinkedList->from_array(0,1,2,3,4,5,6));
is_deeply([$l->to_array], [0,2,4,6,1,3,5], 'long even');

$l = $m->even_odd(MyLinkedList->from_array(0,1,2,3,4,5,6,7));
is_deeply([$l->to_array], [0,2,4,6,1,3,5,7], 'long odd');

done_testing;

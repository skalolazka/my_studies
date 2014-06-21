#!/usr/bin/perl

package MyReverseLL;

use MyLinkedList;

sub new {
    return bless {} => shift;
}

use Data::Dumper;
sub reverse_ll {
    my ($self, $ll) = @_;

    my ($prev, $cur) = (undef, $ll);
    while ($cur) {
        my $tmp = $cur->{next_node};
        $cur->{next_node} = $prev;
        $prev = $cur;
        $cur = $tmp;
    }
    return $prev;
}

package TestMyReverseLL;

use Test::More;
use Test::Deep;

my $module = MyReverseLL->new;
my $l = MyLinkedList->from_array();
is_deeply($module->reverse_ll($l), undef, 'none');
$l = MyLinkedList->from_array(1);
is_deeply($module->reverse_ll($l), {value => 1, next_node => undef}, 'one');
$l = MyLinkedList->from_array(1,2,3,4,5);
is_deeply($module->reverse_ll($l), {value => 5, next_node => {value => 4, next_node => {value => 3, next_node => {value => 2, next_node => {value => 1, next_node => undef}}}}}, 'long');


done_testing;
